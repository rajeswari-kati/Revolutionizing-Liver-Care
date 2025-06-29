# 🩺 Liver Cirrhosis Risk Prediction using Machine Learning

This is a web-based application that predicts the risk of liver cirrhosis using a Random Forest Classifier trained on clinical and lifestyle features. The app is built with Flask and allows healthcare professionals to input patient data and receive a prediction in real-time.

# https://sweet-gingersnap-f9803c.netlify.app/

📊 Project Highlights

* 🔬 Model: Random Forest Classifier (Scikit-learn)
* 📈 Accuracy: 100% (on training data, based on selected features)
* 🌐 Web Framework: Flask
* 📦 Deployment Ready: Render / Railway / Heroku
* 📁 Input Features: Age, Gender, Alcohol Use, Diabetes Result, Albumin, Bilirubin, SGPT/ALT
* 📌 Frontend: HTML5 + Bootstrap

📂 Project Structure

# Liver-cirrhosis-predictor/

# app.py                    # Flask application

# train\_model.py            # Script to train \& export model

# rf\_model.pkl              # Trained ML model

# normalizer.pkl            # Feature normalizer (L1)

# feature\_names.json        # List of model input features

# requirements.txt          # Python dependencies

# templates/( index.html, result.html )

⚙️ How to Run Locally

1. Install Dependencies
   pip install -r requirements.txt
2. Start Flask App
   python app.py
3. Open in Browser
   http://127.0.0.1:5000

🧪 Sample Features (used in model)

* Age
* Gender (0 = female, 1 = male)
* Duration of alcohol consumption (years)
* Diabetes Result (0 = no, 1 = yes)
* Albumin (g/dl)
* Total Bilirubin (mg/dl)
* SGPT/ALT (U/L)

🚀 Deployment Guide (Render or Railway)

1. Create requirements.txt and Procfile (already included)
2. Push code to GitHub
3. On Render or Railway:

   * New → Web Service
   * Build command: pip install -r requirements.txt
   * Start command: gunicorn app:app

Your app will be live on your free hosted URL!

👨‍💼 Project details:
# Team id:LTVIP2025TMID47117
# Katireddy Rajeswari
Guided under SmartBridge - IIC Internship 2025
Role: Project Leader \& ML Developer
Project: "Revolutionizing Liver Care through AI"

📃 License
This project is for educational and research use under the MIT License.

