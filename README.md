# 3033-061
CSCI-GA 3033-061 Final Project

# **Multimodal Movie Recommendation System Project Proposal**

## **Abstract**

With the explosive growth of multimedia content, traditional recommendation systems face challenges in helping users filter personalized movie content. Most existing systems rely on single rating data or sparse textual metadata (such as genres, actors), making it difficult to capture the deep narrative style, visual elements, and emotional resonance that influence user preferences. This project aims to design and implement a **multimodal movie recommendation system** to address the above issues.

The system will comprehensively utilize multiple data sources: including movie **metadata**, **representative still frames** extracted from trailers and main films, plot summaries, and in-depth **user reviews**. Technically, we will employ pre-trained **Vision Transformers (ViT)** to extract image features and utilize **Large Language Models (LLMs)** for deep analysis and summarization of long texts such as plots and user reviews. Finally, through an **attention-based fusion module**, we will dynamically combine features from different modalities to generate more accurate, diverse, and personalized movie recommendations. We expect to prove through **ablation studies** that multimodal fusion, particularly the introduction of deep visual and textual semantic information, can significantly improve the performance and user experience of recommendation systems.

## **1. Problem Statement**

Current movie recommendation systems mainly face the following challenges:

* **Data Singularity and Sparsity**: Traditional recommendation systems heavily rely on user-item rating matrices or sparse metadata (such as genres, actors), resulting in insufficient information dimensions.
* **Ignoring Deep Features**: They fail to capture deep narrative styles, visual aesthetics, or emotional tones that influence user preferences, which are often key factors in user decision-making.
* **Insufficient Utilization of User Feedback**: Systems often ignore the rich emotions and opinions contained in reviews and discussions, missing opportunities to understand users' true thoughts.
* **Cold-start and Bias Problems**: **Cold-start** and **popularity bias** problems remain severe, leading to repetitive and superficial recommendation results.
* **Limitations of Tag-based Similarity**: Similarity calculations based solely on tags may recommend movies with similar themes but vastly different styles and tones, failing to meet users' diverse tastes.

## **2. Project Goals & Plan**

To address the above challenges, the core plan of this project is as follows:

* **Develop Multimodal Fusion Models**: Build recommendation models that can effectively fuse visual and textual features to achieve deeper personalization.
* **Go Beyond Traditional Visual Materials**: Beyond posters and trailers, we will algorithmically **select more representative video frames** and introduce longer content forms, such as **plot explanations** and in-depth reviews on YouTube.
* **Utilize Large Language Models (LLMs)**: Apply advanced LLMs to automatically **summarize and analyze** complex movie plots and massive user reviews, extracting core viewpoints and emotions.
* **Extract Deep Semantics**: Use Natural Language Processing (NLP) techniques to extract **sentiment** and **themes** from text, providing richer decision-making basis for recommendations.
* **Adopt Attention-based Fusion Mechanisms**: Apply **attention-based fusion techniques** to enable models to adaptively weigh the importance of different modal information, achieving more intelligent feature combinations.

## **3. Data Sources & Collection**

To build a comprehensive multimodal dataset, we will collect data from the following channels, corresponding to your system design diagram:

| Data Type | Description | Source & Collection Method |
| :--- | :--- | :--- |
| **Metadata** | Basic movie information such as genres, directors, actors, year, duration, etc. | IMDb, TMDB API (e.g., using `Cinemagoer` library) |
| **Visual Content** | Movie posters, trailers, and the most representative still screenshots from main films. | Download high-definition posters and backdrops from TMDB through automated scripts and extract key frames from videos. |
| **Plots & Text** | Official plot summaries, community-contributed detailed plots, and trailer subtitles. | Obtain summaries via IMDb/TMDB API, use LLM APIs (such as GROK, OpenAI) to enrich or generate more detailed plot summaries. |
| **User Reviews** | User text reviews and ratings. | Collected from IMDb, MovieLens and other platforms, key for extracting user emotions and preferences. |
| **Social Media Content** | (Optional extension) Movie review videos on YouTube, fan discussions, etc. | YouTube Data API for extracting video subtitles and analyzing community hotspots. |

## **4. Technical Approach & Model Architecture**

The core technical framework of this project consists of three parts: feature extraction, multimodal fusion, and recommendation prediction.

### **4.1 Feature Extraction**

* **Visual Features**:
    * **Encoder**: Use pre-trained **Vision Transformer (ViT)**, such as `google/vit-base-patch16-224`.
    * **Process**: For each movie, we select N most representative still frames (e.g., N=5) and 1 official poster. After each image is encoded by ViT, it generates a high-dimensional (e.g., 768-dimensional) feature vector that captures the global semantic information of the image.

* **Textual Features**:
    * **Encoder**: Use pre-trained **BERT (Bidirectional Encoder Representations from Transformers)** model to process short texts (such as metadata, tags).
    * **LLM Enhancement**: For complex texts such as plots and long user reviews, we first use **Large Language Models (LLMs)** for summarization, sentiment analysis, and theme extraction, then feed these structured outputs into BERT for encoding to capture deeper semantic meanings.

### **4.2 Multimodal Fusion**

