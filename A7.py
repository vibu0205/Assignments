import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("glass_model.pkl")

# UI Title
st.title("🔍 Glass Type Predictor")
st.markdown("Enter chemical compositions below to predict the **Glass Type**:")

# Inputs
ri = st.number_input("Refractive Index (RI)", value=1.52, step=0.01)
na = st.number_input("Sodium (Na)", value=13.0, step=0.1)
mg = st.number_input("Magnesium (Mg)", value=3.0, step=0.1)
al = st.number_input("Aluminum (Al)", value=1.0, step=0.1)
si = st.number_input("Silicon (Si)", value=72.0, step=0.1)
k  = st.number_input("Potassium (K)", value=0.5, step=0.1)
ca = st.number_input("Calcium (Ca)", value=8.0, step=0.1)
ba = st.number_input("Barium (Ba)", value=0.0, step=0.1)
fe = st.number_input("Iron (Fe)", value=0.0, step=0.1)

# Predict button
if st.button("Predict"):
    input_data = np.array([[ri, na, mg, al, si, k, ca, ba, fe]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Glass Type: {prediction}")
