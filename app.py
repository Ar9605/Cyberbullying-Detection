import os
import gdown
import streamlit as st
import joblib
import numpy as np
from textblob import TextBlob
import re
import string

# =======================
# 📥 Download model from Google Drive
# =======================

MODEL_FILE_ID = '10Sujo4zk-EkPUB01DtONm98kS0aovKew'

def download_model(file_id, output='cyberbullying_model.pkl'):
    url = f'https://drive.google.com/uc?id={file_id}'
    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)

download_model(MODEL_FILE_ID)


# =======================
# 🔍 Text Preprocessing
# =======================
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'\@w+|\#','', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def add_sentiment_features(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

# =======================
# 🔮 Load Model and Vectorizer
# =======================
try:
    model = joblib.load("cyberbullying_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
except Exception as e:
    st.error(f"Error loading model or vectorizer: {e}")
    st.stop()

# =======================
# 🎯 Streamlit App
# =======================
st.title("🚫 Cyberbullying Detection App")
st.markdown("Enter a tweet to check if it contains cyberbullying content.")

user_input = st.text_area("Type your tweet here:", "")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        cleaned_text = preprocess_text(user_input)
        polarity, subjectivity = add_sentiment_features(cleaned_text)
        tfidf_features = vectorizer.transform([cleaned_text]).toarray()
        features = np.hstack([tfidf_features, np.array([[polarity, subjectivity]])])

        prediction = model.predict(features)[0]
        st.success(f"Prediction: **{prediction}**")
