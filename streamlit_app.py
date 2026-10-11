# -*- coding: utf-8 -*-
"""
app.py / streamlit_app.py
Iris Analytics Lab â€” Multidimensional Botanical Data Science & Executive Dashboard.
Deep Tech Obsidian Dark Theme (#0B0F17) with High-Contrast Typography,
Pure NumPy Mathematical Engine, Matplotlib Visual Analytics, and SQLite Persistence.
"""

import os
import sys
import sqlite3
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
from matplotlib.colors import LinearSegmentedColormap
import streamlit as st

# ------------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Iris Analytics Lab | Executive Dashboard",
    page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/64px-Kosaciec_szczecinkowaty_Iris_setosa.jpg",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------------------------
# 2. DESIGN SYSTEM & CSS (OBSIDIAN DARK THEME #0B0F17)
# ------------------------------------------------------------------------------
OBSIDIAN_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg-canvas: #0B0F17;
    --bg-card: #131B2E;
    --bg-card-hover: #1E293B;
    --border-color: rgba(51, 65, 85, 0.45);
    --border-highlight: rgba(56, 189, 248, 0.5);
    --cyan: #38BDF8;
    --emerald: #34D399;
    --amber: #F59E0B;
    --lavender: #A78BFA;
    --red: #F43F5E;
    --text-white: #F8FAFC;
    --text-slate: #94A3B8;
    --text-muted: #64748B;
}

html, body, .stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    background-color: var(--bg-canvas) !important;
    color: var(--text-slate) !important;
}

.stApp > header {
    background-color: rgba(11, 15, 23, 0.9) !important;
    backdrop-filter: blur(12px) !important;
    border-bottom: 1px solid var(--border-color) !important;
}

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 3rem !important;
    max-width: 1400px !important;
}

h1, h2, h3, h4, h5, h6 {
    color: var(--text-white) !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em !important;
}

p, li, span, div {
    color: var(--text-slate);
    line-height: 1.6;
}

strong, b {
    color: var(--text-white) !important;
}

/* Sticky Executive Top Navigation Header */
.top-header-banner {
    position: sticky;
    top: 0;
    z-index: 99;
    width: 100%;
    background: linear-gradient(135deg, rgba(19, 27, 46, 0.92) 0%, rgba(14, 21, 38, 0.95) 100%);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 1rem 1.5rem;
    margin-bottom: 1.25rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.25rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.05);
}

.brand-section {
    display: flex;
    align-items: center;
    gap: 14px;
}

.brand-title {
    font-size: 1.25rem;
    font-weight: 800;
    color: var(--text-white);
    letter-spacing: -0.01em;
    line-height: 1.15;
}

.brand-sub {
    font-size: 0.78rem;
    color: var(--cyan);
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-top: 2px;
}

.status-badge-active {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--emerald);
    background: rgba(52, 211, 153, 0.12);
    border: 1px solid rgba(52, 211, 153, 0.35);
    padding: 6px 14px;
    border-radius: 20px;
}

.status-badge-academic {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--cyan);
    background: rgba(56, 189, 248, 0.12);
    border: 1px solid rgba(56, 189, 248, 0.35);
    padding: 6px 14px;
    border-radius: 20px;
}

.pulse-dot {
    width: 8px;
    height: 8px;
    background: var(--emerald);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--emerald);
    animation: pulseGlow 2s infinite;
}

@keyframes pulseGlow {
    0% { transform: scale(0.95); opacity: 0.8; }
    50% { transform: scale(1.15); opacity: 1; }
    100% { transform: scale(0.95); opacity: 0.8; }
}

/* Metric Cards */
.obs-metric-card {
    background: linear-gradient(145deg, #131B2E 0%, #17223B 100%);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 1.25rem 1.35rem;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
    transition: all 0.25s ease;
    margin-bottom: 0.75rem;
}

.obs-metric-card:hover {
    transform: translateY(-2px);
    border-color: var(--border-highlight);
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.5), 0 0 20px rgba(56, 189, 248, 0.15);
}

.metric-title {
    font-size: 0.76rem;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 4px;
}

.metric-value {
    font-size: 1.95rem;
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -0.02em;
    margin: 4px 0;
}

.metric-subtitle {
    font-size: 0.8rem;
    color: var(--text-slate);
    margin-top: 4px;
}

/* Content Cards & Guides */
.obs-panel {
    background: linear-gradient(145deg, #131B2E 0%, #162035 100%);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1.25rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
}

.obs-guide-card {
    background: rgba(19, 27, 46, 0.75);
    border: 1px solid var(--border-color);
    border-left: 4px solid var(--cyan);
    border-radius: 12px;
    padding: 1.25rem 1.4rem;
    margin: 1rem 0;
    color: var(--text-slate);
}

.obs-guide-title {
    color: var(--text-white);
    font-weight: 700;
    font-size: 1.05rem;
    margin-bottom: 0.5rem;
}

/* Native Tabs Styling */
.stTabs [data-baseweb="tab-list"] {
    background: #131B2E !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 14px !important;
    padding: 6px !important;
    gap: 8px !important;
    margin-bottom: 1.25rem !important;
}

.stTabs [data-baseweb="tab"] {
    background-color: transparent !important;
    color: var(--text-muted) !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    border-radius: 10px !important;
    padding: 10px 20px !important;
    transition: all 0.2s ease !important;
    border: none !important;
}

.stTabs [data-baseweb="tab"]:hover {
    color: var(--text-white) !important;
    background: rgba(255, 255, 255, 0.05) !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(56, 189, 248, 0.25) 0%, rgba(14, 77, 107, 0.4) 100%) !important;
    color: var(--cyan) !important;
    border: 1px solid rgba(56, 189, 248, 0.5) !important;
    box-shadow: 0 0 16px rgba(56, 189, 248, 0.25) !important;
}

.stTabs [data-baseweb="tab-panel"] {
    padding-top: 0.5rem !important;
}

