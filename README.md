# Multimodal-Twitter-Sentiment-Analysis

Multimodal-Twitter-Sentiment-Analysis
This repository contains the implementation of a multimodal Twitter Sentiment Analysis project that aims to classify sentiments (positive, negative, or neutral) using both textual and optional contextual features. The project explores multiple machine learning and deep learning models, such as SVM, Decision Tree, Bi-LSTM, and BART, applied to a dataset of 1.6 million tweets. It also leverages GloVe embeddings for richer semantic understanding of the tweets.

### Table of Contents
1. [Overview]
2. [Project Structure]
3. [Dataset]
4. [Preprocessing and Embeddings]
5. [Models Implemented]
6. [Installation]
7. [Usage]
8. [Results]
9. [Future Work]
10. [Contributors]
11. [License]

### Overview
The objective of this project is to analyze sentiments of tweets using both traditional and deep learning approaches. The repository includes:

* Exploratory Data Analysis (EDA) and visualizations.
* Preprocessing and tokenization using GloVe embeddings.
* Comparative performance of SVM, Decision Tree, Bi-LSTM, and BART models.

### Project Structure
📁 Multimodal-Twitter-Sentiment-Analysis/
│
├── 📁 Dataset/                          # Contains the dataset files
│   ├── tweets.csv                       # Main dataset of tweets (2.33 GB)
│   └── glove.6B.100d.txt                 # GloVe embeddings (100D, pre-trained)
│
├── Sentiment_Analysis_Data_Visualization.ipynb  # Jupyter notebook for data exploration and visualizations
├── Sentiment_Analysis_SVM.ipynb                 # SVM model implementation
├── Sentiment_Analysis_Decision_Tree.ipynb        # Decision Tree implementation
├── Sentiment_Analysis_LSTM_modified.ipynb        # Bi-LSTM model implementation with GloVe
├── Sentiment_Analysis_BART.ipynb                 # BART model implementation


