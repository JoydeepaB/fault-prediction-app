<div align="center">

# ⚙️ Fault Prediction App : Bearing Fault Prediction from Vibration Signals.

### *Can an AI "hear" a machine breaking down — before it actually breaks?*

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn&logoColor=white)](https://scikit-learn.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-FF6F00?logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#)

**100% test accuracy** · **4 models benchmarked** · **Live predictions in your browser**

</div>

---

## 💡 The Idea

Bearings fail silently — by the time a machine sounds "wrong" to the human ear, the damage is often already done. This project teaches a model to read a bearing's **vibration signature** and flag trouble early, turning a wall of raw sensor noise into one clear answer:

> **Normal · Inner-Race Fault · Outer-Race Fault · Ball Fault**

No manual inspection. No guesswork. Just numbers in, diagnosis out — live, in a browser.

---

## 🏆 Model Showdown

Four very different approaches went head-to-head on the same data:

| Model | Test Accuracy | Verdict |
|---|:---:|---|
| 🌲 **Random Forest** | **100%** | ✅ **Deployed** — fast, interpretable, zero GPU needed |
| 🔵 SVM | 100% | Strong, but a black box on *why* |
| 🧠 CNN (1D, Keras) | 100% | Matched the leaders — at 15x the training cost |
| ⚡ XGBoost | 87.8% | Solid, but untuned here |

**The twist:** the "simple" classical model matched a deep neural network stride for stride — and still tells you *exactly* which feature tipped its decision. Sometimes the smartest model isn't the fanciest one.

---

## 🧬 What the Model "Sees"

Every vibration window gets reduced to 10 tell-tale numbers:

```
mean · rms · std · kurtosis · skewness
peak · crest_factor · dominant_freq
spectral_energy · spectral_entropy
```

Think of it as a vibration "fingerprint" — unique enough to tell a healthy bearing from a dying one.

## 📦 Dataset

Trained on the **CWRU (Case Western Reserve University)** bearing vibration dataset — the gold-standard public benchmark used across bearing-fault-diagnosis research.

---

## ⚡ Quick Start

```bash
git clone https://github.com/JoydeepaB/fault-prediction-app.git
cd fault-prediction-app
pip install -r requirements.txt
python app.py
```

Open **`http://127.0.0.1:5000`**, punch in a few readings, hit **Predict** — done.

## 🗂️ Under the Hood

```
fault-prediction-app/
├── app.py                 ← Flask API — loads the model, serves predictions
├── model.pkl               ← Trained Random Forest
├── scaler.pkl               ← Feature scaler
├── label_encoder.pkl        ← Fault-label decoder
├── requirements.txt
└── templates/
    └── index.html            ← The web form you actually see
```

## 🧪 Proof It Works

Fed a **real, known-Normal** sample straight from the dataset:

| mean | rms | kurtosis | crest_factor | spectral_entropy |
|:---:|:---:|:---:|:---:|:---:|
| 0.0124 | 0.0760 | -0.2437 | 2.866 | 7.281 |

**→ Prediction: `Normal`** ✅ *(verified against ground truth, not a lucky guess)*

---

## 🛠️ Built With

`Python` `Flask` `scikit-learn` `XGBoost` `TensorFlow / Keras` `joblib` `HTML/CSS/JS`

## 🔮 What's Next

- [ ] 🌐 Public deployment on Render
- [ ] 🎛️ Hyperparameter tuning for XGBoost
- [ ] 🔊 Robustness testing under noisy/real-world conditions
- [ ] 📊 Live feature-importance chart in the UI

---

<div align="center">

### 👤 Joydeepa Banik
*B.Tech , NIT Agartala*

</div>
