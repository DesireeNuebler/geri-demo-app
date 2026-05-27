'KERNEL TRICK PAGE'

import streamlit as st 

col1, col2 = st.columns([2, 1]) 
with col1: 
    st.title("") 
with col2: 
    st.image("app/assets/LMU_Klinikum_Logo.jpg", width=800)


st.title("The SVM Kernel Trick")

col1, col2 = st.columns([10, 1])   # adjust ratio to move left/right


with open("app/assets/kernel_animation.html", "r") as f:
    kernel_anim_html = f.read()


with col1:
     st.iframe(srcdoc=kernel_anim_html, height=1000, scrolling=True)


if st.button("⬅ Back"): 
    st.switch_page("main.py")

    
if st.button("⬅ Back to Model"): 
    st.switch_page("pages/about_model.py")
