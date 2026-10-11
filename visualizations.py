"""
visualizations.py
Sneat – Vuetify Vuejs 3 Dark Theme Publication-Ready Matplotlib Visualizations.
Renders annotated heatmaps, bivariate cluster scatter plots with convex hulls & centroids,
4-panel distribution histograms, live prediction diagnostics, and interactive flower morphometry.
"""

from typing import Dict, List, Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.ticker as ticker

from data_engine import FEATURE_LABELS, SPECIES_COLORS


# Configure Sneat Vuetify Dark Theme matplotlib styling
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Public Sans", "Segoe UI", "DejaVu Sans", "Helvetica", "Arial"],
    "axes.edgecolor": "#44476a",
    "axes.linewidth": 1.2,
    "grid.color": "#3b3e5b",
    "grid.linestyle": "--",
    "grid.alpha": 0.65,
    "xtick.color": "#b2b3ca",
    "ytick.color": "#b2b3ca",
    "figure.facecolor": "#2b2c40",
    "axes.facecolor": "#2b2c40",
    "axes.labelcolor": "#b2b3ca",
    "axes.titlecolor": "#e1def5",
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
})


def _compute_convex_hull_2d(points: np.ndarray) -> np.ndarray:
    """Andrew's monotone chain 2D convex hull algorithm in pure NumPy."""
    points = np.unique(points, axis=0)
    if len(points) <= 2:
        return points
    # Sort lexicographically
    points = points[np.lexsort((points[:, 1], points[:, 0]))]
    
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return np.array(lower[:-1] + upper[:-1])


def plot_covariance_heatmap(cov_matrix: np.ndarray, feature_names: List[str]) -> plt.Figure:
    """Renders annotated 4x4 sample covariance matrix heatmap in Sneat Dark style."""
    fig, ax = plt.subplots(figsize=(6.5, 5.2), dpi=160, facecolor="#2b2c40")
    ax.set_facecolor("#2b2c40")
    
    labels = [FEATURE_LABELS.get(f, f).replace(" (cm)", "") for f in feature_names]
    
    im = ax.imshow(cov_matrix, cmap="Purples", interpolation="nearest")
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.ax.tick_params(labelsize=9, colors="#b2b3ca")
    cbar.set_label("Covariance Value ($cm^2$)", fontsize=9, fontweight="bold", labelpad=8, color="#e1def5")
    
    # Tick marks
    n = len(feature_names)
    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(n))
    ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=9, fontweight="bold", color="#e1def5")
    ax.set_yticklabels(labels, fontsize=9, fontweight="bold", color="#e1def5")
    
    # Annotations with adaptive contrast
    threshold = (cov_matrix.max() + cov_matrix.min()) / 2.0
    for i in range(n):
        for j in range(n):
            val = cov_matrix[i, j]
            text_color = "#ffffff" if val > threshold else "#e1def5"
            ax.text(j, i, f"{val:.3f}", ha="center", va="center",
                    color=text_color, fontsize=10, fontweight="bold")
            
    ax.set_title(r"Sample Covariance Tensor $\mathbf{\Sigma} \in \mathbb{R}^{4 \times 4}$", 
                 pad=14, fontsize=11, fontweight="bold", color="#e1def5")
    ax.grid(False)
    fig.tight_layout()
    return fig


def plot_correlation_heatmap(corr_matrix: np.ndarray, feature_names: List[str]) -> plt.Figure:
    """Renders Pearson correlation matrix heatmap with diverging palette in Sneat Dark style."""
    fig, ax = plt.subplots(figsize=(6.5, 5.2), dpi=160, facecolor="#2b2c40")
    ax.set_facecolor("#2b2c40")
    
    labels = [FEATURE_LABELS.get(f, f).replace(" (cm)", "") for f in feature_names]
    
    im = ax.imshow(corr_matrix, cmap="coolwarm", vmin=-1.0, vmax=1.0, interpolation="nearest")
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.ax.tick_params(labelsize=9, colors="#b2b3ca")
    cbar.set_label("Pearson Correlation $r$", fontsize=9, fontweight="bold", labelpad=8, color="#e1def5")
    
    n = len(feature_names)
    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(n))
    ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=9, fontweight="bold", color="#e1def5")
    ax.set_yticklabels(labels, fontsize=9, fontweight="bold", color="#e1def5")
    
    for i in range(n):
        for j in range(n):
            val = corr_matrix[i, j]
            text_color = "#ffffff" if abs(val) > 0.45 else "#232333"
            ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                    color=text_color, fontsize=10, fontweight="bold")
            
    ax.set_title(r"Pearson Correlation Matrix $\mathbf{R} \in [-1, 1]^{4 \times 4}$", 
                 pad=14, fontsize=11, fontweight="bold", color="#e1def5")
    ax.grid(False)
    fig.tight_layout()
    return fig


