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

####
import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Random Forest Visualization")

# -----------------------------
# Simulated forest prediction
# -----------------------------
np.random.seed(42)

n_trees = 25
ghd_probability = 0.72

votes = np.random.choice(
    [1, 0],
    size=n_trees,
    p=[ghd_probability, 1 - ghd_probability]
)

ghd_votes = votes.sum()
non_votes = n_trees - ghd_votes

# -----------------------------
# MINI FOREST (LEFT PANEL)
# -----------------------------
n_cols = 5
x = np.tile(np.arange(n_cols), n_trees // n_cols)
y = np.repeat(np.arange(n_trees // n_cols)[::-1], n_cols)

fig_forest = go.Figure()

fig_forest.add_trace(
    go.Scatter(
        x=x,
        y=y,
        mode="markers+text",
        text=["🌳"] * n_trees,
        textposition="middle center",
        marker=dict(
            size=45,
            color=np.where(votes == 1, "#2ca02c", "#d62728"),
            line=dict(width=1, color="white")
        ),
        hovertemplate=[
            "GHD" if v == 1 else "Non-GHD" for v in votes
        ]
    )
)

fig_forest.update_layout(
    title="Mini Forest Voting",
    title_font=dict(family="Times New Roman", size=20),
    font=dict(family="Times New Roman", size=14),
    height=350,
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    paper_bgcolor="white",
    plot_bgcolor="white",
    margin=dict(l=10, r=10, t=50, b=10)
)

# -----------------------------
# SIMPLE EXAMPLE TREE (RIGHT PANEL)
# -----------------------------
fig_tree = go.Figure()

# Nodes (manual layout)
nodes = {
    "IGF-I < 120": (0.5, 1.0),
    "GHBP < 500": (0.25, 0.6),
    "BMI < 30": (0.75, 0.6),
    "GHD": (0.2, 0.2),
    "Non-GHD": (0.6, 0.2),
    "GHD ": (0.85, 0.2),
}

edges = [
    ("IGF-I < 120", "GHBP < 500"),
    ("IGF-I < 120", "BMI < 30"),
    ("GHBP < 500", "GHD"),
    ("GHBP < 500", "Non-GHD"),
    ("BMI < 30", "GHD "),
]

# Draw edges
for parent, child in edges:
    fig_tree.add_shape(
        type="line",
        x0=nodes[parent][0],
        y0=nodes[parent][1],
        x1=nodes[child][0],
        y1=nodes[child][1],
        line=dict(color="gray", width=2)
    )

# Draw nodes
for label, (x0, y0) in nodes.items():
    color = "#1f77b4" if "<" in label else "#2ca02c" if "GHD" in label else "#d62728"

    fig_tree.add_trace(
        go.Scatter(
            x=[x0],
            y=[y0],
            mode="markers+text",
            text=[label],
            textposition="top center",
            marker=dict(size=40, color=color),
            hoverinfo="skip"
        )
    )

fig_tree.update_layout(
    title="Example Decision Tree (Simplified)",
    title_font=dict(family="Times New Roman", size=20),
    font=dict(family="Times New Roman", size=14),
    height=350,
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    paper_bgcolor="white",
    plot_bgcolor="white",
    margin=dict(l=10, r=10, t=50, b=10)
)

# -----------------------------
# STREAMLIT LAYOUT
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_forest, use_container_width=True)

with col2:
    st.plotly_chart(fig_tree, use_container_width=True)

# -----------------------------
# FINAL OUTPUT
# -----------------------------
st.markdown("## Final Prediction")

st.metric(
    label="Probability of GHD",
    value=f"{ghd_votes / n_trees:.1%}"
)

st.write(f"🟢 GHD votes: {ghd_votes}")
st.write(f"🔴 Non-GHD votes: {non_votes}")

#####


st.subheader("Explainability")
st.markdown("For explainability **SHAP values** have been generated.The idea of SHAP values is to break down any machine learning model predictions and explain the contribution\
             of each feature. Coming from game theory, each feature is allocated an importance value for a specific prediction, \
            showing how much that feature pushed the result away from the average prediction. SHAP values of the trained model enable insights to the learned model structure, the SHAP value of a single prediction allows a deeper understanding of specific patient characteristics with respect to the learned model behaviour.")


if st.button("Understand SHAP values of the trained model."): 
    st.switch_page("pages/about_shap_gen.py")


if st.button("⬅ Back"): 
    st.switch_page("main.py")
