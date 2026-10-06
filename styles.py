"""
styles.py
Custom styling, CSS theme injection, responsive layout, metric cards, and Easter Egg UI enhancements
for the Iris EDA Streamlit Dashboard CSE Mini-Project.
"""

def get_custom_css(antigravity_mode: bool = False) -> str:
    """Returns custom responsive CSS styles for Streamlit."""
    
    antigravity_animation = ""
    if antigravity_mode:
        antigravity_animation = """
        @keyframes antigravityFloat {
            0% { transform: translateY(0px) rotate(0deg); }
            25% { transform: translateY(-8px) rotate(-1deg); }
            50% { transform: translateY(-16px) rotate(1.5deg); }
            75% { transform: translateY(-6px) rotate(-0.5deg); }
            100% { transform: translateY(0px) rotate(0deg); }
        }
        .main .block-container {
            animation: antigravityFloat 6s ease-in-out infinite;
        }
        .antigravity-banner {
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #db2777 100%);
            color: #ffffff !important;
            padding: 1.25rem 1.75rem;
            border-radius: 14px;
            margin-bottom: 1.5rem;
            box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.2);
            animation: antigravityFloat 4s ease-in-out infinite;
        }
        """

    return f"""
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    code, pre, .stCode {{
        font-family: 'JetBrains Mono', monospace !important;
    }}

    /* Global layout responsiveness */
    .block-container {{
        padding-top: 1.5rem;
        padding-bottom: 3.5rem;
        padding-left: clamp(1rem, 3vw, 2.5rem) !important;
        padding-right: clamp(1rem, 3vw, 2.5rem) !important;
        max-width: 100% !important;
    }}

    /* Hero Banner with Responsive Typography */
    .hero-banner {{
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #312e81 100%);
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 16px;
        padding: clamp(1.2rem, 3vw, 2.25rem);
        margin-bottom: 1.5rem;
        color: #ffffff;
        box-shadow: 0 8px 30px rgba(15, 23, 42, 0.35);
        position: relative;
        overflow: hidden;
    }}

    .hero-banner::after {{
        content: "";
        position: absolute;
        top: -50%;
        right: -10%;
        width: 320px;
        height: 320px;
        background: radial-gradient(circle, rgba(129, 140, 248, 0.25) 0%, rgba(0,0,0,0) 70%);
        pointer-events: none;
    }}

    .hero-title {{
        font-size: clamp(1.4rem, 2.8vw, 2.2rem);
        font-weight: 800;
        letter-spacing: -0.025em;
        margin: 0 0 0.5rem 0;
        background: linear-gradient(90deg, #ffffff 0%, #e0e7ff 60%, #a5b4fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
    }}

    .hero-subtitle {{
        font-size: clamp(0.85rem, 1.4vw, 1.02rem);
        color: #cbd5e1;
        margin: 0 0 1rem 0;
        max-width: 880px;
        line-height: 1.5;
    }}

    .badge-container {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        align-items: center;
    }}

    .badge {{
        display: inline-flex;
        align-items: center;
        padding: 0.25rem 0.65rem;
        border-radius: 9999px;
        font-size: clamp(0.7rem, 1.1vw, 0.78rem);
        font-weight: 600;
        letter-spacing: 0.03em;
        text-transform: uppercase;
        white-space: nowrap;
    }}

    .badge-cse {{
        background-color: rgba(99, 102, 241, 0.2);
        color: #a5b4fc;
        border: 1px solid rgba(99, 102, 241, 0.4);
    }}

    .badge-tech {{
        background-color: rgba(16, 185, 129, 0.2);
        color: #6ee7b7;
        border: 1px solid rgba(16, 185, 129, 0.4);
    }}

    .badge-academic {{
        background-color: rgba(244, 63, 94, 0.2);
        color: #fda4af;
        border: 1px solid rgba(244, 63, 94, 0.4);
    }}

    /* Metric Cards Grid */
    .metric-card {{
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(226, 232, 240, 0.18);
        border-radius: 12px;
        padding: clamp(0.85rem, 1.8vw, 1.25rem);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 0.5rem;
    }}

    .metric-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.15);
        border-color: rgba(99, 102, 241, 0.4);
    }}

    .metric-label {{
        font-size: 0.76rem;
        font-weight: 600;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.35rem;
    }}

    .metric-value {{
        font-size: clamp(1.4rem, 2.4vw, 1.85rem);
        font-weight: 800;
        color: #0f172a;
        line-height: 1.1;
    }}

    @media (prefers-color-scheme: dark) {{
        .metric-value {{
            color: #f8fafc;
        }}
    }}

    .metric-desc {{
        font-size: 0.74rem;
        color: #64748b;
        margin-top: 0.35rem;
    }}

    /* Sidebar Custom Components */
    .sidebar-section-title {{
        font-size: 0.8rem;
        font-weight: 700;
        color: #6366f1;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }}

    .sidebar-card {{
        background: rgba(99, 102, 241, 0.06);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 10px;
        padding: 0.85rem;
        margin-bottom: 0.9rem;
    }}

    .team-member-item {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.38rem 0;
        border-bottom: 1px dashed rgba(148, 163, 184, 0.25);
        font-size: 0.83rem;
    }}

    .team-member-item:last-child {{
        border-bottom: none;
    }}

    .team-member-name {{
        font-weight: 600;
        color: #334155;
    }}

    @media (prefers-color-scheme: dark) {{
        .team-member-name {{
            color: #e2e8f0;
        }}
    }}

    .team-member-role {{
        font-size: 0.72rem;
        background: rgba(99, 102, 241, 0.15);
        color: #6366f1;
        padding: 0.15rem 0.5rem;
        border-radius: 6px;
        font-weight: 600;
    }}

    /* Math Box */
    .math-card {{
        background: rgba(15, 23, 42, 0.03);
        border-left: 4px solid #6366f1;
        border-radius: 0 10px 10px 0;
        padding: 1rem 1.25rem;
        margin: 1rem 0;
        overflow-x: auto;
    }}

    @media (prefers-color-scheme: dark) {{
        .math-card {{
            background: rgba(30, 41, 59, 0.4);
            border-left: 4px solid #818cf8;
        }}
    }}

    /* Prediction Card */
    .prediction-box {{
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(16, 185, 129, 0.1) 100%);
        border: 2px solid rgba(99, 102, 241, 0.35);
        border-radius: 14px;
        padding: clamp(1rem, 2vw, 1.5rem);
        text-align: center;
        margin-bottom: 1.25rem;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.08);
    }}

    .species-tag {{
        display: inline-block;
        padding: 0.4rem 1.4rem;
        border-radius: 9999px;
        font-size: clamp(1.2rem, 2.5vw, 1.6rem);
        font-weight: 800;
        margin: 0.5rem 0;
        letter-spacing: -0.01em;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }}

    .tag-setosa {{
        background: #e0e7ff;
        color: #4338ca;
        border: 2px solid #818cf8;
    }}

    .tag-versicolor {{
        background: #fce7f3;
        color: #be185d;
        border: 2px solid #f472b6;
    }}

    .tag-virginica {{
        background: #d1fae5;
        color: #047857;
        border: 2px solid #34d399;
    }}

    /* Custom Streamlit adjustments for mobile screens */
    div[data-testid="stMetricValue"] {{
        font-weight: 700;
        font-size: clamp(1.2rem, 2vw, 1.7rem) !important;
    }}

    @media (max-width: 768px) {{
        .hero-banner {{
            padding: 1.1rem 1rem;
            border-radius: 12px;
        }}
        .hero-title {{
            font-size: 1.35rem;
        }}
        .hero-subtitle {{
            font-size: 0.85rem;
        }}
        .badge {{
            font-size: 0.68rem;
            padding: 0.2rem 0.5rem;
        }}
        .species-tag {{
            font-size: 1.2rem;
            padding: 0.3rem 1rem;
        }}
        .stButton button {{
            padding: 0.35rem 0.6rem !important;
            font-size: 0.82rem !important;
        }}
    }}

    /* Easter egg animation */
    {antigravity_animation}
    </style>
    """


