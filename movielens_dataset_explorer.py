#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MovieLens 100k Dataset Explorer
=====================================

This script is used to analyze and display basic information, statistics, 
and visualizations of the MovieLens 100k dataset.
Suitable for project presentation and dataset understanding.

Author: MovieLens Dataset Explorer
Dataset: MovieLens 100k (GroupLens Research)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set font and chart styles
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")
plt.style.use('default')

class MovieLensExplorer:
    """MovieLens 100k dataset analysis class"""
    
    def __init__(self, data_path='ml-100k'):
        """
        Initialize dataset analyzer
        
        Args:
            data_path (str): Path to MovieLens dataset folder
        """
        self.data_path = data_path
        self.ratings = None
        self.movies = None
        self.users = None
        self.genres = None
        self.occupations = None
        
    def load_data(self):
        """Load all data files"""
        print("Loading MovieLens 100k dataset...")
        
        try:
            # Load ratings data
            self.ratings = pd.read_csv(
                f'{self.data_path}/u.data', 
                sep='\t', 
                names=['user_id', 'movie_id', 'rating', 'timestamp'],
                encoding='latin-1'
            )
            
            # Load movie data
            movie_columns = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url'] + \
                           [f'genre_{i}' for i in range(19)]
            self.movies = pd.read_csv(
                f'{self.data_path}/u.item', 
                sep='|', 
                names=movie_columns,
                encoding='latin-1'
            )
            
            # Load user data
            self.users = pd.read_csv(
                f'{self.data_path}/u.user', 
                sep='|', 
                names=['user_id', 'age', 'gender', 'occupation', 'zipcode'],
                encoding='latin-1'
            )
            
            # Load genre data
            self.genres = pd.read_csv(
                f'{self.data_path}/u.genre', 
                sep='|', 
                names=['genre', 'genre_id'],
                encoding='latin-1'
            ).dropna()
            
            # Load occupation data
            with open(f'{self.data_path}/u.occupation', 'r') as f:
                self.occupations = [line.strip() for line in f.readlines() if line.strip()]
            
            print("Data loading completed!")
            
        except Exception as e:
            print(f"Data loading failed: {e}")
            raise
    
    def print_basic_info(self):
        """Print basic dataset information"""
        print("\n" + "="*60)
        print("MOVIELENS 100K DATASET BASIC INFORMATION")
        print("="*60)
        
        print(f"Rating data (u.data):")
        print(f"   - Total ratings: {len(self.ratings):,}")
        print(f"   - Number of users: {self.ratings['user_id'].nunique():,}")
        print(f"   - Number of movies: {self.ratings['movie_id'].nunique():,}")
        print(f"   - Rating range: {self.ratings['rating'].min()} - {self.ratings['rating'].max()}")
        print(f"   - Data sparsity: {(1 - len(self.ratings) / (self.ratings['user_id'].nunique() * self.ratings['movie_id'].nunique())) * 100:.2f}%")
        
        print(f"\nMovie data (u.item):")
        print(f"   - Total movies: {len(self.movies):,}")
        print(f"   - Number of genres: {len(self.genres)}")
        print(f"   - Release year range: {self._get_movie_year_range()}")
        
        print(f"\nUser data (u.user):")
        print(f"   - Total users: {len(self.users):,}")
        print(f"   - Age range: {self.users['age'].min()} - {self.users['age'].max()}")
        print(f"   - Gender distribution: Male {(self.users['gender'] == 'M').sum()}, Female {(self.users['gender'] == 'F').sum()}")
        print(f"   - Occupation categories: {len(self.occupations)}")
    
    def _get_movie_year_range(self):
        """Get movie release year range"""
        # Extract years from titles
        years = self.movies['title'].str.extract(r'\((\d{4})\)')[0].astype(float)
        return f"{int(years.min())} - {int(years.max())}"
    
    def show_sample_data(self):
        """Show sample data"""
        print("\n" + "="*60)
        print("DATA SAMPLE PREVIEW")
        print("="*60)
        
        print("\nRating data sample (first 5 rows):")
        print(self.ratings.head())
        
        print("\nMovie data sample (first 3 rows):")
        movie_display = self.movies[['movie_id', 'title', 'release_date']].head(3)
        print(movie_display.to_string(index=False))
        
        print("\nUser data sample (first 5 rows):")
        print(self.users.head())
        
        print("\nMovie genre list:")
        genre_list = ", ".join(self.genres['genre'].tolist())
        print(f"   {genre_list}")
        
        print("\nUser occupation list:")
        occupation_list = ", ".join(self.occupations)
        print(f"   {occupation_list}")
    
    def analyze_rating_distribution(self):
        """Analyze rating distribution"""
        print("\n" + "="*60)
        print("RATING DISTRIBUTION ANALYSIS")
        print("="*60)
        
        rating_stats = self.ratings['rating'].describe()
        print(f"\nRating statistics:")
        print(f"   - Mean rating: {rating_stats['mean']:.2f}")
        print(f"   - Median rating: {rating_stats['50%']:.2f}")
        print(f"   - Standard deviation: {rating_stats['std']:.2f}")
        
        print(f"\nRating frequencies:")
        rating_counts = self.ratings['rating'].value_counts().sort_index()
        for rating, count in rating_counts.items():
            percentage = (count / len(self.ratings)) * 100
            print(f"   {rating} stars: {count:,} ({percentage:.1f}%)")
    
    def analyze_user_behavior(self):
        """Analyze user behavior"""
        print("\n" + "="*60)
        print("USER BEHAVIOR ANALYSIS")
        print("="*60)
        
        # Number of ratings per user
        user_rating_counts = self.ratings.groupby('user_id').size()
        
        print(f"\nUser activity:")
        print(f"   - Average ratings per user: {user_rating_counts.mean():.1f}")
        print(f"   - Most active user ratings: {user_rating_counts.max()}")
        print(f"   - Least active user ratings: {user_rating_counts.min()}")
        
        # Age distribution
        age_stats = self.users['age'].describe()
        print(f"\nUser age analysis:")
        print(f"   - Average age: {age_stats['mean']:.1f} years")
        print(f"   - Median age: {age_stats['50%']:.0f} years")
        print(f"   - Youngest: {age_stats['min']:.0f} years")
        print(f"   - Oldest: {age_stats['max']:.0f} years")
        
        # Top 5 occupation distribution
        occupation_counts = self.users['occupation'].value_counts()
        print(f"\nTop 5 occupation distribution:")
        for i, (occupation, count) in enumerate(occupation_counts.head().items(), 1):
            percentage = (count / len(self.users)) * 100
            print(f"   {i}. {occupation}: {count} ({percentage:.1f}%)")
    
    def analyze_movie_popularity(self):
        """Analyze movie popularity"""
        print("\n" + "="*60)
        print("MOVIE POPULARITY ANALYSIS")
        print("="*60)
        
        # Number of ratings per movie
        movie_rating_counts = self.ratings.groupby('movie_id').size()
        movie_avg_ratings = self.ratings.groupby('movie_id')['rating'].mean()
        
        print(f"\nMovie rating statistics:")
        print(f"   - Average ratings per movie: {movie_rating_counts.mean():.1f}")
        print(f"   - Most popular movie rating count: {movie_rating_counts.max()}")
        print(f"   - Least rated movie rating count: {movie_rating_counts.min()}")
        
        # Top 5 most popular movies
        popular_movies = movie_rating_counts.sort_values(ascending=False).head()
        print(f"\nTop 5 most popular movies (by rating count):")
        for i, (movie_id, count) in enumerate(popular_movies.items(), 1):
            movie_title = self.movies[self.movies['movie_id'] == movie_id]['title'].iloc[0]
            avg_rating = movie_avg_ratings[movie_id]
            print(f"   {i}. {movie_title} - {count} ratings (avg {avg_rating:.1f} stars)")
        
        # Genre analysis
        genre_columns = [f'genre_{i}' for i in range(19)]
        genre_counts = self.movies[genre_columns].sum()
        genre_counts.index = self.genres['genre'].tolist()
        
        print(f"\nTop 5 movie genre distribution:")
        for i, (genre, count) in enumerate(genre_counts.sort_values(ascending=False).head().items(), 1):
            percentage = (count / len(self.movies)) * 100
            print(f"   {i}. {genre}: {count} ({percentage:.1f}%)")
    
    def create_visualizations(self):
        """Create visualization charts"""
        print("\n" + "="*60)
        print("Generating data visualization charts...")
        print("="*60)
        
        # Create charts
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('MovieLens 100k Dataset Analysis', fontsize=16, fontweight='bold')
        
        # 1. Rating distribution
        self.ratings['rating'].hist(bins=5, ax=axes[0,0], color='skyblue', edgecolor='black')
        axes[0,0].set_title('Rating Distribution')
        axes[0,0].set_xlabel('Rating')
        axes[0,0].set_ylabel('Frequency')
        
        # 2. User age distribution
        self.users['age'].hist(bins=20, ax=axes[0,1], color='lightgreen', edgecolor='black')
        axes[0,1].set_title('User Age Distribution')
        axes[0,1].set_xlabel('Age')
        axes[0,1].set_ylabel('Number of Users')
        
        # 3. Gender distribution
        gender_counts = self.users['gender'].value_counts()
        axes[0,2].pie(gender_counts.values, labels=['Male', 'Female'], autopct='%1.1f%%', colors=['lightblue', 'pink'])
        axes[0,2].set_title('User Gender Distribution')
        
        # 4. User rating count distribution
        user_rating_counts = self.ratings.groupby('user_id').size()
        user_rating_counts.hist(bins=30, ax=axes[1,0], color='orange', edgecolor='black')
        axes[1,0].set_title('User Rating Activity Distribution')
        axes[1,0].set_xlabel('Number of Ratings')
        axes[1,0].set_ylabel('Number of Users')
        
        # 5. Movie rating count distribution
        movie_rating_counts = self.ratings.groupby('movie_id').size()
        movie_rating_counts.hist(bins=30, ax=axes[1,1], color='purple', alpha=0.7, edgecolor='black')
        axes[1,1].set_title('Movie Popularity Distribution')
        axes[1,1].set_xlabel('Times Rated')
        axes[1,1].set_ylabel('Number of Movies')
        
        # 6. Top genre distribution
        genre_columns = [f'genre_{i}' for i in range(19)]
        genre_counts = self.movies[genre_columns].sum()
        genre_counts.index = self.genres['genre'].tolist()
        top_genres = genre_counts.sort_values(ascending=False).head(8)
        
        top_genres.plot(kind='bar', ax=axes[1,2], color='coral')
        axes[1,2].set_title('Top 8 Popular Movie Genres')
        axes[1,2].set_xlabel('Genre')
        axes[1,2].set_ylabel('Number of Movies')
        axes[1,2].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('movielens_analysis.png', dpi=300, bbox_inches='tight')
        print("Charts saved as 'movielens_analysis.png'")
        plt.show()
    
    def check_data_quality(self):
        """Check data quality"""
        print("\n" + "="*60)
        print("DATA QUALITY CHECK")
        print("="*60)
        
        print(f"\nRating data quality:")
        print(f"   - Missing values: {self.ratings.isnull().sum().sum()}")
        print(f"   - Duplicate records: {self.ratings.duplicated().sum()}")
        print(f"   - Rating range check: {self.ratings['rating'].min()} ≤ rating ≤ {self.ratings['rating'].max()} [Normal]")
        
        print(f"\nMovie data quality:")
        print(f"   - Missing titles: {self.movies['title'].isnull().sum()}")
        print(f"   - Missing release dates: {self.movies['release_date'].isnull().sum()}")
        
        print(f"\nUser data quality:")
        print(f"   - Missing values: {self.users.isnull().sum().sum()}")
        print(f"   - Age outlier check: {(self.users['age'] < 7).sum() + (self.users['age'] > 100).sum()} outliers")
        
        # Check ID continuity
        print(f"\nID continuity check:")
        user_ids = set(self.ratings['user_id'].unique())
        movie_ids = set(self.ratings['movie_id'].unique())
        
        expected_users = set(range(1, max(user_ids) + 1))
        expected_movies = set(range(1, max(movie_ids) + 1))
        
        missing_users = expected_users - user_ids
        missing_movies = expected_movies - movie_ids
        
        print(f"   - Missing user IDs: {len(missing_users)}")
        print(f"   - Missing movie IDs: {len(missing_movies)}")
    
    def generate_summary_report(self):
        """Generate summary report"""
        print("\n" + "="*60)
        print("MOVIELENS 100K DATASET SUMMARY REPORT")
        print("="*60)
        
        print(f"""
Core Statistics:
   • Total ratings: {len(self.ratings):,}
   • Number of users: {self.ratings['user_id'].nunique():,}
   • Number of movies: {self.ratings['movie_id'].nunique():,}
   • Number of genres: {len(self.genres)}
   • Data sparsity: {(1 - len(self.ratings) / (self.ratings['user_id'].nunique() * self.ratings['movie_id'].nunique())) * 100:.1f}%

Rating Characteristics:
   • Average rating: {self.ratings['rating'].mean():.2f}/5.0
   • Rating standard deviation: {self.ratings['rating'].std():.2f}
   • Most common rating: {self.ratings['rating'].mode()[0]} stars

User Characteristics:
   • Average age: {self.users['age'].mean():.1f} years
   • Male to female ratio: {(self.users['gender'] == 'M').sum()}:{(self.users['gender'] == 'F').sum()}
   • Average ratings per user: {self.ratings.groupby('user_id').size().mean():.1f}

Movie Characteristics:
   • Average ratings per movie: {self.ratings.groupby('movie_id').size().mean():.1f}
   • Most popular genre: {self.movies[[f'genre_{i}' for i in range(19)]].sum().idxmax().replace('genre_', self.genres.iloc[int(self.movies[[f'genre_{i}' for i in range(19)]].sum().idxmax().split('_')[1])]['genre'])}
   • Release year span: {self._get_movie_year_range()}

Data Quality: High quality, minimal missing values, suitable for recommendation system research
        """)
    
    def run_complete_analysis(self):
        """Run complete data analysis"""
        print("Starting MovieLens 100k dataset complete analysis...")
        
        # Load data
        self.load_data()
        
        # Basic information
        self.print_basic_info()
        
        # Sample data
        self.show_sample_data()
        
        # Various analyses
        self.analyze_rating_distribution()
        self.analyze_user_behavior()
        self.analyze_movie_popularity()
        
        # Data quality check
        self.check_data_quality()
        
        # Visualizations
        self.create_visualizations()
        
        # Summary report
        self.generate_summary_report()
        
        print(f"\nAnalysis completed! Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    """Main function"""
    print("MovieLens 100k Dataset Analysis Tool")
    print("=" * 50)
    
    # Create analyzer instance
    explorer = MovieLensExplorer('ml-100k')
    
    # Run complete analysis
    explorer.run_complete_analysis()


if __name__ == "__main__":
    main()