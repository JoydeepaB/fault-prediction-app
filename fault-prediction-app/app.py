from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
le = joblib.load("label_encoder.pkl")

FEATURE_ORDER = [
    "mean", "rms", "std", "kurtosis", "skewness",
    "peak", "crest_factor", "dominant_freq",
    "spectral_energy", "spectral_entropy"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    try:
        features = np.array([[float(data[k]) for k in FEATURE_ORDER]])
    except KeyError as e:
        return jsonify({"error": f"Missing feature: {e}"}), 400

    features_scaled = scaler.transform(features)
    pred = model.predict(features_scaled)
    label = le.inverse_transform(pred)[0]
    return jsonify({"prediction": label})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)