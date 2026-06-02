'MAIN PAGE'

import streamlit as st
import pandas as pd


col1, col2 = st.columns([2, 1]) 
with col1: 
    st.title("") 
with col2: 
    st.image("assets/LMU_Klinikum_Logo.jpg", width=800)


st.title("GERI - A Demo App for Risk Prediction")
st.subheader("""**Hello, my name is GERI!**  
This is short for **G**eriatric
**E**ndocrine
**R**esistance
**I**nsights!
""")
st.markdown("This application has been developed to help to predict the risk for hormone resistance\
             for eldery patients. Requesting certain pages might require some seconds.")


st.markdown("🎉 **Welcome to the app!** 🎉")
st.toast("App loaded successfully!")



if st.button("Please send me some ballons!"):
    st.balloons()

if st.button("Go to prediction."):
    st.switch_page("pages/screening_sarc.py")


if st.button("Tell me more about the underlying model."):
    st.switch_page("pages/about_model.py")  


if st.button("Tell me more about the used data."):
    st.switch_page("pages/about_data.py")
