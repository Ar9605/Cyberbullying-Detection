# 🚨 Cyberbullying Detection App

A machine learning-based web application that detects different types of cyberbullying from social media text using a stacking ensemble classifier.

Built using:
- 🐍 Python
- 📊 Scikit-learn, TF-IDF
- 🤖 Logistic Regression, Random Forest, SVM, Neural Net
- 🌐 Streamlit for the frontend
- 🧠 TextBlob for sentiment analysis

---

## 💡 Features

- Classifies text into multiple cyberbullying categories (e.g., hate speech, not cyberbullying, etc.)
- Uses a **Stacking Classifier** with multiple base models
- Incorporates **sentiment analysis** features
- Simple and interactive Streamlit frontend

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/cyberbullying-detector.git
cd cyberbullying-detector
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🗃️ Folder Structure

```
cyberbullying-detector/
├── app.py                    # Streamlit frontend
├── cyberbullying_model.pkl   # Trained stacking model
├── tfidf_vectorizer.pkl      # Fitted TF-IDF vectorizer
├── requirements.txt          # List of dependencies
└── README.md                 # This file
```

---

## 📦 Requirements

You can install dependencies manually or use the included `requirements.txt`:

```
text
streamlit
scikit-learn
textblob
nltk
joblib
numpy
pandas
```


---

## 🧠 Model Info

- **TF-IDF** used to convert text into numerical vectors (max 5000 features)
- **Sentiment features**: polarity and subjectivity
- **Final model**: Stacking Classifier with Logistic Regression as meta-learner
- Balanced with **SMOTE** to address class imbalance


---

## 👤 Author

**Abhinav Raj**  
Bachelor's in Computer Science – SRM IST  
Passionate about Machine Learning, NLP, and Data Analysis.
