# QR Phishing Detector 

An ML-based QR Phishing Detection System that analyzes URLs and predicts whether a website is *Safe* or *Suspicious* using machine learning and URL feature extraction.

---

##  Project Overview

QR Code phishing (Quishing) is a cybersecurity threat where attackers use malicious QR codes to redirect users to fake or harmful websites.

This project aims to detect phishing URLs by extracting important URL-based features and applying a trained machine learning model to generate a prediction along with a risk score.

The system provides a simple interface where users can enter a URL and get instant security analysis.

---

##  Features

*  URL-based phishing detection
*  Machine learning based classification
*  Risk score generation
*  Safe / Suspicious prediction
*  URL feature extraction
*  Real-time analysis using Flask API
*  User-friendly web interface

---

#  Tech Stack

## Frontend

* HTML
* CSS
* JavaScript

## Backend

* Python
* Flask

## Machine Learning

* Scikit-learn
* Pandas
* NumPy
* Joblib

---

#  Project Structure

```
QR-Phishing-Detector
│
├── backend
│   │
│   ├── app.py
│   │   └── Flask API server and model prediction logic
│   │
│   ├── feature.py
│   │   └── URL feature extraction module
│   │
│   ├── train_model.py
│   │   └── Machine learning model training script
│   │
│   ├── phishing_model.pkl
│   │   └── Trained ML model file
│   │
│   └── requirements.txt
│       └── Required Python dependencies
│
├── frontend
│   │
│   ├── index.html
│   │   └── User interface
│   │
│   ├── style.css
│   │   └── Frontend styling
│   │
│   └── script.js
│       └── Frontend logic and API connection
│
├── screenshots
│   └── Project screenshots
│
└── README.md
```

---

#  Installation & Setup

## 1. Clone Repository

```
git clone <repository-url>
```

Navigate into project:

```
cd QR-Phishing-Detector
```

---

# Backend Setup

Go to backend folder:

```
cd backend
```

Install required dependencies:

```
pip install -r requirements.txt
```

Run Flask server:

```
python app.py
```

Backend will start at:

```
http://127.0.0.1:5000
```

---

# Frontend Setup

Open frontend folder.

Run the frontend using Live Server or any local server.

The frontend communicates with the Flask backend API for URL analysis.

---

#  Machine Learning Workflow

The system follows these steps:

1. URL dataset collection
2. Data preprocessing
3. URL feature extraction
4. Machine learning model training
5. Model saving using Joblib
6. Flask API integration
7. Real-time URL prediction

---

#  URL Features Analyzed

The model extracts different URL-based security features such as:

* URL length
* HTTPS availability
* IP address presence
* Special characters
* Domain-related information
* Suspicious URL patterns

---

#  Output

The system provides:

* URL classification:

  * Safe
  * Suspicious

* Risk Score:

  * Percentage-based security risk estimation

* Extracted URL features

---

#  Future Improvements

* QR image scanning support
* Browser extension integration
* Deep learning based phishing detection
* Real-time threat intelligence integration
* Mobile application support

---

#  Applications

* Personal cybersecurity protection
* Safe browsing assistance
* QR code security checking
* Phishing awareness and prevention

---

# 👩 Author

*Shambhwi Priya*

Computer Science Engineering Student

---

#  License

This project is developed for educational and research purposes.

```
```
