"""
streamlit_app.py
Iris Flower Data Analysis Suite â€” Deep Tech Obsidian Edition.
Full-Stack Multidimensional Data Science Dashboard powered by pure NumPy,
Matplotlib visual analytics, and SQLite persistence.
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
    render_top_navbar,
    render_hero_banner,
    render_sidebar_header,
    render_easter_egg_card,
    render_species_cards_html,
    render_team_footer,
)


# ------------------------------------------------------------------------------
# 1. Page Configuration & Obsidian Dark Theme
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Iris Analytics Lab | Deep Tech Obsidian",
    page_icon="ðŸŒ¸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply Deep Tech Obsidian CSS
if "antigravity_active" not in st.session_state:
    st.session_state.antigravity_active = False

st.markdown(get_custom_css(antigravity_mode=st.session_state.antigravity_active), unsafe_allow_html=True)

# Sticky Top Navigation Bar
st.markdown(render_top_navbar(), unsafe_allow_html=True)

# Initialize SQLite Database
database.init_db()


# ------------------------------------------------------------------------------
# 2. Session State & Preset Management
# ------------------------------------------------------------------------------
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
# 3. Load Dataset (Cached)
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
# 4. Sidebar Controls & Global Slicing Filters
# ------------------------------------------------------------------------------
with st.sidebar:
    st.markdown(render_sidebar_header(), unsafe_allow_html=True)

    st.markdown("#### ðŸ” Slicing Filters")
    st.caption("Filter botanical observations across all analytical modules.")

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
        st.warning("âš ï¸ Select at least one species. Defaulting to all.")
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
    st.markdown("#### ðŸš€ Experimental Mode")
    if st.button("ðŸŒŒ Toggle Antigravity Float", use_container_width=True):
        st.session_state.antigravity_active = not st.session_state.antigravity_active
        st.rerun()


# ------------------------------------------------------------------------------
# 5. Apply Slicing & Active Data
# ------------------------------------------------------------------------------
df_filtered = filter_dataset(df_raw, selected_species, filter_ranges)
db_stats = database.get_prediction_stats()

# Hero Branding Banner
st.markdown(render_hero_banner(), unsafe_allow_html=True)

if st.session_state.antigravity_active:
    st.markdown(render_easter_egg_card(), unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# 6. MODULE 1: High-Contrast Obsidian KPI Metric Cards
# ------------------------------------------------------------------------------
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    pct_visible = (len(df_filtered) / len(df_raw) * 100) if len(df_raw) > 0 else 0
    st.markdown(
        f"""
        <div class="obs-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 1.5rem;">ðŸŒ¸</span>
                <span class="badge-sneat bg-label-primary">{pct_visible:.1f}% Active</span>
            </div>
            <div style="color: #64748B; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em;">SPECIMEN COUNT</div>
            <div style="color: #38BDF8; font-size: 2rem; font-weight: 800; line-height: 1.1; margin: 4px 0;">{len(df_filtered)} <span style="font-size: 1rem; color: #64748B; font-weight: 500;">/ 150</span></div>
            <div style="color: #94A3B8; font-size: 0.8rem;">Anderson &amp; Fisher (1936)</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi2:
    st.markdown(
        """
        <div class="obs-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 1.5rem;">ðŸ“</span>
                <span class="badge-sneat bg-label-info">4D Tensor</span>
            </div>
            <div style="color: #64748B; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em;">FEATURE SPACE</div>
            <div style="color: #38BDF8; font-size: 2rem; font-weight: 800; line-height: 1.1; margin: 4px 0;">4 Dims</div>
            <div style="color: #94A3B8; font-size: 0.8rem;">Sepal &amp; Petal Dimensions</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi3:
    st.markdown(
        """
        <div class="obs-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 1.5rem;">ðŸ“ˆ</span>
                <span class="badge-sneat bg-label-success">Pearson r</span>
            </div>
            <div style="color: #64748B; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em;">STRONG CORRELATION</div>
            <div style="color: #34D399; font-size: 2rem; font-weight: 800; line-height: 1.1; margin: 4px 0;">+0.963</div>
            <div style="color: #94A3B8; font-size: 0.8rem;">Petal Length &bull; Petal Width</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi4:
    st.markdown(
        """
        <div class="obs-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 1.5rem;">ðŸŽ¯</span>
                <span class="badge-sneat bg-label-warning">Separability</span>
            </div>
            <div style="color: #64748B; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em;">SETOSA BOUNDARY</div>
            <div style="color: #F59E0B; font-size: 2rem; font-weight: 800; line-height: 1.1; margin: 4px 0;">100% Clean</div>
            <div style="color: #94A3B8; font-size: 0.8rem;">Linear cut at PL &le; 2.45 cm</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
# ------------------------------------------------------------------------------
# 7. Main Dashboard Modules (5 Deep Tech Tabs)
# ------------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "ðŸŒ¿ Botanical Anatomy & Synthesizer",
    "ðŸ“Š Dataset Records & Summary",
    "ðŸ§® Mathematical Engine (NumPy)",
    "ðŸ“ˆ Visual Analytics Gallery",
    "ðŸŽ¯ Centroid Classifier & SQLite",
])


# ==============================================================================
# TAB 1: MODULE 2 â€” BOTANICAL ANATOMY & INTERACTIVE SYNTHESIZER
# ==============================================================================
with tab1:
    st.subheader("ðŸŒ¿ Module 2: Botanical Anatomy & Species Taxonomy")
    st.markdown(
        """
        <div class="formula-card">
            <div class="formula-title">ðŸ“– Understanding Iris Flower Anatomy (Falls vs. Standards)</div>
            The Iris blossom is biologically defined by two distinct floral petal whorls:
            <ul style="margin: 0.4rem 0 0 1.25rem; padding: 0;">
                <li><strong>Falls (Sepals):</strong> The three lower, spreading blades that droop outward. They display nectar guides for pollinating bees.</li>
                <li><strong>Standards (Petals):</strong> The three upright, erect inner petals that rise vertically to crown the central reproductive core.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Render Side-by-side taxonomy cards
    st.markdown(render_species_cards_html(), unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("ðŸŒ¸ Interactive Dimension Synthesizer (2D Morphological Silhouette)")
    st.markdown(
        "Move the measurement sliders below to synthesize a flower specimen in real time. "
        "The anatomical vector silhouette and polar radar profile scale dynamically to match your exact dimensions."
    )

    # Archetype Presets
    st.markdown("**Quick Archetype Presets:**")
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        st.button("ðŸŒ± Typical Setosa (Small Petals)", on_click=set_flower_preset, args=(5.0, 3.4, 1.5, 0.2), use_container_width=True)
    with p2:
        st.button("ðŸŒ¿ Typical Versicolor (Medium)", on_click=set_flower_preset, args=(5.9, 2.8, 4.3, 1.3), use_container_width=True)
    with p3:
        st.button("ðŸŒº Typical Virginica (Large)", on_click=set_flower_preset, args=(6.6, 3.0, 5.6, 2.0), use_container_width=True)
    with p4:
        st.button("ðŸ”„ Reset Default Flower", on_click=set_flower_preset, args=(5.8, 3.0, 4.2, 1.3), use_container_width=True)

    # 4 Morphometric Sliders
    f_c1, f_c2, f_c3, f_c4 = st.columns(4)
    with f_c1:
        curr_sl = st.slider("Sepal Length (cm)", 4.0, 8.0, float(st.session_state["flower_sl"]), 0.1, key="flower_sl")
    with f_c2:
        curr_sw = st.slider("Sepal Width (cm)", 2.0, 4.5, float(st.session_state["flower_sw"]), 0.1, key="flower_sw")
    with f_c3:
        curr_pl = st.slider("Petal Length (cm)", 1.0, 7.0, float(st.session_state["flower_pl"]), 0.1, key="flower_pl")
    with f_c4:
        curr_pw = st.slider("Petal Width (cm)", 0.1, 2.6, float(st.session_state["flower_pw"]), 0.1, key="flower_pw")

    # Predict live species for synthesized dimensions
    input_vector = np.array([curr_sl, curr_sw, curr_pl, curr_pw], dtype=float)
    baseline_centroids = compute_species_centroids(df_raw, FEATURE_COLS)
    pred_res = predict_nearest_centroid(input_vector, baseline_centroids)
    curr_predicted = pred_res["predicted_species"]

    # Render Live Scaled Flower Diagram (Dark Theme #0B0F17)
    fig_flower = plot_interactive_iris_flower(
        sepal_length=curr_sl,
        sepal_width=curr_sw,
        petal_length=curr_pl,
        petal_width=curr_pw,
        predicted_species=curr_predicted,
    )
    st.pyplot(fig_flower, use_container_width=True)

    # Synthesized Flower Diagnostics
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        st.markdown(
            f"""
            <div class="obs-card">
                <strong style="color:#F8FAFC;">ðŸ” Synthesized Specimen Diagnostics:</strong><br>
                Classified as <strong style="color:#38BDF8;">Iris {curr_predicted}</strong> with 
                <strong style="color:#34D399;">{pred_res['proximity_pct'][curr_predicted]:.1f}%</strong> confidence.<br><br>
                &bull; <strong>Petal Area Proxy (PL &times; PW):</strong> {curr_pl * curr_pw:.2f} cmÂ²<br>
                &bull; <strong>Sepal Area Proxy (SL &times; SW):</strong> {curr_sl * curr_sw:.2f} cmÂ²<br>
                &bull; <strong>Petal-to-Sepal Length Ratio:</strong> {(curr_pl / curr_sl):.2f}
            </div>
            """,
            unsafe_allow_html=True,
        )
    with g_col2:
        st.markdown(
            """
            <div class="obs-card">
                <strong style="color:#F8FAFC;">ðŸ’¡ Botanical Recognition Rules:</strong><br>
                &bull; <strong style="color:#38BDF8;">Iris Setosa:</strong> Petal Length &le; 2.45 cm &mdash; short, delicate inner petals.<br>
                &bull; <strong style="color:#F59E0B;">Iris Versicolor:</strong> Petal Length 3.0 &ndash; 5.1 cm &mdash; balanced proportions.<br>
                &bull; <strong style="color:#A78BFA;">Iris Virginica:</strong> Petal Length &gt; 4.8 cm &mdash; large, majestic standards and falls.
            </div>
            """,
            unsafe_allow_html=True,
        )


# ==============================================================================
# TAB 2: DATASET RECORDS & EXPLORER
# ==============================================================================
with tab2:
    st.subheader("ðŸ“Š Botanical Observations & Summary Statistics")
    st.markdown(
        """
        <div class="formula-card">
            <div class="formula-title">Dataset Overview &amp; Engineered Shape Indices</div>
            This table contains the 150 historical specimens with two engineered geometric descriptors:
            <strong>Petal Aspect Ratio</strong> ($PL / PW$) and <strong>Petal Area Proxy</strong> ($PL \times PW \text{ cm}^2$).
        </div>
        """,
        unsafe_allow_html=True,
    )

    t2_col1, t2_col2 = st.columns([3, 1])
    with t2_col1:
        search_kw = st.text_input("ðŸ” Quick Search records:", "")
    with t2_col2:
        st.write("")
        st.write("")
        csv_data = df_filtered.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="ðŸ“¥ Export Filtered CSV",
            data=csv_data,
            file_name="iris_obsidian_data.csv",
            mime="text/csv",
            use_container_width=True,
        )

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
            "petal_area_proxy": st.column_config.NumberColumn("Petal Area (cmÂ²)", format="%.2f"),
            "species": st.column_config.TextColumn("Species Class"),
        },
    )

    st.markdown("---")
    st.subheader("Species Descriptive Aggregations (Pandas GroupBy)")
    numeric_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width", "petal_ratio", "petal_area_proxy"]
    valid_cols = [c for c in numeric_cols if c in df_filtered.columns]
    if not df_filtered.empty:
        agg_summary = df_filtered.groupby("species")[valid_cols].agg(["mean", "std", "min", "max"]).round(2)
        st.dataframe(agg_summary, use_container_width=True)
    else:
        st.warning("No specimens match current filters.")


