import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Random Forest Visualization")
np.random.seed(42)


col1, col2 = st.columns([2, 1]) 
with col1: 

    
    
    
    # -----------------------------
    # DATA
    # -----------------------------
    n_trees = 25
    prob = 0.33
    
    votes = np.random.choice([1, 0], size=n_trees, p=[prob, 1 - prob])
    
    resistant_votes = votes.sum()
    sensitive_votes = n_trees - resistant_votes
    
    fig = go.Figure()
    
    # =============================
    # 🌳 LEFT: FOREST (STRICT RANGE 0–0.9)
    # =============================
    n_cols = 5
    x_forest = np.tile(np.arange(n_cols), n_trees // n_cols) / n_cols * 0.9
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

with col2: 

    
    # =============================
    # 🌲 RIGHT: TREE (STRICT RANGE 1.1–2.0)
    # =============================
    shift = 1.3
    
    nodes = {
        "GH < threshold?": (shift + 0.5, 1.0),
        "Low IGF-I": (shift + 0.25, 0.6),
        "High IGF-I": (shift + 0.75, 0.6),
        "Resistant": (shift + 0.2, 0.2),
        "Sensitive": (shift + 0.6, 0.2),
        "Resistant alt": (shift + 0.85, 0.2),
    }
    
    edges = [
        ("GH < threshold?", "Low IGF-I"),
        ("GH < threshold?", "High IGF-I"),
        ("Low IGF-I", "Resistant"),
        ("Low IGF-I", "Sensitive"),
        ("High IGF-I", "Resistant alt"),
    ]
    
    # draw edges
    for p, c in edges:
        fig.add_shape(
            type="line",
            x0=nodes[p][0],
            y0=nodes[p][1],
            x1=nodes[c][0],
            y1=nodes[c][1],
            line=dict(color="gray", width=2)
        )
    
    # draw nodes
    for label, (x, y) in nodes.items():
        if "GH" in label:
            color = "#1f77b4"
        elif "Resistant" in label:
            color = "#d62728"
        else:
            color = "#2ca02c"
    
        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode="markers+text",
            text=[label],
            textposition="top center",
            marker=dict(size=40, color=color),
            showlegend=False,
            hoverinfo="skip"
        ))
    
    # =============================
    # LAYOUT (CRITICAL)
    # =============================
    fig.update_layout(
        title="Random Forest (Left) vs Decision Tree (Right)",
        height=600,
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(family="Times New Roman", size=14),
    
        # KEY FIX: hard separation
        xaxis=dict(visible=False, range=[0, 2.2]),
        yaxis=dict(visible=False, range=[-0.2, 1.2]),
    
        margin=dict(l=10, r=10, t=60, b=10)
    )
    
    st.plotly_chart(fig, use_container_width=True)

# =============================
# OUTPUT
# =============================
st.markdown("## Final Prediction")

st.metric(
    "Probability of GH-resistance",
    f"{resistant_votes / n_trees:.1%}"
)

st.write(f"🔴 GH-resistant votes: {resistant_votes}")
st.write(f"🟢 GH-sensitive votes: {sensitive_votes}")
