'SHAP FOR SPECIFIC PREDICTION PAGE'

import streamlit as st
import shap

col1, col2 = st.columns([2, 1]) 
with col1: 
    st.title("") 
with col2: 
    st.image("assets/LMU_Klinikum_Logo.jpg", width=800)

st.title("Feature Contribution for the Patients Prediction")



with open("assets/model.pkl", "rb") as f: 
    model = pickle.load(f)
explainer = shap.Explainer(model,)
shap_values = explainer(X_test)
# Compute SHAP values
shap_values_pos = shap_values[:, :, 1]  
shap_values = explainer(X_test)

# Select one observation (e.g., index 0)
shap.plots.waterfall(shap_values_pos[0])


if st.button("Understand feature contribution in the whole model."): 
    st.switch_page("pages/about_shap_gen.py")




if st.button("⬅ Back to prediction"): 
    st.switch_page("pages/predict.py")


if st.button("⬅ Back"): 
    st.switch_page("main.py")
