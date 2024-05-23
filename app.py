import streamlit as st
import pandas as pd
import joblib

model = joblib.load(r'best_model.sav')

st.title('Car Price Prediction')

# Input features
feature1 = st.number_input('year')
feature2 = st.number_input('km_driven')
feature3 = st.number_input('fuel')
st.caption("Petrol:0, Diesel:1, CNG:2, LPG:3, Electric:4")
feature4 = st.number_input('seller_type')
st.caption("Dealer:0, Individual:1, Trustmark Dealer:2")
feature5 = st.number_input('transmission')
st.caption("Manual:0, Automatic:1")
feature6 = st.number_input('owner')
st.caption("First Owner:0, Second Owner:1, Third Owner:2, Fourth & Above Owner:3, Test Drive Car:4")
# Add all necessary input fields...

# Predict button
if st.button('Predict'):
    input_data = pd.DataFrame([[feature1, feature2, feature3, feature4, feature5, feature6]], columns=['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner'])
    prediction = model.predict(input_data)
    st.write(f'Predicted Price: {prediction[0]}')
