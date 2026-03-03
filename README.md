# 🏥 Multiple Disease Prediction System

A Machine Learning web application that predicts the likelihood of multiple diseases including Liver Disease, Kidney Disease, and Parkinson's Disease using patient data.

***

## 📌 Project Overview

The Multiple Disease Prediction System is a scalable and accurate tool that:

- Assists in early detection of diseases
- Improves decision-making for healthcare providers
- Reduces diagnostic time and cost by providing quick predictions

***

## 🦠 Diseases Predicted

| Disease | Dataset | Algorithm | Target |
| :-- | :-- | :-- | :-- |
| Liver Disease | Indian Liver Patient Dataset | Random Forest | 1 = Disease, 0 = Healthy |
| Kidney Disease | Kidney Disease Dataset | Random Forest | CKD / Not CKD |
| Parkinson's Disease | Parkinson's Dataset | Random Forest | 1 = Parkinson's, 0 = Healthy |


***

## 📁 Project Structure

```
Multiple Disease Prediction/
│
├── data/
│   ├── indian_liver_patient.csv
│   ├── kidney_disease.csv
│   └── parkinsons.csv
│
├── models/
│   ├── liver_model.pkl
│   ├── kidney_model.pkl
│   └── parkinson_model.pkl
│
├── notebooks/
│   └── model_training.ipynb
│
├── app.py
└── README.md
```


***

## 🛠️ Tools \& Technologies

- **Programming Language:** Python 3.x
- **Libraries:** Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn
- **Web Framework:** Streamlit
- **IDE:** VS Code (Jupyter Notebook)
- **Version Control:** GitHub

***

## 📊 Dataset Information

### 🔵 Liver Disease Dataset

- **Source:** Indian Liver Patient Dataset
- **Rows:** 583 patients
- **Features:** Age, Gender, Bilirubin levels, Enzyme levels, Proteins, Albumin
- **Target:** 1 = Liver Disease, 2 = No Disease


### 🔴 Kidney Disease Dataset

- **Source:** Chronic Kidney Disease Dataset
- **Rows:** 400 patients
- **Features:** 25 features including BP, Blood Glucose, Hemoglobin, Creatinine
- **Target:** ckd / notckd


### 🟢 Parkinson's Dataset

- **Source:** Parkinson's Disease Dataset
- **Rows:** 195 voice recordings
- **Features:** 22 voice measurement features (Jitter, Shimmer, HNR, etc.)
- **Target:** 1 = Parkinson's, 0 = Healthy

***

## 🔄 Workflow

```
Input Data → Preprocessing → Model Inference → Prediction Output
```

1. **Input:** User enters symptoms and test results via Streamlit form
2. **Preprocessing:** Missing values handled, categorical data encoded, features scaled
3. **Model Inference:** Trained Random Forest model predicts disease
4. **Output:** Displays prediction result with risk level

***

## 🚀 How to Use the App

1. Open the app in browser
2. Select disease from the **sidebar**
3. Enter patient details in the input form
4. Click the **Predict** button
5. View the prediction result

***

## 📦 Requirements

```
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
xgboost
pickle5
```
