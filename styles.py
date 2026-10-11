"""
styles.py
Mono Bootstrap Theme & Botanical Branding for the Iris Flower Data Analysis Suite.
Clean, ultra-high-contrast, monochromatic typography with structured Bootstrap component styling.
Guarantees 100% readability across all headings, body text, widgets, sliders, tags, tabs, and tables.
"""

def get_custom_css(antigravity_mode: bool = False) -> str:
    """Returns Mono Bootstrap CSS styles with crisp borders, dark text, and clean typography."""
    
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
       MONO BOOTSTRAP DESIGN SYSTEM & HIGH-CONTRAST TYPOGRAPHY
       ========================================================================= */
    :root {{
        --mono-dark: #0f172a;
        --mono-body: #1e293b;
        --mono-muted: #475569;
        --mono-light-bg: #f8fafc;
        --mono-card-border: #e2e8f0;
        --mono-border-strong: #cbd5e1;
    }}

    /* Global App Container & Base Font */
    html, body, .stApp {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
        color: #0f172a !important;
        background-color: #ffffff !important;
    }}

    .stApp [data-testid="stHeader"] {{
        background-color: rgba(255, 255, 255, 0.95) !important;
    }}

    .block-container {{
        padding-top: 1.25rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 100% !important;
    }}

    /* =========================================================================
       HEADINGS & PARAGRAPHS (100% VISIBLE & HIGH-CONTRAST)
       ========================================================================= */
    h1, h2, h3, h4, h5, h6,
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {{
        color: #0f172a !important;
        font-weight: 700 !important;
        letter-spacing: -0.015em !important;
    }}

    p, li, .stMarkdown p, .stMarkdown li, [data-testid="stMarkdownContainer"] p {{
        color: #1e293b !important;
        font-size: 0.95rem;
        line-height: 1.6;
    }}

    strong, b, .stMarkdown strong, .stMarkdown b {{
        color: #0f172a !important;
        font-weight: 700 !important;
    }}

    .stCaption, [data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] p {{
        color: #475569 !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
    }}

    /* =========================================================================
       SIDEBAR CONTROLS & LABELS
       ========================================================================= */
    section[data-testid="stSidebar"] {{
        background-color: #f8fafc !important;
        border-right: 1px solid #e2e8f0 !important;
    }}

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {{
        color: #0f172a !important;
    }}

    section[data-testid="stSidebar"] .stCaption,
    section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {{
        color: #475569 !important;
    }}

    /* Widget Labels (Sliders, Selectors, Inputs) */
    [data-testid="stWidgetLabel"],
    [data-testid="stWidgetLabel"] label,
    [data-testid="stWidgetLabel"] p,
    [data-testid="stWidgetLabel"] span {{
        color: #0f172a !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
    }}

    /* Sliders: Values, Min, Max & Numbers */
    div[data-testid="stThumbValue"],
    div[data-testid="stThumbValue"] * {{
        color: #0f172a !important;
        font-weight: 700 !important;
        font-size: 0.88rem !important;
    }}

    div[data-testid="stTickBarMin"],
    div[data-testid="stTickBarMax"],
    [data-testid="stSliderTickBar"] * {{
        color: #475569 !important;
        font-weight: 600 !important;
        font-size: 0.82rem !important;
    }}

    /* =========================================================================
       TABS NAVIGATION (MONO BOOTSTRAP)
       ========================================================================= */
    div[data-baseweb="tab-list"] {{
        border-bottom: 2px solid #e2e8f0 !important;
        gap: 0.5rem !important;
        background: transparent !important;
        margin-bottom: 1rem !important;
    }}

    button[data-baseweb="tab"] {{
        color: #475569 !important;
        font-weight: 600 !important;
        font-size: 0.92rem !important;
        padding: 0.65rem 1.1rem !important;
        border-radius: 0.375rem 0.375rem 0 0 !important;
        border: 1px solid transparent !important;
        background: transparent !important;
        transition: all 0.15s ease-in-out !important;
    }}

    button[data-baseweb="tab"] p,
    button[data-baseweb="tab"] div,
    button[data-baseweb="tab"] span {{
        color: inherit !important;
        font-weight: inherit !important;
    }}

    button[data-baseweb="tab"]:hover {{
        color: #0f172a !important;
        background-color: #f1f5f9 !important;
    }}

    button[data-baseweb="tab"][aria-selected="true"] {{
        color: #0f172a !important;
        font-weight: 700 !important;
        background-color: #ffffff !important;
        border-color: #cbd5e1 #cbd5e1 #ffffff !important;
        border-bottom: 3px solid #0f172a !important;
    }}

    /* =========================================================================
       MULTISELECT TAGS & DROPDOWNS
       ========================================================================= */
    div[data-baseweb="tag"] {{
        background-color: #0f172a !important;
        color: #ffffff !important;
        border: 1px solid #0f172a !important;
        border-radius: 4px !important;
        padding: 2px 8px !important;
    }}

    div[data-baseweb="tag"] span,
    div[data-baseweb="tag"] div,
    div[data-baseweb="tag"] [role="presentation"] {{
        color: #ffffff !important;
        fill: #ffffff !important;
        font-weight: 600 !important;
    }}

    div[data-baseweb="select"] {{
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 4px !important;
    }}

    div[data-baseweb="select"] * {{
        color: #0f172a !important;
    }}

    ul[role="listbox"] li, div[role="option"] {{
        color: #0f172a !important;
        background-color: #ffffff !important;
        font-weight: 500 !important;
    }}

    ul[role="listbox"] li:hover, div[role="option"]:hover {{
        background-color: #f1f5f9 !important;
    }}

    /* =========================================================================
       FORM INPUTS (TEXT & NUMBER)
       ========================================================================= */
    input[type="text"], input[type="number"],
    .stTextInput input, .stNumberInput input {{
        color: #0f172a !important;
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 4px !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
    }}

    input[type="text"]:focus, input[type="number"]:focus {{
        border-color: #0f172a !important;
        box-shadow: 0 0 0 1px #0f172a !important;
    }}

    /* =========================================================================
       BUTTONS (HIGH-CONTRAST & CRISP)
       ========================================================================= */
    .stButton > button {{
        border-radius: 0.375rem !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
        transition: all 0.15s ease-in-out !important;
    }}

    .stButton > button[kind="primary"] {{
        background-color: #0f172a !important;
        color: #ffffff !important;
        border: 1px solid #0f172a !important;
    }}

    .stButton > button[kind="primary"] p,
    .stButton > button[kind="primary"] span {{
        color: #ffffff !important;
    }}

    .stButton > button[kind="primary"]:hover {{
        background-color: #1e293b !important;
        border-color: #1e293b !important;
    }}

    .stButton > button[kind="secondary"],
    .stButton > button:not([kind="primary"]) {{
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
    }}

    .stButton > button[kind="secondary"] p,
    .stButton > button:not([kind="primary"]) p,
    .stButton > button:not([kind="primary"]) span {{
        color: #0f172a !important;
    }}

    .stButton > button[kind="secondary"]:hover,
    .stButton > button:not([kind="primary"]):hover {{
        background-color: #f8fafc !important;
        border-color: #94a3b8 !important;
        color: #0f172a !important;
    }}

    /* Download Button */
    .stDownloadButton > button {{
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 0.375rem !important;
        font-weight: 600 !important;
    }}

    .stDownloadButton > button p,
    .stDownloadButton > button span {{
        color: #0f172a !important;
    }}

    .stDownloadButton > button:hover {{
        background-color: #f1f5f9 !important;
        border-color: #94a3b8 !important;
    }}

    /* =========================================================================
       DATAFRAME & TABLES
       ========================================================================= */
    [data-testid="stDataFrame"] {{
        border: 1px solid #e2e8f0 !important;
        border-radius: 0.375rem !important;
    }}

    [data-testid="stDataFrame"] * {{
        color: #0f172a !important;
    }}

    /* Alerts */
    [data-testid="stAlert"] {{
        border-radius: 0.375rem !important;
        border: 1px solid #cbd5e1 !important;
        padding: 0.75rem 1rem !important;
    }}

    [data-testid="stAlert"] p,
    [data-testid="stAlert"] span,
    [data-testid="stAlert"] div {{
        color: #0f172a !important;
        font-weight: 500 !important;
    }}

    /* =========================================================================
       BOOTSTRAP HERO BANNER & CARDS
       ========================================================================= */
    .hero-banner {{
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 0.5rem;
        padding: 1.5rem 1.75rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04);
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1.5rem;
        flex-wrap: wrap;
    }}

    .hero-content {{
        flex: 1;
        min-width: 280px;
    }}

    .hero-title-row {{
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.4rem;
    }}

    .hero-title {{
        font-size: 1.75rem;
        font-weight: 800;
        color: #0f172a !important;
        margin: 0;
        letter-spacing: -0.02em;
        line-height: 1.2;
    }}

    .hero-subtitle {{
        font-size: 0.95rem;
        color: #334155 !important;
        margin: 0 0 0.85rem 0;
        line-height: 1.5;
    }}

    /* Mono Bootstrap Badges */
    .badge-container {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem;
        align-items: center;
    }}

    .badge-mono {{
        display: inline-flex;
        align-items: center;
        padding: 0.25rem 0.65rem;
        border-radius: 0.25rem;
        font-size: 0.78rem;
        font-weight: 600;
        background: #f1f5f9;
        color: #1e293b !important;
        border: 1px solid #cbd5e1;
        letter-spacing: 0.01em;
    }}

    .badge-mono-dark {{
        background: #0f172a !important;
        color: #ffffff !important;
        border: 1px solid #0f172a !important;
    }}

    .badge-mono-blue {{
        background: #eff6ff;
        color: #1d4ed8 !important;
        border: 1px solid #bfdbfe;
    }}

    /* Stat & Metric Cards */
    .stat-card {{
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 0.375rem;
        padding: 1rem 1.15rem;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        margin-bottom: 0.75rem;
        transition: border-color 0.15s ease-in-out;
    }}

    .stat-card:hover {{
        border-color: #94a3b8;
    }}

    .stat-label {{
        font-size: 0.75rem;
        font-weight: 700;
        color: #475569 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.25rem;
    }}

    .stat-value {{
        font-size: 1.7rem;
        font-weight: 800;
        color: #0f172a !important;
        line-height: 1.1;
    }}

    .stat-sub {{
        font-size: 0.82rem;
        color: #475569 !important;
        margin-top: 0.35rem;
        font-weight: 500;
    }}

    /* Formula & Plain English Explanation Box */
    .formula-card {{
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #0f172a;
        border-radius: 0.25rem;
        padding: 1.1rem 1.35rem;
        margin: 1rem 0;
        font-size: 0.93rem;
        line-height: 1.6;
        color: #1e293b !important;
    }}

    .formula-card strong {{
        color: #0f172a !important;
    }}

    .formula-title {{
        font-size: 1rem;
        font-weight: 700;
        color: #0f172a !important;
        margin-bottom: 0.45rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }}

    /* Anatomical Diagram Guides */
    .anatomy-card {{
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 0.375rem;
        padding: 1.15rem;
        margin-bottom: 1rem;
        color: #1e293b !important;
        font-size: 0.92rem;
        line-height: 1.55;
    }}

    .anatomy-card strong {{
        color: #0f172a !important;
    }}

    /* Prediction Result Banner */
    .prediction-card {{
        background: #f8fafc;
        border: 2px solid #0f172a;
        border-radius: 0.5rem;
        padding: 1.5rem;
        text-align: center;
        margin-bottom: 1rem;
    }}

    .prediction-title {{
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        font-weight: 700;
        color: #475569 !important;
        margin-bottom: 0.5rem;
    }}

    .prediction-species {{
        font-size: 2rem;
        font-weight: 800;
        color: #0f172a !important;
        letter-spacing: -0.02em;
        margin: 0.25rem 0;
    }}

    /* Easter egg clean banner */
    .antigravity-banner {{
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-left: 4px solid #475569;
        padding: 1rem 1.25rem;
        border-radius: 0.375rem;
        margin-bottom: 1.25rem;
    }}

    {antigravity_animation}
    </style>
    """


def get_iris_logo_svg(size: int = 40) -> str:
    """Returns a sleek, modern botanical SVG logo for Iris Flower Data Analysis."""
    return f"""
    <svg width="{size}" height="{size}" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="46" fill="#0f172a" stroke="#334155" stroke-width="2"/>
        <!-- Stylized Flower Petals & Data Grid -->
        <path d="M50 16 C45 32 36 44 26 50 C38 52 46 62 50 82 C54 62 62 52 74 50 C64 44 55 32 50 16 Z" 
              fill="#ffffff" fill-opacity="0.95"/>
        <!-- Inner Petal Core -->
        <path d="M50 30 C48 40 43 47 38 50 C44 52 48 57 50 70 C52 57 56 52 62 50 C57 47 52 40 50 30 Z" 
              fill="#94a3b8"/>
        <!-- Botanical Stamen & Node -->
        <circle cx="50" cy="50" r="5" fill="#38bdf8"/>
        <line x1="50" y1="50" x2="50" y2="82" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
        <line x1="26" y1="50" x2="74" y2="50" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2 2"/>
    </svg>
    """


def render_hero_banner():
    """Renders the top branding banner with the Iris logo and Mono Bootstrap styling."""
    logo = get_iris_logo_svg(46)
    return f"""
    <div class="hero-banner">
        <div class="hero-content">
            <div class="hero-title-row">
                {logo}
                <div>
                    <h1 class="hero-title">Iris Flower Data Analysis</h1>
                </div>
            </div>
            <p class="hero-subtitle">
                Interactive multidimensional exploration, live morphometric flower visualization, 
                and linear algebra statistical modeling based on the famous Fisher Iris dataset.
            </p>
            <div class="badge-container">
                <span class="badge-mono badge-mono-dark">Mono Bootstrap Theme</span>
                <span class="badge-mono">150 Botanical Specimens</span>
                <span class="badge-mono">3 Species (Setosa • Versicolor • Virginica)</span>
                <span class="badge-mono badge-mono-blue">Real-Time Flower Morphometry</span>
            </div>
        </div>
    </div>
    """


def render_sidebar_header():
    """Renders clean sidebar brand identity."""
    logo = get_iris_logo_svg(34)
    return f"""
    <div style="display: flex; align-items: center; gap: 10px; padding: 0.5rem 0 1rem 0; border-bottom: 1px solid #e2e8f0; margin-bottom: 1rem;">
        {logo}
        <div>
            <div style="font-weight: 700; font-size: 1.05rem; color: #0f172a; line-height: 1.2;">Iris Flower</div>
            <div style="font-size: 0.78rem; color: #64748b; font-weight: 500;">Data Analysis Suite</div>
        </div>
    </div>
    """


def render_easter_egg_card():
    """Renders clean Easter Egg homage card."""
    return """
    <div class="antigravity-banner">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
            <div>
                <strong style="color: #0f172a; font-size: 0.95rem;">🚀 Python Easter Egg: <code>import antigravity</code></strong>
                <p style="margin: 4px 0 0 0; font-size: 0.86rem; color: #475569;">
                    Homage to XKCD #353: <em>"I wrote 20 short programs in Python yesterday. It was wonderful. Now I am flying!"</em>
                </p>
            </div>
            <div>
                <a href="https://xkcd.com/353/" target="_blank" 
                   style="background: #0f172a; color: #ffffff; padding: 0.45rem 0.9rem; border-radius: 0.25rem; text-decoration: none; font-size: 0.82rem; font-weight: 600; display: inline-block;">
                    View XKCD #353 ↗
                </a>
            </div>
        </div>
    </div>
    """