/* Prediction Result Banner */
.prediction-banner {
    background: linear-gradient(145deg, #131B2E 0%, #1A2846 100%);
    border: 2px solid var(--cyan);
    border-radius: 16px;
    padding: 1.75rem 2rem;
    box-shadow: 0 10px 32px rgba(56, 189, 248, 0.25);
    text-align: center;
    margin-bottom: 1.25rem;
}

.pred-species-title {
    color: var(--text-white);
    font-size: 2.2rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    margin: 8px 0;
}

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background-color: #0E1524 !important;
    border-right: 1px solid var(--border-color) !important;
}

section[data-testid="stSidebar"] * {
    color: var(--text-slate) !important;
}

section[data-testid="stSidebar"] h1, 
section[data-testid="stSidebar"] h2, 
section[data-testid="stSidebar"] h3 {
    color: var(--text-white) !important;
}

/* Buttons, Sliders, Tables */
.stButton button {
    background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%) !important;
    color: #F8FAFC !important;
    font-weight: 600 !important;
    border: 1px solid rgba(56, 189, 248, 0.5) !important;
    border-radius: 10px !important;
    padding: 0.6rem 1.4rem !important;
    box-shadow: 0 4px 14px rgba(2, 132, 199, 0.35) !important;
    transition: all 0.2s ease !important;
}

.stButton button:hover {
    background: linear-gradient(135deg, #38BDF8 0%, #0284C7 100%) !important;
    color: #0B0F17 !important;
    box-shadow: 0 6px 20px rgba(56, 189, 248, 0.55) !important;
    transform: translateY(-2px) !important;
}

.stSlider [data-baseweb="slider"] {
    color: var(--cyan) !important;
}

.stSlider [data-testid="stThumbValue"] {
    background-color: #131B2E !important;
    color: var(--cyan) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 6px !important;
}

.stSelectbox > div > div, .stMultiSelect > div > div {
    background-color: #131B2E !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 10px !important;
    color: var(--text-white) !important;
}

.stMultiSelect [data-baseweb="tag"] {
    background: rgba(56, 189, 248, 0.15) !important;
    color: var(--cyan) !important;
    border: 1px solid rgba(56, 189, 248, 0.4) !important;
    border-radius: 8px !important;
}

.stDataFrame {
    border: 1px solid var(--border-color) !important;
    border-radius: 12px !important;
    overflow: hidden !important;
}

.stDataFrame thead tr th {
    background-color: #131B2E !important;
    color: var(--cyan) !important;
    font-weight: 700 !important;
    border-bottom: 1px solid var(--border-color) !important;
}

.stDataFrame tbody tr td {
    color: var(--text-slate) !important;
    background-color: #0B0F17 !important;
    border-bottom: 1px solid rgba(51, 65, 85, 0.25) !important;
}

.stDataFrame tbody tr:hover td {
    background-color: #131B2E !important;
}

div[data-testid="stInfo"] {
    background-color: rgba(56, 189, 248, 0.08) !important;
    border-left: 4px solid var(--cyan) !important;
    border-radius: 0 10px 10px 0 !important;
    color: var(--text-slate) !important;
}
</style>
"""
st.markdown(OBSIDIAN_CSS, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# 3. EMBEDDED SVG LOGO & ASSETS (ZERO EXTERNAL NETWORK DEPENDENCY)
# ------------------------------------------------------------------------------
LOGO_SVG = """
<svg width="46" height="46" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="logoBgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0F17" />
      <stop offset="100%" stop-color="#131B2E" />
    </linearGradient>
    <filter id="cyanGlowEffect" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="#38BDF8" flood-opacity="0.65" />
    </filter>
  </defs>
  <rect x="4" y="4" width="92" height="92" rx="22" fill="url(#logoBgGrad)" stroke="#38BDF8" stroke-width="2" filter="url(#cyanGlowEffect)" />
  <ellipse cx="50" cy="22" rx="6" ry="15" fill="#38BDF8" fill-opacity="0.45" stroke="#38BDF8" stroke-width="1.2" />
  <ellipse cx="28" cy="64" rx="6" ry="15" transform="rotate(-60 28 64)" fill="#38BDF8" fill-opacity="0.45" stroke="#38BDF8" stroke-width="1.2" />
  <ellipse cx="72" cy="64" rx="6" ry="15" transform="rotate(60 72 64)" fill="#38BDF8" fill-opacity="0.45" stroke="#38BDF8" stroke-width="1.2" />
  <ellipse cx="50" cy="60" rx="5" ry="12" fill="#38BDF8" fill-opacity="0.85" stroke="#F8FAFC" stroke-width="1" />
  <ellipse cx="32" cy="36" rx="5" ry="12" transform="rotate(-60 32 36)" fill="#38BDF8" fill-opacity="0.85" stroke="#F8FAFC" stroke-width="1" />
  <ellipse cx="68" cy="36" rx="5" ry="12" transform="rotate(60 68 36)" fill="#38BDF8" fill-opacity="0.85" stroke="#F8FAFC" stroke-width="1" />
  <circle cx="50" cy="50" r="6" fill="#34D399" stroke="#ffffff" stroke-width="1.5" />
</svg>
"""

# ------------------------------------------------------------------------------
# 4. DATABASE INITIALIZATION & HELPERS
# ------------------------------------------------------------------------------
DB_PATH = "data/predictions.db"

def init_database():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            sepal_length REAL,
            sepal_width REAL,
            petal_length REAL,
            petal_width REAL,
            predicted_species TEXT,
            confidence_pct REAL,
            distance_cm REAL
        )
    """)
    conn.commit()
    conn.close()

def log_prediction_db(sl, sw, pl, pw, species, conf, dist):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO predictions (sepal_length, sepal_width, petal_length, petal_width, predicted_species, confidence_pct, distance_cm)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (sl, sw, pl, pw, species, conf, dist))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def get_recent_predictions_db(limit=10):
    if not os.path.exists(DB_PATH):
        return pd.DataFrame()
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(f"SELECT id, timestamp, sepal_length, sepal_width, petal_length, petal_width, predicted_species, confidence_pct, distance_cm FROM predictions ORDER BY id DESC LIMIT {limit}", conn)
    conn.close()
    return df

