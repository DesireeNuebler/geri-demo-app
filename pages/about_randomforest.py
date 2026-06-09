import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Random Forest Visualization")

np.random.seed(42)

# -----------------------------
# FOREST SIMULATION
# -----------------------------
n_trees = 25
gh_resistance_prob = 0.33

votes = np.random.choice(
    [1, 0],
    size=n_trees,
    p=[gh_resistance_prob, 1 - gh_resistance_prob]
)

resistant_votes = votes.sum()
sensitive_votes = n_trees - resistant_votes

fig = go.Figure()

# =============================
# 🌳 LEFT: MINI FOREST
# =============================
n_cols = 5
x_forest = np.tile(np.arange(n_cols), n_trees // n_cols)
y_forest = np.repeat(np.arange(n_trees // n_cols)[::-1], n_cols)

fig.add_trace(go.Scatter(
    x=x_forest,
    y=y_forest,
    mode="markers+text",
    text=["🌳"] * n_trees,
    textposition="middle center",
    marker=dict(
        size=45,
        color=np.where(votes == 1, "#d62728", "#2ca02c")
    ),
    name="Decision: Forest",
    hovertemplate=[
        "GH-resistant" if v == 1 else "GH-sensitive" for v in votes
    ]
))

# =============================
# 🌲 RIGHT: EXAMPLE TREE (SHIFTED)
# =============================
shift_x = 1.6  # pushes tree to the right

nodes = {
    "GH < threshold?": (shift_x + 0.5, 1.0),
    "Low IGF-I": (shift_x + 0.25, 0.6),
    "High IGF-I": (shift_x + 0.75, 0.6),
    "Resistant": (shift_x + 0.2, 0.2),
    "Sensitive": (shift_x + 0.6, 0.2),
    "Resistant (alt)": (shift_x + 0.85, 0.2),
}

edges = [
    ("GH < threshold?", "Low IGF-I"),
    ("GH < threshold?", "High IGF-I"),
    ("Low IGF-I", "Resistant"),
    ("Low IGF-I", "Sensitive"),
    ("High IGF-I", "Resistant (alt)"),
]

# Draw tree edges
for parent, child in edges:
    fig.add_shape(
        type="line",
        x0=nodes[parent][0],
        y0=nodes[parent][1],
        x1=nodes[child][0],
        y1=nodes[child][1],
        line=dict(color="gray", width=2)
    )

# Draw tree nodes
for label, (x0, y0) in nodes.items():
    if "GH" in label:
        color = "#1f77b4"
    elif "Resistant" in label:
        color = "#d62728"
    else:
        color = "#2ca02c"

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

# -----------------------------
# LAYOUT (IMPORTANT PART)
# -----------------------------
fig.update_layout(
    title="Random Forest (Left) + Example Decision Tree (Right)",
    title_font=dict(family="Times New Roman", size=22),
    font=dict(family="Times New Roman", size=14),
    height=600,
    paper_bgcolor="white",
    plot_bgcolor="white",
    margin=dict(l=20, r=20, t=60, b=20),

    # KEY: expand x-axis to fit both panels
    xaxis=dict(visible=False, range=[-0.5, 3]),
    yaxis=dict(visible=False, range=[-0.2, 1.2])
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# OUTPUT
# -----------------------------
st.markdown("## Final Prediction")

st.metric(
    label="Probability of GH-resistance",
    value=f"{resistant_votes / n_trees:.1%}"
)

st.write(f"🔴 GH-resistant votes: {resistant_votes}")
st.write(f"🟢 GH-sensitive votes: {sensitive_votes}")
