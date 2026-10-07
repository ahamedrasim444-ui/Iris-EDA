"""
visualizations.py
Publication-ready Matplotlib visualization suite for the Iris EDA Dashboard.
Renders annotated heatmaps, bivariate cluster scatter plots with convex hulls & centroids,
4-panel distribution histograms, and live prediction diagnostics.
"""

from typing import Dict, List, Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.ticker as ticker

from data_engine import FEATURE_LABELS, SPECIES_COLORS


# Configure consistent modern matplotlib styling
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "DejaVu Sans", "Helvetica", "Arial"],
    "axes.edgecolor": "#cbd5e1",
    "axes.linewidth": 1.2,
    "grid.color": "#e2e8f0",
    "grid.linestyle": "--",
    "grid.alpha": 0.7,
    "xtick.color": "#475569",
    "ytick.color": "#475569",
    "figure.facecolor": "#ffffff",
    "axes.facecolor": "#ffffff",
    "axes.labelcolor": "#1e293b",
    "axes.titlecolor": "#0f172a",
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
    """Renders annotated 4x4 sample covariance matrix heatmap."""
    fig, ax = plt.subplots(figsize=(6.5, 5.2), dpi=160)
    
    labels = [FEATURE_LABELS.get(f, f).replace(" (cm)", "") for f in feature_names]
    
    im = ax.imshow(cov_matrix, cmap="Blues", interpolation="nearest")
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.ax.tick_params(labelsize=9)
    cbar.set_label("Covariance Value ($cm^2$)", fontsize=9, fontweight="bold", labelpad=8)
    
    # Tick marks
    n = len(feature_names)
    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(n))
    ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=9, fontweight="bold")
    ax.set_yticklabels(labels, fontsize=9, fontweight="bold")
    
    # Annotations with adaptive contrast
    threshold = (cov_matrix.max() + cov_matrix.min()) / 2.0
    for i in range(n):
        for j in range(n):
            val = cov_matrix[i, j]
            text_color = "#ffffff" if val > threshold else "#0f172a"
            ax.text(j, i, f"{val:.3f}", ha="center", va="center",
                    color=text_color, fontsize=10, fontweight="bold")
            
    ax.set_title(r"Sample Covariance Tensor $\mathbf{\Sigma} \in \mathbb{R}^{4 \times 4}$", 
                 pad=14, fontsize=11, fontweight="bold")
    ax.grid(False)
    fig.tight_layout()
    return fig


