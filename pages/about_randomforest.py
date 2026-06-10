import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Random Forest Visualization")
np.random.seed(42)

n_trees = 25
prob = 0.33 # probability for GH-resistance

votes = np.random.choice([1, 0], size=n_trees, p=[prob, 1 - prob])
resistant_votes = votes.sum()
sensitive_votes = n_trees - resistant_votes


# FIGURE 1: FOREST --------

fig_forest = go.Figure()

n_cols = 5
x_forest = np.tile(np.arange(n_cols), n_trees // n_cols)
y_forest = np.repeat(np.arange(n_trees // n_cols)[::-1], n_cols)

fig_forest.add_trace(go.Scatter(
    x=x_forest,
    y=y_forest,
    mode="markers+text",
    text=["🌳"] * n_trees,
    textposition="middle center",
    marker=dict(
        size=45,
        color=np.where(votes == 1, "#d62728", "#2ca02c")
    ),
    hovertemplate=[
        "GH-resistant" if v == 1 else "GH-sensitive" for v in votes
    ],
    name="Forest"
))

fig_forest.update_layout(
    title="Random Forest with 25 Trees",
    height=500,
    paper_bgcolor="white",
    plot_bgcolor="white",
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    margin=dict(l=10, r=10, t=50, b=10)
)


# FIGURE 2: DECISION TREE ----------

fig_tree = go.Figure()

nodes = {
    "GH < threshold?": (0.5, 1.0),
    "Low IGF-I": (0.25, 0.6),
    "High IGF-I": (0.75, 0.6),
    "Resistant": (0.2, 0.2),
    "Sensitive": (0.6, 0.2),
    "Resistant ": (0.85, 0.2),
}

edges = [
    ("GH < threshold?", "Low IGF-I"),
    ("GH < threshold?", "High IGF-I"),
    ("Low IGF-I", "Resistant"),
    ("Low IGF-I", "Sensitive"),
    ("High IGF-I", "Resistant "),
]

# edges
for p, c in edges:
    fig_tree.add_shape(
        type="line",
        x0=nodes[p][0],
        y0=nodes[p][1],
        x1=nodes[c][0],
        y1=nodes[c][1],
        line=dict(color="gray", width=2)
    )

# nodes
for label, (x, y) in nodes.items():
    if "GH" in label:
        color = "#1f77b4"
    elif "Resistant" in label:
        color = "#d62728"
    else:
        color = "#2ca02c"

    fig_tree.add_trace(go.Scatter(
        x=[x],
        y=[y],
        mode="markers+text",
        text=[label],
        textposition="top center",
        marker=dict(size=40, color=color),
        hoverinfo="skip",
        showlegend=False
    ))

fig_tree.update_layout(
    title="Example Tree 🌳",
    height=500,
    paper_bgcolor="white",
    plot_bgcolor="white",
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    margin=dict(l=10, r=10, t=50, b=10)
)


col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_forest, use_container_width=True)
with col2:
    st.plotly_chart(fig_tree, use_container_width=True)

# OUTPUT ------
col1, col2 = st.columns(2)
with col1:
    st.markdown("## Final Prediction")
    st.metric(
        "Probability of GH-resistance",
        f"{resistant_votes / n_trees:.1%}"
    )
    
    st.write(f"🔴 GH-resistant votes: {resistant_votes}")
    st.write(f"🟢 GH-sensitive votes: {sensitive_votes}") 

with col2:
    st.info("\n\n\n\nThe decision rules are illustrative and do not match with the real trained model. The developed model combines 250 trees.", width=400)

