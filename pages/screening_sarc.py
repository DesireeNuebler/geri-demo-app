'SCREENING I PAGE'

import streamlit as st 


col1, col2 = st.columns([2, 1]) 
with col1: 
    st.title("") 
with col2: 
    st.image("assets/LMU_Klinikum_Logo.jpg", width=800)

st.title("Screening for Model")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("**The model is trained for a certain target population. Please answer the following three screening questions.**")
st.markdown("")
st.markdown("")

st.markdown("**1. Sarcopenia:**")

has_sarcopenia = st.radio("Does your patient has a sarcopenia diagnosis?", options=["Please select...","Yes","No","I am not sure."])

if has_sarcopenia == "Please select...":
    st.warning("No choice has been made.", width=210)

elif has_sarcopenia != "Yes":
    st.switch_page("pages/screening_exit.py")

else:
     st.switch_page("pages/screening_igf1.py")
