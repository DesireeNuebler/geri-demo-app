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
# Create figure
# -----------------------------
fig = go.Figure()

# =============================
# 🌳 TRACE 1: MINI FOREST
# =============================
n_cols = 5
x = np.tile(np.arange(n_cols), n_trees // n_cols)
y = np.repeat(np.arange(n_trees // n_cols)[::-1], n_cols)

fig.add_trace(go.Scatter(
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
    name="Decision: Forest",
    hovertemplate=[
        "GH-resistant" if v == 1 else "GH-sensitive" for v in votes
    ]
))

# =============================
# 🌲 TRACE 2: EXAMPLE TREE
# (First split = GH)
# =============================

nodes = {
    "GH < 5 pmol/L?": (0.5, 1.0),
    "Low IGF-I": (0.25, 0.6),
    "High IGF-I": (0.75, 0.6),
    "GH-resistant": (0.2, 0.2),
    "GH-sensitive": (0.6, 0.2),
    "GH-resistant" ": (0.85, 0.2),
}

edges = [
    ("GH < 5 pmol/L?", "Low IGF-I"),
    ("GH < 5 pmol/L?", "High IGF-I"),
    ("Low IGF-I", "GHD"),
    ("Low IGF-I", "Non-GHD"),
    ("High IGF-I", "GHD "),
]

# Draw edges (tree structure)
for parent, child in edges:
    fig.add_shape(
        type="line",
        x0=nodes[parent][0],
        y0=nodes[parent][1],
        x1=nodes[child][0],
        y1=nodes[child][1],
        line=dict(color="gray", width=2)
    )

# Draw nodes
for label, (x0, y0) in nodes.items():
    if "GH" in label:
        color = "#1f77b4"
    elif "GHD" in label:
        color = "#2ca02c"
    else:
        color = "#d62728"

    fig.add_trace(go.Scatter(
        x=[x0],
        y=[y0],
        mode="markers+text",
        text=[label],
        textposition="top center",
        marker=dict(size=40, color=color),
        name="Decision: Example Tree",
        showlegend=False,
        hoverinfo="skip"
    ))

# =============================
# LAYOUT
# =============================
fig.update_layout(
    title="Random Forest Decision Process with 25 Trees",
    title_font=dict(family="Times New Roman", size=22),
    font=dict(family="Times New Roman", size=14),
    height=550,
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    paper_bgcolor="white",
    plot_bgcolor="white",
    margin=dict(l=10, r=10, t=60, b=10),
    legend=dict(title="Model Components")
)

# =============================
# SHOW FIGURE
# =============================
st.plotly_chart(fig, use_container_width=True)

# =============================
# OUTPUT STATS
# =============================
st.markdown("## Final Prediction")

st.metric(
    label="Probability of GH-resistance",
    value=f"{ghd_votes / n_trees:.1%}"
)

st.write(f"🔴 GH-resistance votes: {ghd_votes}")
st.write(f"🟢  GH-sensitivity votes: {non_votes}")
