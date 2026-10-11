"""
styles.py
Sneat – Vuetify Vuejs 3 Admin Template Dark Theme & Botanical Branding.
Clean, modern, high-contrast, professional dark mode dashboard styling based on Sneat Vuetify 3 Dark.
Guarantees 100% visual logo display (Base64 img) and crystal-clear text readability on dark surfaces.
"""

import base64
import os

# Base64 encoded Sneat Botanical Iris Logo SVG (100% immune to markdown code indentation bugs)
SNEAT_IRIS_LOGO_B64 = (
    "PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InNuZWF0R3JhZGllbnQiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjNjk2Y2ZmIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjUwJSIgc3RvcC1jb2xvcj0iIzc4N2JmZiIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjODU1Y2Y2IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxmaWx0ZXIgaWQ9InNuZWF0R2xvdyIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjNjk2Y2ZmIiBmbG9vZC1vcGFjaXR5PSIwLjM1IiAvPgogICAgPC9maWx0ZXI+CiAgPC9kZWZzPgogIDwhLS0gU25lYXQgSWNvbmljIFJvdW5kZWQgQmFkZ2UgLS0+CiAgPHJlY3QgeD0iNCIgeT0iNCIgd2lkdGg9IjkyIiBoZWlnaHQ9IjkyIiByeD0iMjIiIGZpbGw9InVybCgjc25lYXRHcmFkaWVudCkiIGZpbHRlcj0idXJsKCNzbmVhdEdsb3cpIiAvPgogIDwhLS0gQm90YW5pY2FsIElyaXMgUGV0YWxzICYgU3ltbWV0cnkgLS0+CiAgPHBhdGggZD0iTTUwIDE4IEM0NSAzMiAzNiA0NCAyNiA1MCBDMzggNTIgNDYgNjIgNTAgODIgQzU0IDYyIDYyIDUyIDc0IDUwIEM2NCA0NCA1NSAzMiA1MCAxOCBaIiBmaWxsPSIjZmZmZmZmIiBmaWxsLW9wYWNpdHk9IjAuOTUiIC8+CiAgPCEtLSBJbm5lciBTdGFuZGFyZCBQZXRhbHMgLS0+CiAgPHBhdGggZD0iTTUwIDMwIEM0NyA0MCA0MyA0NyAzOCA1MCBDNDQgNTIgNDcgNTcgNTAgNzAgQzUzIDU3IDU2IDUyIDYyIDUwIEM1NyA0NyA1MyA0MCA1MCAzMCBaIiBmaWxsPSIjZTdlN2ZmIiAvPgogIDwhLS0gR29sZGVuIEJpb2xvZ2ljYWwgQ29yZSBTdGFtZW4gLS0+CiAgPGNpcmNsZSBjeD0iNTAiIGN5PSI1MCIgcj0iNS41IiBmaWxsPSIjNzFkZDM3IiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgLz4KICA8IS0tIEJvdGFuaWNhbCBDYWxpYnJhdGlvbiBBeGlzIExpbmUgLS0+CiAgPGxpbmUgeDE9IjUwIiB5MT0iNTAiIHgyPSI1MCIgeTI9IjgwIiBzdHJva2U9IiMwM2MzZWMiIHN0cm9rZS13aWR0aD0iMi41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIC8+CiAgPGxpbmUgeDE9IjI4IiB5MT0iNTAiIHgyPSI3MiIgeTI9IjUwIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMS4yIiBzdHJva2UtZGFzaGFycmF5PSIyIDIiIHN0cm9rZS1vcGFjaXR5PSIwLjgiIC8+Cjwvc3ZnPgo="
)


def get_iris_logo_img(size: int = 42) -> str:
    """Returns an HTML img tag with base64 data URI to guarantee 100% visual display in Streamlit without code escaping."""
    return f'<img src="data:image/svg+xml;base64,{SNEAT_IRIS_LOGO_B64}" width="{size}" height="{size}" alt="Sneat Logo" style="vertical-align:middle;display:inline-block;border-radius:10px;box-shadow:0 3px 10px rgba(105,108,255,0.5);" />'