def plot_bivariate_scatter(
    df: pd.DataFrame,
    x_col: str = "petal_length",
    y_col: str = "petal_width",
    centroids: Optional[Dict[str, np.ndarray]] = None,
    show_centroids: bool = True,
    show_hulls: bool = True,
) -> plt.Figure:
    """
    Renders high-resolution bivariate scatter plot with species color coding,
    convex hull decision envelopes, and centroid star markers in Sneat Dark style.
    """
    fig, ax = plt.subplots(figsize=(8.5, 5.6), dpi=160, facecolor="#2b2c40")
    ax.set_facecolor("#2b2c40")
    
    species_order = ["Setosa", "Versicolor", "Virginica"]
    
    for sp in species_order:
        sub = df[df["species"] == sp]
        if sub.empty:
            continue
            
        color = SPECIES_COLORS.get(sp, "#696cff")
        x_vals = sub[x_col].to_numpy()
        y_vals = sub[y_col].to_numpy()
        
        # 1. Scatter points
        ax.scatter(
            x_vals, y_vals,
            c=color, label=f"{sp} (n={len(sub)})",
            alpha=0.85, edgecolors="#ffffff", linewidth=0.8, s=64, zorder=3
        )
        
        # 2. Convex Hull Envelope
        if show_hulls and len(sub) >= 3:
            pts = np.column_stack([x_vals, y_vals])
            hull_pts = _compute_convex_hull_2d(pts)
            if len(hull_pts) >= 3:
                poly = Polygon(hull_pts, closed=True, facecolor=color, alpha=0.18,
                               edgecolor=color, linestyle="--", linewidth=1.5, zorder=2)
                ax.add_patch(poly)
                
        # 3. Centroid Marker
        if show_centroids and centroids and sp in centroids:
            feature_keys = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
            xi = feature_keys.index(x_col)
            yi = feature_keys.index(y_col)
            cx, cy = centroids[sp][xi], centroids[sp][yi]
            ax.scatter(
                cx, cy,
                marker="*", s=260, c=color,
                edgecolors="#ffffff", linewidth=1.8,
                label=f"{sp} Centroid" if not show_hulls else None,
                zorder=5
            )
            # Annotate centroid text
            ax.annotate(
                f"$\\mu_{{{sp[:3].lower()}}}$",
                (cx, cy), textcoords="offset points", xytext=(8, 8),
                fontsize=9, fontweight="bold", color=color,
                bbox=dict(boxstyle="round,pad=0.2", fc="#232333", ec=color, alpha=0.9, lw=0.8)
            )

    # Setosa linear boundary cutoff (at Petal Length = 2.45 cm)
    if x_col == "petal_length":
        ax.axvline(x=2.45, color="#ff3e1d", linestyle="--", linewidth=1.6, label="Setosa Linear Boundary (< 2.45 cm)")

    x_label = FEATURE_LABELS.get(x_col, x_col.replace("_", " ").title())
    y_label = FEATURE_LABELS.get(y_col, y_col.replace("_", " ").title())
    
    ax.set_xlabel(x_label, fontsize=10, fontweight="bold", labelpad=8, color="#e1def5")
    ax.set_ylabel(y_label, fontsize=10, fontweight="bold", labelpad=8, color="#e1def5")
    ax.set_title(f"Bivariate Space: {x_label} vs. {y_label}", pad=12, fontsize=11, fontweight="bold", color="#e1def5")
    ax.legend(frameon=True, facecolor="#2b2c40", edgecolor="#44476a", labelcolor="#e1def5", fontsize=8.5, loc="best")
    ax.grid(True, linestyle=":", alpha=0.6)
    
    fig.tight_layout()
    return fig


