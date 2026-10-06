"""
app.py
Multidimensional Exploratory Data Analysis of the Iris Dataset
Utilizing NumPy, Pandas, and Matplotlib.

CSE Mini-Project Dashboard
"""

import streamlit as st
import numpy as np
import pandas as pd

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
    plot_covariance_heatmap,
    plot_correlation_heatmap,
    plot_bivariate_scatter,
    plot_distributions_grid,
    plot_prediction_diagnostics,
    plot_query_point_projection,
)
from styles import get_custom_css, render_hero_banner, render_easter_egg_card


# ------------------------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Iris EDA & Multidimensional Analytics | CSE Mini-Project",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ------------------------------------------------------------------------------
# State Initialization
# ------------------------------------------------------------------------------
if "antigravity_active" not in st.session_state:
    st.session_state.antigravity_active = False

# Preset values for Tab 4 classifier
if "pred_sl" not in st.session_state:
    st.session_state.pred_sl = 5.8
if "pred_sw" not in st.session_state:
    st.session_state.pred_sw = 3.0
if "pred_pl" not in st.session_state:
    st.session_state.pred_pl = 4.2
if "pred_pw" not in st.session_state:
    st.session_state.pred_pw = 1.3


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
# Sidebar Controls & Project Information
# ------------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🎓 CSE Mini-Project")
    st.caption("**Course:** Data Science & Multidimensional Analytics (CS601)")
    
    # Project Info Card
    with st.expander("👥 Team Members & Guide", expanded=False):
        st.markdown(
            """
            <div class="sidebar-card">
                <div class="team-member-item">
                    <span class="team-member-name">1. Adnan Hameed</span>
                    <span class="team-member-role">Lead / Pipeline</span>
                </div>
                <div class="team-member-item">
                    <span class="team-member-name">2. Bhavana K.</span>
                    <span class="team-member-role">Pandas Eng.</span>
                </div>
                <div class="team-member-item">
                    <span class="team-member-name">3. Chethan R.</span>
                    <span class="team-member-role">NumPy Linear Alg.</span>
                </div>
                <div class="team-member-item">
                    <span class="team-member-name">4. Divya Sharma</span>
                    <span class="team-member-role">Matplotlib & UI</span>
                </div>
                <div style="margin-top: 10px; padding-top: 8px; border-top: 1px solid rgba(148, 163, 184, 0.3); font-size: 0.8rem;">
                    <strong>Faculty Guide:</strong><br>
                    Dr. K. S. Ramanujan, Ph.D.<br>
                    <em>Dept. of Computer Science & Engg.</em>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### 🔍 Dynamic Filters")

    # Species Multi-select
    all_species = sorted(df_raw["species"].unique().tolist())
    selected_species = st.multiselect(
        "Select Species:",
        options=all_species,
        default=all_species,
        help="Filter the analysis by one or more Iris botanical classes.",
    )

    if not selected_species:
        st.warning("Please select at least one species to display data.")
        selected_species = all_species

    # Range Sliders
    sl_min, sl_max = float(df_raw["sepal_length"].min()), float(df_raw["sepal_length"].max())
    sw_min, sw_max = float(df_raw["sepal_width"].min()), float(df_raw["sepal_width"].max())
    pl_min, pl_max = float(df_raw["petal_length"].min()), float(df_raw["petal_length"].max())
    pw_min, pw_max = float(df_raw["petal_width"].min()), float(df_raw["petal_width"].max())

    sepal_len_range = st.slider("Sepal Length Range (cm)", sl_min, sl_max, (sl_min, sl_max), step=0.1)
    sepal_wid_range = st.slider("Sepal Width Range (cm)", sw_min, sw_max, (sw_min, sw_max), step=0.1)
    petal_len_range = st.slider("Petal Length Range (cm)", pl_min, pl_max, (pl_min, pl_max), step=0.1)
    petal_wid_range = st.slider("Petal Width Range (cm)", pw_min, pw_max, (pw_min, pw_max), step=0.1)

    ranges = {
        "sepal_length": sepal_len_range,
        "sepal_width": sepal_wid_range,
        "petal_length": petal_len_range,
        "petal_width": petal_wid_range,
    }

    st.markdown("---")
    
    # Antigravity Easter Egg Section
    st.markdown("### 🪐 Easter Egg")
    btn_label = "Disable Antigravity" if st.session_state.antigravity_active else "🚀 import antigravity"
    if st.button(btn_label, use_container_width=True, type="secondary"):
        st.session_state.antigravity_active = not st.session_state.antigravity_active
        st.rerun()

    if st.session_state.antigravity_active:
        st.success("Anti-Gravity Module engaged! Hover over elements to feel the levitation.")


# Inject Custom CSS
st.markdown(get_custom_css(antigravity_mode=st.session_state.antigravity_active), unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# Filter Data
# ------------------------------------------------------------------------------
df_filtered = filter_dataset(df_raw, selected_species, ranges)


# ------------------------------------------------------------------------------
# Main Dashboard Header & Hero
# ------------------------------------------------------------------------------
st.markdown(render_hero_banner(), unsafe_allow_html=True)

if st.session_state.antigravity_active:
    st.markdown(render_easter_egg_card(), unsafe_allow_html=True)

# Overview Metric Cards
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
with m_col1:
    st.metric(
        label="Filtered Samples",
        value=f"{len(df_filtered)} / {len(df_raw)}",
        delta=f"{(len(df_filtered)/len(df_raw)*100):.1f}% Active",
    )
with m_col2:
    st.metric(
        label="Feature Dimensions",
        value="4 Primary + 4 Derived",
        delta="8 Total Columns",
    )
with m_col3:
    active_classes = df_filtered["species"].nunique() if not df_filtered.empty else 0
    st.metric(
        label="Active Classes",
        value=f"{active_classes} Species",
        delta="Setosa / Versi / Virg",
    )
with m_col4:
    avg_petal_ratio = df_filtered["petal_ratio"].mean() if not df_filtered.empty else 0.0
    st.metric(
        label="Mean Petal Aspect Ratio",
        value=f"{avg_petal_ratio:.2f}",
        delta="PL / PW Index",
    )

st.write("")


# ------------------------------------------------------------------------------
# Main Tabs
# ------------------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Tab 1: Dataset Explorer & Pandas Aggregations",
    "🧮 Tab 2: NumPy Mathematical Engine",
    "📈 Tab 3: Visual Analytics Suite",
    "🎯 Tab 4: Interactive Centroid Predictor",
])


# ==============================================================================
# TAB 1: DATASET EXPLORER & PANDAS AGGREGATIONS
# ==============================================================================
with tab1:
    st.markdown("### 🗂️ Interactive Dataset Explorer & Feature Engineering")
    st.write(
        "Inspect the raw Fisher Iris observations alongside engineered features including "
        "**Petal Aspect Ratio** ($PL/PW$), **Sepal Aspect Ratio** ($SL/SW$), and **Area Proxies**."
    )

    t1_col1, t1_col2 = st.columns([3, 1])
    with t1_col1:
        search_kw = st.text_input("🔍 Search rows (filter by species or measurement value):", "")
    with t1_col2:
        st.write("")
        st.write("")
        csv_data = df_filtered.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Export Filtered CSV",
            data=csv_data,
            file_name="filtered_iris_dataset.csv",
            mime="text/csv",
            use_container_width=True,
        )

    # Display Filtered Data
    display_df = df_filtered.copy()
    if search_kw:
        mask = display_df.astype(str).apply(lambda row: row.str.contains(search_kw, case=False).any(), axis=1)
        display_df = display_df[mask]

    st.dataframe(
        display_df,
        use_container_width=True,
        height=300,
        column_config={
            "sepal_length": st.column_config.NumberColumn("Sepal Length (cm)", format="%.1f"),
            "sepal_width": st.column_config.NumberColumn("Sepal Width (cm)", format="%.1f"),
            "petal_length": st.column_config.NumberColumn("Petal Length (cm)", format="%.1f"),
            "petal_width": st.column_config.NumberColumn("Petal Width (cm)", format="%.1f"),
            "petal_ratio": st.column_config.NumberColumn("Petal Ratio (PL/PW)", format="%.2f"),
            "sepal_ratio": st.column_config.NumberColumn("Sepal Ratio (SL/SW)", format="%.2f"),
            "petal_area_proxy": st.column_config.NumberColumn("Petal Area Proxy (cm²)", format="%.2f"),
            "sepal_area_proxy": st.column_config.NumberColumn("Sepal Area Proxy (cm²)", format="%.2f"),
            "species": st.column_config.TextColumn("Species Class"),
        },
    )

    st.markdown("---")
    st.markdown("### 📑 Pandas Parametric Descriptive Statistics")
    
    stat_tab1, stat_tab2 = st.tabs(["Comprehensive Feature Statistics", "GroupBy Species Aggregations"])
    
    with stat_tab1:
        all_numerical = FEATURE_COLS + ["petal_ratio", "sepal_ratio", "petal_area_proxy", "sepal_area_proxy"]
        stats_df = compute_descriptive_stats(df_filtered, all_numerical)
        if not stats_df.empty:
            st.dataframe(
                stats_df.style.format("{:.3f}").background_gradient(cmap="Blues", subset=["mean", "std", "iqr"]),
                use_container_width=True,
            )
        else:
            st.warning("No data points available with current filter constraints.")

    with stat_tab2:
        species_agg = compute_species_aggregations(df_filtered)
        if not species_agg.empty:
            st.write("Grouped means, standard deviations, and medians stratified across botanical classes:")
            st.dataframe(species_agg.style.format("{:.2f}"), use_container_width=True)
        else:
            st.warning("No data points available for grouping.")


# ==============================================================================
# TAB 2: NUMPY MATHEMATICAL ENGINE
# ==============================================================================
with tab2:
    st.markdown("### 🧮 Pure NumPy Linear Algebra & Tensor Decomposition")
    st.markdown(
        r"""
        <div class="math-card">
            <strong>Theoretical Formulation:</strong><br>
            Given a data matrix $\mathbf{X} \in \mathbb{R}^{n \times 4}$, the sample covariance tensor 
            $\mathbf{\Sigma}$ is evaluated by centering vectors around the empirical mean $\mathbf{\mu} = \frac{1}{n}\sum_{i=1}^n \mathbf{x}_i$:
            $$\mathbf{X}_{\text{centered}} = \mathbf{X} - \mathbf{1}\mathbf{\mu}^T, \quad 
            \mathbf{\Sigma} = \frac{1}{n-1} \mathbf{X}_{\text{centered}}^T \mathbf{X}_{\text{centered}}$$
            Pearson correlation matrix is normalized via the standard deviation diagonal matrix $\mathbf{D} = \text{diag}(\mathbf{\Sigma})^{1/2}$:
            $$\mathbf{R} = \mathbf{D}^{-1} \mathbf{\Sigma} \mathbf{D}^{-1}$$
        </div>
        """,
        unsafe_allow_html=True,
    )

    if len(df_filtered) < 2:
        st.warning("Covariance calculation requires at least 2 samples. Please broaden your sidebar filters.")
    else:
        # NumPy Covariance & Correlation Computation
        manual_cov, np_cov = compute_covariance_matrix_manual(df_filtered, FEATURE_COLS)
        manual_corr, np_corr = compute_correlation_matrix_manual(df_filtered, FEATURE_COLS)
        
        # Verify Numerical Agreement
        cov_max_error = np.max(np.abs(manual_cov - np_cov))
        corr_max_error = np.max(np.abs(manual_corr - np_corr))
        
        st.caption(
            f"✅ **NumPy Precision Verification:** Manual outer product implementation vs. `np.cov` error: "
            f"**{cov_max_error:.2e}** | Correlation error vs `np.corrcoef`: **{corr_max_error:.2e}**."
        )

        n_col1, n_col2 = st.columns(2)
        with n_col1:
            st.markdown(r"#### Sample Covariance Heatmap $\mathbf{\Sigma}$")
            fig_cov = plot_covariance_heatmap(manual_cov, FEATURE_COLS)
            st.pyplot(fig_cov, use_container_width=True)
            
            with st.expander("View Raw 4x4 NumPy Covariance Array"):
                st.code(np.array2string(manual_cov, precision=4, suppress_small=True), language="python")

        with n_col2:
            st.markdown(r"#### Pearson Correlation Heatmap $\mathbf{R}$")
            fig_corr = plot_correlation_heatmap(manual_corr, FEATURE_COLS)
            st.pyplot(fig_corr, use_container_width=True)
            
            with st.expander("View Raw 4x4 NumPy Correlation Array"):
                st.code(np.array2string(manual_corr, precision=4, suppress_small=True), language="python")

        st.markdown("---")
        st.markdown("### 🧬 Class Mean Centroids & Eigen-Decomposition")
        
        c_col1, c_col2 = st.columns(2)
        with c_col1:
            st.markdown(r"#### Species Mean Centroid Vectors $\mathbf{\mu}_k$")
            centroids = compute_species_centroids(df_filtered, FEATURE_COLS)
            
            centroid_data = []
            for sp, vec in centroids.items():
                centroid_data.append({
                    "Species": sp,
                    "Sepal Length (cm)": f"{vec[0]:.2f}",
                    "Sepal Width (cm)": f"{vec[1]:.2f}",
                    "Petal Length (cm)": f"{vec[2]:.2f}",
                    "Petal Width (cm)": f"{vec[3]:.2f}",
                })
            st.dataframe(pd.DataFrame(centroid_data), use_container_width=True, hide_index=True)
            st.caption(r"Centroids are computed as $\mathbf{\mu}_k = \frac{1}{N_k} \sum_{i \in \mathcal{C}_k} \mathbf{x}_i$.")

        with c_col2:
            st.markdown("#### Principal Eigenvalues & Variance Explained")
            eigen_res = compute_eigen_decomposition(manual_cov)
            
            eigen_df = pd.DataFrame({
                "Component": [f"PC{i+1}" for i in range(4)],
                "Eigenvalue (λ)": eigen_res["eigenvalues"],
                "Variance Explained (%)": eigen_res["variance_explained_pct"],
                "Cumulative Var (%)": eigen_res["cumulative_variance_pct"],
            })
            st.dataframe(
                eigen_df.style.format({
                    "Eigenvalue (λ)": "{:.4f}",
                    "Variance Explained (%)": "{:.2f}%",
                    "Cumulative Var (%)": "{:.2f}%",
                }),
                use_container_width=True,
                hide_index=True,
            )
            st.caption(
                f"**Observation:** First principal component explains "
                f"**{eigen_res['variance_explained_pct'][0]:.1f}%** of total variance in the current view."
            )


# ==============================================================================
# TAB 3: VISUAL ANALYTICS SUITE
# ==============================================================================
with tab3:
    st.markdown("### 🎨 Matplotlib Visual Analytics Suite")
    st.write(
        "Interactive bivariate scatter plots equipped with species convex hull envelopes, "
        "centroid anchors, and multi-panel distribution histograms."
    )

    v_col1, v_col2 = st.columns([2, 1])
    with v_col1:
        feature_options = list(FEATURE_LABELS.keys())
        scat_x = st.selectbox("X-Axis Feature:", feature_options, index=2, format_func=lambda x: FEATURE_LABELS[x])
    with v_col2:
        scat_y = st.selectbox("Y-Axis Feature:", feature_options, index=3, format_func=lambda x: FEATURE_LABELS[x])

    hull_check = st.checkbox("Display Convex Hull Decision Envelopes", value=True)
    centroid_check = st.checkbox("Display Species Centroid Markers (★)", value=True)

    if not df_filtered.empty:
        all_centroids = compute_species_centroids(df_filtered, FEATURE_COLS)
        fig_scatter = plot_bivariate_scatter(
            df_filtered,
            x_col=scat_x,
            y_col=scat_y,
            centroids=all_centroids,
            show_centroids=centroid_check,
            show_hulls=hull_check,
        )
        st.pyplot(fig_scatter, use_container_width=True)
    else:
        st.warning("No data points match current filter criteria.")

    st.markdown("---")
    st.markdown("### 📊 4-Panel Multidimensional Distribution Histograms")
    st.write("Stratified comparative frequency distribution across all 4 anatomical dimensions:")
    
    if not df_filtered.empty:
        fig_hist = plot_distributions_grid(df_filtered)
        st.pyplot(fig_hist, use_container_width=True)
    else:
        st.warning("Distribution histograms require active samples.")


# ==============================================================================
# TAB 4: INTERACTIVE CENTROID PREDICTOR / CLASSIFIER
# ==============================================================================
with tab4:
    st.markdown("### 🎯 Live Nearest-Centroid Classifier via Pure NumPy")
    st.markdown(
        r"""
        <div class="math-card">
            <strong>Decision Rule:</strong><br>
            A sample $\mathbf{x} = [SL, SW, PL, PW]^T$ is assigned to the botanical class $\mathcal{C}_k$ whose 
            mean centroid $\mathbf{\mu}_k$ minimizes the $L_2$ Euclidean distance:
            $$\hat{y} = \arg\min_{k \in \{Setosa, Versicolor, Virginica\}} \|\mathbf{x} - \mathbf{\mu}_k\|_2 
            = \arg\min_k \sqrt{\sum_{j=1}^4 (x_j - \mu_{k,j})^2}$$
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Preset Dimension Quick-Select Buttons
    st.markdown("**Quick Preset Profiles:**")
    p_col1, p_col2, p_col3, p_col4 = st.columns(4)
    with p_col1:
        if st.button("🌸 Typical Setosa", use_container_width=True):
            st.session_state.pred_sl = 5.0
            st.session_state.pred_sw = 3.5
            st.session_state.pred_pl = 1.4
            st.session_state.pred_pw = 0.2
            st.rerun()
    with p_col2:
        if st.button("🌿 Typical Versicolor", use_container_width=True):
            st.session_state.pred_sl = 5.9
            st.session_state.pred_sw = 2.7
            st.session_state.pred_pl = 4.2
            st.session_state.pred_pw = 1.3
            st.rerun()
    with p_col3:
        if st.button("🌺 Typical Virginica", use_container_width=True):
            st.session_state.pred_sl = 6.6
            st.session_state.pred_sw = 3.0
            st.session_state.pred_pl = 5.5
            st.session_state.pred_pw = 2.0
            st.rerun()
    with p_col4:
        if st.button("🔄 Reset Default", use_container_width=True):
            st.session_state.pred_sl = 5.8
            st.session_state.pred_sw = 3.0
            st.session_state.pred_pl = 4.2
            st.session_state.pred_pw = 1.3
            st.rerun()

    # Dimension Sliders
    sl_col1, sl_col2 = st.columns(2)
    with sl_col1:
        in_sl = st.slider("Input Sepal Length (cm)", 4.0, 8.0, float(st.session_state.pred_sl), 0.1, key="in_sl_slider")
        in_sw = st.slider("Input Sepal Width (cm)", 2.0, 4.5, float(st.session_state.pred_sw), 0.1, key="in_sw_slider")
    with sl_col2:
        in_pl = st.slider("Input Petal Length (cm)", 1.0, 7.0, float(st.session_state.pred_pl), 0.1, key="in_pl_slider")
        in_pw = st.slider("Input Petal Width (cm)", 0.1, 2.6, float(st.session_state.pred_pw), 0.1, key="in_pw_slider")

    # Construct Query Vector
    query_vector = np.array([in_sl, in_sw, in_pl, in_pw], dtype=float)

    # Compute Centroids on baseline raw dataset to maintain consistent ground truth
    baseline_centroids = compute_species_centroids(df_raw, FEATURE_COLS)
    prediction_result = predict_nearest_centroid(query_vector, baseline_centroids)

    pred_species = prediction_result["predicted_species"]
    min_dist = prediction_result["min_distance"]
    distances = prediction_result["distances"]
    proximities = prediction_result["proximity_pct"]

    # Display Prediction Box
    tag_class = f"tag-{pred_species.lower()}"
    st.markdown(
        f"""
        <div class="prediction-box">
            <div style="font-size: 0.95rem; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">
                Live NumPy Prediction
            </div>
            <div class="species-tag {tag_class}">
                Iris {pred_species}
            </div>
            <div style="font-size: 1rem; color: #334155; margin-top: 4px;">
                Centroid Euclidean Distance: <strong>{min_dist:.3f} cm</strong> &nbsp;|&nbsp; 
                Confidence Proximity: <strong>{proximities[pred_species]:.1f}%</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Visual Diagnostics
    pred_viz_col1, pred_viz_col2 = st.columns([1, 1])
    with pred_viz_col1:
        st.markdown("#### Centroid Distance & Proximity Metrics")
        fig_diag = plot_prediction_diagnostics(distances, proximities, pred_species)
        st.pyplot(fig_diag, use_container_width=True)

    with pred_viz_col2:
        st.markdown("#### Query Space Projection vs. Clusters")
        fig_proj = plot_query_point_projection(
            df_raw,
            query_vector,
            baseline_centroids,
            pred_species,
            x_col="petal_length",
            y_col="petal_width",
        )
        st.pyplot(fig_proj, use_container_width=True)

    # Detailed Numerical Breakdown
    with st.expander("📐 Mathematical Distance Breakdown & Coordinate Vectors"):
        st.write(rf"**Query Vector $\mathbf{{x}}$:** `[SL={in_sl}, SW={in_sw}, PL={in_pl}, PW={in_pw}]`")
        
        detail_data = []
        for sp in ["Setosa", "Versicolor", "Virginica"]:
            c_vec = baseline_centroids[sp]
            coord_str = f"[{c_vec[0]:.2f}, {c_vec[1]:.2f}, {c_vec[2]:.2f}, {c_vec[3]:.2f}]"
            detail_data.append({
                "Species Class": sp,
                r"Centroid Vector $\mathbf{\mu}_k$": coord_str,
                r"Euclidean Distance $\|\mathbf{x} - \mathbf{\mu}_k\|_2$": f"{distances[sp]:.4f} cm",
                "Softmax Proximity Score": f"{proximities[sp]:.2f}%",
                "Winner": "🏆 Closest" if sp == pred_species else "-",
            })
        st.dataframe(pd.DataFrame(detail_data), use_container_width=True, hide_index=True)


# ------------------------------------------------------------------------------
# Footer
# ------------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #64748b; font-size: 0.82rem; padding: 1rem 0;">
        <strong>CSE Mini-Project:</strong> Multidimensional Exploratory Data Analysis of the Iris Dataset<br>
        Developed with Streamlit, NumPy, Pandas, and Matplotlib • Department of Computer Science & Engineering
    </div>
    """,
    unsafe_allow_html=True,
)
