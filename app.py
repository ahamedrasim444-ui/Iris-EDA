"""
app.py
Multidimensional Exploratory Data Analysis of the Iris Dataset
Utilizing NumPy, Pandas, Matplotlib, and SQLite Database.

CSE Mini-Project Dashboard
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
    plot_covariance_heatmap,
    plot_correlation_heatmap,
    plot_bivariate_scatter,
    plot_boxplot_dispersion,
    plot_distributions_grid,
    plot_prediction_diagnostics,
    plot_query_point_projection,
)
from styles import get_custom_css, render_hero_banner, render_easter_egg_card


# ------------------------------------------------------------------------------
# Page Configuration & Theme
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Iris EDA & Multidimensional Analytics | CSE Mini-Project",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize SQLite Database
database.init_db()


# ------------------------------------------------------------------------------
# Session State Initialization
# ------------------------------------------------------------------------------
if "antigravity_active" not in st.session_state:
    st.session_state.antigravity_active = False

def set_classifier_preset(sl: float, sw: float, pl: float, pw: float):
    st.session_state["slider_sl"] = float(sl)
    st.session_state["slider_sw"] = float(sw)
    st.session_state["slider_pl"] = float(pl)
    st.session_state["slider_pw"] = float(pw)

if "slider_sl" not in st.session_state:
    st.session_state["slider_sl"] = 5.8
if "slider_sw" not in st.session_state:
    st.session_state["slider_sw"] = 3.0
if "slider_pl" not in st.session_state:
    st.session_state["slider_pl"] = 4.2
if "slider_pw" not in st.session_state:
    st.session_state["slider_pw"] = 1.3


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
    st.caption("**Course:** Data Science & Multidimensional Analytics")
    
    # Team Credentials Card
    with st.expander("👥 Team Members & Faculty Guide", expanded=True):
        st.markdown(
            """
            <div class="sidebar-card">
                <div class="team-member-item">
                    <span class="team-member-name">1. Balaji (Team Lead)</span>
                    <span class="team-member-role">Project Lead</span>
                </div>
                <div class="team-member-item">
                    <span class="team-member-name">2. Ahamed Rasim</span>
                    <span class="team-member-role">Data & Pandas</span>
                </div>
                <div class="team-member-item">
                    <span class="team-member-name">3. Kishore Kumar</span>
                    <span class="team-member-role">NumPy Engine</span>
                </div>
                <div class="team-member-item">
                    <span class="team-member-name">4. Aadthiyan</span>
                    <span class="team-member-role">Visual Analytics</span>
                </div>
                <div style="margin-top: 10px; padding-top: 8px; border-top: 1px solid #e2e8f0; font-size: 0.83rem;">
                    <strong>Faculty Guide:</strong><br>
                    Prof. Keerthana<br>
                    <em>Department of Computer Science & Engineering</em>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### 🔍 Global Slicing Filters")

    # Species Multi-select
    all_species = sorted(df_raw["species"].unique().tolist())
    selected_species = st.multiselect(
        "Filter by Botanical Species:",
        options=all_species,
        default=all_species,
        help="Select one or more Iris classes to focus the statistical analysis.",
    )

    if not selected_species:
        st.warning("Please choose at least one species.")
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
    
    # Python Antigravity Easter Egg Section
    st.markdown("### 🚀 Python Easter Egg")
    btn_label = "Disable Antigravity" if st.session_state.antigravity_active else "Trigger 'import antigravity'"
    if st.button(btn_label, use_container_width=True):
        st.session_state.antigravity_active = not st.session_state.antigravity_active
        st.rerun()

    if st.session_state.antigravity_active:
        st.info("Launched XKCD #353 in your session! 'I wrote 20 short programs in Python... now I am flying!'")


# Inject Neat Custom CSS
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
db_stats = database.get_prediction_stats()
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Active Instances",
        value=f"{len(df_filtered)} Samples",
        delta=f"{len(df_filtered)} / {len(df_raw)} visible",
    )
