import streamlit as st
import pickle
import numpy as np

# Load models
liver_model    = pickle.load(open('models/liver_model.pkl', 'rb'))
kidney_model   = pickle.load(open('models/kidney_model.pkl', 'rb'))
parkinson_model = pickle.load(open('models/parkinson_model.pkl', 'rb'))

st.title("🏥 Multiple Disease Prediction System")
st.sidebar.title("Select Disease")
disease = st.sidebar.selectbox("Choose:", ["Liver Disease", "Kidney Disease", "Parkinson's Disease"])

# ---- LIVER ----
if disease == "Liver Disease":
    st.header("🔵 Liver Disease Prediction")
    age = st.number_input("Age", 1, 100)
    gender = st.selectbox("Gender", ["Male", "Female"])
    tb = st.number_input("Total Bilirubin")
    db = st.number_input("Direct Bilirubin")
    alkphos = st.number_input("Alkaline Phosphotase")
    alamine = st.number_input("Alamine Aminotransferase")
    aspartate = st.number_input("Aspartate Aminotransferase")
    tp = st.number_input("Total Proteins")
    albumin = st.number_input("Albumin")
    ag_ratio = st.number_input("Albumin and Globulin Ratio")

    if st.button("Predict Liver Disease"):
        gender_enc = 1 if gender == "Male" else 0
        input_data = np.array([[age, gender_enc, tb, db, alkphos, alamine, aspartate, tp, albumin, ag_ratio]])
        result = liver_model.predict(input_data)
        st.success("⚠️ Liver Disease Detected" if result[0] == 1 else "✅ No Liver Disease")

# ---- KIDNEY ----
elif disease == "Kidney Disease":
    st.header("🔴 Kidney Disease Prediction")
    st.info("Enter patient values for 25 features (age, bp, sg, al, su, etc.)")
    # Add number inputs for each of the 25 features
    features = ['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr',
                'bu','sc','sod','pot','hemo','pcv','wc','rc',
                'htn','dm','cad','appet','pe','ane']
    inputs = [st.number_input(f, value=0.0) for f in features]
    if st.button("Predict Kidney Disease"):
        result = kidney_model.predict([inputs])
        st.success("⚠️ CKD Detected" if result[0] == 1 else "✅ No Kidney Disease")

# ---- PARKINSON ----
elif disease == "Parkinson's Disease":
    st.header("🟢 Parkinson's Disease Prediction")
    feature_names = ['MDVP:Fo(Hz)','MDVP:Fhi(Hz)','MDVP:Flo(Hz)','MDVP:Jitter(%)','MDVP:Jitter(Abs)',
                     'MDVP:RAP','MDVP:PPQ','Jitter:DDP','MDVP:Shimmer','MDVP:Shimmer(dB)',
                     'Shimmer:APQ3','Shimmer:APQ5','MDVP:APQ','Shimmer:DDA','NHR','HNR',
                     'RPDE','DFA','spread1','spread2','D2','PPE']
    inputs = [st.number_input(f, value=0.0, format="%.5f") for f in feature_names]
    if st.button("Predict Parkinson's"):
        result = parkinson_model.predict([inputs])
        st.success("⚠️ Parkinson's Detected" if result[0] == 1 else "✅ No Parkinson's")
