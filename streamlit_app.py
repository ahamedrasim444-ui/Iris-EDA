"""
streamlit_app.py
Iris Flower Data Analysis Suite
Interactive Multidimensional Data Science, Real-Time Flower Morphometry,
and Statistical Modeling with Mono Bootstrap Styling.
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import database
from data_engine import (
    FEATURE_COLS,
    FEATURE_LABELS,
    SPECIES_COLORS,
    load_dataset,
    filter_dataset,
    compute_descriptive_stats,
    compute_species_aggregations,
    compute_covariance_matrix_manual,
    compute_correlation_matrix_manual,
    compute_species_centroids,
    compute_eigen_decomposition,
    predict_nearest_centroid,
)
from visualizations import (
    plot_interactive_iris_flower,
    plot_covariance_heatmap,
    plot_correlation_heatmap,
    plot_bivariate_scatter,
    plot_boxplot_dispersion,
    plot_distributions_grid,
    plot_prediction_diagnostics,
    plot_query_point_projection,
)
from styles import (
    get_custom_css,
    render_hero_banner,
    render_sidebar_header,
    render_easter_egg_card,
)


# ------------------------------------------------------------------------------
# Page Configuration & Mono Bootstrap Theme
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Iris Flower Data Analysis | Morphometry & Statistics",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply Mono Bootstrap CSS
st.markdown(get_custom_css(antigravity_mode=st.session_state.get("antigravity_active", False)), unsafe_allow_html=True)

# Initialize SQLite Database
database.init_db()


# ------------------------------------------------------------------------------
# Session State & Preset Management
# ------------------------------------------------------------------------------
if "antigravity_active" not in st.session_state:
    st.session_state.antigravity_active = False

def set_flower_preset(sl: float, sw: float, pl: float, pw: float):
    st.session_state["flower_sl"] = float(sl)
    st.session_state["flower_sw"] = float(sw)
    st.session_state["flower_pl"] = float(pl)
    st.session_state["flower_pw"] = float(pw)

if "flower_sl" not in st.session_state:
    st.session_state["flower_sl"] = 5.8
if "flower_sw" not in st.session_state:
    st.session_state["flower_sw"] = 3.0
if "flower_pl" not in st.session_state:
    st.session_state["flower_pl"] = 4.2
if "flower_pw" not in st.session_state:
    st.session_state["flower_pw"] = 1.3


# ------------------------------------------------------------------------------
# Load Dataset (Cached)
# ------------------------------------------------------------------------------
@st.cache_data
def get_data():
    return load_dataset("data/iris.csv")

try:
    df_raw = get_data()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()


# ------------------------------------------------------------------------------
# Sidebar Controls & Global Slicing Filters
# ------------------------------------------------------------------------------
with st.sidebar:
    st.markdown(render_sidebar_header(), unsafe_allow_html=True)

    st.markdown("#### 🔍 Global Slicing Filters")
    st.caption("Filter botanical observations across all analytical tabs.")

    # Quick Reset Filters Button
    if st.button("🔄 Reset All Filters to Default", use_container_width=True):
        st.session_state["filter_species"] = sorted(df_raw["species"].unique().tolist())
        st.session_state["f_sl"] = (float(df_raw["sepal_length"].min()), float(df_raw["sepal_length"].max()))
        st.session_state["f_sw"] = (float(df_raw["sepal_width"].min()), float(df_raw["sepal_width"].max()))
        st.session_state["f_pl"] = (float(df_raw["petal_length"].min()), float(df_raw["petal_length"].max()))
        st.session_state["f_pw"] = (float(df_raw["petal_width"].min()), float(df_raw["petal_width"].max()))
        st.rerun()

    # Species Multi-select
    all_species = sorted(df_raw["species"].unique().tolist())
    if "filter_species" not in st.session_state:
        st.session_state["filter_species"] = all_species

    selected_species = st.multiselect(
        "Botanical Species:",
        options=all_species,
        default=st.session_state["filter_species"],
        help="Select one, two, or all three Iris classes to include.",
        key="filter_species",
    )

    if not selected_species:
        st.warning("⚠️ Select at least one species. Defaulting to all.")
        selected_species = all_species

    st.markdown("---")
    st.markdown("**Dimension Range Limits (cm):**")

    sl_min, sl_max = float(df_raw["sepal_length"].min()), float(df_raw["sepal_length"].max())
    sw_min, sw_max = float(df_raw["sepal_width"].min()), float(df_raw["sepal_width"].max())
    pl_min, pl_max = float(df_raw["petal_length"].min()), float(df_raw["petal_length"].max())
    pw_min, pw_max = float(df_raw["petal_width"].min()), float(df_raw["petal_width"].max())

    range_sl = st.slider("Sepal Length Range", sl_min, sl_max, (sl_min, sl_max), 0.1, key="f_sl")
    range_sw = st.slider("Sepal Width Range", sw_min, sw_max, (sw_min, sw_max), 0.1, key="f_sw")
    range_pl = st.slider("Petal Length Range", pl_min, pl_max, (pl_min, pl_max), 0.1, key="f_pl")
    range_pw = st.slider("Petal Width Range", pw_min, pw_max, (pw_min, pw_max), 0.1, key="f_pw")

    filter_ranges = {
        "sepal_length": range_sl,
        "sepal_width": range_sw,
        "petal_length": range_pl,
        "petal_width": range_pw,
    }

    st.markdown("---")
    st.markdown("#### 🚀 System Controls")
    if st.button("🌌 Toggle Antigravity Mode", use_container_width=True):
        st.session_state.antigravity_active = not st.session_state.antigravity_active
        st.rerun()


# ------------------------------------------------------------------------------
# Filter Application & Active Counts
# ------------------------------------------------------------------------------
df_filtered = filter_dataset(df_raw, selected_species, filter_ranges)
db_stats = database.get_prediction_stats()

# Top Hero Branding Banner
st.markdown(render_hero_banner(), unsafe_allow_html=True)

if st.session_state.antigravity_active:
    st.markdown(render_easter_egg_card(), unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# Key Metric KPI Cards (Mono Bootstrap Theme)
# ------------------------------------------------------------------------------
col1, col2, col3, col4 = st.columns(4)
with col1:
    pct_visible = (len(df_filtered) / len(df_raw) * 100) if len(df_raw) > 0 else 0
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-label">Active Filtered Flowers</div>
            <div class="stat-value">{len(df_filtered)} <span style="font-size:1rem;font-weight:500;color:#64748b;">/ {len(df_raw)}</span></div>
            <div class="stat-sub">{pct_visible:.1f}% of total specimen collection</div>
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-label">Morphometric Dimensions</div>
            <div class="stat-value">4 Primary</div>
            <div class="stat-sub">Sepal L/W + Petal L/W (cm)</div>
        </div>
        """, unsafe_allow_html=True
    )

