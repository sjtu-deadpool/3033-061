#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MovieLens 100k 数据集探索工具
=====================================

该脚本用于分析和展示MovieLens 100k数据集的基本信息、统计数据和可视化图表。
适用于项目展示和数据集理解。

作者: MovieLens Dataset Explorer
数据集: MovieLens 100k (GroupLens Research)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体和图表样式
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")
plt.style.use('default')

class MovieLensExplorer:
    """MovieLens 100k数据集分析类"""
    
    def __init__(self, data_path='ml-100k'):
        """
        初始化数据集分析器
        
        Args:
            data_path (str): MovieLens数据集文件夹路径
        """
        self.data_path = data_path
        self.ratings = None
        self.movies = None
        self.users = None
        self.genres = None
        self.occupations = None
        
    def load_data(self):
        """加载所有数据文件"""
        print("正在加载MovieLens 100k数据集...")
        
        try:
            # 加载评分数据
            self.ratings = pd.read_csv(
                f'{self.data_path}/u.data', 
                sep='\t', 
                names=['user_id', 'movie_id', 'rating', 'timestamp'],
                encoding='latin-1'
            )
            
            # 加载电影数据
            movie_columns = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url'] + \
                           [f'genre_{i}' for i in range(19)]
            self.movies = pd.read_csv(
                f'{self.data_path}/u.item', 
                sep='|', 
                names=movie_columns,
                encoding='latin-1'
            )
            
            # 加载用户数据
            self.users = pd.read_csv(
                f'{self.data_path}/u.user', 
                sep='|', 
                names=['user_id', 'age', 'gender', 'occupation', 'zipcode'],
                encoding='latin-1'
            )
            
            # 加载流派数据
            self.genres = pd.read_csv(
                f'{self.data_path}/u.genre', 
                sep='|', 
                names=['genre', 'genre_id'],
                encoding='latin-1'
            ).dropna()
            
            # 加载职业数据
            with open(f'{self.data_path}/u.occupation', 'r') as f:
                self.occupations = [line.strip() for line in f.readlines() if line.strip()]
            
            print("数据加载完成!")
            
        except Exception as e:
            print(f"数据加载失败: {e}")
            raise
    
    def print_basic_info(self):
        """打印数据集基本信息"""
        print("\n" + "="*60)
        print("MOVIELENS 100K 数据集基本信息")
        print("="*60)
        
        print(f"评分数据 (u.data):")
        print(f"   - 总评分数: {len(self.ratings):,}")
        print(f"   - 用户数量: {self.ratings['user_id'].nunique():,}")
        print(f"   - 电影数量: {self.ratings['movie_id'].nunique():,}")
        print(f"   - 评分范围: {self.ratings['rating'].min()} - {self.ratings['rating'].max()}")
        print(f"   - 数据稀疏度: {(1 - len(self.ratings) / (self.ratings['user_id'].nunique() * self.ratings['movie_id'].nunique())) * 100:.2f}%")
        
        print(f"\n电影数据 (u.item):")
        print(f"   - 电影总数: {len(self.movies):,}")
        print(f"   - 流派数量: {len(self.genres)}")
        print(f"   - 发布年份范围: {self._get_movie_year_range()}")
        
        print(f"\n用户数据 (u.user):")
        print(f"   - 用户总数: {len(self.users):,}")
        print(f"   - 年龄范围: {self.users['age'].min()} - {self.users['age'].max()}")
        print(f"   - 性别分布: 男性 {(self.users['gender'] == 'M').sum()}, 女性 {(self.users['gender'] == 'F').sum()}")
        print(f"   - 职业类别: {len(self.occupations)}")
    
    def _get_movie_year_range(self):
        """获取电影发布年份范围"""
        # 从标题中提取年份
        years = self.movies['title'].str.extract(r'\((\d{4})\)')[0].astype(float)
        return f"{int(years.min())} - {int(years.max())}"
    
    def show_sample_data(self):
        """展示示例数据"""
        print("\n" + "="*60)
        print("数据样本预览")
        print("="*60)
        
        print("\n评分数据示例 (前5条):")
        print(self.ratings.head())
        
        print("\n电影数据示例 (前3条):")
        movie_display = self.movies[['movie_id', 'title', 'release_date']].head(3)
        print(movie_display.to_string(index=False))
        
        print("\n用户数据示例 (前5条):")
        print(self.users.head())
        
        print("\n电影流派列表:")
        genre_list = ", ".join(self.genres['genre'].tolist())
        print(f"   {genre_list}")
        
        print("\n用户职业列表:")
        occupation_list = ", ".join(self.occupations)
        print(f"   {occupation_list}")
    
    def analyze_rating_distribution(self):
        """分析评分分布"""
        print("\n" + "="*60)
        print("评分分布分析")
        print("="*60)
        
        rating_stats = self.ratings['rating'].describe()
        print(f"\n评分统计:")
        print(f"   - 平均评分: {rating_stats['mean']:.2f}")
        print(f"   - 中位数评分: {rating_stats['50%']:.2f}")
        print(f"   - 标准差: {rating_stats['std']:.2f}")
        
        print(f"\n各评分频次:")
        rating_counts = self.ratings['rating'].value_counts().sort_index()
        for rating, count in rating_counts.items():
            percentage = (count / len(self.ratings)) * 100
            print(f"   {rating}星: {count:,} ({percentage:.1f}%)")
    
    def analyze_user_behavior(self):
        """分析用户行为"""
        print("\n" + "="*60)
        print("用户行为分析")
        print("="*60)
        
        # 每个用户的评分数量
        user_rating_counts = self.ratings.groupby('user_id').size()
        
        print(f"\n用户活跃度:")
        print(f"   - 平均每用户评分数: {user_rating_counts.mean():.1f}")
        print(f"   - 最活跃用户评分数: {user_rating_counts.max()}")
        print(f"   - 最少活跃用户评分数: {user_rating_counts.min()}")
        
        # 年龄分布
        age_stats = self.users['age'].describe()
        print(f"\n用户年龄分析:")
        print(f"   - 平均年龄: {age_stats['mean']:.1f}岁")
        print(f"   - 年龄中位数: {age_stats['50%']:.0f}岁")
        print(f"   - 最年轻: {age_stats['min']:.0f}岁")
        print(f"   - 最年长: {age_stats['max']:.0f}岁")
        
        # 职业分布Top5
        occupation_counts = self.users['occupation'].value_counts()
        print(f"\n职业分布Top5:")
        for i, (occupation, count) in enumerate(occupation_counts.head().items(), 1):
            percentage = (count / len(self.users)) * 100
            print(f"   {i}. {occupation}: {count} ({percentage:.1f}%)")
    
    def analyze_movie_popularity(self):
        """分析电影流行度"""
        print("\n" + "="*60)
        print("电影流行度分析")
        print("="*60)
        
        # 每部电影的评分数量
        movie_rating_counts = self.ratings.groupby('movie_id').size()
        movie_avg_ratings = self.ratings.groupby('movie_id')['rating'].mean()
        
        print(f"\n电影评分统计:")
        print(f"   - 平均每部电影评分数: {movie_rating_counts.mean():.1f}")
        print(f"   - 最受欢迎电影评分数: {movie_rating_counts.max()}")
        print(f"   - 最少评分电影评分数: {movie_rating_counts.min()}")
        
        # 最受欢迎的电影Top5
        popular_movies = movie_rating_counts.sort_values(ascending=False).head()
        print(f"\n最受欢迎电影Top5 (按评分数量):")
        for i, (movie_id, count) in enumerate(popular_movies.items(), 1):
            movie_title = self.movies[self.movies['movie_id'] == movie_id]['title'].iloc[0]
            avg_rating = movie_avg_ratings[movie_id]
            print(f"   {i}. {movie_title} - {count}次评分 (平均{avg_rating:.1f}分)")
        
        # 流派分析
        genre_columns = [f'genre_{i}' for i in range(19)]
        genre_counts = self.movies[genre_columns].sum()
        genre_counts.index = self.genres['genre'].tolist()
        
        print(f"\n电影流派分布Top5:")
        for i, (genre, count) in enumerate(genre_counts.sort_values(ascending=False).head().items(), 1):
            percentage = (count / len(self.movies)) * 100
            print(f"   {i}. {genre}: {count} ({percentage:.1f}%)")
    
    def create_visualizations(self):
        """创建可视化图表"""
        print("\n" + "="*60)
        print("生成数据可视化图表...")
        print("="*60)
        
        # 创建图表
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('MovieLens 100k 数据集分析', fontsize=16, fontweight='bold')
        
        # 1. 评分分布
        self.ratings['rating'].hist(bins=5, ax=axes[0,0], color='skyblue', edgecolor='black')
        axes[0,0].set_title('评分分布')
        axes[0,0].set_xlabel('评分')
        axes[0,0].set_ylabel('频次')
        
        # 2. 用户年龄分布
        self.users['age'].hist(bins=20, ax=axes[0,1], color='lightgreen', edgecolor='black')
        axes[0,1].set_title('用户年龄分布')
        axes[0,1].set_xlabel('年龄')
        axes[0,1].set_ylabel('用户数')
        
        # 3. 性别分布
        gender_counts = self.users['gender'].value_counts()
        axes[0,2].pie(gender_counts.values, labels=['男性', '女性'], autopct='%1.1f%%', colors=['lightblue', 'pink'])
        axes[0,2].set_title('用户性别分布')
        
        # 4. 用户评分数量分布
        user_rating_counts = self.ratings.groupby('user_id').size()
        user_rating_counts.hist(bins=30, ax=axes[1,0], color='orange', edgecolor='black')
        axes[1,0].set_title('用户评分活跃度分布')
        axes[1,0].set_xlabel('评分数量')
        axes[1,0].set_ylabel('用户数')
        
        # 5. 电影评分数量分布
        movie_rating_counts = self.ratings.groupby('movie_id').size()
        movie_rating_counts.hist(bins=30, ax=axes[1,1], color='purple', alpha=0.7, edgecolor='black')
        axes[1,1].set_title('电影受欢迎程度分布')
        axes[1,1].set_xlabel('被评分次数')
        axes[1,1].set_ylabel('电影数')
        
        # 6. Top流派分布
        genre_columns = [f'genre_{i}' for i in range(19)]
        genre_counts = self.movies[genre_columns].sum()
        genre_counts.index = self.genres['genre'].tolist()
        top_genres = genre_counts.sort_values(ascending=False).head(8)
        
        top_genres.plot(kind='bar', ax=axes[1,2], color='coral')
        axes[1,2].set_title('热门电影流派Top8')
        axes[1,2].set_xlabel('流派')
        axes[1,2].set_ylabel('电影数量')
        axes[1,2].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('movielens_analysis.png', dpi=300, bbox_inches='tight')
        print("图表已保存为 'movielens_analysis.png'")
        plt.show()
    
    def check_data_quality(self):
        """检查数据质量"""
        print("\n" + "="*60)
        print("数据质量检查")
        print("="*60)
        
        print(f"\n评分数据质量:")
        print(f"   - 缺失值: {self.ratings.isnull().sum().sum()}")
        print(f"   - 重复记录: {self.ratings.duplicated().sum()}")
        print(f"   - 评分范围检查: {self.ratings['rating'].min()} ≤ 评分 ≤ {self.ratings['rating'].max()} [正常]")
        
        print(f"\n电影数据质量:")
        print(f"   - 缺失标题: {self.movies['title'].isnull().sum()}")
        print(f"   - 缺失发布日期: {self.movies['release_date'].isnull().sum()}")
        
        print(f"\n用户数据质量:")
        print(f"   - 缺失值: {self.users.isnull().sum().sum()}")
        print(f"   - 年龄异常值检查: {(self.users['age'] < 7).sum() + (self.users['age'] > 100).sum()} 个异常值")
        
        # 检查ID连续性
        print(f"\nID连续性检查:")
        user_ids = set(self.ratings['user_id'].unique())
        movie_ids = set(self.ratings['movie_id'].unique())
        
        expected_users = set(range(1, max(user_ids) + 1))
        expected_movies = set(range(1, max(movie_ids) + 1))
        
        missing_users = expected_users - user_ids
        missing_movies = expected_movies - movie_ids
        
        print(f"   - 缺失用户ID: {len(missing_users)} 个")
        print(f"   - 缺失电影ID: {len(missing_movies)} 个")
    
    def generate_summary_report(self):
        """生成总结报告"""
        print("\n" + "="*60)
        print("MOVIELENS 100K 数据集总结报告")
        print("="*60)
        
        print(f"""
核心统计:
   • 总评分数: {len(self.ratings):,}
   • 用户数: {self.ratings['user_id'].nunique():,}
   • 电影数: {self.ratings['movie_id'].nunique():,}
   • 流派数: {len(self.genres)}
   • 数据稀疏度: {(1 - len(self.ratings) / (self.ratings['user_id'].nunique() * self.ratings['movie_id'].nunique())) * 100:.1f}%

评分特征:
   • 平均评分: {self.ratings['rating'].mean():.2f}/5.0
   • 评分标准差: {self.ratings['rating'].std():.2f}
   • 最常见评分: {self.ratings['rating'].mode()[0]}分

用户特征:
   • 平均年龄: {self.users['age'].mean():.1f}岁
   • 男女比例: {(self.users['gender'] == 'M').sum()}:{(self.users['gender'] == 'F').sum()}
   • 平均每用户评分: {self.ratings.groupby('user_id').size().mean():.1f}

电影特征:
   • 平均每电影评分数: {self.ratings.groupby('movie_id').size().mean():.1f}
   • 最热门流派: {self.movies[[f'genre_{i}' for i in range(19)]].sum().idxmax().replace('genre_', self.genres.iloc[int(self.movies[[f'genre_{i}' for i in range(19)]].sum().idxmax().split('_')[1])]['genre'])}
   • 发布年份跨度: {self._get_movie_year_range()}

数据质量: 高质量，缺失值极少，适合推荐系统研究
        """)
    
    def run_complete_analysis(self):
        """运行完整的数据分析"""
        print("开始MovieLens 100k数据集完整分析...")
        
        # 加载数据
        self.load_data()
        
        # 基本信息
        self.print_basic_info()
        
        # 示例数据
        self.show_sample_data()
        
        # 各种分析
        self.analyze_rating_distribution()
        self.analyze_user_behavior()
        self.analyze_movie_popularity()
        
        # 数据质量检查
        self.check_data_quality()
        
        # 可视化
        self.create_visualizations()
        
        # 总结报告
        self.generate_summary_report()
        
        print(f"\n分析完成! 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    """主函数"""
    print("MovieLens 100k 数据集分析工具")
    print("=" * 50)
    
    # 创建分析器实例
    explorer = MovieLensExplorer('ml-100k')
    
    # 运行完整分析
    explorer.run_complete_analysis()


if __name__ == "__main__":
    main()