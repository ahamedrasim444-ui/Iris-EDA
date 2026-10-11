"""
styles.py
Deep Tech Obsidian Design System & Visual Identity.
Palette:
  - Background: Pure Deep Obsidian (#0B0F17) with layered elevation (#131B2E and #1E293B)
  - Borders & Dividers: Translucent borders (#334155 with 40-50% opacity)
  - Primary Accent: Electric Cyan (#38BDF8) & Neon Emerald (#34D399)
  - Secondary Accent: Soft Lavender (#A78BFA) for Virginica, Warm Amber (#F59E0B) for Versicolor
  - Typography: Pure white (#F8FAFC) headers, crisp slate (#94A3B8) body text
"""

import base64
import os

# Base64 encoded Deep Tech Obsidian Botanical Iris Logo SVG
OBSIDIAN_IRIS_LOGO_B64 = (
    "PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9Im9ic0dyYWQiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMzhCREY4IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjUwJSIgc3RvcC1jb2xvcj0iIzFFQThFMCIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMEU3QkE4IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxmaWx0ZXIgaWQ9ImN5YW5HbG93IiB4PSItMjAlIiB5PSItMjAlIiB3aWR0aD0iMTQwJSIgaGVpZ2h0PSIxNDAlIj4KICAgICAgPGZlRHJvcFNoYWRvdyBkeD0iMCIgZHk9IjQiIHN0ZERldmlhdGlvbj0iNiIgZmxvb2QtY29sb3I9IiMzOEJERjgiIGZsb29kLW9wYWNpdHk9IjAuMzUiIC8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPCEtLSBTbmVhdCBJY29uaWMgUm91bmRlZCBCYWRnZSAtLT4KICA8cmVjdCB4PSI0IiB5PSI0IiB3aWR0aD0iOTIiIGhlaWdodD0iOTIiIHJ4PSIyMiIgZmlsbD0iIzBCMEYxNyIgc3Ryb2tlPSIjMzhCREY4IiBzdHJva2Utd2lkdGg9IjIiIGZpbHRlcj0idXJsKCNjeWFuR2xvdykiIC8+CiAgPCEtLSBCb3RhbmljYWwgSXJpcyBQZXRhbHMgJiBTeW1tZXRyeSAtLT4KICA8cGF0aCBkPSJNNTAgMTggQzQ1IDMyIDM2IDQ0IDI2IDUwIEMzOCA1MiA0NiA2MiA1MCA4MiBDNTQgNjIgNjIgNTIgNzQgNTAgQzY0IDQ0IDU1IDMyIDUwIDE4IFoiIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC45NSIgLz4KICA8IS0tIElubmVyIFN0YW5kYXJkIFBldGFscyAtLT4KICA8cGF0aCBkPSJNNTAgMzAgQzQ3IDQwIDQzIDQ3IDM4IDUwIEM0NCA1MiA0NyA1NyA1MCA3MCBDNTMgNTcgNTYgNTIgNjIgNTAgQzU3IDQ3IDUzIDQwIDUwIDMwIFoiIGZpbGw9IiNlN2U3ZmYiIC8+CiAgPCEtLSBHb2xkZW4gQmlvbG9naWNhbCBDb3JlIFN0YW1lbiAtLT4KICA8Y2lyY2xlIGN4PSI1MCIgY3k9IjUwIiByPSI1LjUiIGZpbGw9IiMzNEQzOTkiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIyIiAvPgogIDwhLS0gQm90YW5pY2FsIENhbGlicmF0aW9uIEF4aXMgTGluZSAtLT4KICA8bGluZSB4MT0iNTAiIHkxPSI1MCIgeDI9IjUwIiB5Mj0iODAiIHN0cm9rZT0iIzM4QkRGOCIgc3Ryb2tlLXdpZHRoPSIyLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8bGluZSB4MT0iMjgiIHkxPSI1MCIgeDI9IjcyIiB5Mj0iNTAiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIxLjIiIHN0cm9rZS1kYXNoYXJyYXk9IjIgMiIgc3Ryb2tlLW9wYWNpdHk9IjAuOCIgLz4KPC9zdmc+Cg=="
)

# Compatibility alias
SNEAT_IRIS_LOGO_B64 = OBSIDIAN_IRIS_LOGO_B64