with col3:
    active_classes = df_filtered["species"].nunique() if not df_filtered.empty else 0
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-label">Included Species</div>
            <div class="stat-value">{active_classes} <span style="font-size:1rem;font-weight:500;color:#64748b;">Classes</span></div>
            <div class="stat-sub">Setosa • Versicolor • Virginica</div>
        </div>
        """, unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-label">Saved Queries</div>
            <div class="stat-value">{db_stats["total_records"]} <span style="font-size:1rem;font-weight:500;color:#64748b;">Logs</span></div>
            <div class="stat-sub">Connected SQLite Database</div>
        </div>
        """, unsafe_allow_html=True
    )

st.write("")


# ------------------------------------------------------------------------------
# Main Application Tabs
# ------------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌸 Tab 1: Interactive Flower Visualizer",
    "📊 Tab 2: Dataset & Flower Records",
    "🧮 Tab 3: Statistical Engine (Formulas & Meanings)",
    "📈 Tab 4: Visual Analytics Gallery (Matplotlib)",
    "🎯 Tab 5: Live Species Classifier & History",
])


# ==============================================================================
# TAB 1: INTERACTIVE IRIS FLOWER VISUALIZER
# ==============================================================================
with tab1:
    st.subheader("🌸 Interactive Iris Flower Morphometry & Scaling")
    st.markdown(
        """
        <div class="formula-card">
            <div class="formula-title">📖 How Iris Flower Anatomy Works (Sepal vs. Petal)</div>
            An Iris flower is composed of two primary floral leaf structures that distinguish each species:
            <ul style="margin: 0.4rem 0 0 1.25rem; padding: 0;">
                <li><strong>Sepals (Outer Falls):</strong> The drooping, lower leaves that hang outward. They feature yellow nectar signals to guide pollinators.</li>
                <li><strong>Petals (Inner Standards):</strong> The upright, inner blades that stand vertically above the flower core.</li>
            </ul>
            <strong>Try it below:</strong> Move the sliders to change Sepal and Petal lengths/widths. The flower diagram will <strong>resize dynamically</strong> to match your exact dimensions!
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Preset Quick Buttons
    st.markdown("**Quick Archetype Presets:**")
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.button("🌱 Typical Setosa (Tiny Petals)", on_click=set_flower_preset, args=(5.0, 3.4, 1.5, 0.2), use_container_width=True)
    with p2:
        st.button("🌿 Typical Versicolor (Medium)", on_click=set_flower_preset, args=(5.9, 2.8, 4.3, 1.3), use_container_width=True)
    with p3:
        st.button("🌺 Typical Virginica (Large)", on_click=set_flower_preset, args=(6.6, 3.0, 5.6, 2.0), use_container_width=True)
    with p4:
        st.button("🔄 Reset Default Flower", on_click=set_flower_preset, args=(5.8, 3.0, 4.2, 1.3), use_container_width=True)

    # 4 Morphometric Sliders
    st.markdown("#### Adjust Flower Dimensions in Centimeters (cm):")
    f_c1, f_c2, f_c3, f_c4 = st.columns(4)
    with f_c1:
        curr_sl = st.slider("Sepal Length (cm)", 4.0, 8.0, float(st.session_state["flower_sl"]), 0.1, key="flower_sl")
    with f_c2:
        curr_sw = st.slider("Sepal Width (cm)", 2.0, 4.5, float(st.session_state["flower_sw"]), 0.1, key="flower_sw")
    with f_c3:
        curr_pl = st.slider("Petal Length (cm)", 1.0, 7.0, float(st.session_state["flower_pl"]), 0.1, key="flower_pl")
    with f_c4:
        curr_pw = st.slider("Petal Width (cm)", 0.1, 2.6, float(st.session_state["flower_pw"]), 0.1, key="flower_pw")

    # Calculate live nearest species
    input_vector = np.array([curr_sl, curr_sw, curr_pl, curr_pw], dtype=float)
    baseline_centroids = compute_species_centroids(df_raw, FEATURE_COLS)
    pred_res = predict_nearest_centroid(input_vector, baseline_centroids)
    curr_predicted = pred_res["predicted_species"]

    # Render Live Scaled Flower Diagram
    fig_flower = plot_interactive_iris_flower(
        sepal_length=curr_sl,
        sepal_width=curr_sw,
        petal_length=curr_pl,
        petal_width=curr_pw,
        predicted_species=curr_predicted,
    )
    st.pyplot(fig_flower, use_container_width=True)

    # Anatomical Takeaway Guide
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        st.markdown(
            f"""
            <div class="anatomy-card">
                <strong>🔍 Biological Classification for this Flower:</strong><br>
                Based on your dimensions, this flower is classified as <strong>Iris {curr_predicted}</strong> 
                (confidence score: <strong>{pred_res['proximity_pct'][curr_predicted]:.1f}%</strong>).<br><br>
                • <strong>Petal Area:</strong> {curr_pl * curr_pw:.2f} cm²<br>
                • <strong>Sepal Area:</strong> {curr_sl * curr_sw:.2f} cm²<br>
                • <strong>Petal/Sepal Length Ratio:</strong> {(curr_pl / curr_sl):.2f}
            </div>
            """,
            unsafe_allow_html=True,
        )
    with g_col2:
        st.markdown(
            """
            <div class="anatomy-card">
                <strong>💡 Botanical Rule of Thumb:</strong><br>
                • <strong>Iris Setosa:</strong> Extremely short petals (< 2.45 cm) that appear as small inner tufts.<br>
                • <strong>Iris Versicolor:</strong> Moderate, slender petals (~4.2 cm) with proportional sepals.<br>
                • <strong>Iris Virginica:</strong> Large, majestic flowers with long, wide petals (> 5.0 cm).
            </div>
            """,
            unsafe_allow_html=True,
        )


# ==============================================================================
# TAB 2: DATASET & FLOWER RECORDS
# ==============================================================================
with tab2:
    st.subheader("Botanical Dataset Records & Engineered Dimensions")
    st.markdown(
        """
        <div class="formula-card">
            <div class="formula-title">📊 About the Dataset Records</div>
            This table contains the 150 historical observations recorded by botanist Edgar Anderson and popularized by statistician Ronald Fisher.
            We have enriched the table with two practical engineered shape indicators:
            <strong>Petal Ratio</strong> (Length ÷ Width) and <strong>Petal Area Proxy</strong> (Length × Width in cm²).
        </div>
        """,
        unsafe_allow_html=True,
    )

    t2_col1, t2_col2 = st.columns([3, 1])
    with t2_col1:
        search_kw = st.text_input("🔍 Quick Search records (filter by species, number, or text):", "")
    with t2_col2:
        st.write("")
        st.write("")
        csv_data = df_filtered.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Filtered CSV",
            data=csv_data,
            file_name="iris_flower_data.csv",
            mime="text/csv",
            use_container_width=True,
        )

    # Filtered Table Display
    display_df = df_filtered.copy()
    if search_kw:
        mask = display_df.astype(str).apply(lambda row: row.str.contains(search_kw, case=False).any(), axis=1)
        display_df = display_df[mask]

    st.dataframe(
        display_df,
        use_container_width=True,
        height=280,
        column_config={
            "sepal_length": st.column_config.NumberColumn("Sepal Length (cm)", format="%.1f"),
            "sepal_width": st.column_config.NumberColumn("Sepal Width (cm)", format="%.1f"),
            "petal_length": st.column_config.NumberColumn("Petal Length (cm)", format="%.1f"),
            "petal_width": st.column_config.NumberColumn("Petal Width (cm)", format="%.1f"),
            "petal_ratio": st.column_config.NumberColumn("Petal Ratio (L/W)", format="%.2f"),
            "sepal_ratio": st.column_config.NumberColumn("Sepal Ratio (L/W)", format="%.2f"),
            "petal_area_proxy": st.column_config.NumberColumn("Petal Area (cm²)", format="%.2f"),
            "species": st.column_config.TextColumn("Species Class"),
        },
    )

    st.markdown("---")
    st.subheader("Species Summary Statistics (Averages & Ranges)")
    
    numeric_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width", "petal_ratio", "petal_area_proxy"]
    valid_cols = [c for c in numeric_cols if c in df_filtered.columns]
    
    if not df_filtered.empty:
        agg_summary = df_filtered.groupby("species")[valid_cols].agg(["mean", "std", "min", "max"]).round(2)
        st.dataframe(agg_summary, use_container_width=True)
    else:
        st.warning("No rows match the active filter constraints.")


# ==============================================================================
# TAB 3: STATISTICAL ENGINE (UNDERSTANDABLE FORMULAS & MEANINGS)
# ==============================================================================
with tab3:
    st.subheader("🧮 Statistical Foundation: Plain-English Guides & Formulas")
    st.markdown(
        """
        <div class="formula-card">
            <div class="formula-title">💡 Understanding the Mathematics Without Complex Jargon</div>
            Data science is often wrapped in intimidating notation, but the underlying concepts are simple:
            <ul style="margin: 0.35rem 0 0 1.25rem; padding: 0;">
                <li><strong>Average (Mean):</strong> The typical center measurement for each flower trait.</li>
                <li><strong>Covariance:</strong> Tells us whether two traits grow together or oppose each other.</li>
                <li><strong>Pearson Correlation:</strong> A clean score from <strong>-1.0 to +1.0</strong> showing relationship strength.</li>
                <li><strong>Principal Component Analysis (PCA):</strong> Identifies the single biggest trait difference between flowers.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if len(df_filtered) < 2:
        st.warning("Calculating relationships requires at least 2 flower samples. Please widen your sidebar filters.")
    else:
        manual_cov, np_cov = compute_covariance_matrix_manual(df_filtered, FEATURE_COLS)
        manual_corr, np_corr = compute_correlation_matrix_manual(df_filtered, FEATURE_COLS)

        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown("#### 1. Average (Mean) Measurements")
            st.markdown(
                r"""
                **Formula:** $\mu = \frac{\sum x}{N}$ *(Sum of all values divided by count)*
                """
            )
            mean_vector = np.mean(df_filtered[FEATURE_COLS].to_numpy(), axis=0)
            mean_df = pd.DataFrame(
                mean_vector.reshape(1, 4), 
                columns=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
            )
            st.dataframe(mean_df.round(2), use_container_width=True, hide_index=True)
            st.caption("These are the typical baseline dimensions for the currently filtered flowers.")

            st.markdown("---")
            st.markdown(r"#### 2. Covariance Matrix ($\mathbf{\Sigma}$)")
            st.markdown(
                r"""
                **Formula:** $\text{Cov}(X, Y) = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{N - 1}$
                <br><span style="color:#64748b;font-size:0.85rem;">
                Positive values mean as one measurement grows, the other also tends to grow.
                </span>
                """,
                unsafe_allow_html=True
            )
            cov_df = pd.DataFrame(
                manual_cov,
                index=["Sepal L", "Sepal W", "Petal L", "Petal W"],
                columns=["Sepal L", "Sepal W", "Petal L", "Petal W"],
            )
            st.dataframe(cov_df.round(3), use_container_width=True)

        with col_m2:
            st.markdown("#### 3. Pearson Correlation Matrix ($r$)")
            st.markdown(
                r"""
                **Formula:** $r = \frac{\text{Cov}(X, Y)}{\sigma_X \cdot \sigma_Y}$ *(Scaled from -1.0 to +1.0)*
                <br><span style="color:#64748b;font-size:0.85rem;">
                +1.0 = perfect direct link • 0.0 = completely unrelated • -1.0 = opposite.
                </span>
                """,
                unsafe_allow_html=True
            )
            corr_df = pd.DataFrame(
                manual_corr,
                index=["Sepal L", "Sepal W", "Petal L", "Petal W"],
                columns=["Sepal L", "Sepal W", "Petal L", "Petal W"],
            )
            st.dataframe(corr_df.round(3), use_container_width=True)

            # Plain-English Key Finding
            st.info(
                "💡 **Clear Takeaway:** Petal Length and Petal Width have an astounding correlation of "
                "**r = +0.96**. In simple terms: whenever an Iris flower has a longer petal, it is almost "
                "guaranteed to have a wider petal!"
            )

        st.markdown("---")
        st.subheader("Visual Heatmaps (Covariance vs. Correlation)")
        h_col1, h_col2 = st.columns(2)
        with h_col1:
            fig_cov = plot_covariance_heatmap(manual_cov, FEATURE_COLS)
            st.pyplot(fig_cov, use_container_width=True)
        with h_col2:
            fig_corr = plot_correlation_heatmap(manual_corr, FEATURE_COLS)
            st.pyplot(fig_corr, use_container_width=True)

        st.markdown("---")
        st.subheader("Principal Component Analysis (PCA): What Matters Most")
        st.markdown(
            """
            <div class="formula-card">
                <strong>What does PCA do?</strong> Instead of analyzing 4 measurements separately, PCA combines them 
                into master 'principal components'. <strong>Component 1 (PC1)</strong> represents overall flower size 
                and alone accounts for the vast majority of the total variation!
            </div>
            """,
            unsafe_allow_html=True,
        )
        eigen_res = compute_eigen_decomposition(manual_cov)
        eigen_df = pd.DataFrame({
            "Principal Component": ["PC1 (Overall Flower Size)", "PC2 (Sepal Ratio)", "PC3 (Subtle Variation)", "PC4 (Minor Noise)"],
            "Eigenvalue (λ)": eigen_res["eigenvalues"],
            "Variance Explained (%)": eigen_res["variance_explained_pct"],
            "Cumulative Total (%)": eigen_res["cumulative_variance_pct"],
        })
        st.dataframe(
            eigen_df.style.format({
                "Eigenvalue (λ)": "{:.4f}",
                "Variance Explained (%)": "{:.2f}%",
                "Cumulative Total (%)": "{:.2f}%",
            }),
            use_container_width=True,
            hide_index=True,
        )


# ==============================================================================
# TAB 4: VISUAL ANALYTICS GALLERY (MATPLOTLIB)
# ==============================================================================
with tab4:
    st.subheader("📈 Publication-Quality Visual Analytics Suite (Matplotlib)")
    st.markdown(
        """
        <div class="formula-card">
            <div class="formula-title">👓 How to Read These Visualizations</div>
            Each figure highlights a distinct biological relationship. Look at Figure 1: 
            notice how the purple cluster (Setosa) sits completely on its own below the <strong>2.45 cm line</strong>. 
            This visual boundary is why computer algorithms can classify Setosa with 100% precision!
        </div>
        """,
        unsafe_allow_html=True,
    )

    vg_col1, vg_col2 = st.columns(2)
    with vg_col1:
        st.markdown("#### Figure 1: Petal Length vs. Petal Width Clusters")
        if not df_filtered.empty:
            all_centroids = compute_species_centroids(df_filtered, FEATURE_COLS)
            fig_scatter = plot_bivariate_scatter(
                df_filtered,
                x_col="petal_length",
                y_col="petal_width",
                centroids=all_centroids,
                show_centroids=True,
                show_hulls=True,
            )
            st.pyplot(fig_scatter, use_container_width=True)
            st.caption("★ Stars indicate cluster centers (centroids). Polygons enclose all points per species.")

    with vg_col2:
        st.markdown("#### Figure 2: Boxplot Dispersion Across Species")
        if not df_filtered.empty:
            fig_box = plot_boxplot_dispersion(df_filtered, feature="petal_length")
            st.pyplot(fig_box, use_container_width=True)
            st.caption("Horizontal lines mark medians and interquartile ranges (IQR). Setosa shows zero overlap with the others.")

    st.markdown("---")
    st.markdown("#### Figure 3: Four-Panel Dimensional Distribution Histograms")
    if not df_filtered.empty:
        fig_hist = plot_distributions_grid(df_filtered, FEATURE_COLS)
        st.pyplot(fig_hist, use_container_width=True)
        st.caption("Dashed vertical lines indicate species mean values. Notice the bimodal peaks in petal dimensions.")


# ==============================================================================
# TAB 5: LIVE SPECIES CLASSIFIER & DATABASE LOGGER
# ==============================================================================
with tab5:
    st.subheader("🎯 Live Species Classifier (Nearest Centroid) & SQLite Logger")
    st.markdown(
        r"""
        <div class="formula-card">
            <div class="formula-title">🧠 How the Classification Algorithm Works</div>
            This classifier uses pure <strong>Euclidean distance in 4 dimensions</strong>:
            <br>$$\text{Distance} = \sqrt{(sl - \mu_{sl})^2 + (sw - \mu_{sw})^2 + (pl - \mu_{pl})^2 + (pw - \mu_{pw})^2}$$
            It compares your flower against typical Setosa, Versicolor, and Virginica averages. 
            The species with the <strong>shortest distance</strong> is the predicted winner!
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Use the current flower slider values from Tab 1
    t5_c1, t5_c2, t5_c3, t5_c4 = st.columns(4)
    with t5_c1:
        c_sl = st.number_input("Sepal Length (cm)", 4.0, 8.0, float(st.session_state["flower_sl"]), 0.1, key="num_sl")
    with t5_c2:
        c_sw = st.number_input("Sepal Width (cm)", 2.0, 4.5, float(st.session_state["flower_sw"]), 0.1, key="num_sw")
    with t5_c3:
        c_pl = st.number_input("Petal Length (cm)", 1.0, 7.0, float(st.session_state["flower_pl"]), 0.1, key="num_pl")
    with t5_c4:
        c_pw = st.number_input("Petal Width (cm)", 0.1, 2.6, float(st.session_state["flower_pw"]), 0.1, key="num_pw")

    c_point = np.array([c_sl, c_sw, c_pl, c_pw], dtype=float)
    c_centroids = compute_species_centroids(df_raw, FEATURE_COLS)
    c_pred_res = predict_nearest_centroid(c_point, c_centroids)

    c_species = c_pred_res["predicted_species"]
    c_dist = c_pred_res["min_distance"]
    c_dists = c_pred_res["distances"]
    c_prox = c_pred_res["proximity_pct"]

    st.markdown("---")
    res_c1, res_c2 = st.columns([1, 1])
    with res_c1:
        st.markdown(
            f'''
            <div class="prediction-card">
                <div class="prediction-title">Predicted Species Match</div>
                <div class="prediction-species">🌸 Iris {c_species}</div>
                <div style="color:#475569;font-size:0.95rem;margin-top:0.4rem;">
                    Shortest Distance: <strong>{c_dist:.3f} cm</strong> • Confidence: <strong>{c_prox[c_species]:.1f}%</strong>
                </div>
            </div>
            ''',
            unsafe_allow_html=True
        )

        # Database Log Button
        if st.button("💾 Save This Prediction to SQLite Database", type="primary", use_container_width=True):
            new_id = database.log_prediction(
                sepal_length=c_sl,
                sepal_width=c_sw,
                petal_length=c_pl,
                petal_width=c_pw,
                predicted_species=c_species,
                confidence_pct=round(c_prox[c_species], 1),
                distance_cm=round(c_dist, 4),
            )
            st.toast(f"✅ Prediction #{new_id} saved to database!", icon="💾")
            st.rerun()

    with res_c2:
        dist_df = pd.DataFrame([
            {"Species": sp, "Distance to Center (cm)": f"{c_dists[sp]:.3f} cm", "Match Confidence (%)": f"{c_prox[sp]:.1f}%"}
            for sp in ["Setosa", "Versicolor", "Virginica"]
        ])
        st.dataframe(dist_df, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("#### 2D Spatial Projection & Diagnostics")
    d_c1, d_c2 = st.columns(2)
    with d_c1:
        fig_diag = plot_prediction_diagnostics(c_dists, c_prox, c_species)
        st.pyplot(fig_diag, use_container_width=True)
    with d_c2:
        fig_proj = plot_query_point_projection(
            df_raw,
            c_point,
            c_centroids,
            c_species,
            x_col="petal_length",
            y_col="petal_width",
        )
        st.pyplot(fig_proj, use_container_width=True)

    st.markdown("---")
    st.subheader("🗄️ Saved Database Logs (SQLite `data/predictions.db`)")
    recent_db_df = database.get_recent_predictions(limit=10)
    if not recent_db_df.empty:
        st.dataframe(recent_db_df, use_container_width=True, hide_index=True)
        if st.button("🗑️ Clear All Database History"):
            database.clear_prediction_history()
            st.success("Database records cleared.")
            st.rerun()
    else:
        st.info("No predictions saved yet. Click 'Save This Prediction to SQLite Database' above to log entries!")


# ------------------------------------------------------------------------------
# Mono Bootstrap Clean Footer (No Academic / Student Names)
# ------------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #64748b; font-size: 0.85rem; padding: 1.5rem 0; line-height: 1.6;">
        <strong>Iris Flower Data Analysis</strong> • Multidimensional Morphometry & Statistical Suite<br>
        Powered by NumPy, Pandas, Matplotlib, Streamlit & SQLite Database<br>
        <span style="color: #0f172a; font-weight: 600;">Mono Bootstrap Architecture • 24/7 Production Deployment</span>
    </div>
    """,
    unsafe_allow_html=True,
)
