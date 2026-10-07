"""
styles.py
Clean, minimalist, high-contrast, professional styling for the Iris EDA Dashboard.
Focuses on neatness, maximum font visibility, and uncluttered presentation.
"""

def get_custom_css(antigravity_mode: bool = False) -> str:
    """Returns clean, high-contrast CSS styles."""
    
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
    /* Clean System Typography */
    html, body, [class*="css"] {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
        color: #0f172a !important;
    }}

    /* Global layout padding */
    .block-container {{
        padding-top: 1.5rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 100% !important;
    }}

    /* Neat, Minimalist Header Banner (Not overly colorful) */
    .hero-banner {{
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-left: 5px solid #2563eb;
        border-radius: 8px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }}

    .hero-title {{
        font-size: 1.65rem;
        font-weight: 700;
        color: #0f172a !important;
        margin: 0 0 0.35rem 0;
        line-height: 1.3;
    }}

    .hero-subtitle {{
        font-size: 0.95rem;
        color: #334155 !important;
        margin: 0 0 0.75rem 0;
        line-height: 1.5;
    }}

    /* Neat Badges */
    .badge-container {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem;
        align-items: center;
    }}

    .badge {{
        display: inline-flex;
        align-items: center;
        padding: 0.2rem 0.6rem;
        border-radius: 4px;
        font-size: 0.76rem;
        font-weight: 600;
        background: #e2e8f0;
        color: #1e293b;
        border: 1px solid #cbd5e1;
    }}

    /* Neat Metric Cards */
    .metric-card {{
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1rem 1.1rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        margin-bottom: 0.5rem;
    }}

    .metric-label {{
        font-size: 0.78rem;
        font-weight: 600;
        color: #64748b !important;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: 0.25rem;
    }}

    .metric-value {{
        font-size: 1.6rem;
        font-weight: 700;
        color: #0f172a !important;
        line-height: 1.1;
    }}

    /* Sidebar Clean Card */
    .sidebar-card {{
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 0.85rem;
        margin-bottom: 0.85rem;
    }}

    .team-member-item {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.35rem 0;
        border-bottom: 1px solid #e2e8f0;
        font-size: 0.83rem;
    }}

    .team-member-item:last-child {{
        border-bottom: none;
    }}

    .team-member-name {{
        font-weight: 600;
        color: #1e293b;
    }}

    .team-member-role {{
        font-size: 0.72rem;
        background: #e2e8f0;
        color: #334155;
        padding: 0.15rem 0.45rem;
        border-radius: 4px;
        font-weight: 500;
    }}

    /* Neat Plain-English Explanation Box */
    .explain-box {{
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #3b82f6;
        border-radius: 0 6px 6px 0;
        padding: 0.85rem 1.1rem;
        margin: 0.75rem 0;
        font-size: 0.92rem;
        line-height: 1.5;
        color: #1e293b;
    }}

    /* Prediction Result Banner (Neat & Visible) */
    .prediction-box {{
        background: #f8fafc;
        border: 2px solid #2563eb;
        border-radius: 8px;
        padding: 1.25rem;
        text-align: center;
        margin-bottom: 1rem;
    }}

    .species-tag {{
        display: inline-block;
        padding: 0.4rem 1.5rem;
        border-radius: 6px;
        font-size: 1.45rem;
        font-weight: 700;
        margin: 0.4rem 0;
    }}

    .tag-setosa {{
        background: #eff6ff;
        color: #1d4ed8;
        border: 1px solid #93c5fd;
    }}

    .tag-versicolor {{
        background: #fdf2f8;
        color: #be185d;
        border: 1px solid #fbcfe8;
    }}

    .tag-virginica {{
        background: #f0fdf4;
        color: #15803d;
        border: 1px solid #bbf7d0;
    }}

    /* Easter egg clean banner */
    .antigravity-banner {{
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-left: 4px solid #8b5cf6;
        padding: 1rem 1.25rem;
        border-radius: 6px;
        margin-bottom: 1rem;
    }}

    /* High contrast text overrides */
    h1, h2, h3, h4, p, span, label, div {{
        color: inherit;
    }}

    {antigravity_animation}
    </style>
    """


def render_hero_banner():
    """Renders neat top title banner with clear typography."""
    return """
    <div class="hero-banner">
        <div class="hero-title">Multidimensional Exploratory Analysis of the Iris Dataset</div>
        <div class="hero-subtitle">
            An interactive data science application demonstrating <strong>NumPy array mathematics</strong>, 
            <strong>Pandas data processing</strong>, and <strong>Matplotlib visual analytics</strong>.
        </div>
        <div class="badge-container">
            <span class="badge">CSE Mini-Project</span>
            <span class="badge">NumPy • Pandas • Matplotlib</span>
            <span class="badge">Fisher Iris (150 Samples)</span>
            <span class="badge">Connected to SQLite Database</span>
        </div>
    </div>
    """


def render_easter_egg_card():
    """Renders clean Easter Egg homage card."""
    return """
    <div class="antigravity-banner">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
            <div>
                <strong style="color: #4c1d95; font-size: 1rem;">🚀 Python Easter Egg: <code>import antigravity</code></strong>
                <p style="margin: 4px 0 0 0; font-size: 0.88rem; color: #334155;">
                    Homage to XKCD #353: <em>"I wrote 20 short programs in Python yesterday. It was wonderful. Now I am flying!"</em>
                </p>
            </div>
            <div>
                <a href="https://xkcd.com/353/" target="_blank" 
                   style="background: #2563eb; color: #ffffff; padding: 0.4rem 0.8rem; border-radius: 4px; text-decoration: none; font-size: 0.82rem; font-weight: 600;">
                    Open XKCD #353 Comic ↗
                </a>
            </div>
        </div>
    </div>
    """
