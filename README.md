# 🚨 Cyberbullying Detection on Twitter

A machine learning project that detects cyberbullying on Twitter using multiple supervised models and natural language processing (NLP) techniques.

---

## 📂 Project Structure

```
cyberbullying-detection/
├── app.py
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
└── (cyberbullying_model.pkl) [Downloaded at runtime]
```

---

## 💾 Model Download (Google Drive)

The main ML model (`cyberbullying_model.pkl`) is **not pushed to GitHub** due to size limitations.

Instead, it is downloaded at runtime using `gdown` from Google Drive.

### Model File Info:
- **Google Drive File ID**: `10Sujo4zk-EkPUB01DtONm98kS0aovKew`

### Download code in `app.py`:

```python
import gdown
import os

MODEL_FILE_ID = '10Sujo4zk-EkPUB01DtONm98kS0aovKew'
MODEL_FILENAME = 'cyberbullying_model.pkl'

def download_model(file_id, output=MODEL_FILENAME):
    url = f'https://drive.google.com/uc?id={file_id}'
    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)

download_model(MODEL_FILE_ID)
```

---

## 🛠 Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/Ar9605/cyberbullying-detection.git
cd cyberbullying-detection
```

2. **Install dependencies**

Make sure to use a Python version compatible with the dependencies (Python 3.9–3.11 recommended).

```bash
pip install -r requirements.txt
```

> ⚠️ Note: `numpy==1.26.4` is used to ensure compatibility with Streamlit and model serialization.

---

## 🚀 Run the App Locally

```bash
streamlit run app.py
```

Open the provided local URL in your browser to interact with the app.

---

## 🧠 ML Models Used

- TF-IDF Vectorizer
- Logistic Regression (or other supervised models)
- Trained using labeled cyberbullying tweets dataset

---

## ⚙️ Dependencies

See `requirements.txt`:

```
streamlit==1.35.0
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.4.2
joblib==1.4.2
gdown==5.1.0
nltk==3.8.1
textblob==0.18.0
```

---

## 👨‍💻 Author

**Abhinav Raj**  
B.Tech CSE | SRM IST  