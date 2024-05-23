# Car Price Prediction

This project aims to predict car prices using a machine learning model. The project includes data exploration, data preprocessing, model training, and deployment using Streamlit and GitHub.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [Model Deployment](#model-deployment)
- [Running the App Locally](#running-the-app-locally)
- [Deploying on Streamlit Cloud](#deploying-on-streamlit-cloud)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project utilizes a dataset containing details about various cars. The primary goal is to predict the selling price of a car based on features such as year, kilometers driven, fuel type, seller type, transmission, and owner.

## Dataset

The dataset used for this project can be downloaded from [CAR DETAILS Dataset](#). It includes the following features:
- `year`: Year of manufacture
- `km_driven`: Kilometers driven
- `fuel`: Fuel type (e.g., Petrol, Diesel, CNG, LPG, Electric)
- `seller_type`: Seller type (e.g., Dealer, Individual, Trustmark Dealer)
- `transmission`: Transmission type (e.g., Manual, Automatic)
- `owner`: Number of previous owners

## Data Preprocessing

Data preprocessing steps include:
- Handling missing values
- Encoding categorical variables
- Scaling numerical features

## Model Training

Several machine learning models were trained and evaluated, including:
- Linear Regression
- Random Forest Regressor
- Lasso Regression
- K-Nearest Neighbors Regressor

The best model was selected based on performance metrics and saved for deployment.

## Model Deployment

The trained model is deployed using Streamlit, which allows for an interactive web application to predict car prices.

## Running the Ap
