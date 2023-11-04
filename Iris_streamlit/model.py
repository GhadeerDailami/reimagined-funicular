import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("D:\DataScience\iris.csv")
X = df.drop(columns = "species")
y = df.species

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.25, stratify = y)

# train model

rf_model = RandomForestClassifier()
rf_model.fit(X,y)

#checking accuracy
train_score = rf_model.score(X_train, y_train)
test_score = rf_model.score(X_test, y_test)


st.write(train_score, test_score)

joblib.dump(rf_model, "rf_model.sav")

