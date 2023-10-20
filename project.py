
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
    TV = st.sidebar.slider('TV', 4.3, 7.9, 5.4)
    Radio = st.sidebar.slider('Radio', 2.0, 4.4, 3.4)
    Newspaper = st.sidebar.slider('Newspaper', 1.0, 6.9, 1.3)
    Sale = st.sidebar.slider('Sales', 0.1, 2.5, 0.2)
    data = {'TV': TV,
            'Radio': Radio,
            'petal_length': petal_length,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("Advertising.h5", "wb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)

