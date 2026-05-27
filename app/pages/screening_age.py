'SCREENING III PAGE'

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

st.markdown("**3. Age:**")


is_older_than_74 =st.radio("Is your patient at least 70 years old?", options=["Please select...","Yes","No","I am not sure."])

if is_older_than_74 == "Please select...":
        st.warning("No choice has been made.", width=210)


elif is_older_than_74 is not "Yes":
    st.switch_page("pages/screening_exit.py")

else:
     st.switch_page("pages/input.py")