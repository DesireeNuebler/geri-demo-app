import streamlit as st


st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("**The model should not be used. Based on your value the patient differs from the target population.**")

if st.button("⬅ Back to Start"): 
    st.switch_page("main.py")

if st.button("Go back to first screening."): 
    st.switch_page("pages/screening_sarc.py")