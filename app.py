import streamlit as st
import random, math
import pandas as pd
import plotly.graph_objects as go

from chord import ChordRing
from simulation import ChordSimulator, scalability_experiment

st.set_page_config(layout="wide")

# =========================
# 🔥 FIXED UI (VISIBLE + PREMIUM)
# =========================
st.markdown("""
<style>

/* Background */
html, body {
    background: #0a192f;
    color: #ffffff;
    font-family: 'Inter', sans-serif;
}

/* Navbar */
.navbar {
    display:flex;
    justify-content:space-between;
    align-items:center;
    background:#112240;
    padding:16px 30px;
    border-radius:14px;
    margin-bottom:20px;
}

/* Title */
.title {
    font-size:26px;
    font-weight:700;
    color:#ffffff;
}

/* Controls */
.control {
    background:#112240;
    padding:20px;
    border-radius:14px;
    margin-bottom:20px;
}

/* Sliders visibility */
.stSlider label {
    color: #ffffff !important;
}
.stSlider div {
    color: #ffffff !important;
}

/* Buttons */
.stButton button {
    background: linear-gradient(135deg,#3b82f6,#06b6d4);
    color:white;
    border-radius:10px;
    padding:10px 18px;
    font-weight:600;
    border:none;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    color:#9ca3af;
}
.stTabs [aria-selected="true"] {
    color:#3b82f6;
    border-bottom:2px solid #3b82f6;
}

/* Fix invisible text */
label, .stMarkdown, .stText {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# NAVBAR
# =========================
st.markdown("""
<div class="navbar">
    <div class="title">🔗 Chord DHT Simulator</div>
    <div style="color:#3b82f6;">Clean UI v2</div>
</div>
""", unsafe_allow_html=True)

# =========================
# CONTROLS
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    m = st.slider("Bit Size (m)", 3, 8, 6)

with col2:
    max_nodes = 2**m
    n = st.slider("Nodes", 2, min(20, max_nodes), 8)

with col3:
    build = st.button("🚀 Build Network")

if build:
    ring = ChordRing(m)
    for nid in random.sample(range(2**m), n):
        ring.add_node(nid)
    st.session_state.ring = ring

# =========================
# TABS
# =========================
tabs = st.tabs(["Topology", "Finger", "Lookup", "Simulation", "Scalability"])

# =========================
# TOPOLOGY
# =========================
with tabs[0]:
    if "ring" in st.session_state:
        ring = st.session_state.ring
        nodes = ring.get_nodes()

        fig = go.Figure()

        for node in nodes:
            angle = 2 * math.pi * node / (2**m)
            x = math.cos(angle)
            y = math.sin(angle)

            fig.add_trace(go.Scatter(
                x=[x], y=[y],
                mode="markers+text",
                text=[str(node)],
                marker=dict(size=14, color="#3b82f6"),
                textposition="top center"
            ))

        fig.update_layout(
            paper_bgcolor="#0a192f",
            plot_bgcolor="#0a192f",
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

# =========================
# FINGER
# =========================
with tabs[1]:
    if "ring" in st.session_state:
        ring = st.session_state.ring

        node_id = st.selectbox("Node", ring.get_nodes())
        node = ring.nodes[node_id]

        data = []
        for i in range(m):
            start = (node.id + 2**i) % (2**m)
            succ = node.finger[i].id
            data.append([i, start, succ])

        st.dataframe(pd.DataFrame(data, columns=["i","start","successor"]))

# =========================
# LOOKUP
# =========================
with tabs[2]:
    if "ring" in st.session_state:
        ring = st.session_state.ring

        key = st.number_input("Key", 0, 2**m-1, 10)
        start = st.selectbox("Start Node", ring.get_nodes())

        if st.button("Run Lookup"):
            current = ring.nodes[start]
            path = []

            while True:
                path.append(current.id)

                if current.in_interval(key, current.id, current.successor.id, True):
                    path.append(current.successor.id)
                    break

                nxt = current.closest_preceding_node(key)

                if nxt == current:
                    path.append(current.successor.id)
                    break

                current = nxt

            st.success(f"Path: {path}")
            st.success(f"Hops: {len(path)-1}")

# =========================
# SIMULATION
# =========================
with tabs[3]:
    if st.button("Run Simulation"):
        sim = ChordSimulator(m, n)
        df = pd.DataFrame(sim.run_lookups(50))

        st.metric("Avg Hops", round(df["hops"].mean(),2))
        st.metric("Max Hops", df["hops"].max())

        fig = go.Figure()
        fig.add_histogram(x=df["hops"])
        fig.update_layout(
            paper_bgcolor="#0a192f",
            plot_bgcolor="#0a192f"
        )
        st.plotly_chart(fig)

# =========================
# SCALABILITY
# =========================
with tabs[4]:
    if st.button("Run Scalability"):
        df = pd.DataFrame(scalability_experiment(m))

        fig = go.Figure()
        fig.add_scatter(x=df["nodes"], y=df["avg_hops"])
        fig.add_scatter(
            x=df["nodes"],
            y=[math.log2(x) for x in df["nodes"]],
            name="log2(N)"
        )

        fig.update_layout(
            paper_bgcolor="#0a192f",
            plot_bgcolor="#0a192f"
        )

        st.plotly_chart(fig)