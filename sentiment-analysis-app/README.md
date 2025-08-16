# 🎬 Sentiment Analysis of IMDB Reviews

This is a simple **Sentiment Analysis Web App** built with **Python, scikit-learn, and Streamlit**.  
It predicts whether a movie review is **Positive 🙂** or **Negative 🙁**.

---

## 🔍 Overview
- **Dataset**: [IMDB 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)  
- **Preprocessing**: text cleaning, stopwords removal, stemming  
- **Features**: TF-IDF Vectorization (1-2 grams, 20k features)  
- **Models**: Logistic Regression & Multinomial Naive Bayes  
- **Deployment**: Streamlit App  

---

## 🚀 How to Run Locally

1. Clone this repo or download the files:
   ```bash
   git clone https://github.com/YOUR-USERNAME/sentiment-analysis-app.git
   cd sentiment-analysis-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser at:
   ```
   http://localhost:8501
   ```

---

## 🌐 Deploy on Streamlit Cloud

1. Push this repo to GitHub.  
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and connect your GitHub account.  
3. Select the repo and file `app.py`.  
4. Deploy and get a live link to share! 🎉  

---

## 📊 Example

**Input:**  
```
"This movie was amazing! The actors did a great job."
```

**Output:**  
```
Prediction: Positive 🙂
```

---

## 🔗 Links
- Dataset: [Kaggle IMDB Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- Streamlit: [Streamlit Website](https://streamlit.io/)
