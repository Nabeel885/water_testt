import streamlit as st
import joblib
import numpy as np


model = joblib.load('water_model.pkl')

st.title("Water Quality Prediction App 💧")


ph = st.number_input("pH")
hardness = st.number_input("Hardness")
solids = st.number_input("Solids")
chloramines = st.number_input("Chloramines")
sulfate = st.number_input("Sulfate")
conductivity = st.number_input("Conductivity")
organic_carbon = st.number_input("Organic Carbon")
trihalomethanes = st.number_input("Trihalomethanes")
turbidity = st.number_input("Turbidity")

input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                        conductivity, organic_carbon, trihalomethanes, turbidity]])

if st.button("Predict"):
    result = model.predict(input_data)
    if result[0] == 1:
        st.success("✅ Water is Safe to Drink")
    else:
        st.error("❌ Water is NOT Safe to Drink")