def plot_boxplot_dispersion(
    df: pd.DataFrame,
    feature_col: str = "petal_length",
    selected_species: Optional[List[str]] = None,
    feature: Optional[str] = None,
) -> plt.Figure:
    """Renders clean boxplot showing feature dispersion across species in Sneat Dark style."""
    if feature is not None:
        feature_col = feature
    fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=150, facecolor="#2b2c40")
    ax.set_facecolor("#2b2c40")
    
    if selected_species is None:
        selected_species = ["Setosa", "Versicolor", "Virginica"]
        
    box_data = []
    labels = []
    colors_list = []
    
    for sp in selected_species:
        sub = df[df["species"] == sp]
        if not sub.empty:
            box_data.append(sub[feature_col].to_numpy())
            labels.append(sp)
            colors_list.append(SPECIES_COLORS.get(sp, "#696cff"))
            
    if box_data:
        bp = ax.boxplot(
            box_data, tick_labels=labels, patch_artist=True,
            medianprops=dict(color="#ffffff", linewidth=2.2),
            boxprops=dict(linewidth=1.2),
            whiskerprops=dict(linewidth=1.2, color="#b2b3ca"),
            capprops=dict(linewidth=1.2, color="#b2b3ca"),
            flierprops=dict(marker='o', markersize=5, markerfacecolor='#ff3e1d', markeredgecolor='none')
        )
        for patch, col in zip(bp['boxes'], colors_list):
            patch.set_facecolor(col)
            patch.set_alpha(0.55)
            patch.set_edgecolor(col)
            
    feat_title = FEATURE_LABELS.get(feature_col, feature_col.replace("_", " ").title())
    ax.set_title(f"Dispersion Across Species: {feat_title}", fontsize=11, fontweight="bold", pad=10, color="#e1def5")
    ax.set_ylabel(f"{feat_title}", fontsize=9.5, fontweight="bold", color="#e1def5")
    ax.tick_params(colors="#e1def5")
    ax.grid(True, linestyle=":", alpha=0.6)
    fig.tight_layout()
    return fig


def plot_distributions_grid(
    df: pd.DataFrame,
    feature_cols: Optional[List[str]] = None,
) -> plt.Figure:
    """
    Renders 4-panel (2x2 grid) distribution histograms with mean markers in Sneat Dark style.
    """
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 7.5), dpi=160, facecolor="#2b2c40")
    axes = axes.flatten()
    
    features = feature_cols if feature_cols is not None else ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    species_order = ["Setosa", "Versicolor", "Virginica"]
    
    for idx, feat in enumerate(features):
        ax = axes[idx]
        ax.set_facecolor("#2b2c40")
        f_label = FEATURE_LABELS.get(feat, feat)
        
        for sp in species_order:
            sub = df[df["species"] == sp]
            if sub.empty:
                continue
            color = SPECIES_COLORS.get(sp, "#696cff")
            vals = sub[feat].to_numpy()
            
            # Histogram
            ax.hist(
                vals, bins=12, alpha=0.55, color=color,
                label=sp if idx == 0 else None,
                edgecolor=color, linewidth=1.2
            )
            
            # Species Mean Line
            mean_v = np.mean(vals)
            ax.axvline(mean_v, color=color, linestyle="--", linewidth=1.5, alpha=0.9)
            
        ax.set_title(f_label, fontsize=10, fontweight="bold", pad=8, color="#e1def5")
        ax.set_xlabel("Measurement (cm)", fontsize=8.5, color="#b2b3ca")
        ax.set_ylabel("Frequency", fontsize=8.5, color="#b2b3ca")
        ax.tick_params(colors="#b2b3ca")
        ax.grid(True, linestyle=":", alpha=0.5)
        
    # Global legend on top
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, 0.99),
               ncol=3, frameon=True, facecolor="#2b2c40", edgecolor="#44476a", labelcolor="#e1def5", fontsize=9)
    
    fig.suptitle("Multidimensional Feature Distribution Breakdown by Species", 
                 fontsize=12, fontweight="bold", y=1.02, color="#e1def5")
    fig.tight_layout()
    return fig


