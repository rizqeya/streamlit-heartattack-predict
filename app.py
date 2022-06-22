#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import joblib
import collections


# Function Format
binary_options = {
    1:"Yes",
    0:"No"}

diabetes_options = {
    2:"Yes",
    1:"Borderline Diabetes",
    0:"No"}

income_options = {
    4:">$50,000",
    3:"$35,000 - $50,000",
    2:"$25,000 - $35,000",
    1:"$15,000 - $25,000",
    0:"<$15,000"}

checkup_options = {
    4:"5 Year or More",
    3:"Past 5 Year",
    2:"Past 2 Year",
    1:"Past Year",
    0:"Never"}

# Title
st.header("Heart Attack Prediction App")

# Input bar 1
weight = st.number_input("Weight", min_value=0, max_value=1000)

# Input bar 2
sleeptime = st.number_input("How many hours do you sleep?", min_value=0, max_value=24)

# Dropdown input
diabetes = st.selectbox("Do you have diabetes?", (0, 1, 2), format_func=lambda x: diabetes_options.get(x))
exercise = st.selectbox("Do you Exercise regularly?", (0, 1), format_func=lambda x: binary_options.get(x))
smoker = st.selectbox("Do you Smoke regularly?", (0, 1), format_func=lambda x: binary_options.get(x))
bmi = st.selectbox("Do you Obese?", (0, 1), format_func=lambda x: binary_options.get(x))
heavydrinker = st.selectbox("Are you a heavy drinker?", (0, 1), format_func=lambda x: binary_options.get(x))
income = st.selectbox("How much is your income annualy?", (0, 1, 2, 3, 4), format_func=lambda x: income_options.get(x))
bingedrinker = st.selectbox("Are you a binge drinker?", (0, 1), format_func=lambda x: binary_options.get(x))
checkup = st.selectbox("When was the last time you did a general checkup?", (0, 1, 2, 3, 4), format_func=lambda x: checkup_options.get(x))

output = ""
input_dict = {"Diabetes" : diabetes, "SleepTime" : sleeptime, "Exercise" : exercise, "Smoker" : smoker, "BMI" : bmi, "Weight" : weight,
    "HeavyDrinker" : heavydrinker, "Income" : income, "BingeDrinker" : bingedrinker, "Checkup" : checkup}

 
input_df = pd.DataFrame([input_dict])
print(type(input_dict))

# If button is pressed
if st.button("Submit"):
    
    # Unpickle classifier
    clf = joblib.load("clf.pkl")
    
    prediction = clf.predict(input_df)
    if prediction == 1:
        prediction = "Berisiko"
    else :
        prediction = "Normal"
    st.subheader(f"Prediksi risiko serangan jantung yaitu {prediction}")