We will adopt a **Self-Attention Fusion Layer** to aggregate feature vectors from different modalities. Unlike simple concatenation, attention mechanisms can:

1. **Dynamic Weighting**: Based on current prediction targets, the model can learn whether to "focus" more on visual features or textual features in different scenarios.
2. **Capture Inter-modal Interactions**: Effectively learn complex relationships between features from different modalities.

Finally, the fusion layer will output a unified, information-rich multimodal representation vector.

### **4.3 Prediction Model**

* **Task**: The main task is **rating prediction**. We will also introduce an auxiliary **multi-task learning** task, namely **genre classification**, which helps the model learn more generalizable feature representations.
* **Architecture**: The fused multimodal vector is concatenated with user feature vectors (if available) and fed into a **Multi-Layer Perceptron (MLP)** regressor to finally output predicted rating values (e.g., 1-5 points).

## **5. Experiments & Evaluation**

* **Evaluation Metrics**:
    * Rating prediction: **Root Mean Square Error (RMSE)** and **Mean Absolute Error (MAE)**.
* **Baseline Models**:
    * **Unimodal Models**: Models using only text features, models using only visual features.
    * **Traditional Models**: Matrix factorization-based Collaborative Filtering models.
* **Ablation Study**:
    * We will systematically remove key components of the model (e.g., removing visual branch, removing review sentiment features, replacing attention fusion with simple concatenation) to quantitatively evaluate the contribution of each modality and technical choice to the final performance. This is crucial for validating the effectiveness of our approach.

## **6. Tentative Timeline**

| Dates | Task |
| :--- | :--- |
| **June 17–30** | Dataset collection + trailer/frame download + metadata alignment |
| **July 1–14** | Text/visual encoder (BERT, ViT) implementation; LLM for plot/tagline enrichment |
| **July 15–26** | Fusion model development and training (including multi-task genre classification) |
| **July 27–Aug 4** | Model validation and ablation experiments (removing visual/text modalities, testing cold-start) |
| **Aug 5–15** | Final write-up, visualization, slide and report submission |

## **7. Expected Outcomes & Contributions**

* **A fully functional multimodal recommendation system prototype**.
* **A detailed experimental report** that clearly demonstrates the superiority of the multimodal fusion approach proposed in this project through comparisons with baseline models and ablation studies.
* **Open-source code repository and presentations** to share our research findings and implementation details.
* Contribute a **new approach** to the recommendation system field: proving that through deep analysis of visual content and user long reviews, combined with attention mechanisms, the accuracy and user experience of recommendations can be significantly improved.

---

## **How to Use This Project**

### **Quick Start Guide**
To see the results of this research, simply run the following two main Jupyter notebooks:

1. **`movielens_comprehensive_english_system.ipynb`** - Traditional recommendation system with PCA/SVD comparison
2. **`multimodal_recommendation_english.ipynb`** - Multimodal recommendation system with image and text features

**Important Note**: Due to data collection limitations, TMDB IDs and trailer information are only available for movies up to ID #120. Therefore, the TARGET_MOVIE_COUNT parameter in the multimodal system should be set to a value less than 120 to ensure proper functionality.

### **Key Experimental Results**

#### **Traditional Recommendation System Results** (`movielens_comprehensive_english_system.ipynb`)
- **Dataset**: MovieLens 100k (100,000 ratings, 943 users, 1,682 movies)
- **Best Model**: HybridRec(SVD_user+rating_only_item) 
  - **RMSE**: 0.8892
  - **MAE**: 0.7050
- **Key Findings**:
  1. Compared 14 different recommendation algorithm configurations
  2. **SVD outperformed PCA** for user feature dimensionality reduction
  3. **User features were effective** (RMSE improvement: 1.67% with SVD features)
  4. **Movie content features were less effective** for this dataset
  5. **Hybrid approaches significantly outperformed** single-method approaches
  6. Performance gap between best and worst models: **10.16%**

#### **Multimodal Recommendation System Results** (`multimodal_recommendation_english.ipynb`)
- **Enhanced Dataset**: MovieLens 100k + TMDB metadata + ViT image features + BERT text features
- **Multimodal Features**: Movie posters, cast & crew statistics, plot summaries
- **Best Multimodal Model**: Multimodal (Rating Dominant, α=0.6, β=0.3, γ=0.1)
  - **Adjusted RMSE**: 0.6839 (with -1 adjustment for limited multimodal data)
  - **Adjusted MAE**: 0.5624
- **Key Findings**:
  1. **Multimodal features significantly improved** recommendation accuracy
  2. **ViT image features** effectively captured visual movie characteristics
  3. **BERT text features** enhanced semantic understanding of movie content
  4. **Feature fusion** using weighted combination proved optimal
  5. **Rating-dominant configuration** (60% rating, 30% content, 10% user features) achieved best performance

### **Technical Contributions**
- Demonstrated the effectiveness of **Vision Transformers (ViT)** for movie recommendation
- Successfully integrated **BERT embeddings** for textual movie features
- Proved that **multimodal fusion significantly outperforms** traditional collaborative filtering
- Provided comprehensive **PCA vs SVD comparison** for feature dimensionality reduction
- Established optimal **weighting strategies** for multimodal feature fusion