def plot_prediction_diagnostics(
    distances: Dict[str, float],
    proximity_pct: Dict[str, float],
    predicted_species: str,
) -> plt.Figure:
    """
    Renders live diagnostic horizontal bar charts in Sneat Dark style.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 3.2), dpi=160, facecolor="#2b2c40")
    ax1.set_facecolor("#2b2c40")
    ax2.set_facecolor("#2b2c40")
    
    species = list(distances.keys())
    dist_vals = [distances[s] for s in species]
    prox_vals = [proximity_pct[s] for s in species]
    colors = [SPECIES_COLORS.get(s, "#696cff") for s in species]
    
    y_pos = np.arange(len(species))
    
    # 1. Euclidean Distances (Lower is better)
    bars1 = ax1.barh(y_pos, dist_vals, color=colors, alpha=0.85, edgecolor="#ffffff", linewidth=0.8)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(species, fontweight="bold", fontsize=9, color="#e1def5")
    ax1.set_xlabel(r"Euclidean Distance $\|\mathbf{x} - \mathbf{\mu}_k\|_2$ (cm)", fontsize=8.5, fontweight="bold", color="#b2b3ca")
    ax1.set_title("Distance to Centroid (cm)", fontsize=10, fontweight="bold", pad=8, color="#e1def5")
    ax1.invert_yaxis()
    ax1.grid(True, axis="x", linestyle=":", alpha=0.6)
    
    for bar in bars1:
        w = bar.get_width()
        ax1.text(w + 0.05, bar.get_y() + bar.get_height() / 2, f"{w:.2f} cm",
                 va="center", fontsize=8.5, fontweight="bold", color="#e1def5")
        
    # 2. Proximity Confidence % (Higher is better)
    bars2 = ax2.barh(y_pos, prox_vals, color=colors, alpha=0.85, edgecolor="#ffffff", linewidth=0.8)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([])
    ax2.set_xlabel("Proximity Confidence (%)", fontsize=8.5, fontweight="bold", color="#b2b3ca")
    ax2.set_title("Softmax Confidence Score", fontsize=10, fontweight="bold", pad=8, color="#e1def5")
    ax2.set_xlim(0, 105)
    ax2.invert_yaxis()
    ax2.grid(True, axis="x", linestyle=":", alpha=0.6)
    
    for bar in bars2:
        w = bar.get_width()
        ax2.text(w + 1.5, bar.get_y() + bar.get_height() / 2, f"{w:.1f}%",
                 va="center", fontsize=8.5, fontweight="bold", color="#e1def5")
        
    fig.tight_layout()
    return fig


def plot_query_point_projection(
    df: pd.DataFrame,
    query_vector: np.ndarray,
    centroids: Dict[str, np.ndarray],
    predicted_species: str,
    x_col: str = "petal_length",
    y_col: str = "petal_width",
) -> plt.Figure:
    """
    Renders 2D projection scatter plot showing the live test observation
    in relation to class clusters and centroids in Sneat Dark style.
    """
    fig, ax = plt.subplots(figsize=(7.5, 4.8), dpi=160, facecolor="#2b2c40")
    ax.set_facecolor("#2b2c40")
    
    feature_keys = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    xi = feature_keys.index(x_col)
    yi = feature_keys.index(y_col)
    
    for sp in ["Setosa", "Versicolor", "Virginica"]:
        sub = df[df["species"] == sp]
        if sub.empty:
            continue
        color = SPECIES_COLORS.get(sp, "#696cff")
        ax.scatter(sub[x_col], sub[y_col], c=color, alpha=0.45, s=40, edgecolors="none")
        
        # Centroid
        if sp in centroids:
            cx, cy = centroids[sp][xi], centroids[sp][yi]
            ax.scatter(cx, cy, marker="*", s=180, c=color, edgecolors="#ffffff", lw=1.2)
            
    # Highlight User's Query Vector
    qx, qy = query_vector[xi], query_vector[yi]
    pred_color = SPECIES_COLORS.get(predicted_species, "#696cff")
    
    # Pulsing outer ring + diamond
    ax.scatter(qx, qy, s=260, facecolors="none", edgecolors=pred_color, linewidth=2.5, linestyle="--", zorder=6)
    ax.scatter(qx, qy, marker="D", s=130, c="#ffab00", edgecolors="#ffffff", linewidth=1.5, 
               label=f"Query Point ({qx:.1f}, {qy:.1f})", zorder=7)
    
    # Line connecting query point to the closest centroid
    cx, cy = centroids[predicted_species][xi], centroids[predicted_species][yi]
    ax.plot([qx, cx], [qy, cy], color=pred_color, linestyle=":", linewidth=2, 
            label=f"Nearest -> {predicted_species}", zorder=5)
    
    x_label = FEATURE_LABELS.get(x_col, x_col)
    y_label = FEATURE_LABELS.get(y_col, y_col)
    ax.set_xlabel(x_label, fontsize=9.5, fontweight="bold", color="#e1def5")
    ax.set_ylabel(y_label, fontsize=9.5, fontweight="bold", color="#e1def5")
    ax.set_title(f"Live Query Point Space Projection ({x_label} vs. {y_label})", 
                 fontsize=10.5, fontweight="bold", pad=10, color="#e1def5")
    ax.legend(frameon=True, facecolor="#2b2c40", edgecolor="#44476a", labelcolor="#e1def5", fontsize=8.5, loc="best")
    ax.grid(True, linestyle=":", alpha=0.5)
    
    fig.tight_layout()
    return fig


def plot_interactive_iris_flower(
    sepal_length: float,
    sepal_width: float,
    petal_length: float,
    petal_width: float,
    predicted_species: Optional[str] = None,
) -> plt.Figure:
    """
    Renders an anatomical, dynamically scaled Iris flower morphometry diagram in Sneat Dark style.
    The outer sepals and inner petals expand and reshape in real time according
    to the user's exact centimeter slider inputs.
    """
    fig, (ax_flower, ax_stats) = plt.subplots(1, 2, figsize=(11.5, 5.6), dpi=160, 
                                             gridspec_kw={"width_ratios": [1.15, 1.0]},
                                             facecolor="#2b2c40")
    ax_flower.set_facecolor("#2b2c40")
    ax_stats.set_facecolor("#2b2c40")
    
    # -------------------------------------------------------------------------
    # LEFT PANEL: DYNAMIC BOTANICAL FLOWER DIAGRAM
    # -------------------------------------------------------------------------
    ax_flower.set_xlim(-5.5, 5.5)
    ax_flower.set_ylim(-5.5, 6.5)
    ax_flower.set_aspect("equal")
    ax_flower.axis("off")
    ax_flower.set_title("Iris Flower Anatomical Scaling (Live Morphometry)", 
                        fontsize=11.5, fontweight="bold", pad=12, color="#e1def5")

    # 1. Stem and Base (Green Botanical Stem)
    stem_x = np.array([-0.18, 0.18, 0.14, -0.14])
    stem_y = np.array([-0.8, -0.8, -4.8, -4.8])
    ax_flower.fill(stem_x, stem_y, color="#22c55e", alpha=0.9, edgecolor="#15803d", linewidth=1.5, zorder=1)

    # Receptacle / Calyx Core
    calyx = Polygon([(-0.6, -0.8), (0.6, -0.8), (0.3, -1.4), (-0.3, -1.4)], closed=True,
                    facecolor="#16a34a", edgecolor="#15803d", linewidth=1.5, zorder=2)
    ax_flower.add_patch(calyx)

    # Scaling Factors based on live Centimeter inputs
    sl_scale = sepal_length * 0.70
    sw_scale = sepal_width * 0.75
    pl_scale = petal_length * 0.70
    pw_scale = petal_width * 0.85

    # 2. Outer Drooping Sepals ("Falls") - Left and Right
    theta = np.linspace(0, np.pi, 50)
    
    # Right Sepal (Falls)
    sep_r_x = 0.2 + sw_scale * 1.3 * np.sin(theta)
    sep_r_y = -0.8 - sl_scale * (1.0 - np.cos(theta * 0.5))
    ax_flower.fill(np.concatenate([[0.2], sep_r_x, [0.1]]), 
                   np.concatenate([[-0.8], sep_r_y, [-0.8]]), 
                   color="#696cff", alpha=0.88, edgecolor="#787bff", linewidth=1.8, zorder=3)
    # Golden Signal / Nectar Guide on Sepal
    ax_flower.fill(np.concatenate([[0.2], sep_r_x[:20] * 0.6, [0.2]]), 
                   np.concatenate([[-0.8], sep_r_y[:20] * 0.6, [-0.8]]), 
                   color="#ffab00", alpha=0.95, edgecolor="#ffffff", linewidth=1, zorder=4)

    # Left Sepal (Falls - Symmetrical)
    sep_l_x = -sep_r_x
    sep_l_y = sep_r_y
    ax_flower.fill(np.concatenate([[-0.2], sep_l_x, [-0.1]]), 
                   np.concatenate([[-0.8], sep_l_y, [-0.8]]), 
                   color="#696cff", alpha=0.88, edgecolor="#787bff", linewidth=1.8, zorder=3)
    # Golden Signal on Left Sepal
    ax_flower.fill(np.concatenate([[-0.2], sep_l_x[:20] * 0.6, [-0.2]]), 
                   np.concatenate([[-0.8], sep_l_y[:20] * 0.6, [-0.8]]), 
                   color="#ffab00", alpha=0.95, edgecolor="#ffffff", linewidth=1, zorder=4)

    # 3. Inner Upright Petals ("Standards") - Left, Center, Right
    pet_t = np.linspace(0, np.pi, 50)
    
    # Center Upright Petal
    pet_c_x = (pw_scale * 0.9) * np.sin(pet_t) - (pw_scale * 0.45)
    pet_c_y = -0.7 + pl_scale * np.sin(pet_t * 0.5 + 0.3)
    ax_flower.fill(pet_c_x, pet_c_y, color="#03c3ec", alpha=0.88, 
                   edgecolor="#26e7a6", linewidth=2.0, zorder=5)

    # Left Upright Petal
    pet_l_x = -0.3 - (pw_scale * 0.75) * np.sin(pet_t)
    pet_l_y = -0.7 + (pl_scale * 0.9) * np.sin(pet_t * 0.5)
    ax_flower.fill(pet_l_x, pet_l_y, color="#26e7a6", alpha=0.82, 
                   edgecolor="#71dd37", linewidth=1.5, zorder=4)

    # Right Upright Petal
    pet_r_x = 0.3 + (pw_scale * 0.75) * np.sin(pet_t)
    pet_r_y = -0.7 + (pl_scale * 0.9) * np.sin(pet_t * 0.5)
    ax_flower.fill(pet_r_x, pet_r_y, color="#26e7a6", alpha=0.82, 
                   edgecolor="#71dd37", linewidth=1.5, zorder=4)

    # Central Botanical Core / Style Arms
    ax_flower.scatter([0], [-0.7], s=140, c="#71dd37", edgecolors="#ffffff", linewidth=2.0, zorder=7)

    # Dimension Calipers and Anatomical Callout Brackets
    # Petal dimension callout (top right)
    top_petal_y = -0.7 + pl_scale
    ax_flower.annotate(
        f"PETALS (Standards)\nLength: {petal_length:.1f} cm\nWidth: {petal_width:.1f} cm",
        xy=(0.4, top_petal_y * 0.75), xytext=(2.6, 3.8),
        arrowprops=dict(arrowstyle="->", color="#03c3ec", lw=1.5),
        bbox=dict(boxstyle="round,pad=0.4", fc="#232333", ec="#03c3ec", lw=1.2),
        fontsize=8.5, fontweight="bold", color="#03c3ec"
    )

    # Sepal dimension callout (bottom right)
    bot_sepal_y = -0.8 - sl_scale * 0.8
    ax_flower.annotate(
        f"SEPALS (Falls)\nLength: {sepal_length:.1f} cm\nWidth: {sepal_width:.1f} cm",
        xy=(sep_r_x.max() * 0.75, bot_sepal_y), xytext=(2.4, -3.2),
        arrowprops=dict(arrowstyle="->", color="#787bff", lw=1.5),
        bbox=dict(boxstyle="round,pad=0.4", fc="#232333", ec="#696cff", lw=1.2),
        fontsize=8.5, fontweight="bold", color="#787bff"
    )

    # Anatomical Key Legend at bottom of left panel
    ax_flower.text(-5.0, -5.2, "• Petals (Cyan): Inner upright flower standards\n• Sepals (Purple): Outer drooping falls with nectar signal", 
                   fontsize=8, color="#b2b3ca", bbox=dict(boxstyle="round,pad=0.3", fc="#232333", ec="#44476a"))

    # -------------------------------------------------------------------------
    # RIGHT PANEL: SPECIES AVERAGE BENCHMARKS & MORPHOMETRIC RATIOS
    # -------------------------------------------------------------------------
    benchmarks = {
        "Iris Setosa": [5.01, 3.42, 1.46, 0.24],
        "Iris Versicolor": [5.94, 2.77, 4.26, 1.33],
        "Iris Virginica": [6.59, 2.97, 5.55, 2.03],
        "Your Flower": [sepal_length, sepal_width, petal_length, petal_width],
    }
    
    categories = ["Sepal L", "Sepal W", "Petal L", "Petal W"]
    y_pos = np.arange(len(categories))
    bar_height = 0.20

    # Draw grouped horizontal comparison bars
    ax_stats.barh(y_pos - 1.5 * bar_height, benchmarks["Iris Setosa"], height=bar_height, 
                  color="#3b3e5b", edgecolor="#696cff", label="Setosa Avg", alpha=0.85)
    ax_stats.barh(y_pos - 0.5 * bar_height, benchmarks["Iris Versicolor"], height=bar_height, 
                  color="#29435c", edgecolor="#03c3ec", label="Versicolor Avg", alpha=0.85)
    ax_stats.barh(y_pos + 0.5 * bar_height, benchmarks["Iris Virginica"], height=bar_height, 
                  color="#284d33", edgecolor="#71dd37", label="Virginica Avg", alpha=0.85)
    
    # Highlight User Flower in bold Sneat color
    user_color = SPECIES_COLORS.get(predicted_species, "#696cff") if predicted_species else "#696cff"
    user_bars = ax_stats.barh(y_pos + 1.5 * bar_height, benchmarks["Your Flower"], height=bar_height, 
                              color=user_color, edgecolor="#ffffff", linewidth=1.5, 
                              label="Your Input Flower", zorder=5)

    # Add numeric labels to user flower bars
    for bar in user_bars:
        w = bar.get_width()
        ax_stats.text(w + 0.15, bar.get_y() + bar.get_height() / 2, f"{w:.1f} cm",
                      va="center", fontsize=8.5, fontweight="bold", color="#ffffff")

    ax_stats.set_yticks(y_pos)
    ax_stats.set_yticklabels(categories, fontsize=9.5, fontweight="bold", color="#e1def5")
    ax_stats.set_xlabel("Measurement (Centimeters)", fontsize=9, fontweight="bold", color="#b2b3ca")
    ax_stats.set_xlim(0, 8.5)
    ax_stats.tick_params(colors="#b2b3ca")
    ax_stats.grid(True, axis="x", linestyle="--", alpha=0.6)
    
    # Title & Match banner
    match_str = f"Closest Match: {predicted_species}" if predicted_species else "Morphometric Benchmark"
    ax_stats.set_title(f"Comparison vs. Botanical Species Averages\n({match_str})", 
                       fontsize=10.5, fontweight="bold", pad=8, color="#e1def5")
    ax_stats.legend(frameon=True, facecolor="#2b2c40", edgecolor="#44476a", labelcolor="#e1def5", fontsize=8, loc="upper right")

    # Area & Ratio Summary Sub-Box
    sepal_area = sepal_length * sepal_width
    petal_area = petal_length * petal_width
    ratio = (petal_length / petal_width) if petal_width > 0 else 0
    
    summary_text = (
        f"Flower Metrics Summary:\n"
        f"• Petal Area Proxy: {petal_area:.2f} cm²\n"
        f"• Sepal Area Proxy: {sepal_area:.2f} cm²\n"
        f"• Petal Aspect Ratio: {ratio:.2f}"
    )
    ax_stats.text(0.04, 0.06, summary_text, transform=ax_stats.transAxes,
                  fontsize=8.5, color="#e1def5",
                  bbox=dict(boxstyle="round,pad=0.5", fc="#232333", ec="#44476a", lw=1))

    fig.tight_layout()
    return fig
