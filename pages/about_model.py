'ABOUT MODEL PAGE'

import streamlit as st

col1, col2 = st.columns([2, 1]) 
with col1: 
    st.title("") 
with col2: 
    st.image("app/assets/LMU_Klinikum_Logo.jpg", width=800)
 
st.title("About the Model: Support Vector Machines")


st.subheader("The Model")
st.markdown("The trained model is a **Support Vector Machine**.\
             The model tries to find a complex function in a higher dimensional feature space that seperates the two class,i.e. resistant and not resistant.\
             In contrast to many other models SVM exploits geometry in finding a good decision function.\
             The **kernel trick** involves the transformation from the orignal feature space into a higher dimensional feature space.\
             In this higher dimensional feature space the classes are linearly seperatable.\
             \n\nAssuming complex non linear relationships, models like the classical logistic regression fail to seperate the two classes:")
st.image("app/assets/log_reg_illustration.jpeg", width=350)
st.markdown("In constrast, the SVM kernel trick solves the problem using transformation.")
if st.button("Illustrate SVM kernel trick."):
    st.switch_page("pages/about_kerneltrick.py")



st.subheader("Explainability")
st.markdown("For explainability **SHAP values** have been generated.The idea of SHAP values is to break down any machine learning model predictions and explain the contribution\
             of each feature. Coming from game theory, each feature is allocated an importance value for a specific prediction, \
            showing how much that feature pushed the result away from the average prediction.")


if st.button("Understand SHAP values of the trained model."): 
    st.switch_page("pages/about_shap_gen.py")


if st.button("⬅ Back"): 
    st.switch_page("main.py")