def get_iris_logo_img(size: int = 42) -> str:
    """Returns an HTML img tag with base64 data URI to guarantee 100% visual display."""
    return f'<img src="data:image/svg+xml;base64,{OBSIDIAN_IRIS_LOGO_B64}" width="{size}" height="{size}" alt="Iris Logo" style="vertical-align:middle;display:inline-block;border-radius:12px;filter:drop-shadow(0 0 10px rgba(56,189,248,0.55));" />'


def get_iris_logo_svg(size: int = 42) -> str:
    """Returns raw SVG string."""
    return f"""
    <svg width="{size}" height="{size}" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect x="4" y="4" width="92" height="92" rx="22" fill="#0B0F17" stroke="#38BDF8" stroke-width="2" />
      <path d="M50 18 C45 32 36 44 26 50 C38 52 46 62 50 82 C54 62 62 52 74 50 C64 44 55 32 50 18 Z" fill="#ffffff" fill-opacity="0.95" />
      <path d="M50 30 C47 40 43 47 38 50 C44 52 47 57 50 70 C53 57 56 52 62 50 C57 47 53 40 50 30 Z" fill="#e7e7ff" />
      <circle cx="50" cy="50" r="5.5" fill="#34D399" stroke="#ffffff" stroke-width="2" />
      <line x1="50" y1="50" x2="50" y2="80" stroke="#38BDF8" stroke-width="2.5" stroke-linecap="round" />
    </svg>
    """


