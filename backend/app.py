import joblib
from flask_cors import CORS
from feature import extract_features
import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
CORS(app)

# Load ML model
model = joblib.load("phishing_model.pkl")


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "online"
    })


@app.route("/check", methods=["POST"])
def check():
    try:

        data = request.get_json()

        if not data or "url" not in data:
            return jsonify({
                "error": "URL is required"
            }), 400

        url = data["url"]

        # Extract Features
        features = extract_features(url)

        feature_list = list(features.values())

        # Prediction
        prediction = model.predict([feature_list])[0]

        probability = model.predict_proba([feature_list])[0][1]

        risk_score = round(probability * 100)

        status = "Suspicious" if prediction == 1 else "Safe"

        # Reasons
        reasons = []

        if features.get("url_length", 0) > 75:
            reasons.append("Long URL")

        if features.get("having_ip", 0) == 1:
            reasons.append("IP Address detected")

        if features.get("https", 1) == 0:
            reasons.append("HTTPS not found")

        if features.get("dots", 0) > 3:
            reasons.append("Too many dots")

        if len(reasons) == 0:
            reasons.append("No major phishing indicators")

        return jsonify({
            "success": True,
            "url": url,
            "prediction": status,
            "risk_score": risk_score,
            "reasons": reasons,
            "features": features
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)