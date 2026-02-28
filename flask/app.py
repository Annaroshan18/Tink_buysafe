from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import os
import numpy as np
from buysafe import extract_features, convert_to_model_features

# ---------------- APP SETUP ----------------
app = Flask(__name__)
CORS(app)

# Load trained ML model once at startup
model = joblib.load("fraud_model.pkl")


# ---------------- HEALTH CHECK ----------------
@app.route("/", methods=["GET"])
def home():
     return render_template("index.html")
     


# ---------------- PREDICTION ROUTE ----------------
@app.route("/predict", methods=["POST"])
def predict():

    # Check request data
    if not request.json or "url" not in request.json:
        return jsonify({"error": "No URL provided"}), 400

    url = request.json["url"]

    # Extract website features
    raw_features = extract_features(url)

    if not raw_features:
        return jsonify({"error": "Could not analyze website"}), 400

    # Convert to ML features
    features = convert_to_model_features(raw_features)

    feature_array = np.array([[
        features["https"],
        features["ssl_valid"],
        features["refund"],
        features["contact"],
        features["owner_hidden"],
        features["suspicious_words"],
        features["fake_discount"],
        features["domain_age_days"]
    ]])

    # Predict
    fraud_prob = model.predict_proba(feature_array)[0][1]
    trust_score = int((1 - fraud_prob) * 100)

    # Risk category
    if trust_score >= 80:
        risk = "Safe"
    elif trust_score >= 50:
        risk = "Moderate Risk"
    else:
        risk = "High Risk"

    return jsonify({
        "url": url,
        "trust_score": trust_score,
        "risk": risk
    })



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render gives PORT
    app.run(host="0.0.0.0", port=port)