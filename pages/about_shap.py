'SHAP FOR SPECIFIC PREDICTION PAGE'

import streamlit as st
import pickle
import numpy as np
import shap
import pandas as pd
import matplotlib.pyplot as plt

col1, col2 = st.columns([2, 1]) 
with col1: 
    st.title("") 
with col2: 
    st.image("assets/LMU_Klinikum_Logo.jpg", width=800)

st.title("Feature Contribution for the Patients Prediction")


# age = st.session_state["age"] 
# sex = st.session_state["sex"] 
# igf1 = st.session_state["igf1"] 
# cortisol = st.session_state["cortisol"]
# t3 = st.session_state["t3"] 
# homa = st.session_state["homa"] 
# gh = st.session_state["gh"] 
# hghbp = st.session_state["hghbp"] 
# insulin = st.session_state["insulin"] 
# bmi = st.session_state["bmi"] 

# st.markdown("### Patient Characteristics")
# cols = st.columns(2)

# items = [
#     ("Age", age),
#     ("Sex", sex),
#     ("IGF‑1", igf1),
#     ("Cortisol", cortisol),
#     ("T3", t3),
#     ("HOMA", homa),
#     ("GH", gh),
#     ("hGHBP", hghbp),
#     ("Insulin", insulin),
#     ("BMI", bmi)
# ]

# for i, (name, value) in enumerate(items):
#     with cols[i % 2]:
#         st.metric(label=name, value=value)

# female =  1 if sex == "Female" else 0

# X = [[female, bmi, insulin, hghbp, homa, gh, t3, cortisol,igf1, age]] # order in training
# skewed = ["insulin", "gh", "cortisol", "igfi", "homa"]
# X_scaled =  np.log1p(X)

with open("assets/explainer.pkl", "rb") as f: 
    explainer = pickle.load(f) # trained explainer
# shap_values = explainer(X_scaled)
# shap_values_pos = shap_values[:, :, 1]  
#shap.plots.waterfall(shap_values_pos)
 # print(shap_values)

X_scaled = pd.DataFrame([[0,2,1,1,1,1,3,3,2,2]])  # example only
shap_values = explainer(X_scaled)
shap_values_pos = shap_values[:, :, 1] 
fig, ax = plt.subplots()
shap.plots.waterfall(shap_values_pos[0], show=False)
st.pyplot(fig)



if st.button("Understand feature contribution in the whole model."): 
    st.switch_page("pages/about_shap_gen.py")




if st.button("⬅ Back to prediction"): 
    st.switch_page("pages/predict.py")


if st.button("⬅ Back"): 
    st.switch_page("main.py")