def plot_correlation_heatmap(corr_matrix: np.ndarray, feature_names: List[str]) -> plt.Figure:
    """Renders Pearson correlation matrix heatmap with diverging palette (-1 to +1)."""
    fig, ax = plt.subplots(figsize=(6.5, 5.2), dpi=160)
    
    labels = [FEATURE_LABELS.get(f, f).replace(" (cm)", "") for f in feature_names]
    
    im = ax.imshow(corr_matrix, cmap="coolwarm", vmin=-1.0, vmax=1.0, interpolation="nearest")
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.ax.tick_params(labelsize=9)
    cbar.set_label("Pearson Correlation $r$", fontsize=9, fontweight="bold", labelpad=8)
    
    n = len(feature_names)
    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(n))
    ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=9, fontweight="bold")
    ax.set_yticklabels(labels, fontsize=9, fontweight="bold")
    
    for i in range(n):
        for j in range(n):
            val = corr_matrix[i, j]
            text_color = "#ffffff" if abs(val) > 0.65 else "#0f172a"
            ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                    color=text_color, fontsize=10, fontweight="bold")
            
    ax.set_title(r"Pearson Correlation Matrix $\mathbf{R} \in [-1, 1]^{4 \times 4}$", 
                 pad=14, fontsize=11, fontweight="bold")
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
    convex hull decision envelopes, and centroid star markers.
    """
    fig, ax = plt.subplots(figsize=(8.5, 5.6), dpi=160)
    
    species_order = ["Setosa", "Versicolor", "Virginica"]
    
    for sp in species_order:
        sub = df[df["species"] == sp]
        if sub.empty:
            continue
            
        color = SPECIES_COLORS.get(sp, "#6366F1")
        x_vals = sub[x_col].to_numpy()
        y_vals = sub[y_col].to_numpy()
        
        # 1. Scatter points
        ax.scatter(
            x_vals, y_vals,
            c=color, label=f"{sp} (n={len(sub)})",
            alpha=0.75, edgecolors="#ffffff", linewidth=0.8, s=64, zorder=3
        )
        
        # 2. Convex Hull Decision Envelopes
        if show_hulls and len(sub) >= 3:
            pts = np.column_stack((x_vals, y_vals))
            hull_pts = _compute_convex_hull_2d(pts)
            if len(hull_pts) >= 3:
                poly = Polygon(
                    hull_pts, closed=True,
                    facecolor=color, alpha=0.12,
                    edgecolor=color, linestyle="--", linewidth=1.5, zorder=2
                )
                ax.add_patch(poly)
                
        # 3. Class Centroid Star Markers
        if show_centroids:
            if centroids and sp in centroids:
                # If 4-dim vector is passed, index according to col
                feature_keys = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
                if x_col in feature_keys and y_col in feature_keys:
                    xi = feature_keys.index(x_col)
                    yi = feature_keys.index(y_col)
                    cx, cy = centroids[sp][xi], centroids[sp][yi]
                else:
                    cx, cy = np.mean(x_vals), np.mean(y_vals)
            else:
                cx, cy = np.mean(x_vals), np.mean(y_vals)
                
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
                bbox=dict(boxstyle="round,pad=0.2", fc="#ffffff", ec=color, alpha=0.9, lw=0.8)
            )

    # Setosa linear boundary cutoff (at Petal Length = 2.45 cm)
    if x_col == "petal_length":
        ax.axvline(x=2.45, color="#dc2626", linestyle="--", linewidth=1.6, label="Setosa Linear Boundary (< 2.45 cm)")

    x_label = FEATURE_LABELS.get(x_col, x_col.replace("_", " ").title())
    y_label = FEATURE_LABELS.get(y_col, y_col.replace("_", " ").title())
    
    ax.set_xlabel(x_label, fontsize=10, fontweight="bold", labelpad=8)
    ax.set_ylabel(y_label, fontsize=10, fontweight="bold", labelpad=8)
    ax.set_title(f"Bivariate Space: {x_label} vs. {y_label}", pad=12, fontsize=11, fontweight="bold")
    ax.legend(frameon=True, facecolor="#ffffff", edgecolor="#cbd5e1", fontsize=8.5, loc="best")
    ax.grid(True, linestyle=":", alpha=0.6)
    
    fig.tight_layout()
    return fig


def plot_boxplot_dispersion(
    df: pd.DataFrame,
    feature_col: str = "petal_length",
    selected_species: Optional[List[str]] = None,
) -> plt.Figure:
    """Renders clean boxplot showing feature dispersion across species."""
    fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=150)
    
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
            colors_list.append(SPECIES_COLORS.get(sp, "#2563eb"))
            
    if box_data:
        bp = ax.boxplot(
            box_data, tick_labels=labels, patch_artist=True,
            medianprops=dict(color="#0f172a", linewidth=2),
            boxprops=dict(linewidth=1.2),
            whiskerprops=dict(linewidth=1.2, color="#475569"),
            capprops=dict(linewidth=1.2, color="#475569"),
            flierprops=dict(marker='o', markersize=5, markerfacecolor='#dc2626', markeredgecolor='none')
        )
        for patch, col in zip(bp['boxes'], colors_list):
            patch.set_facecolor(col)
            patch.set_alpha(0.4)
            patch.set_edgecolor(col)
            
    feat_title = FEATURE_LABELS.get(feature_col, feature_col.replace("_", " ").title())
    ax.set_title(f"Dispersion Across Species: {feat_title}", fontsize=11, fontweight="bold", pad=10)
    ax.set_ylabel(f"{feat_title}", fontsize=9.5, fontweight="bold")
    ax.grid(True, linestyle=":", alpha=0.6)
    fig.tight_layout()
    return fig


def plot_distributions_grid(df: pd.DataFrame) -> plt.Figure:
    """
    Renders 4-panel (2x2 grid) distribution histograms with mean markers for each dimension.
    """
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 7.5), dpi=160)
    axes = axes.flatten()
    
    features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    species_order = ["Setosa", "Versicolor", "Virginica"]
    
    for idx, feat in enumerate(features):
        ax = axes[idx]
        f_label = FEATURE_LABELS.get(feat, feat)
        
        for sp in species_order:
            sub = df[df["species"] == sp]
            if sub.empty:
                continue
            color = SPECIES_COLORS.get(sp, "#6366F1")
            vals = sub[feat].to_numpy()
            
            # Histogram
            ax.hist(
                vals, bins=12, alpha=0.45, color=color,
                label=sp if idx == 0 else None,
                edgecolor=color, linewidth=1.2
            )
            
            # Species Mean Line
            mean_v = np.mean(vals)
            ax.axvline(mean_v, color=color, linestyle="--", linewidth=1.4, alpha=0.85)
            
        ax.set_title(f_label, fontsize=10, fontweight="bold", pad=8)
        ax.set_xlabel("Measurement (cm)", fontsize=8.5)
        ax.set_ylabel("Frequency", fontsize=8.5)
        ax.grid(True, linestyle=":", alpha=0.5)
        
    # Global legend on top
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, 0.99),
               ncol=3, frameon=True, facecolor="#ffffff", edgecolor="#cbd5e1", fontsize=9)
    
    fig.suptitle("Multidimensional Feature Distribution Breakdown by Species", 
                 fontsize=12, fontweight="bold", y=1.02)
    fig.tight_layout()
    return fig


def plot_prediction_diagnostics(
    distances: Dict[str, float],
    proximity_pct: Dict[str, float],
    predicted_species: str,
) -> plt.Figure:
    """
    Renders live diagnostic horizontal bar charts comparing Euclidean distances
    and normalized proximity confidence scores to species centroids.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 3.2), dpi=160)
    
    species = list(distances.keys())
    dist_vals = [distances[s] for s in species]
    prox_vals = [proximity_pct[s] for s in species]
    colors = [SPECIES_COLORS.get(s, "#6366F1") for s in species]
    
    y_pos = np.arange(len(species))
    
    # 1. Euclidean Distances (Lower is better)
    bars1 = ax1.barh(y_pos, dist_vals, color=colors, alpha=0.85, edgecolor="#0f172a", linewidth=0.8)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(species, fontweight="bold", fontsize=9)
    ax1.set_xlabel(r"Euclidean Distance $\|\mathbf{x} - \mathbf{\mu}_k\|_2$ (cm)", fontsize=8.5, fontweight="bold")
    ax1.set_title("Metric Distance to Centroid", fontsize=10, fontweight="bold", pad=8)
    ax1.invert_yaxis()
    ax1.grid(True, axis="x", linestyle=":", alpha=0.6)
    
    for bar in bars1:
        w = bar.get_width()
        ax1.text(w + 0.05, bar.get_y() + bar.get_height() / 2, f"{w:.2f} cm",
                 va="center", fontsize=8.5, fontweight="bold", color="#334155")
        
    # 2. Proximity Confidence % (Higher is better)
    bars2 = ax2.barh(y_pos, prox_vals, color=colors, alpha=0.85, edgecolor="#0f172a", linewidth=0.8)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([])
    ax2.set_xlabel("Proximity Confidence (%)", fontsize=8.5, fontweight="bold")
    ax2.set_title("Softmax Proximity Score", fontsize=10, fontweight="bold", pad=8)
    ax2.set_xlim(0, 105)
    ax2.invert_yaxis()
    ax2.grid(True, axis="x", linestyle=":", alpha=0.6)
    
    for bar in bars2:
        w = bar.get_width()
        ax2.text(w + 1.5, bar.get_y() + bar.get_height() / 2, f"{w:.1f}%",
                 va="center", fontsize=8.5, fontweight="bold", color="#334155")
        
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
    in relation to class clusters and centroids.
    """
    fig, ax = plt.subplots(figsize=(7.5, 4.8), dpi=160)
    
    feature_keys = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    xi = feature_keys.index(x_col)
    yi = feature_keys.index(y_col)
    
    for sp in ["Setosa", "Versicolor", "Virginica"]:
        sub = df[df["species"] == sp]
        if sub.empty:
            continue
        color = SPECIES_COLORS.get(sp, "#6366F1")
        ax.scatter(sub[x_col], sub[y_col], c=color, alpha=0.35, s=36, edgecolors="none")
        
        # Centroid
        if sp in centroids:
            cx, cy = centroids[sp][xi], centroids[sp][yi]
            ax.scatter(cx, cy, marker="*", s=160, c=color, edgecolors="#ffffff", lw=1.2)
            
    # Highlight User's Query Vector
    qx, qy = query_vector[xi], query_vector[yi]
    pred_color = SPECIES_COLORS.get(predicted_species, "#4f46e5")
    
    # Pulsing outer ring + diamond
    ax.scatter(qx, qy, s=260, facecolors="none", edgecolors=pred_color, linewidth=2.5, linestyle="--", zorder=6)
    ax.scatter(qx, qy, marker="D", s=120, c="#fbbf24", edgecolors="#0f172a", linewidth=1.5, 
               label=f"Query Point ({qx:.1f}, {qy:.1f})", zorder=7)
    
    # Line connecting query point to the closest centroid
    cx, cy = centroids[predicted_species][xi], centroids[predicted_species][yi]
    ax.plot([qx, cx], [qy, cy], color=pred_color, linestyle=":", linewidth=2, 
            label=f"Nearest -> {predicted_species}", zorder=5)
    
    x_label = FEATURE_LABELS.get(x_col, x_col)
    y_label = FEATURE_LABELS.get(y_col, y_col)
    ax.set_xlabel(x_label, fontsize=9.5, fontweight="bold")
    ax.set_ylabel(y_label, fontsize=9.5, fontweight="bold")
    ax.set_title(f"Live Query Point Space Projection ({x_label} vs. {y_label})", 
                 fontsize=10.5, fontweight="bold", pad=10)
    ax.legend(frameon=True, facecolor="#ffffff", edgecolor="#cbd5e1", fontsize=8.5, loc="best")
    ax.grid(True, linestyle=":", alpha=0.5)
    
    fig.tight_layout()
    return fig
