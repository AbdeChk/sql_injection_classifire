#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import joblib
import pickle
from PIL import Image



model =  joblib.load('sql_injection_pipeline.pkl')


#image = Image.open('./sql_2019272.png')
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image('sql_img.png')

with col3:
    st.write(' ')



#st.title('SQL Injection Classifier')
st.markdown("<h1 style='text-align: center; color: white;'>SQL Injection Classifier</h1>", unsafe_allow_html=True)

#st.markdown("<h2 style='text-align: center; color: black;'>Smaller headline in black </h2>", unsafe_allow_html=True)

#st.image(image, width=200)


# Create a text input box
query = st.text_input('Enter a query')

# Make a prediction when the user clicks a button
if st.button('Predict'):
    # Make a prediction using the trained model
    prediction = model.predict([query])[0]

    # Display the prediction
    if prediction == 0:
        st.write('The query is classified as SQL injection ❌')
    else:
        st.write('The query is classified as legitimate ✅')



