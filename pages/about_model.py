'ABOUT MODEL PAGE'

import streamlit as st

col1, col2 = st.columns([2, 1]) 
with col1: 
    st.title("") 
with col2: 
    st.image("assets/LMU_Klinikum_Logo.jpg", width=800)
 
st.title("The Random Forest Model")

st.subheader("The Model")
st.markdown("The trained model is a **Random Forest Model**. Assuming complex non linear relationships, models like the classical logistic regression fail to seperate the two classes.Machine learning models overcome this restriction and handle correlated predictors gracefully.
The basic concept of a random forest model is a decision tree that tries to find a complex function to seperate the patients into GH-sensitive and GH-resistant by sequently learing decision rules. 
This idea is repeated multiple times resulting in a model consisting a various independent trees with each one voting for a class given the input.")

st.subheader("Explainability")
st.markdown("For explainability **SHAP values** have been generated.The idea of SHAP values is to break down any machine learning model predictions and explain the contribution\
             of each feature. Coming from game theory, each feature is allocated an importance value for a specific prediction, \
            showing how much that feature pushed the result away from the average prediction.")


if st.button("Understand SHAP values of the trained model."): 
    st.switch_page("pages/about_shap_gen.py")


if st.button("⬅ Back"): 
    st.switch_page("main.py")
