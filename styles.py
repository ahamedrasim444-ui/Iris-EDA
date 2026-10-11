"""
styles.py
Mono Bootstrap Theme & Botanical Branding for the Iris Flower Data Analysis Suite.
Clean, high-contrast, monochromatic typography with structured Bootstrap component styling.
"""

def get_custom_css(antigravity_mode: bool = False) -> str:
    """Returns Mono Bootstrap CSS styles with crisp borders and clean typography."""
    
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
       MONO BOOTSTRAP DESIGN SYSTEM
       ========================================================================= */
    html, body, [class*="css"] {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
        color: #0f172a !important;
        background-color: #ffffff;
    }}

    /* Global layout padding */
    .block-container {{
        padding-top: 1.25rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 100% !important;
    }}

    /* Mono Bootstrap Card */
    .mono-card {{
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 0.375rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
        margin-bottom: 1.25rem;
        overflow: hidden;
    }}

    .mono-card-header {{
        background-color: #f8fafc;
        border-bottom: 1px solid #e2e8f0;
        padding: 0.75rem 1.25rem;
        font-size: 0.95rem;
        font-weight: 600;
        color: #0f172a;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}

    .mono-card-body {{
        padding: 1.25rem;
    }}

    /* Hero Banner: Clean Monochromatic Header */
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
        font-weight: 700;
        color: #0f172a !important;
        margin: 0;
        letter-spacing: -0.02em;
        line-height: 1.2;
    }}

    .hero-subtitle {{
        font-size: 0.95rem;
        color: #475569 !important;
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
        color: #1e293b;
        border: 1px solid #cbd5e1;
        letter-spacing: 0.01em;
    }}

    .badge-mono-dark {{
        background: #0f172a;
        color: #ffffff;
        border: 1px solid #0f172a;
    }}

    .badge-mono-blue {{
        background: #eff6ff;
        color: #1d4ed8;
        border: 1px solid #bfdbfe;
    }}

    /* Stat & Metric Cards (Bootstrap Mono) */
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
        font-weight: 600;
        color: #64748b !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.25rem;
    }}

    .stat-value {{
        font-size: 1.7rem;
        font-weight: 700;
        color: #0f172a !important;
        line-height: 1.1;
    }}

    .stat-sub {{
        font-size: 0.8rem;
        color: #64748b;
        margin-top: 0.35rem;
    }}

    /* Formula & Plain English Explanation Box */
    .formula-card {{
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #0f172a;
        border-radius: 0.25rem;
        padding: 1rem 1.25rem;
        margin: 1rem 0;
        font-size: 0.92rem;
        line-height: 1.6;
        color: #1e293b;
    }}

    .formula-title {{
        font-size: 0.95rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.35rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }}

    /* Anatomical Diagram Guides */
    .anatomy-card {{
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 0.375rem;
        padding: 1.1rem;
        margin-bottom: 1rem;
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
        font-weight: 600;
        color: #64748b;
        margin-bottom: 0.5rem;
    }}

    .prediction-species {{
        font-size: 2rem;
        font-weight: 800;
        color: #0f172a;
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

    /* High contrast text */
    h1, h2, h3, h4, p, span, label, div {{
        color: inherit;
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

