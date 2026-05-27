'SCREENING II PAGE'

import streamlit as st 

col1, col2 = st.columns([2, 1]) 
with col1: 
    st.title("") 
with col2: 
    st.image("app/assets/LMU_Klinikum_Logo.jpg", width=800)


st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")


st.markdown("**2. IGF1:**")


col1, col2 = st.columns([2, 1])

with col1:
    has_igf1_deficient =st.radio("Does your patient suffer from IGF1 deficient?", options=["Please select...","Yes","No","I am not sure."])

with col2:    
    st.info("IGF1 Deficiency:  \nFemale: <67 ng/ml  \nMale: <86 ng/ml", width=210)

if has_igf1_deficient == "Please select...":
        st.warning("No choice has been made.", width=210)


elif has_igf1_deficient is not "Yes":
    st.switch_page("pages/screening_exit.py")

else:
     st.switch_page("pages/screening_age.py")