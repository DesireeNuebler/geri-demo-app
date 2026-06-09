'CONNECT TO MODEL AND PREDICT PAGE'

import streamlit as st
import pickle
import numpy as np

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

expert_features = ["female", "bmi", "insulin", "hghbp", "homa", "gh", "t3", "cortisol","igfi", "age"] # order in training script
# order of X have to be exactly like in training # huhu check this!!!
X = [[female, bmi, insulin, hghbp, homa, gh, t3, cortisol,igf1, age]]
skewed = ["insulin", "gh", "cortisol", "igfi", "homa"]
X_scaled =  np.log1p(X)

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



if st.button("Understand the feature contributions to the prediction."): 
    st.switch_page("pages/about_shap.py")


if st.button("⬅ Back to patient input."): 
    st.switch_page("pages/input.py")

if st.button("⬅ Back"):
        st.switch_page("main.py")
