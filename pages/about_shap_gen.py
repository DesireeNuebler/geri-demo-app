'GEN SHAP PAGE'

import streamlit as st

col1, col2 = st.columns([2, 1]) 
with col1: 
    st.title("") 
with col2: 
    st.image("assets/LMU_Klinikum_Logo.jpg", width=800)
 
st.title("Shap Values for the Random Forest Model")

st.markdown("Think of SHAP values as an unknown currency:\
             We cannot explicity calculate each predictors effect but we can tell how much of the currency\
             a predictor owns and how much this currency pushes to positive or to negative class. Here, the positive class refers to being GH-resistant.\
             \nSome predictors contributions correlate with other features contributions.")

st.image("assets/shap_values.png", width=800)


if st.button("⬅ Back to Start."): 
    st.switch_page("main.py")

if st.button("Go to prediction."): 
    st.switch_page("pages/screening_sarc.py")
