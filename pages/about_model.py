'ABOUT MODEL PAGE'

import streamlit as st

col1, col2 = st.columns([2, 1]) 
with col1: 
    st.title("") 
with col2: 
    st.image("assets/LMU_Klinikum_Logo.jpg", width=800)
 
st.title("The Random Forest Model")

st.subheader("The Model")
st.markdown("The trained model is a **Random Forest Model**.Assuming complex non linear relationships, models like the classical logistic regression fail to seperate the two classes. Machine learning models overcome this restriction and handle correlated predictors gracefully. The basic concept of a random forest model is a decision tree that tries to find a complex function to seperate the patients into GH-sensitive and GH-resistant by sequently learing decision rules. This idea is repeated multiple times resulting in a model consisting a various independent trees with each one voting for a class given the input.")

import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.subheader("How the Random Forest Makes a Decision")

# Example probability from your model
ghd_probability = 0.74

# Simulate 50 trees voting
n_trees = 50
votes = np.random.choice(
    [1, 0],
    size=n_trees,
    p=[ghd_probability, 1 - ghd_probability]
)

# Arrange trees in a grid
n_cols = 10
x = np.tile(np.arange(n_cols), n_trees // n_cols)
y = np.repeat(np.arange(n_trees // n_cols)[::-1], n_cols)

colors = np.where(votes == 1, "#2ca02c", "#d62728")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=x,
        y=y,
        mode="markers+text",
        text=["🌳"] * n_trees,
        textposition="middle center",
        marker=dict(
            size=40,
            color=colors,
            opacity=0.85,
            line=dict(width=1, color="white")
        ),
        hovertemplate=np.where(
            votes == 1,
            "Tree vote: GHD<extra></extra>",
            "Tree vote: Non-GHD<extra></extra>"
        )
    )
)

fig.update_layout(
    title="Individual Tree Votes",
    title_font=dict(
        family="Times New Roman",
        size=22
    ),
    font=dict(
        family="Times New Roman",
        size=14
    ),
    height=400,
    showlegend=False,
    xaxis=dict(
        visible=False
    ),
    yaxis=dict(
        visible=False
    ),
    margin=dict(l=20, r=20, t=60, b=20),
    paper_bgcolor="white",
    plot_bgcolor="white"
)

st.plotly_chart(fig, use_container_width=True)

# Vote summary
ghd_votes = votes.sum()
non_votes = len(votes) - ghd_votes

st.markdown(
    f"""
### Forest Vote

🟢 **GHD:** {ghd_votes} trees

🔴 **Non-GHD:** {non_votes} trees

### Final Prediction

**Probability of GHD: {ghd_votes / len(votes):.1%}**
"""
)



st.subheader("Explainability")
st.markdown("For explainability **SHAP values** have been generated.The idea of SHAP values is to break down any machine learning model predictions and explain the contribution\
             of each feature. Coming from game theory, each feature is allocated an importance value for a specific prediction, \
            showing how much that feature pushed the result away from the average prediction. SHAP values of the trained model enable insights to the learned model structure, the SHAP value of a single prediction allows a deeper understanding of specific patient characteristics with respect to the learned model behaviour.")


if st.button("Understand SHAP values of the trained model."): 
    st.switch_page("pages/about_shap_gen.py")


if st.button("⬅ Back"): 
    st.switch_page("main.py")
