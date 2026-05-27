'EXPERT FEATURE CORRELATIONPLOT PAGE'

import streamlit as st

col1, col2 = st.columns([2, 1]) 
with col1: 
    st.title("") 
with col2: 
    st.image("app/assets/LMU_Klinikum_Logo.jpg", width=800)
 
st.title("About the Data")



with open("app/assets/corr_plot.html", "r", encoding="utf-8") as f:
        html = f.read()

st.components.v1.html(html, height=1000, scrolling=True)




if st.button("⬅ Back to Data"): 
    st.switch_page("pages/about_data.py")

if st.button("⬅ Back"): 
    st.switch_page("main.py")