def clear_database_db():
    if os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        conn.cursor().execute("DELETE FROM predictions")
        conn.commit()
        conn.close()

init_database()

# ------------------------------------------------------------------------------
# 5. DATASET LOADING (CACHED)
# ------------------------------------------------------------------------------
FEATURE_COLS = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
SPECIES_COLORS = {
    "Setosa": "#38BDF8",     # Electric Cyan
    "Versicolor": "#F59E0B", # Warm Amber
    "Virginica": "#A78BFA",  # Soft Lavender
}

@st.cache_data
def load_iris_dataset():
    paths = ["data/iris.csv", "iris.csv"]
    df = None
    for p in paths:
        if os.path.exists(p):
            df = pd.read_csv(p)
            break
    if df is None:
        raise FileNotFoundError("Iris dataset not found.")
    df.columns = [c.strip().lower().replace(" ", "_").replace("_(cm)", "") for c in df.columns]
    df["species"] = df["species"].astype(str).str.capitalize()
    df["petal_ratio"] = (df["petal_length"] / df["petal_width"].replace(0, np.nan)).round(2)
    df["petal_area_proxy"] = (df["petal_length"] * df["petal_width"]).round(2)
    return df

try:
    df_raw = load_iris_dataset()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()
# ------------------------------------------------------------------------------
# 6. SIDEBAR CONTROLS & ACADEMIC CREDENTIALS
# ------------------------------------------------------------------------------
with st.sidebar:
    st.markdown(f"""
    <div style="display:flex; align-items:center; gap:12px; padding:0.25rem 0 0.85rem 0; border-bottom:1px solid rgba(51,65,85,0.45); margin-bottom:1rem;">
        {LOGO_SVG}
        <div>
            <div style="font-size:1.15rem; font-weight:800; color:#F8FAFC; letter-spacing:-0.01em; line-height:1.15;">IRIS LAB</div>
            <div style="font-size:0.72rem; color:#38BDF8; font-weight:700; letter-spacing:0.06em; text-transform:uppercase;">EXECUTIVE DASHBOARD</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Filter Flower Species")
    available_species = sorted(df_raw["species"].unique().tolist())
    selected_species = st.multiselect(
        "Select Species to Include:",
        options=available_species,
        default=available_species,
        help="Filter one, two, or all three Iris classes across the dashboard.",
    )
    if not selected_species:
        st.warning("Select at least one species. Defaulting to all.")
        selected_species = available_species

    st.markdown("---")
    st.markdown("### Dimension Range Filters (cm)")

    sl_min, sl_max = float(df_raw["sepal_length"].min()), float(df_raw["sepal_length"].max())
    sw_min, sw_max = float(df_raw["sepal_width"].min()), float(df_raw["sepal_width"].max())
    pl_min, pl_max = float(df_raw["petal_length"].min()), float(df_raw["petal_length"].max())
    pw_min, pw_max = float(df_raw["petal_width"].min()), float(df_raw["petal_width"].max())

    r_sl = st.slider("Sepal Length", sl_min, sl_max, (sl_min, sl_max), 0.1)
    r_sw = st.slider("Sepal Width", sw_min, sw_max, (sw_min, sw_max), 0.1)
    r_pl = st.slider("Petal Length", pl_min, pl_max, (pl_min, pl_max), 0.1)
    r_pw = st.slider("Petal Width", pw_min, pw_max, (pw_min, pw_max), 0.1)

    st.markdown("---")
    st.markdown("""
    <div style="background: rgba(19, 27, 46, 0.7); border: 1px solid rgba(51, 65, 85, 0.45); border-radius: 12px; padding: 1rem; margin-top: 0.5rem;">
        <div style="font-size: 0.8rem; font-weight: 700; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px;">PROJECT TEAM CREDENTIALS</div>
        <div style="font-size: 0.84rem; color: #F8FAFC; font-weight: 600;">Department of Computer Science &amp; Engineering</div>
        <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 2px;">Faculty Guide: <strong style="color:#F8FAFC;">Prof. Keerthana</strong></div>
        <hr style="border:none; border-top:1px solid rgba(51,65,85,0.4); margin:8px 0;" />
        <div style="font-size: 0.78rem; color: #94A3B8; line-height: 1.5;">
            <div>&bull; <strong style="color:#F8FAFC;">Balaji (Team Lead)</strong> &mdash; Architecture</div>
            <div>&bull; <strong style="color:#F8FAFC;">Ahamed Rasim</strong> &mdash; Data Pipeline</div>
            <div>&bull; <strong style="color:#F8FAFC;">Kishore Kumar</strong> &mdash; NumPy Engine</div>
            <div>&bull; <strong style="color:#F8FAFC;">Aadthiyan</strong> &mdash; Visual Analytics</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# 7. FILTER APPLICATION
# ------------------------------------------------------------------------------
df_filtered = df_raw[df_raw["species"].isin(selected_species)].copy()
df_filtered = df_filtered[
    (df_filtered["sepal_length"] >= r_sl[0]) & (df_filtered["sepal_length"] <= r_sl[1]) &
    (df_filtered["sepal_width"] >= r_sw[0]) & (df_filtered["sepal_width"] <= r_sw[1]) &
    (df_filtered["petal_length"] >= r_pl[0]) & (df_filtered["petal_length"] <= r_pl[1]) &
    (df_filtered["petal_width"] >= r_pw[0]) & (df_filtered["petal_width"] <= r_pw[1])
]

# ------------------------------------------------------------------------------
# 8. STICKY TOP NAVIGATION BANNER (100% WIDTH)
# ------------------------------------------------------------------------------
st.markdown(f"""
<div class="top-header-banner">
    <div class="brand-section">
        {LOGO_SVG}
        <div>
            <div class="brand-title">IRIS ANALYTICS LAB</div>
            <div class="brand-sub">Multidimensional Botanical Data Science &amp; Executive Dashboard</div>
        </div>
    </div>
    <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
        <div class="status-badge-active">
            <div class="pulse-dot"></div>
            <span>Status: Active</span>
        </div>
        <div class="status-badge-academic">
            <span>College CSE Mini-Project</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# 9. FOUR NATIVE STREAMLIT DASHBOARD TABS
# ------------------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "1. Overview & Data",
    "2. Visual Analytics",
    "3. Mathematical Engine",
    "4. Live Flower Predictor",
])

# ==============================================================================
# TAB 1: OVERVIEW & BOTANICAL DATA
# ==============================================================================
with tab1:
    # 4 Executive Metric Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="obs-metric-card">
            <div class="metric-title">Total Analyzed Flowers</div>
            <div class="metric-value" style="color:#38BDF8;">{len(df_filtered)} <span style="font-size:1.05rem; color:#64748B; font-weight:500;">/ 150</span></div>
            <div class="metric-subtitle">Sample Size: 150 Flowers (50 per species)</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="obs-metric-card">
            <div class="metric-title">Measured Features</div>
            <div class="metric-value" style="color:#38BDF8;">4 Dimensions</div>
            <div class="metric-subtitle">4 Physical Measurements (cm)</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="obs-metric-card">
            <div class="metric-title">Strongest Correlation</div>
            <div class="metric-value" style="color:#34D399;">+0.96</div>
            <div class="metric-subtitle">Petal Length &amp; Petal Width</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="obs-metric-card">
            <div class="metric-title">Best Distinguisher</div>
            <div class="metric-value" style="color:#F59E0B;">Petal Dimensions</div>
            <div class="metric-subtitle">Setosa Easily Separable (&lt;2.45 cm Petal)</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # Plain-English Botanical Guide
    st.markdown("""
    <div class="obs-guide-card">
        <div class="obs-guide-title">Plain-English Botanical Guide: Sepals vs. Petals</div>
        Every Iris flower has two primary leaf structures used for species identification:
        <ul style="margin: 0.35rem 0 0 1.25rem; padding: 0;">
            <li><strong style="color:#F8FAFC;">Sepals (Falls):</strong> The lower, spreading leaves that droop outward to support the blossom. They protect the flower bud before it opens.</li>
            <li><strong style="color:#F8FAFC;">Petals (Standards):</strong> The upright, colorful inner petals standing vertically above the floral core.</li>
        </ul>
        <div style="margin-top: 8px; color:#38BDF8; font-weight: 600;">
            Why Petals Matter Most: While sepals have overlapping sizes across species, petal length and width provide an immediate, clear distinction between Setosa, Versicolor, and Virginica.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 3 Side-by-Side Species Cards
    s_col1, s_col2, s_col3 = st.columns(3)
    with s_col1:
        st.markdown("""
        <div class="obs-panel" style="border-top: 4px solid #38BDF8;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <h4 style="margin:0; color:#F8FAFC;">Iris Setosa</h4>
                <span style="background:rgba(56,189,248,0.15); color:#38BDF8; font-size:0.75rem; font-weight:700; padding:2px 8px; border-radius:12px;">SMALL PETALS</span>
            </div>
            <div style="font-size:0.83rem; line-height:1.6; color:#94A3B8;">
                <div>&bull; <strong>Petal Length:</strong> 1.0 &ndash; 1.9 cm (Mean: 1.46 cm)</div>
                <div>&bull; <strong>Petal Width:</strong> 0.1 &ndash; 0.6 cm (Mean: 0.25 cm)</div>
                <div>&bull; <strong>Sepal Length:</strong> 4.3 &ndash; 5.8 cm (Mean: 5.01 cm)</div>
                <div>&bull; <strong>Sepal Width:</strong> 2.3 &ndash; 4.4 cm (Mean: 3.43 cm)</div>
            </div>
            <div style="margin-top:10px; padding-top:8px; border-top:1px solid rgba(51,65,85,0.4); font-size:0.78rem; color:#34D399; font-weight:600;">
                Setosa Easily Separable (&lt;2.45 cm Petal)
            </div>
        </div>
        """, unsafe_allow_html=True)

    with s_col2:
        st.markdown("""
        <div class="obs-panel" style="border-top: 4px solid #F59E0B;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <h4 style="margin:0; color:#F8FAFC;">Iris Versicolor</h4>
                <span style="background:rgba(245,158,11,0.15); color:#F59E0B; font-size:0.75rem; font-weight:700; padding:2px 8px; border-radius:12px;">MEDIUM PETALS</span>
            </div>
            <div style="font-size:0.83rem; line-height:1.6; color:#94A3B8;">
                <div>&bull; <strong>Petal Length:</strong> 3.0 &ndash; 5.1 cm (Mean: 4.26 cm)</div>
                <div>&bull; <strong>Petal Width:</strong> 1.0 &ndash; 1.8 cm (Mean: 1.33 cm)</div>
                <div>&bull; <strong>Sepal Length:</strong> 4.9 &ndash; 7.0 cm (Mean: 5.94 cm)</div>
                <div>&bull; <strong>Sepal Width:</strong> 2.0 &ndash; 3.4 cm (Mean: 2.77 cm)</div>
            </div>
            <div style="margin-top:10px; padding-top:8px; border-top:1px solid rgba(51,65,85,0.4); font-size:0.78rem; color:#F59E0B; font-weight:600;">
                Intermediate size; slight overlap with Virginica
            </div>
        </div>
        """, unsafe_allow_html=True)

    with s_col3:
        st.markdown("""
        <div class="obs-panel" style="border-top: 4px solid #A78BFA;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <h4 style="margin:0; color:#F8FAFC;">Iris Virginica</h4>
                <span style="background:rgba(167,139,250,0.15); color:#A78BFA; font-size:0.75rem; font-weight:700; padding:2px 8px; border-radius:12px;">LARGE PETALS</span>
            </div>
            <div style="font-size:0.83rem; line-height:1.6; color:#94A3B8;">
                <div>&bull; <strong>Petal Length:</strong> 4.5 &ndash; 6.9 cm (Mean: 5.55 cm)</div>
                <div>&bull; <strong>Petal Width:</strong> 1.4 &ndash; 2.5 cm (Mean: 2.03 cm)</div>
                <div>&bull; <strong>Sepal Length:</strong> 4.9 &ndash; 7.9 cm (Mean: 6.59 cm)</div>
                <div>&bull; <strong>Sepal Width:</strong> 2.2 &ndash; 3.8 cm (Mean: 2.97 cm)</div>
            </div>
            <div style="margin-top:10px; padding-top:8px; border-top:1px solid rgba(51,65,85,0.4); font-size:0.78rem; color:#A78BFA; font-weight:600;">
                Largest flowers with high petal-to-sepal ratio
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Interactive Dataset Explorer")

    d_col1, d_col2 = st.columns([3, 1])
    with d_col1:
        search_kw = st.text_input("Quick Search Records (filter by text, species, or numbers):", "")
    with d_col2:
        st.write("")
        st.write("")
        csv_bytes = df_filtered.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download Filtered CSV",
            data=csv_bytes,
            file_name="iris_filtered_records.csv",
            mime="text/csv",
            use_container_width=True,
        )

    table_df = df_filtered.copy()
    if search_kw:
        mask = table_df.astype(str).apply(lambda r: r.str.contains(search_kw, case=False).any(), axis=1)
        table_df = table_df[mask]

    st.dataframe(
        table_df,
        use_container_width=True,
        height=300,
        column_config={
            "sepal_length": st.column_config.NumberColumn("Sepal Length (cm)", format="%.1f"),
            "sepal_width": st.column_config.NumberColumn("Sepal Width (cm)", format="%.1f"),
            "petal_length": st.column_config.NumberColumn("Petal Length (cm)", format="%.1f"),
            "petal_width": st.column_config.NumberColumn("Petal Width (cm)", format="%.1f"),
            "petal_ratio": st.column_config.NumberColumn("Petal Ratio (L/W)", format="%.2f"),
            "petal_area_proxy": st.column_config.NumberColumn("Petal Area (cmÂ²)", format="%.2f"),
            "species": st.column_config.TextColumn("Species"),
        },
    )
# ==============================================================================
# TAB 2: VISUAL ANALYTICS GALLERY (MATPLOTLIB)
# ==============================================================================
with tab2:
    st.subheader("Publication-Quality Visual Analytics Gallery")
    st.caption("Custom high-contrast visualizations rendered on Deep Obsidian (#0B0F17) canvas.")

    # Matplotlib Configuration
    plt.rcParams.update({
        "figure.facecolor": "#0B0F17",
        "axes.facecolor": "#131B2E",
        "axes.edgecolor": "#334155",
        "axes.labelcolor": "#94A3B8",
        "axes.titlecolor": "#F8FAFC",
        "xtick.color": "#94A3B8",
        "ytick.color": "#94A3B8",
        "text.color": "#F8FAFC",
        "grid.color": "#334155",
        "grid.linewidth": 0.6,
        "legend.facecolor": "#1E293B",
        "legend.edgecolor": "#334155",
        "legend.labelcolor": "#F8FAFC",
    })

    v_col1, v_col2 = st.columns(2)

    with v_col1:
        st.markdown("#### Figure 1: Petal Length vs. Petal Width Decision Map")
        fig1, ax1 = plt.subplots(figsize=(6.5, 4.8))
        for sp in ["Setosa", "Versicolor", "Virginica"]:
            sub = df_filtered[df_filtered["species"] == sp]
            if not sub.empty:
                ax1.scatter(
                    sub["petal_length"], sub["petal_width"],
                    label=sp, color=SPECIES_COLORS.get(sp, "#38BDF8"),
                    alpha=0.85, s=65, edgecolors="#0B0F17", linewidths=0.8,
                )

        # Prominent dashed red vertical boundary line at 2.45 cm
        ax1.axvline(x=2.45, color="#F43F5E", linestyle="--", linewidth=2.0, label="Setosa Boundary (2.45 cm)")
        ax1.text(2.55, ax1.get_ylim()[1] * 0.9 if ax1.get_ylim()[1] else 2.2, "2.45 cm\nBoundary", color="#F43F5E", fontsize=8.5, fontweight="bold")

        ax1.set_xlabel("Petal Length (cm)")
        ax1.set_ylabel("Petal Width (cm)")
        ax1.set_title("Petal Dimensions & Decision Boundary", fontsize=11, fontweight="bold", pad=10)
        ax1.legend(loc="upper left", framealpha=0.4, fontsize=8.5)
        ax1.grid(True, alpha=0.3)
        fig1.tight_layout()
        st.pyplot(fig1, use_container_width=True)
        plt.close(fig1)

        st.markdown("""
        <div style="background:rgba(19,27,46,0.6); border:1px solid rgba(51,65,85,0.4); border-radius:10px; padding:12px; margin-top:-8px; font-size:0.84rem;">
            <strong style="color:#38BDF8;">Scientific Conclusion:</strong> Petal measurements alone provide a perfect decision boundary at <strong>2.45 cm</strong>. 
            Any iris specimen with a petal length under 2.45 cm is guaranteed to be <strong>Iris Setosa</strong> with 100% precision.
        </div>
        """, unsafe_allow_html=True)

    with v_col2:
        st.markdown("#### Figure 2: Box Plot Distributions Across Species")
        fig2, ax2 = plt.subplots(figsize=(6.5, 4.8))
        species_order = [s for s in ["Setosa", "Versicolor", "Virginica"] if s in df_filtered["species"].unique()]
        if species_order:
            box_data = [df_filtered[df_filtered["species"] == s]["petal_length"].dropna().values for s in species_order]
            bp = ax2.boxplot(
                box_data, patch_artist=True,
                medianprops=dict(color="#F8FAFC", linewidth=2),
                whiskerprops=dict(color="#94A3B8", linewidth=1.2),
                capprops=dict(color="#94A3B8", linewidth=1.5),
                flierprops=dict(marker="o", markerfacecolor="#F43F5E", markersize=4, alpha=0.7),
            )
            for patch, s in zip(bp["boxes"], species_order):
                patch.set_facecolor(SPECIES_COLORS.get(s, "#38BDF8"))
                patch.set_alpha(0.75)
                patch.set_edgecolor("#F8FAFC")

            ax2.set_xticklabels(species_order)
            ax2.set_xlabel("Species")
            ax2.set_ylabel("Petal Length (cm)")
            ax2.set_title("Petal Length Dispersion & Interquartile Spread", fontsize=11, fontweight="bold", pad=10)
            ax2.grid(axis="y", alpha=0.3)
            fig2.tight_layout()
            st.pyplot(fig2, use_container_width=True)
            plt.close(fig2)

        st.markdown("""
        <div style="background:rgba(19,27,46,0.6); border:1px solid rgba(51,65,85,0.4); border-radius:10px; padding:12px; margin-top:-8px; font-size:0.84rem;">
            <strong style="color:#F59E0B;">Scientific Conclusion:</strong> Setosa exhibits tightly clustered variance with zero overlap, 
            whereas Versicolor and Virginica show wider natural dispersion with a small boundary overlap zone between 4.5 and 5.1 cm.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### Figure 3: Four-Panel Feature Distribution Histograms")
    fig3, axes = plt.subplots(2, 2, figsize=(10, 6.5))
    axes = axes.flatten()
    feat_names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]

    for idx, (col_name, feat_title) in enumerate(zip(FEATURE_COLS, feat_names)):
        ax = axes[idx]
        for sp in ["Setosa", "Versicolor", "Virginica"]:
            sub_vals = df_filtered[df_filtered["species"] == sp][col_name].dropna().values
            if len(sub_vals) > 0:
                ax.hist(sub_vals, bins=12, alpha=0.6, label=sp, color=SPECIES_COLORS.get(sp, "#38BDF8"), edgecolor="#0B0F17")
        ax.set_title(f"{feat_title} (cm)", fontsize=10, fontweight="bold")
        ax.set_xlabel("Value (cm)", fontsize=8.5)
        ax.set_ylabel("Frequency", fontsize=8.5)
        ax.grid(alpha=0.25)
        if idx == 0:
            ax.legend(fontsize=7.5, loc="upper right")

    fig3.tight_layout()
    st.pyplot(fig3, use_container_width=True)
    plt.close(fig3)

    st.markdown("""
    <div style="background:rgba(19,27,46,0.6); border:1px solid rgba(51,65,85,0.4); border-radius:10px; padding:12px; margin-top:4px; font-size:0.84rem;">
        <strong style="color:#34D399;">Scientific Conclusion:</strong> Petal dimensions display distinct bimodal and trimodal separation across species classes, 
        confirming that petal morphology serves as the primary discriminant axis in multidimensional feature space.
    </div>
    """, unsafe_allow_html=True)


# ==============================================================================
# TAB 3: MATHEMATICAL ENGINE (NUMPY & PANDAS)
# ==============================================================================
with tab3:
    st.subheader("NumPy Linear Algebra & Statistical Foundations")
    st.caption("Rigorous mathematical formulations executed directly via pure NumPy matrix operations.")

    # 1. Sample Mean Vector Comparison
    st.markdown("#### 1. Sample Mean Vector Comparison Table")
    mean_summary = df_filtered.groupby("species")[FEATURE_COLS].mean().round(2)
    mean_summary.columns = ["Sepal Length (Mean)", "Sepal Width (Mean)", "Petal Length (Mean)", "Petal Width (Mean)"]
    st.dataframe(mean_summary, use_container_width=True)

    st.markdown("---")

    # 2. Covariance and Correlation Matrices
    X_vals = df_filtered[FEATURE_COLS].to_numpy(dtype=float)
    N_samples = len(X_vals)

    if N_samples >= 2:
        # Pure NumPy Covariance
        mu_vec = np.mean(X_vals, axis=0)
        X_centered = X_vals - mu_vec
        cov_matrix = (X_centered.T @ X_centered) / (N_samples - 1)

        # Pure NumPy Correlation
        var_vec = np.diag(cov_matrix)
        std_vec = np.sqrt(np.maximum(var_vec, 1e-9))
        corr_matrix = cov_matrix / np.outer(std_vec, std_vec)
        np.fill_diagonal(corr_matrix, 1.0)

        m_col1, m_col2 = st.columns(2)

        with m_col1:
            st.markdown("#### Covariance Matrix (&Sigma;)")
            fig_cov, ax_c = plt.subplots(figsize=(5.5, 4.2))
            cmap_cov = LinearSegmentedColormap.from_list("cov_c", ["#0B0F17", "#0E4D6B", "#38BDF8"], N=256)
            im_c = ax_c.imshow(cov_matrix, cmap=cmap_cov)
            labels_short = ["SL", "SW", "PL", "PW"]
            ax_c.set_xticks(range(4)); ax_c.set_yticks(range(4))
            ax_c.set_xticklabels(labels_short); ax_c.set_yticklabels(labels_short)
            ax_c.set_title("Sample Covariance Matrix", fontsize=10, fontweight="bold")
            for i in range(4):
                for j in range(4):
                    ax_c.text(j, i, f"{cov_matrix[i, j]:.2f}", ha="center", va="center", color="#F8FAFC", fontsize=8.5)
            fig_cov.tight_layout()
            st.pyplot(fig_cov, use_container_width=True)
            plt.close(fig_cov)

        with m_col2:
            st.markdown("#### Pearson Correlation Matrix (R)")
            fig_cor, ax_r = plt.subplots(figsize=(5.5, 4.2))
            cmap_cor = LinearSegmentedColormap.from_list("cor_c", ["#7C3AED", "#0B0F17", "#34D399"], N=256)
            im_r = ax_r.imshow(corr_matrix, cmap=cmap_cor, vmin=-1, vmax=1)
            ax_r.set_xticks(range(4)); ax_r.set_yticks(range(4))
            ax_r.set_xticklabels(labels_short); ax_r.set_yticklabels(labels_short)
            ax_r.set_title("Pearson Correlation Matrix", fontsize=10, fontweight="bold")
            for i in range(4):
                for j in range(4):
                    ax_r.text(j, i, f"{corr_matrix[i, j]:.2f}", ha="center", va="center", color="#F8FAFC", fontsize=8.5)
            fig_cor.tight_layout()
            st.pyplot(fig_cor, use_container_width=True)
            plt.close(fig_cor)

    st.markdown("---")

    # 3. Simpson's Paradox Explanation Note
    st.markdown("""
    <div class="obs-guide-card" style="border-left-color: #F59E0B;">
        <div class="obs-guide-title" style="color:#F59E0B;">Important Insight: Simpson's Paradox in Iris Data</div>
        <p style="margin: 0; line-height: 1.6;">
            Across the entire dataset, <strong>Sepal Length and Sepal Width have an overall negative correlation (r &approx; -0.12)</strong>. 
            However, when analyzing each species individually, the correlation is <strong>strongly positive</strong>:
            <br>&bull; <strong>Setosa:</strong> +0.74 &nbsp;|&nbsp; <strong>Versicolor:</strong> +0.53 &nbsp;|&nbsp; <strong>Virginica:</strong> +0.46
            <br>This classic statistical paradox happens because Setosa flowers have unusually broad sepals despite having short lengths, which shifts their entire cluster upward and pulls the combined trend line downward.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 4. Principal Component Analysis (PCA) Breakdown
    if N_samples >= 2:
        st.markdown("#### Principal Component Analysis (PCA) Variance Breakdown")
        evals, evecs = np.linalg.eigh(cov_matrix)
        idx_sort = np.argsort(evals)[::-1]
        sorted_evals = evals[idx_sort]
        var_pct = (sorted_evals / np.sum(sorted_evals)) * 100
        cum_var = np.cumsum(var_pct)

        pca_df = pd.DataFrame({
            "Principal Component": ["PC1 (Overall Size)", "PC2 (Sepal Shape)", "PC3 (Fine Trait)", "PC4 (Noise)"],
            "Eigenvalue": sorted_evals.round(4),
            "Variance Explained (%)": [f"{v:.1f}%" for v in var_pct],
            "Cumulative (%)": [f"{c:.1f}%" for c in cum_var],
        })
        st.dataframe(pca_df, use_container_width=True, hide_index=True)


# ==============================================================================
# TAB 4: INTERACTIVE FLOWER PREDICTOR
# ==============================================================================
with tab4:
    st.subheader("Live Species Predictor (Nearest Centroid Classifier)")
    st.caption("Adjust the sliders below to calculate live Euclidean distances to all three species centroids.")

    # Archetype Presets
    st.markdown("**Quick Specimen Archetypes:**")
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        if st.button("Typical Setosa (Small)", use_container_width=True):
            st.session_state["p_sl"] = 5.0
            st.session_state["p_sw"] = 3.5
            st.session_state["p_pl"] = 1.5
            st.session_state["p_pw"] = 0.2
    with p2:
        if st.button("Typical Versicolor (Medium)", use_container_width=True):
            st.session_state["p_sl"] = 5.9
            st.session_state["p_sw"] = 2.8
            st.session_state["p_pl"] = 4.3
            st.session_state["p_pw"] = 1.3
    with p3:
        if st.button("Typical Virginica (Large)", use_container_width=True):
            st.session_state["p_sl"] = 6.6
            st.session_state["p_sw"] = 3.0
            st.session_state["p_pl"] = 5.6
            st.session_state["p_pw"] = 2.0
    with p4:
        if st.button("Reset Default Inputs", use_container_width=True):
            st.session_state["p_sl"] = 5.8
            st.session_state["p_sw"] = 3.0
            st.session_state["p_pl"] = 4.2
            st.session_state["p_pw"] = 1.3

    # Slider Controls
    sl_val = st.session_state.get("p_sl", 5.8)
    sw_val = st.session_state.get("p_sw", 3.0)
    pl_val = st.session_state.get("p_pl", 4.2)
    pw_val = st.session_state.get("p_pw", 1.3)

    sc1, sc2, sc3, sc4 = st.columns(4)
    with sc1:
        q_sl = st.slider("Sepal Length (cm)", 4.0, 8.0, float(sl_val), 0.1, key="slider_sl")
    with sc2:
        q_sw = st.slider("Sepal Width (cm)", 2.0, 4.5, float(sw_val), 0.1, key="slider_sw")
    with sc3:
        q_pl = st.slider("Petal Length (cm)", 1.0, 7.0, float(pl_val), 0.1, key="slider_pl")
    with sc4:
        q_pw = st.slider("Petal Width (cm)", 0.1, 2.6, float(pw_val), 0.1, key="slider_pw")

    # Compute Centroids
    query_point = np.array([q_sl, q_sw, q_pl, q_pw], dtype=float)
    species_list = ["Setosa", "Versicolor", "Virginica"]
    centroids = {}
    for s in species_list:
        sub = df_raw[df_raw["species"] == s][FEATURE_COLS]
        centroids[s] = sub.mean().to_numpy()

    # Calculate Distances
    distances = {s: float(np.linalg.norm(query_point - centroids[s])) for s in species_list}
    predicted_sp = min(distances, key=distances.get)
    min_dist = distances[predicted_sp]

    # Confidence calculation via soft inverse distance
    inv_dists = {s: np.exp(-distances[s] / 0.85) for s in species_list}
    sum_inv = sum(inv_dists.values()) + 1e-9
    confidences = {s: (inv_dists[s] / sum_inv) * 100 for s in species_list}
    pred_conf = confidences[predicted_sp]

    # Prediction Banner
    st.markdown(f"""
    <div class="prediction-banner">
        <div style="font-size: 0.85rem; color: #38BDF8; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;">PREDICTED SPECIES</div>
        <div class="pred-species-title" style="color: {SPECIES_COLORS.get(predicted_sp, '#38BDF8')};">Iris {predicted_sp}</div>
        <div style="font-size: 1rem; color: #94A3B8; margin-top: 6px;">
            Calculated Confidence: <strong style="color:#34D399;">{pred_conf:.1f}%</strong> &bull; Distance to Center: <strong style="color:#F8FAFC;">{min_dist:.2f} cm</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Comparison Table & 2D Projection Plot
    res_c1, res_c2 = st.columns([1, 1.2])

    with res_c1:
        st.markdown("#### Distance to Species Centroids")
        dist_table = pd.DataFrame([
            {
                "Species": sp,
                "Euclidean Distance": f"{distances[sp]:.2f} cm",
                "Match Confidence": f"{confidences[sp]:.1f}%",
                "Status": "Best Match" if sp == predicted_sp else "Alternative"
            }
            for sp in species_list
        ])
        st.dataframe(dist_table, use_container_width=True, hide_index=True)

        if st.button("Log Prediction to SQLite Database", type="primary", use_container_width=True):
            new_row_id = log_prediction_db(q_sl, q_sw, q_pl, q_pw, predicted_sp, round(pred_conf, 1), round(min_dist, 4))
            st.toast(f"Prediction #{new_row_id} logged to SQLite!", icon="*")

    with res_c2:
        st.markdown("#### 2D Spatial Projection (Petal Length vs Width)")
        fig_proj, ax_p = plt.subplots(figsize=(6, 4.2))
        for sp in species_list:
            sub = df_raw[df_raw["species"] == sp]
            ax_p.scatter(sub["petal_length"], sub["petal_width"], color=SPECIES_COLORS.get(sp, "#38BDF8"), alpha=0.35, s=30)
            ax_p.scatter(centroids[sp][2], centroids[sp][3], color=SPECIES_COLORS.get(sp, "#38BDF8"), marker="X", s=140, edgecolors="#F8FAFC", linewidths=1.2)

        # Plot query point
        ax_p.scatter(q_pl, q_pw, color="#34D399", marker="*", s=300, edgecolors="#F8FAFC", linewidths=1.5, label="Your Flower")
        ax_p.plot([q_pl, centroids[predicted_sp][2]], [q_pw, centroids[predicted_sp][3]], color="#34D399", linestyle=":", linewidth=2)

        ax_p.set_xlabel("Petal Length (cm)")
        ax_p.set_ylabel("Petal Width (cm)")
        ax_p.set_title("Input Vector vs. Species Centroids", fontsize=10, fontweight="bold")
        ax_p.legend(framealpha=0.4, fontsize=8)
        ax_p.grid(alpha=0.25)
        fig_proj.tight_layout()
        st.pyplot(fig_proj, use_container_width=True)
        plt.close(fig_proj)

    st.markdown("---")
    st.subheader("SQLite Prediction Log (data/predictions.db)")
    db_records = get_recent_predictions_db(limit=10)
    if not db_records.empty:
        st.dataframe(db_records, use_container_width=True, hide_index=True)
        if st.button("Clear Prediction History"):
            clear_database_db()
            st.success("Database records cleared.")
            st.rerun()
    else:
        st.info("No predictions logged yet. Click 'Log Prediction to SQLite Database' above to persist records.")

# ------------------------------------------------------------------------------
# 10. EXECUTIVE FOOTER & CREDITS
# ------------------------------------------------------------------------------
st.markdown("---")
st.markdown("""
<div style="background: linear-gradient(135deg, #0D1424 0%, #131B2E 100%); border: 1px solid rgba(51, 65, 85, 0.45); border-radius: 16px; padding: 1.75rem 2rem; margin-top: 2rem;">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:1.5rem;">
        <div>
            <div style="font-size:1.15rem; font-weight:800; color:#F8FAFC;">Department of Computer Science &amp; Engineering</div>
            <div style="font-size:0.84rem; color:#38BDF8; font-weight:600; margin-top:2px;">Data Science &amp; Multidimensional Analytics &bull; College CSE Mini-Project</div>
            <div style="font-size:0.8rem; color:#94A3B8; margin-top:6px;">Faculty Guide: <strong style="color:#F8FAFC;">Prof. Keerthana</strong>, Assistant Professor, Dept of CSE</div>
        </div>
        <div style="text-align:right;">
            <span style="background:rgba(56,189,248,0.12); color:#38BDF8; border:1px solid rgba(56,189,248,0.35); font-size:0.75rem; font-weight:700; padding:4px 12px; border-radius:20px;">
                TEAM OF 4 &bull; CSE
            </span>
        </div>
    </div>
    <div style="margin-top:1.25rem; padding-top:1rem; border-top:1px solid rgba(51,65,85,0.4); display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:0.75rem;">
        <div style="background:#0B0F17; padding:10px 14px; border-radius:8px; border:1px solid rgba(51,65,85,0.4);">
            <div style="font-weight:700; color:#F8FAFC; font-size:0.88rem;">Balaji (Team Lead)</div>
            <div style="font-size:0.75rem; color:#38BDF8;">Project Lead &amp; System Architecture</div>
        </div>
        <div style="background:#0B0F17; padding:10px 14px; border-radius:8px; border:1px solid rgba(51,65,85,0.4);">
            <div style="font-weight:700; color:#F8FAFC; font-size:0.88rem;">Ahamed Rasim</div>
            <div style="font-size:0.75rem; color:#34D399;">Data Pipeline &amp; Pandas Engineering</div>
        </div>
        <div style="background:#0B0F17; padding:10px 14px; border-radius:8px; border:1px solid rgba(51,65,85,0.4);">
            <div style="font-weight:700; color:#F8FAFC; font-size:0.88rem;">Kishore Kumar</div>
            <div style="font-size:0.75rem; color:#F59E0B;">NumPy Mathematical &amp; Linear Algebra</div>
        </div>
        <div style="background:#0B0F17; padding:10px 14px; border-radius:8px; border:1px solid rgba(51,65,85,0.4);">
            <div style="font-weight:700; color:#F8FAFC; font-size:0.88rem;">Aadthiyan</div>
            <div style="font-size:0.75rem; color:#A78BFA;">Matplotlib Visual Analytics &amp; UI</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