def get_custom_css(antigravity_mode: bool = False) -> str:
    """Returns Deep Tech Obsidian CSS design system for Iris Analytics Lab."""
    antigravity_animation = ""
    if antigravity_mode:
        antigravity_animation = """
        @keyframes floatEffect {
            0%   { transform: translateY(0px);  }
            50%  { transform: translateY(-8px); }
            100% { transform: translateY(0px);  }
        }
        .main .block-container {
            animation: floatEffect 5s ease-in-out infinite;
        }
        .float-element {
            animation: floatEffect 3.5s ease-in-out infinite;
        }
        """

    css_body = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    :root {
        --bg-obsidian: #0B0F17;
        --bg-card: #131B2E;
        --bg-card-secondary: #1E293B;
        --border-obsidian: rgba(51, 65, 85, 0.45);
        --border-obsidian-hover: rgba(56, 189, 248, 0.4);
        --accent-cyan: #38BDF8;
        --accent-emerald: #34D399;
        --accent-lavender: #A78BFA;
        --accent-amber: #F59E0B;
        --text-heading: #F8FAFC;
        --text-body: #94A3B8;
        --text-muted: #64748B;
        --card-radius: 16px;
    }

    html, body, .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        background-color: var(--bg-obsidian) !important;
        color: var(--text-body) !important;
    }

    .stApp > header {
        background-color: rgba(11, 15, 23, 0.85) !important;
        backdrop-filter: blur(12px) !important;
        border-bottom: 1px solid var(--border-obsidian) !important;
    }

    .block-container {
        padding-top: 1.25rem !important;
        padding-bottom: 3rem !important;
        max-width: 1360px !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: var(--text-heading) !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
    }
    p, li, span {
        color: var(--text-body);
        line-height: 1.65;
    }
    strong, b {
        color: var(--text-heading) !important;
    }
    code {
        font-family: 'JetBrains Mono', monospace !important;
        color: var(--accent-cyan) !important;
        background: rgba(56, 189, 248, 0.1) !important;
        padding: 0.15rem 0.45rem !important;
        border-radius: 6px !important;
        border: 1px solid rgba(56, 189, 248, 0.25) !important;
        font-size: 0.88em !important;
    }

    /* Sticky Top Navigation Bar */
    .obsidian-navbar {
        position: sticky;
        top: 0;
        z-index: 999;
        background: rgba(19, 27, 46, 0.88);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid var(--border-obsidian);
        border-radius: 16px;
        padding: 0.75rem 1.25rem;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.05);
    }
    .nav-brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .nav-brand-title {
        font-size: 1.15rem;
        font-weight: 800;
        color: var(--text-heading);
        letter-spacing: -0.01em;
        line-height: 1.1;
    }
    .nav-badge {
        display: inline-block;
        font-size: 0.7rem;
        font-weight: 600;
        color: var(--accent-cyan);
        background: rgba(56, 189, 248, 0.12);
        border: 1px solid rgba(56, 189, 248, 0.35);
        padding: 2px 8px;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .nav-pills {
        display: flex;
        align-items: center;
        gap: 6px;
        flex-wrap: wrap;
    }
    .nav-pill-item {
        font-size: 0.82rem;
        font-weight: 500;
        color: var(--text-body);
        padding: 6px 12px;
        border-radius: 10px;
        border: 1px solid transparent;
        text-decoration: none;
        transition: all 0.2s ease;
    }
    .nav-pill-item:hover {
        color: var(--text-heading);
        background: rgba(255, 255, 255, 0.05);
        border-color: var(--border-obsidian);
    }
    .nav-pill-active {
        color: var(--accent-cyan) !important;
        background: rgba(56, 189, 248, 0.12) !important;
        border-color: rgba(56, 189, 248, 0.4) !important;
        font-weight: 600 !important;
    }
    .nav-status-pill {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 0.78rem;
        color: var(--accent-emerald);
        background: rgba(52, 211, 153, 0.1);
        border: 1px solid rgba(52, 211, 153, 0.3);
        padding: 5px 12px;
        border-radius: 20px;
        font-weight: 600;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0E1524 !important;
        border-right: 1px solid var(--border-obsidian) !important;
    }
    section[data-testid="stSidebar"] * {
        color: var(--text-body) !important;
    }
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3 {
        color: var(--text-heading) !important;
    }
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stSlider label,
    section[data-testid="stSidebar"] .stMultiSelect label {
        color: var(--text-heading) !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
    }

    /* Layered Cards Elevation */
    .obs-card {
        background: linear-gradient(145deg, #131B2E 0%, #162238 100%);
        border: 1px solid var(--border-obsidian);
        border-radius: var(--card-radius);
        padding: 1.5rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    }
    .obs-card:hover {
        border-color: var(--border-obsidian-hover);
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.55), 0 0 20px rgba(56, 189, 248, 0.1);
    }

    /* KPI Metric Cards */
    div[data-testid="metric-container"] {
        background: linear-gradient(145deg, #131B2E 0%, #1A253D 100%) !important;
        border: 1px solid var(--border-obsidian) !important;
        border-radius: var(--card-radius) !important;
        padding: 1.25rem !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4) !important;
        transition: all 0.25s ease !important;
    }
    div[data-testid="metric-container"]:hover {
        transform: translateY(-3px) !important;
        border-color: rgba(56, 189, 248, 0.5) !important;
        box-shadow: 0 10px 28px rgba(0, 0, 0, 0.5), 0 0 20px rgba(56, 189, 248, 0.18) !important;
    }
    div[data-testid="metric-container"] [data-testid="stMetricLabel"] {
        color: var(--text-muted) !important;
        font-size: 0.8rem !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.06em !important;
    }
    div[data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: var(--accent-cyan) !important;
        font-size: 2.1rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.03em !important;
    }
    div[data-testid="metric-container"] [data-testid="stMetricDelta"] {
        color: var(--accent-emerald) !important;
        font-weight: 600 !important;
    }

    /* Streamlit Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: #131B2E !important;
        border: 1px solid var(--border-obsidian) !important;
        border-radius: 14px !important;
        padding: 5px !important;
        gap: 6px !important;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        color: var(--text-muted) !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
        border-radius: 10px !important;
        padding: 9px 18px !important;
        transition: all 0.2s ease !important;
        border: none !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: var(--text-heading) !important;
        background: rgba(255, 255, 255, 0.05) !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.22) 0%, rgba(14, 77, 107, 0.35) 100%) !important;
        color: var(--accent-cyan) !important;
        border: 1px solid rgba(56, 189, 248, 0.45) !important;
        box-shadow: 0 0 16px rgba(56, 189, 248, 0.25) !important;
    }
    .stTabs [data-baseweb="tab-panel"] {
        padding-top: 1.5rem !important;
    }

    /* Buttons */
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

    /* Sliders, Selects */
    .stSlider [data-baseweb="slider"] {
        color: var(--accent-cyan) !important;
    }
    .stSlider [data-testid="stThumbValue"] {
        background-color: #131B2E !important;
        color: var(--accent-cyan) !important;
        border: 1px solid var(--border-obsidian) !important;
        border-radius: 6px !important;
    }
    .stSelectbox > div > div, .stMultiSelect > div > div {
        background-color: #131B2E !important;
        border: 1px solid var(--border-obsidian) !important;
        border-radius: 10px !important;
        color: var(--text-heading) !important;
    }
    .stMultiSelect [data-baseweb="tag"] {
        background: rgba(56, 189, 248, 0.15) !important;
        color: var(--accent-cyan) !important;
        border: 1px solid rgba(56, 189, 248, 0.4) !important;
        border-radius: 8px !important;
    }

    /* Tables */
    .stDataFrame {
        border: 1px solid var(--border-obsidian) !important;
        border-radius: 12px !important;
        overflow: hidden !important;
    }
    .stDataFrame thead tr th {
        background-color: #131B2E !important;
        color: var(--accent-cyan) !important;
        font-weight: 700 !important;
        border-bottom: 1px solid var(--border-obsidian) !important;
    }
    .stDataFrame tbody tr td {
        color: var(--text-body) !important;
        background-color: #0B0F17 !important;
        border-bottom: 1px solid rgba(51, 65, 85, 0.25) !important;
    }
    .stDataFrame tbody tr:hover td {
        background-color: #131B2E !important;
    }

    /* Formula & Prediction Cards */
    .formula-card {
        background: #131B2E !important;
        border: 1px solid var(--border-obsidian) !important;
        border-left: 4px solid var(--accent-cyan) !important;
        border-radius: 12px !important;
        padding: 1.25rem !important;
        margin: 1rem 0 !important;
        color: var(--text-body) !important;
    }
    .formula-title {
        color: var(--accent-cyan) !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        margin-bottom: 0.5rem !important;
    }
    .prediction-card {
        background: linear-gradient(145deg, #131B2E 0%, #1A2744 100%) !important;
        border-radius: 16px !important;
        border: 2px solid var(--accent-cyan) !important;
        box-shadow: 0 8px 32px rgba(56, 189, 248, 0.25) !important;
        padding: 1.75rem !important;
        text-align: center !important;
    }
    .prediction-species {
        color: var(--text-heading) !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.02em !important;
    }

    /* Sneat Compatibility */
    .sneat-hero-card {
        background: linear-gradient(135deg, #0D1424 0%, #131B2E 50%, #1A253D 100%) !important;
        border: 1px solid var(--border-obsidian) !important;
        border-radius: 20px !important;
        padding: 2rem 2.25rem !important;
        margin-bottom: 1.5rem !important;
        box-shadow: 0 10px 36px rgba(0, 0, 0, 0.5) !important;
    }
    .sneat-hero-title {
        font-size: 1.85rem !important;
        font-weight: 800 !important;
        color: var(--text-heading) !important;
        margin: 0 !important;
    }
    .sneat-hero-subtitle {
        color: var(--text-body) !important;
        font-size: 0.95rem !important;
        margin: 0.5rem 0 1rem 0 !important;
    }
    .badge-sneat {
        display: inline-block;
        padding: 0.3rem 0.75rem;
        border-radius: 8px;
        font-size: 0.76rem;
        font-weight: 600;
        margin-right: 6px;
        margin-bottom: 6px;
    }
    .bg-label-primary {
        background: rgba(56, 189, 248, 0.12) !important;
        color: var(--accent-cyan) !important;
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
    }
    .bg-label-success {
        background: rgba(52, 211, 153, 0.12) !important;
        color: var(--accent-emerald) !important;
        border: 1px solid rgba(52, 211, 153, 0.3) !important;
    }
    .bg-label-info {
        background: rgba(56, 189, 248, 0.15) !important;
        color: var(--accent-cyan) !important;
        border: 1px solid rgba(56, 189, 248, 0.35) !important;
    }
    .bg-label-warning {
        background: rgba(245, 158, 11, 0.12) !important;
        color: var(--accent-amber) !important;
        border: 1px solid rgba(245, 158, 11, 0.3) !important;
    }

    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: var(--bg-obsidian); }
    ::-webkit-scrollbar-thumb { background: #334155; border-radius: 4px; }
    </style>
    """
    if antigravity_animation:
        css_body = css_body.replace("</style>", f"{antigravity_animation}\n    </style>")
    return css_body

def render_top_navbar() -> str:
    """Renders Sticky Top Navigation Bar with glowing cyan botanical logo, section pills, and status badge."""
    logo = get_iris_logo_img(38)
    return f"""
    <div class="obsidian-navbar">
        <div class="nav-brand">
            {logo}
            <div>
                <div class="nav-brand-title">IRIS ANALYTICS LAB</div>
                <div style="display:flex; align-items:center; gap:6px; margin-top:2px;">
                    <span class="nav-badge">v2.0</span>
                    <span style="font-size:0.7rem; color:#64748B; font-weight:500;">Data Science Essentials</span>
                </div>
            </div>
        </div>
        <div class="nav-pills">
            <span class="nav-pill-item nav-pill-active">&#127800; Overview</span>
            <span class="nav-pill-item">&#127807; Botanical Anatomy</span>
            <span class="nav-pill-item">&#129518; Mathematical Engine</span>
            <span class="nav-pill-item">&#128200; Visual Analytics</span>
            <span class="nav-pill-item">&#127919; Centroid Classifier</span>
        </div>
        <div style="display:flex; align-items:center; gap:10px;">
            <div class="nav-status-pill">
                <span style="display:inline-block; width:7px; height:7px; background:#34D399; border-radius:50%; box-shadow:0 0 8px #34D399;"></span>
                <span>NumPy Active</span>
            </div>
            <span style="font-size:0.75rem; color:#94A3B8; background:rgba(255,255,255,0.06); padding:4px 10px; border-radius:12px; border:1px solid rgba(51,65,85,0.5);">
                CSE Mini-Project
            </span>
        </div>
    </div>
    """


def render_hero_banner() -> str:
    """Renders Obsidian Hero Section with logo, KPI highlights, and project credentials."""
    logo = get_iris_logo_img(46)
    return f"""
    <div class="sneat-hero-card">
        <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 0.85rem;">
            {logo}
            <div>
                <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 4px;">
                    <span class="badge-sneat bg-label-primary">OBSIDIAN DEEP TECH v2.0</span>
                    <span class="badge-sneat bg-label-success">100% NUMPY LINEAR ALGEBRA</span>
                </div>
                <h1 class="sneat-hero-title">Iris Flower Data Analysis</h1>
            </div>
        </div>
        <p class="sneat-hero-subtitle">
            Multidimensional botanical data science suite powered by pure NumPy matrix linear algebra, 
            covariance & correlation tensor analysis, and interactive flower morphometry visualization.
        </p>
        <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 0.75rem;">
            <span class="badge-sneat bg-label-primary">&#127769; Deep Tech Obsidian (#0B0F17)</span>
            <span class="badge-sneat bg-label-info">&#127800; 150 Botanical Specimens</span>
            <span class="badge-sneat bg-label-warning">&#128208; 4 Morphometric Dimensions</span>
            <span class="badge-sneat bg-label-success">&#127919; 100% Setosa Linear Separability</span>
        </div>
    </div>
    """


def render_sidebar_header() -> str:
    """Renders glowing Obsidian brand header in the sidebar."""
    logo = get_iris_logo_img(36)
    return f"""
    <div style="display: flex; align-items: center; gap: 12px; padding: 0.2rem 0 0.85rem 0; border-bottom: 1px solid rgba(51, 65, 85, 0.45); margin-bottom: 1rem;">
        {logo}
        <div>
            <div style="font-weight: 800; font-size: 1.15rem; color: #F8FAFC; line-height: 1.1; letter-spacing: -0.02em;">IRIS LAB</div>
            <div style="font-size: 0.7rem; color: #38BDF8; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;">CONTROLS &amp; FILTERS</div>
        </div>
    </div>
    """


def render_easter_egg_card() -> str:
    """Renders Python Easter Egg card with antigravity homage."""
    return """
    <div style="background: linear-gradient(135deg, #131B2E 0%, #1A253D 100%); border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 14px; padding: 1rem 1.25rem; margin-top: 1rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
            <div>
                <strong style="color: #F8FAFC; font-size: 0.92rem;">&#128640; Python Easter Egg: <code>import antigravity</code></strong>
                <p style="margin: 4px 0 0 0; font-size: 0.84rem; color: #94A3B8;">
                    Homage to XKCD #353: <em>"I wrote 20 short programs in Python yesterday. It was wonderful. Now I am flying!"</em>
                </p>
            </div>
            <div>
                <a href="https://xkcd.com/353/" target="_blank" 
                   style="background: #0284C7; color: #ffffff; padding: 0.4rem 0.85rem; border-radius: 8px; text-decoration: none; font-size: 0.8rem; font-weight: 600; display: inline-block; box-shadow: 0 2px 10px rgba(2, 132, 199, 0.4);">
                    View XKCD #353 &nearr;
                </a>
            </div>
        </div>
    </div>
    """


def render_species_cards_html() -> str:
    """Renders Module 2: Side-by-side species taxonomy cards with morphological diagrams."""
    return """
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-bottom: 1.5rem;">
        <!-- Card 1: Setosa -->
        <div style="background: #131B2E; border: 1px solid rgba(56, 189, 248, 0.4); border-top: 4px solid #38BDF8; border-radius: 16px; padding: 1.25rem; box-shadow: 0 8px 24px rgba(0,0,0,0.4);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                <h3 style="color:#F8FAFC; margin:0; font-size:1.15rem;">Iris Setosa</h3>
                <span style="background:rgba(56,189,248,0.15); color:#38BDF8; border:1px solid rgba(56,189,248,0.4); font-size:0.7rem; font-weight:700; padding:2px 8px; border-radius:12px;">LINEARLY SEPARABLE</span>
            </div>
            <div style="background:#0B0F17; border-radius:10px; padding:12px; margin-bottom:12px; text-align:center; border:1px solid rgba(51,65,85,0.4);">
                <svg width="120" height="100" viewBox="0 0 120 100" fill="none">
                    <ellipse cx="60" cy="35" rx="14" ry="24" fill="#38BDF8" fill-opacity="0.35" stroke="#38BDF8" stroke-width="1.8"/>
                    <ellipse cx="38" cy="65" rx="13" ry="22" transform="rotate(-45 38 65)" fill="#38BDF8" fill-opacity="0.35" stroke="#38BDF8" stroke-width="1.8"/>
                    <ellipse cx="82" cy="65" rx="13" ry="22" transform="rotate(45 82 65)" fill="#38BDF8" fill-opacity="0.35" stroke="#38BDF8" stroke-width="1.8"/>
                    <ellipse cx="60" cy="50" rx="7" ry="12" fill="#38BDF8" fill-opacity="0.8" stroke="#F8FAFC" stroke-width="1.2"/>
                    <ellipse cx="48" cy="46" rx="6" ry="11" transform="rotate(-30 48 46)" fill="#38BDF8" fill-opacity="0.8" stroke="#F8FAFC" stroke-width="1.2"/>
                    <ellipse cx="72" cy="46" rx="6" ry="11" transform="rotate(30 72 46)" fill="#38BDF8" fill-opacity="0.8" stroke="#F8FAFC" stroke-width="1.2"/>
                    <circle cx="60" cy="55" r="5" fill="#34D399" stroke="#ffffff" stroke-width="1.5"/>
                </svg>
                <div style="font-size:0.72rem; color:#94A3B8; margin-top:4px;">Morphology: Diminutive Standards &bull; Broad Falls</div>
            </div>
            <div style="font-size:0.83rem; line-height:1.6; color:#94A3B8;">
                <div><strong style="color:#F8FAFC;">Petal Length (Standards):</strong> 1.0 &ndash; 1.9 cm</div>
                <div><strong style="color:#F8FAFC;">Petal Width:</strong> 0.1 &ndash; 0.6 cm</div>
                <div><strong style="color:#F8FAFC;">Sepal Length (Falls):</strong> 4.3 &ndash; 5.8 cm</div>
                <div><strong style="color:#F8FAFC;">Sepal Width:</strong> 2.3 &ndash; 4.4 cm</div>
            </div>
            <div style="margin-top:10px; padding-top:8px; border-top:1px solid rgba(51,65,85,0.4); font-size:0.75rem; color:#38BDF8;">
                â˜… 100% clean threshold cut at Petal Length &le; 2.45 cm
            </div>
        </div>

        <!-- Card 2: Versicolor -->
        <div style="background: #131B2E; border: 1px solid rgba(245, 158, 11, 0.4); border-top: 4px solid #F59E0B; border-radius: 16px; padding: 1.25rem; box-shadow: 0 8px 24px rgba(0,0,0,0.4);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                <h3 style="color:#F8FAFC; margin:0; font-size:1.15rem;">Iris Versicolor</h3>
                <span style="background:rgba(245,158,11,0.15); color:#F59E0B; border:1px solid rgba(245,158,11,0.4); font-size:0.7rem; font-weight:700; padding:2px 8px; border-radius:12px;">INTERMEDIATE CLASS</span>
            </div>
            <div style="background:#0B0F17; border-radius:10px; padding:12px; margin-bottom:12px; text-align:center; border:1px solid rgba(51,65,85,0.4);">
                <svg width="120" height="100" viewBox="0 0 120 100" fill="none">
                    <ellipse cx="60" cy="30" rx="12" ry="27" fill="#F59E0B" fill-opacity="0.35" stroke="#F59E0B" stroke-width="1.8"/>
                    <ellipse cx="36" cy="62" rx="11" ry="24" transform="rotate(-45 36 62)" fill="#F59E0B" fill-opacity="0.35" stroke="#F59E0B" stroke-width="1.8"/>
                    <ellipse cx="84" cy="62" rx="11" ry="24" transform="rotate(45 84 62)" fill="#F59E0B" fill-opacity="0.35" stroke="#F59E0B" stroke-width="1.8"/>
                    <ellipse cx="60" cy="46" rx="8" ry="18" fill="#F59E0B" fill-opacity="0.8" stroke="#F8FAFC" stroke-width="1.2"/>
                    <ellipse cx="46" cy="44" rx="7" ry="16" transform="rotate(-30 46 44)" fill="#F59E0B" fill-opacity="0.8" stroke="#F8FAFC" stroke-width="1.2"/>
                    <ellipse cx="74" cy="44" rx="7" ry="16" transform="rotate(30 74 44)" fill="#F59E0B" fill-opacity="0.8" stroke="#F8FAFC" stroke-width="1.2"/>
                    <circle cx="60" cy="52" r="5" fill="#34D399" stroke="#ffffff" stroke-width="1.5"/>
                </svg>
                <div style="font-size:0.72rem; color:#94A3B8; margin-top:4px;">Morphology: Balanced Standards &bull; Elegant Falls</div>
            </div>
            <div style="font-size:0.83rem; line-height:1.6; color:#94A3B8;">
                <div><strong style="color:#F8FAFC;">Petal Length (Standards):</strong> 3.0 &ndash; 5.1 cm</div>
                <div><strong style="color:#F8FAFC;">Petal Width:</strong> 1.0 &ndash; 1.8 cm</div>
                <div><strong style="color:#F8FAFC;">Sepal Length (Falls):</strong> 4.9 &ndash; 7.0 cm</div>
                <div><strong style="color:#F8FAFC;">Sepal Width:</strong> 2.0 &ndash; 3.4 cm</div>
            </div>
            <div style="margin-top:10px; padding-top:8px; border-top:1px solid rgba(51,65,85,0.4); font-size:0.75rem; color:#F59E0B;">
                â˜… Minor overlap with Virginica near Petal Length 4.8 cm
            </div>
        </div>

        <!-- Card 3: Virginica -->
        <div style="background: #131B2E; border: 1px solid rgba(167, 139, 250, 0.4); border-top: 4px solid #A78BFA; border-radius: 16px; padding: 1.25rem; box-shadow: 0 8px 24px rgba(0,0,0,0.4);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                <h3 style="color:#F8FAFC; margin:0; font-size:1.15rem;">Iris Virginica</h3>
                <span style="background:rgba(167,139,250,0.15); color:#A78BFA; border:1px solid rgba(167,139,250,0.4); font-size:0.7rem; font-weight:700; padding:2px 8px; border-radius:12px;">LARGEST SPECIMEN</span>
            </div>
            <div style="background:#0B0F17; border-radius:10px; padding:12px; margin-bottom:12px; text-align:center; border:1px solid rgba(51,65,85,0.4);">
                <svg width="120" height="100" viewBox="0 0 120 100" fill="none">
                    <ellipse cx="60" cy="26" rx="14" ry="32" fill="#A78BFA" fill-opacity="0.35" stroke="#A78BFA" stroke-width="1.8"/>
                    <ellipse cx="32" cy="62" rx="13" ry="28" transform="rotate(-45 32 62)" fill="#A78BFA" fill-opacity="0.35" stroke="#A78BFA" stroke-width="1.8"/>
                    <ellipse cx="88" cy="62" rx="13" ry="28" transform="rotate(45 88 62)" fill="#A78BFA" fill-opacity="0.35" stroke="#A78BFA" stroke-width="1.8"/>
                    <ellipse cx="60" cy="42" rx="10" ry="22" fill="#A78BFA" fill-opacity="0.8" stroke="#F8FAFC" stroke-width="1.2"/>
                    <ellipse cx="44" cy="40" rx="9" ry="20" transform="rotate(-30 44 40)" fill="#A78BFA" fill-opacity="0.8" stroke="#F8FAFC" stroke-width="1.2"/>
                    <ellipse cx="76" cy="40" rx="9" ry="20" transform="rotate(30 76 40)" fill="#A78BFA" fill-opacity="0.8" stroke="#F8FAFC" stroke-width="1.2"/>
                    <circle cx="60" cy="50" r="5.5" fill="#34D399" stroke="#ffffff" stroke-width="1.5"/>
                </svg>
                <div style="font-size:0.72rem; color:#94A3B8; margin-top:4px;">Morphology: Robust Standards &bull; Sweeping Falls</div>
            </div>
            <div style="font-size:0.83rem; line-height:1.6; color:#94A3B8;">
                <div><strong style="color:#F8FAFC;">Petal Length (Standards):</strong> 4.5 &ndash; 6.9 cm</div>
                <div><strong style="color:#F8FAFC;">Petal Width:</strong> 1.4 &ndash; 2.5 cm</div>
                <div><strong style="color:#F8FAFC;">Sepal Length (Falls):</strong> 4.9 &ndash; 7.9 cm</div>
                <div><strong style="color:#F8FAFC;">Sepal Width:</strong> 2.2 &ndash; 3.8 cm</div>
            </div>
            <div style="margin-top:10px; padding-top:8px; border-top:1px solid rgba(51,65,85,0.4); font-size:0.75rem; color:#A78BFA;">
                â˜… Highest petal area proxy (mean ~11.3 cmÂ²)
            </div>
        </div>
    </div>
    """


def render_team_footer() -> str:
    """Renders Module 6: Footer with Team Members and CSE Department Credits."""
    return """
    <div style="background: linear-gradient(135deg, #0D1424 0%, #131B2E 100%); border: 1px solid rgba(51, 65, 85, 0.45); border-radius: 16px; padding: 2rem 2.5rem; margin-top: 2.5rem; box-shadow: 0 10px 30px rgba(0,0,0,0.4);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 2rem;">
            <div>
                <div style="font-size: 1.25rem; font-weight: 800; color: #F8FAFC; letter-spacing: -0.01em;">
                    Department of Computer Science &amp; Engineering
                </div>
                <div style="font-size: 0.88rem; color: #38BDF8; font-weight: 600; margin-top: 4px;">
                    Data Science &amp; Multidimensional Analytics (CS601) &bull; Mini-Project
                </div>
                <div style="font-size: 0.84rem; color: #94A3B8; margin-top: 8px;">
                    Faculty Guide: <strong style="color: #F8FAFC;">Prof. Keerthana</strong>, Assistant Professor, Dept of CSE
                </div>
            </div>
            <div style="text-align: right;">
                <span style="background: rgba(56, 189, 248, 0.12); color: #38BDF8; border: 1px solid rgba(56, 189, 248, 0.35); font-size: 0.75rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;">
                    TEAM OF 4 &bull; CSE
                </span>
            </div>
        </div>

        <div style="margin-top: 1.5rem; padding-top: 1.25rem; border-top: 1px solid rgba(51, 65, 85, 0.4); display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem;">
            <div style="background: #0B0F17; padding: 12px 16px; border-radius: 10px; border: 1px solid rgba(51,65,85,0.4);">
                <div style="font-weight: 700; color: #F8FAFC; font-size: 0.92rem;">Balaji (Team Lead)</div>
                <div style="font-size: 0.78rem; color: #38BDF8;">Project Lead &amp; System Architecture</div>
            </div>
            <div style="background: #0B0F17; padding: 12px 16px; border-radius: 10px; border: 1px solid rgba(51,65,85,0.4);">
                <div style="font-weight: 700; color: #F8FAFC; font-size: 0.92rem;">Ahamed Rasim</div>
                <div style="font-size: 0.78rem; color: #34D399;">Data Pipeline &amp; Pandas Engineering</div>
            </div>
            <div style="background: #0B0F17; padding: 12px 16px; border-radius: 10px; border: 1px solid rgba(51,65,85,0.4);">
                <div style="font-weight: 700; color: #F8FAFC; font-size: 0.92rem;">Kishore Kumar</div>
                <div style="font-size: 0.78rem; color: #F59E0B;">NumPy Mathematical &amp; Linear Algebra</div>
            </div>
            <div style="background: #0B0F17; padding: 12px 16px; border-radius: 10px; border: 1px solid rgba(51,65,85,0.4);">
                <div style="font-weight: 700; color: #F8FAFC; font-size: 0.92rem;">Aadthiyan</div>
                <div style="font-size: 0.78rem; color: #A78BFA;">Matplotlib Visual Analytics &amp; Frontend UI</div>
            </div>
        </div>

        <div style="margin-top: 1.25rem; text-align: center; font-size: 0.78rem; color: #64748B;">
            Iris Dataset originally collected by Edgar Anderson (1935) &bull; Analyzed by Ronald A. Fisher (1936) &bull; Designed with Deep Tech Obsidian System
        </div>
    </div>
    """
