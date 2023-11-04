import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title("Classifying Iris Flowers")
st.markdown("Toy model to classify Iris flowers as setosa, verginica and vesicolour")

st.header("PLant Features")

sepal_column, petal_column = st.columns(2)

df = pd.read_csv("D:\DataScience\iris.csv")
min_sl, max_sl = min(df['sepal_length']), max(df['sepal_length'])
min_sw, max_sw = min(df['sepal_width']), max(df['sepal_width'])
min_pl, max_pl = min(df['petal_length']), max(df['petal_length'])
min_pw, max_pw = min(df['petal_width']), max(df['petal_width'])

with sepal_column:
    st.text("Sepal Characteristics")
    sepal_length = st.slider("Sepal length in cm", min_sl,max_sl)
    sepal_width = st.slider("Sepal width in cm", min_sw,max_sw)
    
with petal_column:
    st.text("Petal Characteristics")
    petal_length = st.slider("Petal length in cm", min_pl,max_pl)
    petal_width = st.slider("Petal width in cm", min_pw,max_pw)

if st.button("predict Iris flower"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    st.write("The predicted isis flower is: ", predict(input_data)[0])