import streamlit as st
import pandas as pd
import pickle

# Path to the saved model file
filename = 'best_model.sav'

# Load the model
try:
    with open(filename, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error(f"The model file '{filename}' was not found.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()

st.title('Car Price Prediction')

# Input features
feature1 = st.number_input('Year')
feature2 = st.number_input('Kilometers Driven')
feature3 = st.selectbox('Fuel Type', [0, 1, 2, 3, 4])
st.caption("Fuel Type: Petrol:0, Diesel:1, CNG:2, LPG:3, Electric:4")
feature4 = st.selectbox('Seller Type', [0, 1, 2])
st.caption("Seller Type: Dealer:0, Individual:1, Trustmark Dealer:2")
feature5 = st.selectbox('Transmission', [0, 1])
st.caption("Transmission: Manual:0, Automatic:1")
feature6 = st.selectbox('Owner', [0, 1, 2, 3, 4])
st.caption("Owner: First Owner:0, Second Owner:1, Third Owner:2, Fourth & Above Owner:3, Test Drive Car:4")

# Predict button
if st.button('Predict'):
    input_data = pd.DataFrame([[feature1, feature2, feature3, feature4, feature5, feature6]], columns=['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner'])
    try:
        prediction = model.predict(input_data)
        st.write(f'Predicted Price: {prediction[0]}')
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

# Predict button
if st.button('Predict'):
    input_data = pd.DataFrame([[feature1, feature2, feature3, feature4, feature5, feature6]], columns=['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner'])
    prediction = model.predict(input_data)
    st.write(f'Predicted Price: {prediction[0]}')