def get_iris_logo_svg(size: int = 42) -> str:
    """Returns raw SVG if needed."""
    return f"""
    <svg width="{size}" height="{size}" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="sneatGradInline" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#696cff" />
          <stop offset="50%" stop-color="#787bff" />
          <stop offset="100%" stop-color="#855cf6" />
        </linearGradient>
      </defs>
      <rect x="4" y="4" width="92" height="92" rx="22" fill="url(#sneatGradInline)" />
      <path d="M50 18 C45 32 36 44 26 50 C38 52 46 62 50 82 C54 62 62 52 74 50 C64 44 55 32 50 18 Z" fill="#ffffff" fill-opacity="0.95" />
      <path d="M50 30 C47 40 43 47 38 50 C44 52 47 57 50 70 C53 57 56 52 62 50 C57 47 53 40 50 30 Z" fill="#e7e7ff" />
      <circle cx="50" cy="50" r="5.5" fill="#71dd37" stroke="#ffffff" stroke-width="2" />
      <line x1="50" y1="50" x2="50" y2="80" stroke="#03c3ec" stroke-width="2.5" stroke-linecap="round" />
    </svg>
    """


def get_custom_css(antigravity_mode: bool = False) -> str:
    """Returns Sneat – Vuetify Vuejs 3 Admin Template DARK THEME CSS design system."""
    
    antigravity_animation = ""
    if antigravity_mode:
        antigravity_animation = """
        @keyframes floatEffect {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
            100% { transform: translateY(0px); }
        }
        .main .block-container {
            animation: floatEffect 5s ease-in-out infinite;
        }
        """

    return f"""
    <style>
    /* =========================================================================
       SNEAT – VUETIFY VUEJS 3 ADMIN TEMPLATE (DARK THEME DESIGN SYSTEM)
       ========================================================================= */
    @import url('https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&display=swap');

    :root {{
        --sneat-primary: #696cff;
        --sneat-primary-hover: #787bff;
        --sneat-primary-light: rgba(105, 108, 255, 0.16);
        --sneat-secondary: #8592a3;
        --sneat-success: #71dd37;
        --sneat-success-light: rgba(113, 221, 55, 0.16);
        --sneat-info: #03c3ec;
        --sneat-info-light: rgba(3, 195, 236, 0.16);
        --sneat-warning: #ffab00;
        --sneat-warning-light: rgba(255, 171, 0, 0.16);
        --sneat-danger: #ff3e1d;
        --sneat-danger-light: rgba(255, 62, 29, 0.16);
        --sneat-heading: #e1def5;
        --sneat-body: #b2b3ca;
        --sneat-muted: #8688a2;
        --sneat-bg: #232333;
        --sneat-card-bg: #2b2c40;
        --sneat-border: #44476a;
        --sneat-shadow: 0 4px 18px 0 rgba(12, 12, 20, 0.42);
        --sneat-shadow-lg: 0 6px 24px 0 rgba(12, 12, 20, 0.55);
    }}

    /* Global App Container & Dark Base Font (Public Sans) */
    html, body, .stApp {{
        font-family: 'Public Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
        color: #b2b3ca !important;
        background-color: #232333 !important;
    }}

    .stApp [data-testid="stHeader"] {{
        background-color: rgba(35, 35, 51, 0.9) !important;
        backdrop-filter: blur(8px);
    }}

    .block-container {{
        padding-top: 1.25rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 100% !important;
    }}

    /* =========================================================================
       HEADINGS & PARAGRAPHS (CRISP SNEAT DARK TYPOGRAPHY)
       ========================================================================= */
    h1, h2, h3, h4, h5, h6,
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {{
        color: #e1def5 !important;
        font-weight: 600 !important;
        letter-spacing: -0.02em !important;
    }}

    p, li, .stMarkdown p, .stMarkdown li, [data-testid="stMarkdownContainer"] p {{
        color: #b2b3ca !important;
        font-size: 0.9375rem;
        line-height: 1.55;
    }}

    strong, b, .stMarkdown strong, .stMarkdown b {{
        color: #e1def5 !important;
        font-weight: 600 !important;
    }}

    .stCaption, [data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] p {{
        color: #8688a2 !important;
        font-size: 0.8125rem !important;
        font-weight: 500 !important;
    }}

    /* =========================================================================
       SIDEBAR (SNEAT DARK VERTICAL NAVIGATION MENU)
       ========================================================================= */
    section[data-testid="stSidebar"] {{
        background-color: #2b2c40 !important;
        border-right: 1px solid #44476a !important;
        box-shadow: 0 0.125rem 0.375rem 0 rgba(12, 12, 20, 0.3) !important;
    }}

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {{
        color: #e1def5 !important;
    }}

    section[data-testid="stSidebar"] .stCaption,
    section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {{
        color: #8688a2 !important;
    }}

    /* Widget Labels (Inputs, Sliders, Multi-selects) */
    [data-testid="stWidgetLabel"],
    [data-testid="stWidgetLabel"] label,
    [data-testid="stWidgetLabel"] p,
    [data-testid="stWidgetLabel"] span {{
        color: #e1def5 !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.02em;
    }}

    /* Sliders: Values, Min, Max & Numbers in Dark Mode */
    div[data-testid="stThumbValue"],
    div[data-testid="stThumbValue"] * {{
        color: #787bff !important;
        font-weight: 700 !important;
        font-size: 0.875rem !important;
    }}

    div[data-testid="stTickBarMin"],
    div[data-testid="stTickBarMax"],
    [data-testid="stSliderTickBar"] * {{
        color: #8688a2 !important;
        font-weight: 600 !important;
        font-size: 0.75rem !important;
    }}

    /* =========================================================================
       TABS NAVIGATION (VUETIFY 3 V-TABS PILL STYLE - DARK MODE)
       ========================================================================= */
    div[data-baseweb="tab-list"] {{
        border-bottom: none !important;
        gap: 0.5rem !important;
        background: #2b2c40 !important;
        padding: 0.5rem 0.75rem !important;
        border-radius: 0.5rem !important;
        box-shadow: 0 4px 18px 0 rgba(12, 12, 20, 0.42) !important;
        margin-bottom: 1.25rem !important;
        border: 1px solid #44476a !important;
    }}

    button[data-baseweb="tab"] {{
        color: #b2b3ca !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        padding: 0.55rem 1rem !important;
        border-radius: 0.375rem !important;
        border: none !important;
        background: transparent !important;
        transition: all 0.2s ease-in-out !important;
    }}

    button[data-baseweb="tab"] p,
    button[data-baseweb="tab"] div,
    button[data-baseweb="tab"] span {{
        color: inherit !important;
        font-weight: inherit !important;
    }}

    button[data-baseweb="tab"]:hover {{
        color: #787bff !important;
        background-color: rgba(105, 108, 255, 0.16) !important;
    }}

    button[data-baseweb="tab"][aria-selected="true"] {{
        color: #ffffff !important;
        font-weight: 600 !important;
        background-color: #696cff !important;
        box-shadow: 0 3px 12px 0 rgba(105, 108, 255, 0.55) !important;
    }}

    button[data-baseweb="tab"][aria-selected="true"] * {{
        color: #ffffff !important;
    }}

    /* =========================================================================
       VUETIFY CHIPS & MULTISELECT (DARK V-CHIP)
       ========================================================================= */
    div[data-baseweb="tag"] {{
        background-color: rgba(105, 108, 255, 0.2) !important;
        color: #787bff !important;
        border: 1px solid rgba(105, 108, 255, 0.45) !important;
        border-radius: 4px !important;
        padding: 2px 8px !important;
    }}

    div[data-baseweb="tag"] span,
    div[data-baseweb="tag"] div,
    div[data-baseweb="tag"] [role="presentation"] {{
        color: #787bff !important;
        fill: #787bff !important;
        font-weight: 600 !important;
    }}

    div[data-baseweb="select"] {{
        background-color: #2b2c40 !important;
        border: 1px solid #44476a !important;
        border-radius: 0.375rem !important;
        box-shadow: 0 2px 6px rgba(12, 12, 20, 0.25) !important;
    }}

    div[data-baseweb="select"]:hover {{
        border-color: #696cff !important;
    }}

    div[data-baseweb="select"] * {{
        color: #e1def5 !important;
    }}

    ul[role="listbox"], div[role="listbox"] {{
        background-color: #2b2c40 !important;
        border: 1px solid #44476a !important;
    }}

    ul[role="listbox"] li, div[role="option"] {{
        color: #e1def5 !important;
        background-color: #2b2c40 !important;
        font-weight: 500 !important;
    }}

    ul[role="listbox"] li:hover, div[role="option"]:hover {{
        background-color: rgba(105, 108, 255, 0.22) !important;
        color: #787bff !important;
    }}

    /* =========================================================================
       FORM INPUTS (DARK V-TEXT-FIELD)
       ========================================================================= */
    input[type="text"], input[type="number"],
    .stTextInput input, .stNumberInput input {{
        color: #e1def5 !important;
        background-color: #232333 !important;
        border: 1px solid #44476a !important;
        border-radius: 0.375rem !important;
        font-weight: 500 !important;
        font-size: 0.9375rem !important;
        padding: 0.45rem 0.85rem !important;
        box-shadow: 0 1px 3px rgba(12, 12, 20, 0.3) !important;
    }}

    input[type="text"]:focus, input[type="number"]:focus {{
        border-color: #696cff !important;
        box-shadow: 0 0 0 3px rgba(105, 108, 255, 0.25) !important;
    }}

    /* =========================================================================
       BUTTONS (VUETIFY V-BTN DARK MODE)
       ========================================================================= */
    .stButton > button {{
        border-radius: 0.375rem !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        padding: 0.45rem 1.25rem !important;
        transition: all 0.2s ease-in-out !important;
    }}

    .stButton > button[kind="primary"] {{
        background-color: #696cff !important;
        color: #ffffff !important;
        border: none !important;
        box-shadow: 0 3px 12px 0 rgba(105, 108, 255, 0.45) !important;
    }}

    .stButton > button[kind="primary"] p,
    .stButton > button[kind="primary"] span {{
        color: #ffffff !important;
    }}

    .stButton > button[kind="primary"]:hover {{
        background-color: #787bff !important;
        box-shadow: 0 4px 16px 0 rgba(105, 108, 255, 0.6) !important;
        transform: translateY(-1px);
    }}

    .stButton > button[kind="secondary"],
    .stButton > button:not([kind="primary"]) {{
        background-color: #3b3e5b !important;
        color: #e1def5 !important;
        border: 1px solid #44476a !important;
        box-shadow: 0 2px 6px 0 rgba(12, 12, 20, 0.25) !important;
    }}

    .stButton > button[kind="secondary"] p,
    .stButton > button:not([kind="primary"]) p,
    .stButton > button:not([kind="primary"]) span {{
        color: #e1def5 !important;
    }}

    .stButton > button[kind="secondary"]:hover,
    .stButton > button:not([kind="primary"]):hover {{
        background-color: rgba(105, 108, 255, 0.25) !important;
        border-color: #696cff !important;
        color: #787bff !important;
    }}

    /* Download Button */
    .stDownloadButton > button {{
        background-color: #3b3e5b !important;
        color: #787bff !important;
        border: 1px solid #44476a !important;
        border-radius: 0.375rem !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 6px 0 rgba(12, 12, 20, 0.25) !important;
    }}

    .stDownloadButton > button p,
    .stDownloadButton > button span {{
        color: #787bff !important;
    }}

    .stDownloadButton > button:hover {{
        background-color: rgba(105, 108, 255, 0.25) !important;
        border-color: #696cff !important;
    }}

    /* =========================================================================
       DATAFRAME & TABLES (DARK VUETIFY V-DATA-TABLE)
       ========================================================================= */
    [data-testid="stDataFrame"] {{
        background-color: #2b2c40 !important;
        border: 1px solid #44476a !important;
        border-radius: 0.5rem !important;
        box-shadow: 0 4px 18px 0 rgba(12, 12, 20, 0.42) !important;
        overflow: hidden;
    }}

    [data-testid="stDataFrame"] * {{
        color: #e1def5 !important;
    }}

    /* Alerts (Vuetify Dark V-Alert) */
    [data-testid="stAlert"] {{
        border-radius: 0.5rem !important;
        border: 1px solid #44476a !important;
        background-color: #2b2c40 !important;
        box-shadow: 0 4px 18px 0 rgba(12, 12, 20, 0.3) !important;
        padding: 0.75rem 1rem !important;
    }}

    [data-testid="stAlert"] p,
    [data-testid="stAlert"] span,
    [data-testid="stAlert"] div {{
        color: #e1def5 !important;
        font-weight: 500 !important;
    }}

    /* =========================================================================
       SNEAT CARDS, HERO BANNER & AVATAR BOXES (DARK V-CARD)
       ========================================================= */
    .sneat-hero-card {{
        background: #2b2c40;
        border-radius: 0.5rem;
        padding: 1.5rem 1.75rem;
        box-shadow: 0 4px 18px 0 rgba(12, 12, 20, 0.42);
        border: 1px solid #44476a;
        margin-bottom: 1.5rem;
        position: relative;
        overflow: hidden;
    }}

    .sneat-hero-card::after {{
        content: "";
        position: absolute;
        top: 0;
        right: 0;
        width: 250px;
        height: 100%;
        background: radial-gradient(circle at top right, rgba(105, 108, 255, 0.22), transparent 70%);
        pointer-events: none;
    }}

    .sneat-hero-title {{
        font-size: 1.65rem;
        font-weight: 700;
        color: #e1def5 !important;
        margin: 0;
        letter-spacing: -0.02em;
    }}

    .sneat-hero-subtitle {{
        font-size: 0.9375rem;
        color: #b2b3ca !important;
        margin: 0 0 1rem 0;
        line-height: 1.55;
    }}

    /* Sneat Colored Badges (Dark Mode Soft Pills) */
    .badge-container {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        align-items: center;
    }}

    .badge-sneat {{
        display: inline-flex;
        align-items: center;
        padding: 0.25rem 0.65rem;
        border-radius: 0.25rem;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.02em;
    }}

    .bg-label-primary   {{ background-color: rgba(105, 108, 255, 0.16) !important; color: #787bff !important; }}
    .bg-label-success   {{ background-color: rgba(113, 221, 55, 0.16) !important; color: #71dd37 !important; }}
    .bg-label-info      {{ background-color: rgba(3, 195, 236, 0.16) !important; color: #03c3ec !important; }}
    .bg-label-warning   {{ background-color: rgba(255, 171, 0, 0.16) !important; color: #ffab00 !important; }}
    .bg-label-danger    {{ background-color: rgba(255, 62, 29, 0.16) !important; color: #ff3e1d !important; }}
    .bg-label-secondary {{ background-color: rgba(133, 146, 163, 0.16) !important; color: #a5afbb !important; }}

    /* Sneat Metric Cards (V-Card Stat Dark) */
    .sneat-card {{
        background: #2b2c40;
        border-radius: 0.5rem;
        padding: 1.25rem;
        box-shadow: 0 4px 18px 0 rgba(12, 12, 20, 0.42);
        border: 1px solid #44476a;
        margin-bottom: 0.75rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}

    .sneat-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 24px 0 rgba(12, 12, 20, 0.55);
        border-color: #696cff;
    }}

    .sneat-avatar-box {{
        width: 38px;
        height: 38px;
        border-radius: 0.375rem;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
    }}

    .sneat-card-label {{
        font-size: 0.8125rem;
        font-weight: 600;
        color: #8688a2 !important;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-top: 0.5rem;
        margin-bottom: 0.2rem;
    }}

    .sneat-card-value {{
        font-size: 1.65rem;
        font-weight: 700;
        color: #e1def5 !important;
        line-height: 1.15;
    }}

    .sneat-card-sub {{
        font-size: 0.8125rem;
        color: #8688a2 !important;
        margin-top: 0.35rem;
    }}

    /* Sneat Dark Alert / Formula Card (V-Alert) */
    .sneat-alert-card {{
        background: #2b2c40;
        border: 1px solid #44476a;
        border-left: 4px solid #696cff;
        border-radius: 0.5rem;
        padding: 1.15rem 1.35rem;
        margin: 1rem 0;
        box-shadow: 0 4px 18px 0 rgba(12, 12, 20, 0.3);
    }}

    .sneat-alert-title {{
        font-size: 1rem;
        font-weight: 700;
        color: #787bff !important;
        margin-bottom: 0.45rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }}

    .sneat-alert-body {{
        font-size: 0.9375rem;
        line-height: 1.6;
        color: #b2b3ca !important;
    }}

    .sneat-alert-body strong {{
        color: #e1def5 !important;
    }}

    /* Anatomical Guide Card (Dark) */
    .sneat-anatomy-card {{
        background: #2b2c40;
        border: 1px solid #44476a;
        border-radius: 0.5rem;
        padding: 1.25rem;
        box-shadow: 0 4px 18px 0 rgba(12, 12, 20, 0.3);
        margin-bottom: 1rem;
        font-size: 0.9375rem;
        line-height: 1.55;
        color: #b2b3ca !important;
    }}

    .sneat-anatomy-card strong {{
        color: #e1def5 !important;
    }}

    /* Prediction Result Banner (Dark) */
    .sneat-prediction-card {{
        background: #2b2c40;
        border-radius: 0.5rem;
        border: 2px solid #696cff;
        box-shadow: 0 6px 24px 0 rgba(105, 108, 255, 0.28);
        padding: 1.5rem;
        text-align: center;
        margin-bottom: 1rem;
    }}

    .sneat-prediction-title {{
        font-size: 0.8125rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #787bff !important;
        margin-bottom: 0.4rem;
    }}

    .sneat-prediction-species {{
        font-size: 2.2rem;
        font-weight: 800;
        color: #e1def5 !important;
        letter-spacing: -0.02em;
        margin: 0.25rem 0;
    }}

    /* Easter egg clean banner (Dark) */
    .sneat-banner {{
        background: #2b2c40;
        border: 1px solid #44476a;
        border-left: 4px solid #696cff;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: 0 4px 18px 0 rgba(12, 12, 20, 0.3);
        margin-bottom: 1.25rem;
    }}

    /* Compatibility aliases */
    .formula-card {{
        background: #2b2c40 !important;
        border: 1px solid #44476a !important;
        border-left: 4px solid #696cff !important;
        border-radius: 0.5rem !important;
        padding: 1.15rem 1.35rem !important;
        margin: 1rem 0 !important;
        color: #b2b3ca !important;
        box-shadow: 0 4px 18px 0 rgba(12, 12, 20, 0.3) !important;
    }}
    .formula-title {{
        color: #787bff !important;
        font-weight: 700 !important;
    }}
    .anatomy-card {{
        background: #2b2c40 !important;
        border: 1px solid #44476a !important;
        border-radius: 0.5rem !important;
        padding: 1.25rem !important;
        color: #b2b3ca !important;
        box-shadow: 0 4px 18px 0 rgba(12, 12, 20, 0.3) !important;
    }}
    .anatomy-card strong {{
        color: #e1def5 !important;
    }}
    .prediction-card {{
        background: #2b2c40 !important;
        border-radius: 0.5rem !important;
        border: 2px solid #696cff !important;
        box-shadow: 0 6px 24px 0 rgba(105, 108, 255, 0.28) !important;
        padding: 1.5rem !important;
        text-align: center !important;
    }}
    .prediction-title {{
        color: #787bff !important;
        font-weight: 700 !important;
    }}
    .prediction-species {{
        color: #e1def5 !important;
    }}
    .antigravity-banner {{
        background: #2b2c40 !important;
        border: 1px solid #44476a !important;
        border-left: 4px solid #696cff !important;
        padding: 1rem 1.25rem !important;
        border-radius: 0.5rem !important;
    }}

    {antigravity_animation}
    </style>
    """