# ==============================================================================
# TAB 3: MODULE 3 â€” NUMPY MATHEMATICAL FOUNDATIONS
# ==============================================================================
with tab3:
    st.subheader("ðŸ§® Module 3: NumPy Linear Algebra Engine")
    st.markdown(
        """
        <div class="formula-card">
            <div class="formula-title">Mathematical Rigor: Pure NumPy Vector &amp; Matrix Multiplication</div>
            Every statistical tensor is computed from scratch using pure NumPy matrix operations:
            <ul style="margin: 0.35rem 0 0 1.25rem; padding: 0;">
                <li><strong>Sample Mean Vector (&mu;):</strong> $\mu = \\frac{1}{N} \\sum_{i=1}^N x_i$</li>
                <li><strong>Sample Covariance Matrix (&Sigma;):</strong> $\\Sigma = \\frac{1}{N - 1} (X - \\mu)^T (X - \\mu)$</li>
                <li><strong>Pearson Correlation Tensor (R):</strong> $R = D^{-1/2} \\Sigma D^{-1/2}$ where $D = \\text{diag}(\\Sigma)$</li>
                <li><strong>Eigen-Decomposition:</strong> $\\Sigma v_i = \\lambda_i v_i$ for Principal Component Analysis</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if len(df_filtered) < 2:
        st.warning("Covariance calculations require at least 2 observations. Please widen sidebar filters.")
    else:
        manual_cov, np_cov = compute_covariance_matrix_manual(df_filtered, FEATURE_COLS)
        manual_corr, np_corr = compute_correlation_matrix_manual(df_filtered, FEATURE_COLS)

        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown("#### 1. Mean Vector (&mu;)")
            mean_vector = np.mean(df_filtered[FEATURE_COLS].to_numpy(), axis=0)
            mean_df = pd.DataFrame(
                mean_vector.reshape(1, 4),
                columns=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
            )
            st.dataframe(mean_df.round(2), use_container_width=True, hide_index=True)

            st.markdown(r"#### 2. Sample Covariance Matrix ($\mathbf{\Sigma}$)")
            cov_df = pd.DataFrame(
                manual_cov,
                index=["Sepal L", "Sepal W", "Petal L", "Petal W"],
                columns=["Sepal L", "Sepal W", "Petal L", "Petal W"],
            )
            st.dataframe(cov_df.round(3), use_container_width=True)
            cov_diff = np.max(np.abs(manual_cov - np_cov))
            st.caption(f"âœ“ Pure NumPy $(X-\\mu)^T(X-\\mu)/(N-1)$ vs np.cov diff: {cov_diff:.2e}")

        with col_m2:
            st.markdown("#### 3. Pearson Correlation Matrix ($R$)")
            corr_df = pd.DataFrame(
                manual_corr,
                index=["Sepal L", "Sepal W", "Petal L", "Petal W"],
                columns=["Sepal L", "Sepal W", "Petal L", "Petal W"],
            )
            st.dataframe(corr_df.round(3), use_container_width=True)
            corr_diff = np.max(np.abs(manual_corr - np_corr))
            st.caption(f"âœ“ Pure NumPy normalized correlation diff: {corr_diff:.2e}")

            st.info(
                "ðŸ’¡ **Key Discovery:** Petal Length and Petal Width exhibit a correlation coefficient of "
                "**r = +0.963**. Flowers with longer petals consistently develop wider petals!"
            )

        st.markdown("---")
        st.subheader("Covariance & Correlation Heatmaps (#0B0F17 Facecolor)")
        h_col1, h_col2 = st.columns(2)
        with h_col1:
            fig_cov = plot_covariance_heatmap(manual_cov, FEATURE_COLS)
            st.pyplot(fig_cov, use_container_width=True)
        with h_col2:
            fig_corr = plot_correlation_heatmap(manual_corr, FEATURE_COLS)
            st.pyplot(fig_corr, use_container_width=True)

        st.markdown("---")
        st.subheader("Principal Component Analysis (PCA Eigen-Decomposition)")
        eigen_res = compute_eigen_decomposition(manual_cov)
        eigen_df = pd.DataFrame({
            "Principal Component": ["PC1 (Overall Flower Scale)", "PC2 (Sepal Proportion)", "PC3 (Fine Variance)", "PC4 (Residual Noise)"],
            "Eigenvalue (Î»)": eigen_res["eigenvalues"],
            "Variance Explained (%)": eigen_res["variance_explained_pct"],
            "Cumulative (%)": eigen_res["cumulative_variance_pct"],
        })
        st.dataframe(
            eigen_df.style.format({
                "Eigenvalue (Î»)": "{:.4f}",
                "Variance Explained (%)": "{:.2f}%",
                "Cumulative (%)": "{:.2f}%",
            }),
            use_container_width=True,
            hide_index=True,
        )


# ==============================================================================
# TAB 4: MODULE 4 â€” VISUAL ANALYTICS GALLERY (MATPLOTLIB)
# ==============================================================================
with tab4:
    st.subheader("ðŸ“ˆ Module 4: High-Contrast Matplotlib Visual Analytics")
    st.markdown(
        """
        <div class="formula-card">
            <div class="formula-title">Dark-Background Matplotlib Charts with High-Legibility Typography</div>
            Rendered natively on Deep Obsidian (<code>#0B0F17</code>) with Electric Cyan, Warm Amber, and Soft Lavender palettes.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not df_filtered.empty:
        all_centroids = compute_species_centroids(df_filtered, FEATURE_COLS)

        vg1, vg2 = st.columns(2)
        with vg1:
            st.markdown("#### Figure 1: Petal Length vs. Petal Width Scatter")
            fig_scatter = plot_bivariate_scatter(
                df_filtered,
                x_col="petal_length",
                y_col="petal_width",
                centroids=all_centroids,
                boundary_line=True,
            )
            st.pyplot(fig_scatter, use_container_width=True)
            st.caption("Green dashed line indicates the 2.45 cm threshold, separating Setosa with 100% precision.")

        with vg2:
            st.markdown("#### Figure 2: Boxplot Dispersion Across Species")
            fig_box = plot_boxplot_dispersion(df_filtered, feature="petal_length")
            st.pyplot(fig_box, use_container_width=True)
            st.caption("Boxplots display medians, IQRs, and outliers per species class.")

        st.markdown("---")
        st.markdown("#### Figure 3: Four-Panel Gaussian Kernel Density Distributions (KDE)")
        fig_kde = plot_distributions_grid(df_filtered)
        st.pyplot(fig_kde, use_container_width=True)
        st.caption("Probability density functions generated via pure NumPy Gaussian kernel density estimation.")


# ==============================================================================
# TAB 5: MODULE 5 â€” LIVE CENTROID CLASSIFIER & DATABASE LOGGER
# ==============================================================================
with tab5:
    st.subheader("ðŸŽ¯ Module 5: Live Centroid Classifier & SQLite Persistence")
    st.markdown(
        r"""
        <div class="formula-card">
            <div class="formula-title">Euclidean Metric Distance Formulation in 4D</div>
            $$d(x, \mu_k) = \|x - \mu_k\|_2 = \sqrt{\sum_{j=1}^4 (x_j - \mu_{k,j})^2}$$
            The flower is mapped to the species class centroid minimizing the Euclidean metric $d(x, \mu_k)$.
        </div>
        """,
        unsafe_allow_html=True,
    )

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
            f"""
            <div class="prediction-card">
                <div style="font-size: 0.85rem; color: #38BDF8; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 6px;">PREDICTED SPECIES</div>
                <div class="prediction-species">ðŸŒ¸ Iris {c_species}</div>
                <div style="color: #94A3B8; font-size: 0.95rem; margin-top: 8px;">
                    Euclidean Distance: <strong style="color: #F8FAFC;">{c_dist:.3f} cm</strong> &bull; Confidence: <strong style="color: #34D399;">{c_prox[c_species]:.1f}%</strong>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("ðŸ’¾ Log Prediction to SQLite Database", type="primary", use_container_width=True):
            new_id = database.log_prediction(
                sepal_length=c_sl,
                sepal_width=c_sw,
                petal_length=c_pl,
                petal_width=c_pw,
                predicted_species=c_species,
                confidence_pct=round(c_prox[c_species], 1),
                distance_cm=round(c_dist, 4),
            )
            st.toast(f"âœ… Prediction #{new_id} persisted to SQLite!", icon="ðŸ’¾")
            st.rerun()

    with res_c2:
        dist_df = pd.DataFrame([
            {"Species": sp, "Distance to Centroid (cm)": f"{c_dists[sp]:.3f} cm", "Confidence Match (%)": f"{c_prox[sp]:.1f}%"}
            for sp in ["Setosa", "Versicolor", "Virginica"]
        ])
        st.dataframe(dist_df, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("#### Diagnostic Distance Comparison & Spatial Projection")
    d_c1, d_c2 = st.columns(2)
    with d_c1:
        fig_diag = plot_prediction_diagnostics(c_dists, c_prox, c_species)
        st.pyplot(fig_diag, use_container_width=True)
    with d_c2:
        fig_proj = plot_query_point_projection(df_raw, c_point, c_centroids, c_species)
        st.pyplot(fig_proj, use_container_width=True)

    st.markdown("---")
    st.subheader("ðŸ—„ï¸ SQLite Prediction Log (`data/predictions.db`)")
    recent_db_df = database.get_recent_predictions(limit=10)
    if not recent_db_df.empty:
        st.dataframe(recent_db_df, use_container_width=True, hide_index=True)
        if st.button("ðŸ—‘ï¸ Clear Prediction History"):
            database.clear_prediction_history()
            st.success("Database records reset.")
            st.rerun()
    else:
        st.info("No predictions logged yet. Click 'Log Prediction to SQLite Database' above to persist records!")


# ==============================================================================
# MODULE 6: ACADEMIC CREDITS & CSE TEAM FOOTER
# ==============================================================================
st.markdown("---")
st.markdown(render_team_footer(), unsafe_allow_html=True)
