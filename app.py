import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download stopwords (first run only)
nltk.download('stopwords')

# Load the trained model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Setup preprocessing tools
english_stopwords = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text: str) -> str:
    """Clean input text: remove HTML, lowercase, remove non-letters, stopwords, and apply stemming."""
    text = re.sub(r'<.*?>', ' ', str(text))   # remove HTML tags
    text = text.lower()                       # lowercase
    text = re.sub(r'[^a-z]+', ' ', text)      # keep only letters
    tokens = text.split()
    cleaned = [stemmer.stem(t) for t in tokens if t not in english_stopwords]
    return ' '.join(cleaned)

# Streamlit UI
st.title("🎬 IMDB Sentiment Classifier")
st.write("Type a movie review and get a **Positive** or **Negative** prediction.")

# Text input
user_text = st.text_area("Write your review here:", height=150)

# Button to analyze
if st.button("Analyze"):
    if user_text.strip():
        txt = clean_text(user_text)
        vec = vectorizer.transform([txt])
        pred = model.predict(vec)[0]
        label = "Positive 🙂" if int(pred) == 1 else "Negative 🙁"
        st.subheader(f"Prediction: {label}")
    else:
        st.warning("⚠️ Please type something first.")
