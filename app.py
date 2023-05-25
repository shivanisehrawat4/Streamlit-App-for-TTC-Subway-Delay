import streamlit as st
from predict import show_predict
from explore import show_explore


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Explore":
    show_explore()
else:
    show_predict()