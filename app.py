from flask import Flask, render_template, request
import joblib
import json

app = Flask(__name__)

# Load model, normalizer, and feature names
model = joblib.load("rf_model.pkl")
normalizer = joblib.load("normalizer.pkl")

with open("feature_names.json") as f:
    feature_names = json.load(f)

@app.route('/')
def index():
    return render_template("index.html", features=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs in correct order
        input_data = [float(request.form.get(feat, 0)) for feat in feature_names]
        normalized_data = normalizer.transform([input_data])
        prediction = model.predict(normalized_data)[0]

        result = "High Risk of Cirrhosis" if prediction == 1 else "Low Risk of Cirrhosis"
        return render_template("result.html", prediction=result)

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
