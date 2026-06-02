'GEN DATA PAGE'

import streamlit as st

col1, col2 = st.columns([2, 1]) 
with col1: 
    st.title("") 
with col2: 
    st.image("assets/LMU_Klinikum_Logo.jpg", width=800)
 
st.title("About the Data")


with open("assets/spider_plot.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=500)
st.markdown("The mean values over the groups have been normalized to be able to display them together in a radar plot due to different orignal feature scales.")
st.markdown(
    "**This plot is interactive — hover to see values and click legend items to show or hide groups.**"
)



if st.button("See Correlations"): 
    st.switch_page("pages/about_data_corr.py")
    

if st.button("⬅ Back"): 
    st.switch_page("main.py")
