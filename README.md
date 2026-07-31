# QR Phishing Detector

An ML-based QR code phishing detection system. It scans a QR code (or takes a URL directly), extracts 12 URL-based features, and uses a trained Random Forest model to classify the link as **Safe** or **Suspicious** with a risk score.

---

## Project Overview

QR code phishing ("quishing") is a growing cybersecurity threat where attackers embed malicious links inside QR codes to redirect users to fake or harmful websites — bypassing the usual visual cues people rely on to spot a scam link.

This project detects phishing attempts by decoding the QR code in the browser, extracting URL-based features, and running them through a trained machine learning model to predict how risky the link is.

---

## Features

- Upload a QR code image and decode it directly in the browser
- Analyze any URL directly, without needing a QR image
- 12 URL-based features extracted per link (length, HTTPS usage, IP address presence, suspicious keywords, shorteners, special characters, etc.)
- Random Forest classifier trained on a labeled phishing/legitimate URL dataset
- Risk score (0–100%) and Safe / Suspicious verdict
- Clean, terminal-style "security scanner" UI

---

## Tech Stack

**Backend:** Python, Flask, Flask-CORS, scikit-learn, joblib
**Frontend:** HTML, CSS, JavaScript, [jsQR](https://github.com/cozmo/jsQR) for in-browser QR decoding
**Model:** Random Forest Classifier (scikit-learn)

---

## Project Structure

```
Mini project/
├── backend/
│   ├── app.py                  # Flask API (/check endpoint)
│   ├── feature.py              # URL feature extraction (12 features)
│   ├── train_model.py          # Model training script
│   ├── prepare_dataset.py      # Dataset cleaning/prep
│   ├── generate_features.py    # Feature generation for training data
│   ├── phishing_model.pkl      # Trained Random Forest model
│   └── *.csv                   # Datasets
├── frontend/
│   └── index.html              # QR scanner UI (QRISK)
└── requirements.txt
```

---

## How It Works

1. User uploads a QR code image (or types a URL directly) in the frontend.
2. [jsQR](https://github.com/cozmo/jsQR) decodes the QR code in the browser to extract the embedded URL.
3. The URL is sent to the Flask backend via a `POST` request to `/check`.
4. `feature.py` extracts 12 features from the URL, including:
   - URL length
   - HTTPS usage
   - Presence of `@` symbol
   - Presence of hyphens
   - Suspicious keywords (login, verify, secure, bank, etc.)
   - IP address in URL
   - Number of dots, digits, slashes, and special characters
   - Use of known URL shorteners
   - Domain length
5. The trained Random Forest model predicts whether the URL is **Safe** or **Suspicious** and returns a risk score.
6. The frontend displays the verdict, risk score, and feature breakdown.

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/shambhwipriya/QR-PhishingDetector.git
cd QR-PhishingDetector
```

### 2. Set up the backend
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

### 3. Run the Flask server
```bash
python app.py
```
The backend will start at `http://127.0.0.1:5000`.

### 4. Open the frontend
Open `frontend/index.html` in your browser (make sure the backend is running first).

---

## API

### `POST /check`

**Request body:**
```json
{
  "url": "http://secure-login-bank.xyz/verify?id=123"
}
```

**Response:**
```json
{
  "url": "http://secure-login-bank.xyz/verify?id=123",
  "prediction": "Suspicious",
  "risk_score": 86,
  "features": {
    "url_length": 42,
    "has_https": 0,
    "has_at_symbol": 0,
    "has_hyphen": 1,
    "suspicious_word": 1,
    "has_ip": 0,
    "dot_count": 1,
    "digit_count": 3,
    "special_char_count": 3,
    "is_shortened": 0,
    "slash_count": 3,
    "domain_length": 21
  }
}
```

---

## Model Training

The model was trained on a labeled dataset of phishing and legitimate URLs (`phishing_site_urls.csv`) using the following pipeline:

1. `prepare_dataset.py` — cleans and prepares the raw dataset
2. `generate_features.py` — extracts the 12 URL features for every row
3. `train_model.py` — trains a Random Forest Classifier and saves it as `phishing_model.pkl`

---

## Author

**Shambhwi Priya**
College mini project — QR Code Phishing Detection using Machine Learning
