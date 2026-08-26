'INSERT VALUE PAGE'

import streamlit as st

col1, col2 = st.columns([2, 1]) 
with col1: 
    st.title("") 
with col2: 
    st.image("assets/LMU_Klinikum_Logo.jpg", width=800)

st.title("Insert Patient Values...")
st.markdown("Please enter the following values for your patient. The default values represent the average patient found in our dataset. We do not store any inserted values.")


# exemplary for expert based features

sex = st.radio(
"Enter Sex",
options=["Female", "Male"]
)

age = st.number_input(
"Enter age",
min_value=75,
max_value=120,
value=84,      # average
step=1
)

homa = st.number_input(
"Enter HOMA Index",
min_value=1.0,
max_value=8.0, # average
value=2.4,     
step=0.05
)


insulin = st.number_input(
"Enter Insulin",
min_value=2.0,
max_value=25.0, # average
value=9.0,     
step=0.05
)


hghbp = st.number_input(
"Enter GHBP",
min_value=100.0,
max_value=700.0, # default: average
value=605.01,     
step=0.05
)



gh = st.number_input(
"Enter GH",
min_value=0.0,
max_value=15.0, # average
value=1.4,     
step=0.05
)


t3 = st.number_input(
"Enter fT3",
min_value=0.0,
max_value=7.0, # average
value=2.2,     
step=0.05
)

cortisol = st.number_input(
"Enter Cortisol",
min_value=1.0,
max_value=45.0, # average
value=18.1,     
step=1.0
)

bmi = st.number_input(
    "Enter BMI",
        min_value=15.0,
max_value=31.0,
value=25.2,      # average
step=0.1
)



igf1 = st.number_input(
"Enter IGF-I",
min_value=5,
max_value=90, # average
value=52,     
step=1
)


if st.button("⮕ Predict resistance for the patient given values."):
    st.session_state["age"] = age
    st.session_state["sex"] = sex
    st.session_state["igf1"] = igf1
    st.session_state["cortisol"] = cortisol
    st.session_state["t3"] = t3
    st.session_state["homa"] = homa
    st.session_state["gh"] = gh
    st.session_state["hghbp"] = hghbp
    st.session_state["insulin"] = insulin
    st.session_state["bmi"] = bmi
    st.switch_page("pages/predict.py")

if st.button("⬅ Back to Start."): 
    st.switch_page("main.py")