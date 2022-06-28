#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image
import streamlit as st


# In[ ]:
def app():

 st.title("How to Prevent Heart Attack")

 col1, col2 = st.columns(2)

 with col1:
    st.subheader("Maintain healthy diet")
    st.image("diet.jpg")
    """
    A healthy diet can help protect the heart, improve blood pressure and cholesterol, and reduce the risk of type 2 diabetes. A heart-healthy eating plan includes:

    * Vegetables and fruits
    * Beans or other legumes
    * Lean meats and fish
    * Low-fat or fat-free dairy foods
    * Whole grains
    * Healthy fats, such as olive oil
    """

 with col2:
    st.subheader("Be physically active")
    st.image("physical.jpg")
    """
    Regular exercise will make your heart and blood circulatory system more efficient, lower your cholesterol level, and also keep your blood pressure at a healthy level.

    Exercising regularly reduces your risk of having a heart attack. The heart is a muscle and, like any other muscle, benefits from exercise. A strong heart can pump more blood around your body with less effort.
    """

 col3, col4 = st.columns(2)

 with col3:
    st.subheader("Live without smoking")
    st.image("smoking.jpg")
    """
    If you smoke, giving up will reduce your risk of developing CHD.

    Smoking is a major risk factor for developing atherosclerosis (furring of the arteries). It also causes the majority of cases of coronary thrombosis in people under the age of 50.
    """
    
 with col4:
    st.subheader("Get good quality sleep")
    st.image("sleep.jpg")
    """
    People who don't get enough sleep have a higher risk of obesity, high blood pressure, heart attack, diabetes and depression.

    Most adults need at least seven hours of sleep each night. Make sleep a priority in your life. Set a sleep schedule and stick to it by going to bed and waking up at the same times each day. Keep your bedroom dark and quiet, so it's easier to sleep.
    """

 col5, col6 = st.columns(2)


 with col5:
     st.subheader("Reduce your alcohol")
     st.image("alcohol.jpg")
     
     """
     If you drink, do not exceed the maximum recommended limits
     * Men and women are advised not to regularly drink more than 14 units week
     * Spread your drinking over 3 days or more if you drink as much as 14 units a week
     Always avoid binge drinking, as this increases the risk of a heart attack
     """

 with col6:
    st.subheader("Get health screenings")
    st.image("checkup.jpg")

    """
    High blood pressure and high cholesterol can damage the heart and blood vessels. But without testing for them, you probably won't know whether you have these conditions. Regular screening can tell you what your numbers are and whether you need to take action.

    * Blood pressure. Regular blood pressure screenings usually start in childhood. Starting at age 18, blood pressure should be measured at least once every two years to screen for high blood pressure as a risk factor for heart disease and stroke.

    * Cholesterol levels. Adults generally have their cholesterol measured at least once every four to six years.

    * Type 2 diabetes screening. Diabetes is a risk factor for heart disease. screening is recommended beginning at age 45, with retesting every three years

    """