def render_hero_banner() -> str:
    """Renders Sneat – Vuetify Vuejs 3 Admin Welcome Banner with 100% visible base64 logo image."""
    logo = get_iris_logo_img(46)
    return f"""<div class="sneat-hero-card">
    <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 0.75rem;">
        {logo}
        <div>
            <div class="badge-sneat bg-label-primary" style="margin-bottom: 4px;">Sneat • Vuetify Vuejs 3 Dark Suite</div>
            <h2 class="sneat-hero-title">Iris Flower Data Analysis</h2>
        </div>
    </div>
    <p class="sneat-hero-subtitle">
        Interactive multidimensional data science, real-time flower morphometry scaling, and linear algebra statistical modeling.
    </p>
    <div class="badge-container">
        <span class="badge-sneat bg-label-primary">🌙 Vuetify 3 Dark Theme</span>
        <span class="badge-sneat bg-label-info">🌸 150 Botanical Specimens</span>
        <span class="badge-sneat bg-label-success">🌱 3 Species Classes</span>
        <span class="badge-sneat bg-label-warning">📐 Live Flower Morphometry</span>
    </div>
</div>"""


def render_sidebar_header() -> str:
    """Renders Sneat App Brand Header with 100% visible base64 logo image."""
    logo = get_iris_logo_img(38)
    return f"""<div style="display: flex; align-items: center; gap: 12px; padding: 0.4rem 0 1rem 0; border-bottom: 1px solid #44476a; margin-bottom: 1rem;">
    {logo}
    <div>
        <div style="font-weight: 700; font-size: 1.25rem; color: #e1def5; line-height: 1.1; letter-spacing: -0.03em;">sneat</div>
        <div style="font-size: 0.72rem; color: #787bff; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;">IRIS ANALYTICS</div>
    </div>
</div>"""


def render_easter_egg_card() -> str:
    """Renders Sneat Easter Egg homage card."""
    return """<div class="sneat-banner">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
        <div>
            <strong style="color: #e1def5; font-size: 0.95rem;">🚀 Python Easter Egg: <code>import antigravity</code></strong>
            <p style="margin: 4px 0 0 0; font-size: 0.86rem; color: #b2b3ca;">
                Homage to XKCD #353: <em>"I wrote 20 short programs in Python yesterday. It was wonderful. Now I am flying!"</em>
            </p>
        </div>
        <div>
            <a href="https://xkcd.com/353/" target="_blank" 
               style="background: #696cff; color: #ffffff; padding: 0.45rem 0.9rem; border-radius: 0.375rem; text-decoration: none; font-size: 0.82rem; font-weight: 600; display: inline-block; box-shadow: 0 2px 8px rgba(105, 108, 255, 0.5);">
                View XKCD #353 ↗
            </a>
        </div>
    </div>
</div>"""