with col2:
    st.metric(
        label="Morphological Features",
        value="4 Primary + 4 Derived",
        delta="8 Total Dimensions",
    )
with col3:
    active_classes = df_filtered["species"].nunique() if not df_filtered.empty else 0
    st.metric(
        label="Active Classes",
        value=f"{active_classes} Species",
        delta="Setosa / Versi / Virg",
    )
with col4:
    st.metric(
        label="SQLite Database Logs",
        value=f"{db_stats['total_records']} Records",
        delta="🟢 Connected & Persistent",
    )

st.write("")


# ------------------------------------------------------------------------------
# Main Content Tabs
# ------------------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Tab 1: Dataset & Pandas Profiling",
    "🧮 Tab 2: NumPy Mathematical Engine",
    "📈 Tab 3: Matplotlib Visual Suite",
    "🎯 Tab 4: Interactive Classifier & Database Logger",
])


# ==============================================================================
# TAB 1: DATASET & PANDAS PROFILING
# ==============================================================================
with tab1:
    st.subheader("Dataset Overview & Engineered Ratios")
    st.markdown(
        """
        <div class="explain-box">
            <strong>What this tab shows:</strong> The raw botanical records alongside two engineered features: 
            <strong>Petal Aspect Ratio</strong> (Petal Length ÷ Petal Width) and <strong>Petal Area Proxy</strong> (Length × Width).
            These ratios make it easy to see the physical shape differences between flower types.
        </div>
        """,
        unsafe_allow_html=True,
    )

    t1_col1, t1_col2 = st.columns([3, 1])
    with t1_col1:
        search_kw = st.text_input("🔍 Quick Search (filter by any value or text):", "")
    with t1_col2:
        st.write("")
        st.write("")
        csv_data = df_filtered.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Export Filtered CSV",
            data=csv_data,
            file_name="iris_filtered.csv",
            mime="text/csv",
            use_container_width=True,
        )

    # Display Data Table
    display_df = df_filtered.copy()
    if search_kw:
        mask = display_df.astype(str).apply(lambda row: row.str.contains(search_kw, case=False).any(), axis=1)
        display_df = display_df[mask]

    st.dataframe(
        display_df,
        use_container_width=True,
        height=260,
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
    st.subheader("Species-Stratified Statistical Summary (Pandas GroupBy)")
    
    numeric_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width", "petal_ratio", "petal_area_proxy"]
    valid_cols = [c for c in numeric_cols if c in df_filtered.columns]
    
    if not df_filtered.empty:
        agg_summary = df_filtered.groupby("species")[valid_cols].agg(["mean", "std", "min", "max"]).round(3)
        st.dataframe(agg_summary, use_container_width=True)
    else:
        st.warning("No data rows available with current filter constraints.")

    st.markdown("---")
    st.subheader("🗄️ Connected SQLite Database: Live Query Logs")
    st.markdown(
        """
        <div class="explain-box">
            Every classification query performed in <strong>Tab 4</strong> can be saved into the SQLite database file 
            (<code>data/predictions.db</code>). Here are the most recent logged queries:
        </div>
        """,
        unsafe_allow_html=True,
    )

    recent_db_df = database.get_recent_predictions(limit=10)
    if not recent_db_df.empty:
        st.dataframe(recent_db_df, use_container_width=True, hide_index=True)
        if st.button("🗑️ Clear Database History"):
            database.clear_prediction_history()
            st.success("Database logs cleared.")
            st.rerun()
    else:
        st.info("No queries saved yet. Open Tab 4 to test a sample and click 'Save Prediction to Database'!")


# ==============================================================================
# TAB 2: NUMPY MATHEMATICAL ENGINE
# ==============================================================================
with tab2:
    st.subheader("Matrix Operations & Covariance Tensor (NumPy)")
    st.markdown(
        r"""
        <div class="explain-box">
            <strong>Understanding the Linear Algebra in Plain English:</strong>
            <ul style="margin: 0.35rem 0 0 1.25rem; padding: 0;">
                <li><strong>Sample Mean Vector ($\mathbf{\mu}$):</strong> The simple average measurement for each of the 4 dimensions.</li>
                <li><strong>Covariance Matrix ($\mathbf{\Sigma}$):</strong> Tells us whether two features grow together. A positive number means as one feature increases, the other tends to increase as well.</li>
                <li><strong>Pearson Correlation Matrix ($\mathbf{R}$):</strong> Scales covariance between -1.0 and +1.0 so we can immediately compare strength of relationships.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if len(df_filtered) < 2:
        st.warning("Covariance calculation requires at least 2 samples. Please broaden your sidebar filters.")
    else:
        manual_cov, np_cov = compute_covariance_matrix_manual(df_filtered, FEATURE_COLS)
        manual_corr, np_corr = compute_correlation_matrix_manual(df_filtered, FEATURE_COLS)

        col_n1, col_n2 = st.columns(2)
        with col_n1:
            st.markdown("#### Sample Mean Vector $\mathbf{\mu}$ (NumPy):")
            mean_vector = np.mean(df_filtered[FEATURE_COLS].to_numpy(), axis=0)
            mean_df = pd.DataFrame(
                mean_vector.reshape(1, 4), 
                columns=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
            )
            st.dataframe(mean_df.round(3), use_container_width=True, hide_index=True)

            st.markdown("#### $4 \\times 4$ Sample Covariance Matrix $\mathbf{\Sigma}$:")
            cov_df = pd.DataFrame(
                manual_cov,
                index=["Sepal L", "Sepal W", "Petal L", "Petal W"],
                columns=["Sepal L", "Sepal W", "Petal L", "Petal W"],
            )
            st.dataframe(cov_df.round(4), use_container_width=True)

        with col_n2:
            st.markdown("#### $4 \\times 4$ Pearson Correlation Matrix $\mathbf{R}$:")
            corr_df = pd.DataFrame(
                manual_corr,
                index=["Sepal L", "Sepal W", "Petal L", "Petal W"],
                columns=["Sepal L", "Sepal W", "Petal L", "Petal W"],
            )
            st.dataframe(corr_df.round(3), use_container_width=True)
            
            # Key Finding Callout
            st.info(
                "💡 **Key Finding:** Petal Length and Petal Width exhibit an exceptional Pearson correlation of "
                "**r ≈ 0.96**. This proves that longer petals almost always have wider petals."
            )

        st.markdown("---")
        st.subheader("Annotated Correlation & Covariance Heatmaps")
        h_col1, h_col2 = st.columns(2)
        with h_col1:
            fig_cov = plot_covariance_heatmap(manual_cov, FEATURE_COLS)
            st.pyplot(fig_cov, use_container_width=True)
        with h_col2:
            fig_corr = plot_correlation_heatmap(manual_corr, FEATURE_COLS)
            st.pyplot(fig_corr, use_container_width=True)

        st.markdown("---")
        st.subheader("Principal Eigen-Decomposition & Variance Explained")
        eigen_res = compute_eigen_decomposition(manual_cov)
        
        eigen_df = pd.DataFrame({
            "Principal Component": ["PC1", "PC2", "PC3", "PC4"],
            "Eigenvalue (λ)": eigen_res["eigenvalues"],
            "Variance Explained (%)": eigen_res["variance_explained_pct"],
            "Cumulative Variance (%)": eigen_res["cumulative_variance_pct"],
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
            f"**Takeaway:** The first principal component alone captures "
            f"**{eigen_res['variance_explained_pct'][0]:.1f}%** of the total variance across all 4 flower measurements."
        )


# ==============================================================================
# TAB 3: MATPLOTLIB VISUAL SUITE
# ==============================================================================
with tab3:
    st.subheader("Publication-Grade Visual Analytics (Matplotlib)")
    st.markdown(
        """
        <div class="explain-box">
            <strong>What to look for:</strong> In Figure 1, notice the dashed crimson line at <strong>2.45 cm</strong>. 
            Any flower with a petal length shorter than 2.45 cm is guaranteed to be an <strong>Iris Setosa</strong>! 
            This makes Setosa 100% linearly separable from the other two species.
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.markdown("#### Figure 1: Bivariate Scatter & Setosa Boundary")
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
        else:
            st.write("No data available.")

    with col_v2:
        st.markdown("#### Figure 2: Boxplot Dispersion Across Species")
        box_feat = st.selectbox(
            "Select Feature to Compare:",
            options=FEATURE_COLS,
            index=2,
            format_func=lambda x: FEATURE_LABELS.get(x, x),
            key="box_feat_sel",
        )
        if not df_filtered.empty:
            fig_box = plot_boxplot_dispersion(df_filtered, feature_col=box_feat, selected_species=selected_species)
            st.pyplot(fig_box, use_container_width=True)
        else:
            st.write("No data available.")

    st.markdown("---")
    st.subheader("Figure 3: 4-Panel Multi-Attribute Distribution Histograms")
    st.caption("Dashed vertical lines show the mean value for each species:")
    if not df_filtered.empty:
        fig_hist = plot_distributions_grid(df_filtered)
        st.pyplot(fig_hist, use_container_width=True)


# ==============================================================================
# TAB 4: INTERACTIVE CLASSIFIER & DATABASE LOGGER
# ==============================================================================
with tab4:
    st.subheader("Live Nearest-Centroid Classifier (NumPy Distance Vector)")
    st.markdown(
        r"""
        <div class="explain-box">
            <strong>How this works:</strong>
            We compute the mathematical center (centroid $\mathbf{\mu}_c$) for each flower species. 
            When you adjust the sliders below, NumPy computes the straight-line Euclidean distance:
            $$\|\mathbf{x} - \mathbf{\mu}_c\|_2 = \sqrt{\sum_{j=1}^4 (x_j - \mu_{c,j})^2}$$
            The flower class with the shortest distance to your input is assigned as the live prediction.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Preset Quick Buttons
    st.markdown("**Quick Preset Profiles (Click to Auto-Fill Values):**")
    p_col1, p_col2, p_col3, p_col4 = st.columns(4)
    with p_col1:
        st.button("🌸 Typical Setosa", on_click=set_classifier_preset, args=(5.0, 3.4, 1.5, 0.2), use_container_width=True)
    with p_col2:
        st.button("🌿 Typical Versicolor", on_click=set_classifier_preset, args=(5.9, 2.8, 4.3, 1.3), use_container_width=True)
    with p_col3:
        st.button("🌺 Typical Virginica", on_click=set_classifier_preset, args=(6.6, 3.0, 5.6, 2.0), use_container_width=True)
    with p_col4:
        st.button("🔄 Reset Default", on_click=set_classifier_preset, args=(5.8, 3.0, 4.2, 1.3), use_container_width=True)

    # 4 Clean Columns for Sliders (from user's snippet layout)
    st.markdown("#### Adjust Morphological Parameters:")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        in_sl = st.slider("Sepal Length (cm)", 4.0, 8.0, float(st.session_state["slider_sl"]), 0.1, key="slider_sl")
    with c2:
        in_sw = st.slider("Sepal Width (cm)", 2.0, 4.5, float(st.session_state["slider_sw"]), 0.1, key="slider_sw")
    with c3:
        in_pl = st.slider("Petal Length (cm)", 1.0, 7.0, float(st.session_state["slider_pl"]), 0.1, key="slider_pl")
    with c4:
        in_pw = st.slider("Petal Width (cm)", 0.1, 2.6, float(st.session_state["slider_pw"]), 0.1, key="slider_pw")

    # Construct Input Point Vector
    input_point = np.array([in_sl, in_sw, in_pl, in_pw], dtype=float)

    # Baseline Centroids
    baseline_centroids = compute_species_centroids(df_raw, FEATURE_COLS)
    prediction_result = predict_nearest_centroid(input_point, baseline_centroids)

    pred_species = prediction_result["predicted_species"]
    min_dist = prediction_result["min_distance"]
    distances = prediction_result["distances"]
    proximities = prediction_result["proximity_pct"]

    st.markdown("---")
    
    # Results Presentation
    res_col1, res_col2 = st.columns([1, 1])
    with res_col1:
        st.success(f"### Predicted Species: **Iris {pred_species}**")
        st.write(f"**Shortest Euclidean Distance:** `{min_dist:.4f} cm`")
        st.write(f"**Softmax Confidence Score:** `{proximities[pred_species]:.1f}%`")
        
        # Save to Database Button
        if st.button("💾 Save Prediction to SQLite Database", type="primary", use_container_width=True):
            new_id = database.log_prediction(
                sepal_length=in_sl,
                sepal_width=in_sw,
                petal_length=in_pl,
                petal_width=in_pw,
                predicted_species=pred_species,
                confidence_pct=round(proximities[pred_species], 1),
                distance_cm=round(min_dist, 4),
            )
            st.toast(f"✅ Prediction #{new_id} saved to database!", icon="💾")

    with res_col2:
        dist_df = pd.DataFrame([
            {"Species": sp, "Euclidean Distance (cm)": f"{distances[sp]:.4f}", "Confidence Match (%)": f"{proximities[sp]:.1f}%"}
            for sp in ["Setosa", "Versicolor", "Virginica"]
        ])
        st.dataframe(dist_df, use_container_width=True, hide_index=True)

    # Visual Distance Diagnostics & 2D Projection
    st.markdown("---")
    diag_c1, diag_c2 = st.columns(2)
    with diag_c1:
        st.markdown("#### Distance & Confidence Bar Charts")
        fig_diag = plot_prediction_diagnostics(distances, proximities, pred_species)
        st.pyplot(fig_diag, use_container_width=True)

    with diag_c2:
        st.markdown("#### Live Query Point Space Projection")
        fig_proj = plot_query_point_projection(
            df_raw,
            input_point,
            baseline_centroids,
            pred_species,
            x_col="petal_length",
            y_col="petal_width",
        )
        st.pyplot(fig_proj, use_container_width=True)

    # Step-by-Step Math Breakdown
    with st.expander("📐 Step-by-Step Distance Calculation Breakdown"):
        st.write(rf"**Your Input Vector $\mathbf{{x}}$:** `[{in_sl:.2f}, {in_sw:.2f}, {in_pl:.2f}, {in_pw:.2f}]`")
        math_records = []
        for sp in ["Setosa", "Versicolor", "Virginica"]:
            c_vec = baseline_centroids[sp]
            diff = input_point - c_vec
            math_records.append({
                "Species Class": sp,
                r"Centroid $\mathbf{\mu}_c$": f"[{c_vec[0]:.2f}, {c_vec[1]:.2f}, {c_vec[2]:.2f}, {c_vec[3]:.2f}]",
                r"Difference $(\mathbf{x} - \mathbf{\mu}_c)$": f"[{diff[0]:+.2f}, {diff[1]:+.2f}, {diff[2]:+.2f}, {diff[3]:+.2f}]",
                "Euclidean Distance": f"{distances[sp]:.4f} cm",
                "Winner": "🏆 Closest" if sp == pred_species else "-",
            })
        st.dataframe(pd.DataFrame(math_records), use_container_width=True, hide_index=True)


# ------------------------------------------------------------------------------
# Footer
# ------------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #475569; font-size: 0.85rem; padding: 1.25rem 0; line-height: 1.6;">
        <strong>CSE Mini-Project:</strong> Multidimensional Exploratory Data Analysis of the Iris Dataset<br>
        <strong>Team Members:</strong> Balaji (Team Lead) • Ahamed Rasim • Kishore Kumar • Aadthiyan<br>
        <strong>Faculty Guide:</strong> Prof. Keerthana • Department of Computer Science & Engineering<br>
        <span style="color: #059669; font-weight: 600;">Connected Database: SQLite (data/predictions.db)</span>
    </div>
    """,
    unsafe_allow_html=True,
)
