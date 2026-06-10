'CONNECT TO MODEL AND PREDICT PAGE'

import streamlit as st
import pickle
import numpy as np
import pandas as pd

col1, col2 = st.columns([2, 1]) 
with col1: 
    st.title("") 
with col2: 
    st.image("assets/LMU_Klinikum_Logo.jpg", width=800)
 
st.title("Model Prediction")

with open("assets/model.pkl", "rb") as f: 
    model = pickle.load(f)


age = st.session_state["age"] 
sex = st.session_state["sex"] 
igf1 = st.session_state["igf1"] 
cortisol = st.session_state["cortisol"]
t3 = st.session_state["t3"] 
homa = st.session_state["homa"] 
gh = st.session_state["gh"] 
hghbp = st.session_state["hghbp"] 
insulin = st.session_state["insulin"] 
bmi = st.session_state["bmi"] 

st.markdown("### Patient Characteristics")
cols = st.columns(2)

items = [
    ("Age", age),
    ("Sex", sex),
    ("IGF‑1", igf1),
    ("Cortisol", cortisol),
    ("T3", t3),
    ("HOMA", homa),
    ("GH", gh),
    ("hGHBP", hghbp),
    ("Insulin", insulin),
    ("BMI", bmi)
]


for i, (name, value) in enumerate(items):
    with cols[i % 2]:
        st.metric(label=name, value=value)

female =  1 if sex == "Female" else 0


expert_features = ["female", "bmi", "insulin", "hghbp", "homa", "gh", "t3", "cortisol","igf1", "age"] # order in training
skewed = ["insulin", "gh", "cortisol", "igfi", "homa"]

insulin =  np.log1p(insulin)
gh = np.log1p(gh)
cortisol = np.log1p(cortisol)
igfi = np.log1p(igf1)
homa = np.log1p(homa)

original_cols = [
    "female", "bmi", "insulin", "hghbp", "homa",
    "gh", "t3", "cortisol", "igfi", "age"
]

X_scaled = pd.DataFrame(
    [[female, bmi, insulin, hghbp, homa, gh, t3, cortisol, igfi, age]],
    columns=original_cols
)


prediction = model.predict(X_scaled)
predicted_prob = model.predict_proba(X_scaled)[:, 1].item()

predicted_label = "RESISTANT" if prediction == 1 else "SENSITIVE"

# HUHU some variables have to be scaled and or log transformed!! 
# HUHU: Check predictions in code vs in app. app predictions seem to be unreasonable

st.write("")
st.write("")
st.write("")


label_colors = {
    "RESISTANT": "darkred",
    "SENSITIVE": "darkblue"
}

colored_label = f"<span style='color:{label_colors[predicted_label]}; font-weight:bold;'>{predicted_label}</span>"


st.markdown(
    f"**For the given patient the model predicts {colored_label}.**\n\n"
    f"**The risk for being resistant given the model is {predicted_prob * 100:.2f}%.**",
    unsafe_allow_html=True
)

st.info("The predicted probability serves as a risk estimate and lies between 0.2 and 0.6. Given a decision in favor of GH-resistance for predicted probabilities > 0.49 resulted in 1 out of 3 correctly detected GH-resistant patients in model testing procedure.")

if st.button("Understand the feature contributions to the prediction."): 
    st.switch_page("pages/about_shap.py")


if st.button("⬅ Back to patient input."): 
    st.switch_page("pages/input.py")

if st.button("⬅ Back to Start."):
        st.switch_page("main.py")
