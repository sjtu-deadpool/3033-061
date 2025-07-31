# MovieLens 100k 推荐系统 - 环境配置指南

## 项目依赖

本项目基于MovieLens 100k数据集构建电影推荐系统，需要以下Python包：

### 核心依赖
- **pandas**: 数据处理和分析
- **numpy**: 数值计算
- **scikit-learn**: 机器学习算法
- **matplotlib**: 数据可视化
- **seaborn**: 统计图表
- **ipykernel**: Jupyter Notebook支持

## 快速开始

### 方法1：自动安装（推荐）
运行notebook的第一个代码cell，会自动安装所需依赖：
```python
# 运行notebook中的第一个cell即可
```

### 方法2：手动安装
```bash
# 安装所有依赖
pip install -r requirements.txt

# 或者逐个安装
pip install pandas numpy scikit-learn matplotlib seaborn ipykernel jupyter
```

### 方法3：使用conda（推荐用于数据科学）
```bash
# 创建新环境
conda create -n movielens python=3.11

# 激活环境
conda activate movielens

# 安装依赖
conda install pandas numpy scikit-learn matplotlib seaborn jupyter ipykernel

# 或者使用pip安装requirements.txt
pip install -r requirements.txt
```

## 项目文件结构

```
3033-061/
├── ml-100k/                                    # MovieLens数据集
├── requirements.txt                            # 项目依赖配置
├── movielens_dataset_explorer.py              # 数据集分析脚本
├── movielens_recommendation_system.ipynb      # 推荐系统开发notebook
├── SETUP.md                                   # 本配置指南
└── README.md                                  # 项目说明
```

## 使用说明

1. **数据探索**：
   ```bash
   python movielens_dataset_explorer.py
   ```

2. **推荐系统开发**：
   打开并运行 `movielens_recommendation_system.ipynb`

## 常见问题

### Q: notebook运行时提示缺少ipykernel？
A: 运行以下命令：
```bash
pip install ipykernel
python -m ipykernel install --user --name=movielens
```

### Q: 图表中文显示有问题？
A: 系统会自动尝试使用SimHei字体，如果无效请安装中文字体或使用英文标签。

### Q: 内存不足？
A: MovieLens 100k数据集相对较小，如果遇到内存问题，可以：
- 减少批处理大小
- 使用数据抽样
- 增加系统内存

## 预期输出

- **数据分析脚本**：生成 `movielens_analysis.png` 可视化图表
- **推荐系统**：训练好的协同过滤模型和推荐结果

## 下一步

完成第一阶段后，可以考虑：
- 添加更多推荐算法（SVD、NMF等）
- 集成内容特征（电影流派、演员等）
- 实现混合推荐系统
- 添加Web界面展示

---
**注意**：首次运行时自动安装依赖可能需要几分钟时间，请耐心等待。