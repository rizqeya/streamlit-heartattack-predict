#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
from multiapp import MultiApp
from apps import prediction, recommendation # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Prediction", prediction.app)
app.add_app("Recommendation", recommendation.app)

# The main app
app.run()





