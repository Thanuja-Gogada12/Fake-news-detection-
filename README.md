# 📰 Fake News Detection App

A simple and interactive Machine Learning-based web app to detect whether a news article is **REAL** or **FAKE** using natural language processing and classification techniques.

## 🚀 Project Overview

This project is designed as a mini-project for Computer Science Engineering students who are beginners in **Data Science using Python**.

It uses a **TF-IDF vectorizer** and a **PassiveAggressiveClassifier** to classify the given news article as **REAL** or **FAKE**. The web interface is built with **Streamlit**.

## 🧠 Technologies Used

- 🐍 Python
- 📘 Pandas
- ✂️ Scikit-learn
- 🧪 Joblib
- 💬 TF-IDF Vectorizer
- 🖼️ Streamlit

## 📁 Project Structure
fake-news-detection-app/
│
├── app.py # Streamlit frontend
├── model.pkl # Trained ML model (PassiveAggressiveClassifier)
├── tfidf.pkl # Saved TF-IDF vectorizer
├── Fake.csv # Fake news dataset
├── True.csv # Real news dataset
├── train_model.ipynb # Jupyter Notebook to train and save model
├── sample_inputs.txt # Sample texts for testing
├── requirements.txt # List of dependencies
└── README.md # Project description (this file)

## 🔍 How to Run the Project

### 1. Clone the repository
git clone https://github.com/your-username/fake-news-detection-app.git
cd fake-news-detection-app
2. Install dependencies
Make sure you have Python installed, then run:
pip install -r requirements.txt
3. Run the Streamlit app
streamlit run app.py
🧪 Sample Inputs for Testing
Here are some examples you can use in the app:
✅ Real News
NASA announces new Artemis moon mission timeline
❌ Fake News
Pope Francis endorses Donald Trump for re-election campaign
More examples are available in sample_inputs.txt.