def render_hero_banner():
    """Renders the top title banner with metadata pills."""
    return """
    <div class="hero-banner">
        <div class="hero-title">Multidimensional Exploratory Data Analysis of the Iris Dataset</div>
        <div class="hero-subtitle">
            A comprehensive exploratory engineering suite performing multi-attribute statistical decompositions, 
            covariance & correlation tensor modeling via NumPy, dynamic data slicing via Pandas, and publication-ready 
            decision space visualizations with Matplotlib.
        </div>
        <div class="badge-container">
            <span class="badge badge-cse">CSE Mini-Project</span>
            <span class="badge badge-tech">NumPy 2.5 • Pandas 3.0 • Matplotlib 3.11</span>
            <span class="badge badge-academic">Fisher Iris Dataset (1936)</span>
            <span class="badge badge-cse">Department of Computer Science & Engineering</span>
        </div>
    </div>
    """


def render_easter_egg_card():
    """Renders the humorous Easter Egg card when Antigravity mode is toggled."""
    return """
    <div class="antigravity-banner">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
            <div>
                <h3 style="margin: 0 0 4px 0; color: #ffffff; font-size: 1.35rem;">
                    🚀 Python Easter Egg Activated: <code>import antigravity</code>
                </h3>
                <p style="margin: 0; font-size: 0.95rem; color: #f1f5f9; line-height: 1.4;">
                    <em>"I wrote 20 short programs in Python yesterday. It was wonderful. Perl, I'm breaking up with you."</em><br>
                    Homage to <strong>XKCD #353</strong> (Geocaching & Python Flight). You are now floating above the Iris hyperspace!
                </p>
            </div>
            <div>
                <a href="https://xkcd.com/353/" target="_blank" 
                   style="display: inline-block; background: #ffffff; color: #4f46e5; padding: 0.5rem 1rem; 
                          border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 0.85rem; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
                    View Comic #353 ↗
                </a>
            </div>
        </div>
    </div>
    """
