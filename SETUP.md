# MovieLens 100k Recommendation System - Environment Setup Guide

## Project Dependencies

This project builds a movie recommendation system based on the MovieLens 100k dataset and requires the following Python packages:

### Core Dependencies
- **pandas**: Data processing and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms
- **matplotlib**: Data visualization
- **seaborn**: Statistical plots
- **ipykernel**: Jupyter Notebook support

## Quick Start

### Method 1: Automatic Installation (Recommended)
Run the first code cell of the notebook to automatically install required dependencies:
```python
# Simply run the first cell in the notebook
```

### Method 2: Manual Installation
```bash
# Install all dependencies
pip install -r requirements.txt

# Or install individually
pip install pandas numpy scikit-learn matplotlib seaborn ipykernel jupyter
```

### Method 3: Using conda (Recommended for Data Science)
```bash
# Create new environment
conda create -n movielens python=3.11

# Activate environment
conda activate movielens

# Install dependencies
conda install pandas numpy scikit-learn matplotlib seaborn jupyter ipykernel

# Or use pip to install requirements.txt
pip install -r requirements.txt
```

## Project File Structure

```
3033-061/
├── ml-100k/                                    # MovieLens dataset
├── requirements.txt                            # Project dependency configuration
├── movielens_dataset_explorer.py              # Dataset analysis script
├── movielens_comprehensive_english_system.ipynb # Recommendation system(without multimodal but compared PCA and SVD) development notebook
├── multimodal_recommendation_english.ipynb     # Multimodal Recommendation system development notebook
├── SETUP.md                                   # This configuration guide
└── README.md                                  # Project description
```

## Usage Instructions

1. **Data Exploration**:
   ```bash
   python movielens_dataset_explorer.py
   ```

2. **Recommendation System Development**:
   - Open and run `movielens_comprehensive_english_system.ipynb` for recommendation system without multimodal features but comparing PCA and SVD methods
   - Open and run `multimodal_recommendation_english.ipynb` for multimodal recommendation system development

## Frequently Asked Questions

### Q: Missing ipykernel when running notebook?
A: Run the following commands:
```bash
pip install ipykernel
python -m ipykernel install --user --name=movielens
```

### Q: Problems with Chinese character display in plots?
A: The system will automatically try to use the SimHei font. If it doesn't work, please install Chinese fonts or use English labels.

### Q: Out of memory issues?
A: The MovieLens 100k dataset is relatively small. If you encounter memory problems, you can:
- Reduce batch size
- Use data sampling
- Increase system memory

## Expected Output

- **Data Analysis Script**: Generates `movielens_analysis.png` visualization charts
- **Recommendation System**: Trained collaborative filtering models and recommendation results

## Next Steps

After completing the first phase, you can consider:
- Adding more recommendation algorithms (SVD, NMF, etc.)
- Integrating content features (movie genres, actors, etc.)
- Implementing hybrid recommendation systems
- Adding web interface for display

---
**Note**: Automatic dependency installation may take a few minutes when running for the first time. Please be patient.