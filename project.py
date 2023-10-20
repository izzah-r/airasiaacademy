
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
import pickle

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('drive/MyDrive/ColabDataset/Advertising.csv')
df.head()


st.write("""
# Advertising Project

This app predicts the **advertising** types!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 16.0, 100.0, 230.0)
    Radio = st.sidebar.slider('Radio', 10.0, 20.4, 45.9)
    Newspaper = st.sidebar.slider('Newspaper', 45.1, 50.3, 69.3)
    Sale = st.sidebar.slider('Sales', 9.3, 2.5, 22.1)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper,
            'Sales': Sales}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("Advertising.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)

