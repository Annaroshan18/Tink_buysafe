# 🛒 BuySafe — Shopping Link Trust Detector

## Project Description

BuySafe is a web-based security tool that analyzes online shopping links and determines whether a website is safe, suspicious, or high-risk.
It helps users avoid scam shopping pages by examining domain details, security indicators, and behavioral patterns using Machine Learning.

When a user pastes a product or store link, BuySafe:

1. Extracts website security & content features
2. Processes them using a trained ML model
3. Generates a trust score
4. Explains risk level with reasons

The goal is to protect users from fake Instagram shops, phishing stores, and newly created scam websites.

---

##  Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask
* Flask-CORS

### Machine Learning

* Scikit-learn (Random Forest)
* SMOTE (imbalanced-learn)
* Joblib (model saving)

### Data Extraction

* Requests
* BeautifulSoup
* Python-Whois
* SSL / Socket analysis

---

##  Features

*  URL safety detection
*  Trust score (0-100)
*  Risk classification (Safe / Moderate / High Risk)
*  Domain age detection
*  SSL certificate verification
*  Refund & contact policy detection
*  Suspicious words detection
*  Fake discount detection
*  Machine Learning based prediction

---

##  Installation

Clone the project and install dependencies:

```bash
git clone <your-repo-link>
cd BuySafe_Backend
python -m pip install -r requirements.txt
```

---

##  Run the Command

Start backend server:

```bash
python app.py
```

Server runs at:

```
http://127.0.0.1:5000
```

Open frontend `index.html` using Live Server.

---

## Screenshots



Example:

```
<img width="1888" height="915" alt="Screenshot 2026-02-28 093334" src="https://github.com/user-attachments/assets/85b55539-86c8-4962-a009-b0afa119f317" />
screenshots/homepage.png
screenshots/loading.png
screenshots/result.png
```

---

##  Demo Video

(Add your demo link here)

```
https://your-demo-video-link
```

---

##  Architecture Diagram

```
User
 ↓
Frontend (HTML/CSS/JS)
 ↓ API Call
Flask Backend
 ↓
Feature Extractor
 ↓
ML Model (fraud_model.pkl)
 ↓
Trust Score Response
 ↓
Frontend Display
```

---

## API Documentation

### POST /predict

Analyzes a website link.

**Request**

```json
{
  "url": "https://example.com"
}
```

**Response**

```json
{
  "url": "https://example.com",
  "trust_score": 72,
  "risk": "Moderate Risk"
}
```

---

## Team Members

* Anna Roshan – Developer/Frontent
* Ansha Mehrin M N – Backend / ML

---

## License

This project is licensed under the MIT License.
You are free to use, modify and distribute for educational purposes.
