<h1>Multimodal-Twitter-Sentiment-Analysis</h1>

<p>This repository contains the implementation of a multimodal Twitter Sentiment Analysis project aimed at classifying sentiments from tweets. The project uses multiple machine learning and deep learning models, including <strong>SVM</strong>, <strong>Decision Tree</strong>, <strong>Bi-LSTM</strong>, and <strong>BART</strong>. It also leverages <strong>GloVe embeddings</strong> for richer semantic understanding of the tweets.</p>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#overview">Overview</a></li>
  <li><a href="#project-structure">Project Structure</a></li>
  <li><a href="#dataset">Dataset</a></li>
  <li><a href="#preprocessing-and-embeddings">Preprocessing and Embeddings</a></li>
  <li><a href="#models-implemented">Models Implemented</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#results">Results</a></li>
  <li><a href="#future-work">Future Work</a></li>
  <li><a href="#contributors">Contributors</a></li>
  <li><a href="#license">License</a></li>
</ul>

<h2 id="overview">Overview</h2>
<p>The objective of this project is to analyze sentiments of tweets using both traditional and deep learning approaches. The repository includes:</p>
<ul>
  <li>Exploratory Data Analysis (EDA) and visualizations.</li>
  <li>Preprocessing and tokenization using GloVe embeddings.</li>
  <li>Comparative performance of SVM, Decision Tree, Bi-LSTM, and BART models.</li>
</ul>

<h2 id="project-structure">Project Structure</h2>
<ul>
  <li><strong>Multimodal-Twitter-Sentiment-Analysis/</strong>
    <ul>
      <li><strong>Dataset/</strong> – Contains the dataset files
        <ul>
          <li><code>tweets.csv</code> – Main dataset of tweets (2.33 GB)</li>
          <li><code>glove.6B.100d.txt</code> – GloVe embeddings (100D, pre-trained)</li>
        </ul>
      </li>
      <li><code>Sentiment_Analysis_Data_Visualization.ipynb</code> – Jupyter notebook for data exploration and visualizations</li>
      <li><code>Sentiment_Analysis_SVM.ipynb</code> – SVM model implementation</li>
      <li><code>Sentiment_Analysis_Decision_Tree.ipynb</code> – Decision Tree implementation</li>
      <li><code>Sentiment_Analysis_LSTM_modified.ipynb</code> – Bi-LSTM model implementation with GloVe</li>
      <li><code>Sentiment_Analysis_BART.ipynb</code> – BART model implementation</li>
    </ul>
  </li>
</ul>

<h2 id="dataset">Dataset</h2>
<ul>
  <li><strong>tweets.csv:</strong> A CSV file containing 1.6 million tweets with corresponding sentiment labels (positive, negative, neutral).</li>
  <li><strong>glove.6B.100d.txt:</strong> Pre-trained GloVe word embeddings with a 100-dimensional vector space.</li>
</ul>
<p><strong>Dataset Link:</strong> You can download the dataset from <a href="https://drive.google.com/drive/folders/1wm48DA5C-uvGN5FBz8DuptPT4iSDg5PP?usp=drive_link" target="_blank">Google Drive</a>.</p>
<p><strong>Dataset Fields:</strong></p>
<ul>
  <li><code>tweet_id</code>: Unique identifier for each tweet.</li>
  <li><code>text</code>: The tweet's content.</li>
  <li><code>sentiment</code>: The sentiment label (positive, negative).</li>
</ul>
