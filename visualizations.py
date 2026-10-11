"""
visualizations.py
Deep Tech Obsidian themed Matplotlib & SVG visualizations for Iris EDA Dashboard.
All figures use #0B0F17 background with Cyan/Amber/Lavender accents.
"""

import io
import base64
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patheffects as pe

# ─── Deep Tech Obsidian rcParams ────────────────────────────────────────────
BG_CANVAS   = "#0B0F17"
BG_CARD     = "#131B2E"
BG_CARD2    = "#1E293B"
BORDER_COL  = "#334155"
CYAN        = "#38BDF8"
EMERALD     = "#34D399"
AMBER       = "#F59E0B"
LAVENDER    = "#A78BFA"
TEXT_HI     = "#F8FAFC"
TEXT_LO     = "#94A3B8"

SPECIES_COLORS = {
    "Setosa":     CYAN,
    "Versicolor": AMBER,
    "Virginica":  LAVENDER,
}

matplotlib.rcParams.update({
    "figure.facecolor":     BG_CANVAS,
    "axes.facecolor":       BG_CARD,
    "axes.edgecolor":       BORDER_COL,
    "axes.labelcolor":      TEXT_LO,
    "axes.titlecolor":      TEXT_HI,
    "xtick.color":          TEXT_LO,
    "ytick.color":          TEXT_LO,
    "text.color":           TEXT_HI,
    "grid.color":           BORDER_COL,
    "grid.linewidth":       0.6,
    "legend.facecolor":     BG_CARD2,
    "legend.edgecolor":     BORDER_COL,
    "legend.labelcolor":    TEXT_HI,
    "font.family":          "DejaVu Sans",
    "font.size":            10,
    "axes.titlepad":        14,
})


def _obsidian_cmap():
    """Custom colormap: deep obsidian → cyan."""
    return LinearSegmentedColormap.from_list(
        "obsidian_cyan", [BG_CANVAS, "#0E4D6B", CYAN], N=256
    )


def _apply_obsidian_spine(ax):
    for spine in ax.spines.values():
        spine.set_edgecolor(BORDER_COL)
        spine.set_linewidth(0.8)
    ax.tick_params(colors=TEXT_LO, which="both")
    ax.xaxis.label.set_color(TEXT_LO)
    ax.yaxis.label.set_color(TEXT_LO)
    ax.title.set_color(TEXT_HI)


# ─── 1. Covariance Heatmap ──────────────────────────────────────────────────
def plot_covariance_heatmap(cov_matrix: np.ndarray, feature_cols: list) -> plt.Figure:
    labels = ["SL", "SW", "PL", "PW"]
    fig, ax = plt.subplots(figsize=(6, 5), facecolor=BG_CANVAS)
    ax.set_facecolor(BG_CARD)

    cmap = LinearSegmentedColormap.from_list("cov_cmap", [BG_CANVAS, "#0E4D6B", CYAN], N=256)
    im = ax.imshow(cov_matrix, cmap=cmap, aspect="auto")

    ax.set_xticks(range(4)); ax.set_yticks(range(4))
    ax.set_xticklabels(labels, color=TEXT_LO)
    ax.set_yticklabels(labels, color=TEXT_LO)
    ax.set_title("Covariance Matrix Σ", color=TEXT_HI, fontsize=13, fontweight="bold", pad=12)

    for i in range(4):
        for j in range(4):
            val = cov_matrix[i, j]
            col = TEXT_HI if abs(val) > np.max(np.abs(cov_matrix)) * 0.5 else TEXT_LO
            ax.text(j, i, f"{val:.3f}", ha="center", va="center", color=col, fontsize=9)

    cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cb.ax.yaxis.set_tick_params(color=TEXT_LO)
    plt.setp(plt.getp(cb.ax.axes, "yticklabels"), color=TEXT_LO)

    fig.tight_layout()
    _apply_obsidian_spine(ax)
    return fig


# ─── 2. Correlation Heatmap ─────────────────────────────────────────────────
def plot_correlation_heatmap(corr_matrix: np.ndarray, feature_cols: list) -> plt.Figure:
    labels = ["SL", "SW", "PL", "PW"]
    fig, ax = plt.subplots(figsize=(6, 5), facecolor=BG_CANVAS)
    ax.set_facecolor(BG_CARD)

    cmap = LinearSegmentedColormap.from_list(
        "corr_cmap", ["#7C3AED", BG_CANVAS, CYAN], N=256
    )
    im = ax.imshow(corr_matrix, cmap=cmap, vmin=-1, vmax=1, aspect="auto")

    ax.set_xticks(range(4)); ax.set_yticks(range(4))
    ax.set_xticklabels(labels, color=TEXT_LO)
    ax.set_yticklabels(labels, color=TEXT_LO)
    ax.set_title("Pearson Correlation Matrix R", color=TEXT_HI, fontsize=13, fontweight="bold", pad=12)

    for i in range(4):
        for j in range(4):
            val = corr_matrix[i, j]
            col = TEXT_HI if abs(val) > 0.4 else TEXT_LO
            ax.text(j, i, f"{val:.2f}", ha="center", va="center", color=col, fontsize=9)

    cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cb.ax.yaxis.set_tick_params(color=TEXT_LO)
    plt.setp(plt.getp(cb.ax.axes, "yticklabels"), color=TEXT_LO)

    fig.tight_layout()
    _apply_obsidian_spine(ax)
    return fig


# ─── 3. Bivariate Scatter ───────────────────────────────────────────────────
def plot_bivariate_scatter(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    centroids: dict,
    boundary_line: bool = True,
) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(8, 6), facecolor=BG_CANVAS)
    ax.set_facecolor(BG_CARD)

    for sp, grp in df.groupby("species"):
        c = SPECIES_COLORS.get(sp, TEXT_LO)
        ax.scatter(
            grp[x_col], grp[y_col],
            label=sp, color=c, alpha=0.82, edgecolors=BG_CANVAS,
            linewidths=0.6, s=60, zorder=3,
        )
        if sp in centroids:
            cx = centroids[sp][["sepal_length","sepal_width","petal_length","petal_width"].index(x_col)]
            cy = centroids[sp][["sepal_length","sepal_width","petal_length","petal_width"].index(y_col)]
            ax.scatter(cx, cy, color=c, marker="X", s=180, edgecolors=TEXT_HI,
                       linewidths=1.5, zorder=5)

    if boundary_line and x_col == "petal_length":
        ax.axvline(x=2.45, color=EMERALD, linewidth=1.8, linestyle="--",
                   label="Setosa Boundary (2.45 cm)", alpha=0.9)
        ax.text(2.52, ax.get_ylim()[1] * 0.95 if ax.get_ylim()[1] else 2.5,
                "2.45 cm\nboundary", color=EMERALD, fontsize=8, va="top", alpha=0.9)

    ax.set_xlabel(x_col.replace("_", " ").title() + " (cm)", color=TEXT_LO)
    ax.set_ylabel(y_col.replace("_", " ").title() + " (cm)", color=TEXT_LO)
    ax.set_title(f"Bivariate Scatter: {x_col.replace('_',' ').title()} vs {y_col.replace('_',' ').title()}",
                 color=TEXT_HI, fontsize=12, fontweight="bold")
    ax.legend(framealpha=0.3, facecolor=BG_CARD2, edgecolor=BORDER_COL, labelcolor=TEXT_HI)
    ax.grid(True, alpha=0.3, color=BORDER_COL)
    _apply_obsidian_spine(ax)
    fig.tight_layout()
    return fig


# ─── 4. Boxplot Dispersion ──────────────────────────────────────────────────
def plot_boxplot_dispersion(df: pd.DataFrame, feature: str) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(7, 5), facecolor=BG_CANVAS)
    ax.set_facecolor(BG_CARD)

    species_list = ["Setosa", "Versicolor", "Virginica"]
    data_groups = [df[df["species"] == sp][feature].dropna().values for sp in species_list]
    colors_list = [SPECIES_COLORS[sp] for sp in species_list]

    bp = ax.boxplot(
        data_groups,
        patch_artist=True,
        notch=False,
        medianprops=dict(color=TEXT_HI, linewidth=2),
        whiskerprops=dict(color=TEXT_LO, linewidth=1.2),
        capprops=dict(color=TEXT_LO, linewidth=1.5),
        flierprops=dict(marker="o", markerfacecolor=TEXT_LO, markersize=4, alpha=0.6),
    )

    for patch, color in zip(bp["boxes"], colors_list):
        patch.set_facecolor(color)
        patch.set_alpha(0.75)
        patch.set_edgecolor(TEXT_HI)

    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(species_list, color=TEXT_LO)
    ax.set_xlabel("Species", color=TEXT_LO)
    ax.set_ylabel(feature.replace("_", " ").title() + " (cm)", color=TEXT_LO)
    ax.set_title(f"Distribution of {feature.replace('_', ' ').title()} by Species",
                 color=TEXT_HI, fontsize=12, fontweight="bold")
    ax.grid(axis="y", alpha=0.3, color=BORDER_COL)
    _apply_obsidian_spine(ax)
    fig.tight_layout()
    return fig


# ─── 5. Distributions Grid (KDE) ────────────────────────────────────────────
def plot_distributions_grid(df: pd.DataFrame) -> plt.Figure:
    feature_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    feature_labels = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]

    fig, axes = plt.subplots(2, 2, figsize=(10, 7), facecolor=BG_CANVAS)
    axes = axes.flatten()

    for idx, (feat, label) in enumerate(zip(feature_cols, feature_labels)):
        ax = axes[idx]
        ax.set_facecolor(BG_CARD)

        for sp, color in SPECIES_COLORS.items():
            sub = df[df["species"] == sp][feat].dropna().to_numpy()
            if len(sub) < 3:
                continue
            # Pure NumPy Gaussian Kernel Density Estimation
            std_val = float(np.std(sub))
            bw = 1.06 * std_val * (len(sub) ** (-0.2)) if std_val > 0 else 0.3
            bw = max(bw, 0.18)
            xs = np.linspace(sub.min() - 0.4, sub.max() + 0.4, 200)
            u = (xs[:, None] - sub[None, :]) / bw
            ys = np.sum(np.exp(-0.5 * u**2) / (np.sqrt(2 * np.pi) * bw), axis=1) / len(sub)
            ax.plot(xs, ys, color=color, linewidth=2, label=sp)
            ax.fill_between(xs, ys, alpha=0.18, color=color)

        ax.set_xlabel(label + " (cm)", color=TEXT_LO, fontsize=9)
        ax.set_ylabel("Density", color=TEXT_LO, fontsize=9)
        ax.set_title(label, color=TEXT_HI, fontsize=10, fontweight="bold")
        ax.legend(fontsize=7.5, framealpha=0.3, facecolor=BG_CARD2,
                  edgecolor=BORDER_COL, labelcolor=TEXT_HI)
        ax.grid(alpha=0.25, color=BORDER_COL)
        _apply_obsidian_spine(ax)

    fig.suptitle("Feature Probability Density Distributions (KDE)", color=TEXT_HI,
                 fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    return fig


# ─── 6. Prediction Diagnostics ──────────────────────────────────────────────
def plot_prediction_diagnostics(
    distances: dict, proximity_pct: dict, predicted_species: str
) -> plt.Figure:
    species_list = ["Setosa", "Versicolor", "Virginica"]
    colors_list  = [SPECIES_COLORS[s] for s in species_list]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4), facecolor=BG_CANVAS)

    # Left: Distance bar chart
    ax1.set_facecolor(BG_CARD)
    dvals = [distances.get(s, 0) for s in species_list]
    bars = ax1.bar(species_list, dvals, color=colors_list, alpha=0.8,
                   edgecolor=TEXT_HI, linewidth=0.8)
    for bar, val in zip(bars, dvals):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                 f"{val:.3f}", ha="center", va="bottom", color=TEXT_HI, fontsize=9)
    ax1.set_ylabel("Euclidean Distance", color=TEXT_LO)
    ax1.set_title("Distance to Each Centroid", color=TEXT_HI, fontsize=11, fontweight="bold")
    ax1.tick_params(axis="x", colors=TEXT_LO)
    ax1.tick_params(axis="y", colors=TEXT_LO)
    ax1.grid(axis="y", alpha=0.25, color=BORDER_COL)
    _apply_obsidian_spine(ax1)

    # Right: Proximity donut
    ax2.set_facecolor(BG_CARD)
    pvals = [proximity_pct.get(s, 0) for s in species_list]
    wedges, texts, autotexts = ax2.pie(
        pvals,
        labels=species_list,
        colors=colors_list,
        autopct="%1.1f%%",
        startangle=140,
        wedgeprops=dict(width=0.55, edgecolor=BG_CANVAS, linewidth=2),
        textprops=dict(color=TEXT_HI, fontsize=9),
    )
    for at in autotexts:
        at.set_color(BG_CANVAS)
        at.set_fontsize(8.5)
    ax2.set_title(f"Proximity Score\n→ Predicted: {predicted_species}",
                  color=TEXT_HI, fontsize=11, fontweight="bold")

    fig.tight_layout()
    return fig


# ─── 7. Query Point Projection ──────────────────────────────────────────────
def plot_query_point_projection(
    df: pd.DataFrame,
    query_point: np.ndarray,
    centroids: dict,
    predicted_species: str,
) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(7, 5), facecolor=BG_CANVAS)
    ax.set_facecolor(BG_CARD)

    feat_idx = {"sepal_length": 0, "sepal_width": 1, "petal_length": 2, "petal_width": 3}
    xi, yi = 2, 3  # petal_length vs petal_width

    for sp, grp in df.groupby("species"):
        c = SPECIES_COLORS.get(sp, TEXT_LO)
        ax.scatter(grp["petal_length"], grp["petal_width"],
                   color=c, alpha=0.5, s=35, edgecolors="none")

    # Query point
    ax.scatter(query_point[xi], query_point[yi],
               color=EMERALD, marker="*", s=320, zorder=8,
               edgecolors=TEXT_HI, linewidths=1.2, label="Your Input")

    # Lines to centroids
    for sp, centroid in centroids.items():
        c = SPECIES_COLORS.get(sp, TEXT_LO)
        ax.plot([query_point[xi], centroid[xi]], [query_point[yi], centroid[yi]],
                color=c, linestyle=":", linewidth=1.5, alpha=0.7)
        ax.scatter(centroid[xi], centroid[yi], color=c, marker="X", s=150,
                   edgecolors=TEXT_HI, linewidths=1.2, zorder=6)

    ax.set_xlabel("Petal Length (cm)", color=TEXT_LO)
    ax.set_ylabel("Petal Width (cm)", color=TEXT_LO)
    ax.set_title(f"Query Point Projection — Predicted: {predicted_species}",
                 color=TEXT_HI, fontsize=11, fontweight="bold")
    ax.legend(framealpha=0.3, facecolor=BG_CARD2, edgecolor=BORDER_COL, labelcolor=TEXT_HI)
    ax.grid(alpha=0.25, color=BORDER_COL)
    _apply_obsidian_spine(ax)
    fig.tight_layout()
    return fig


# ─── 8. Interactive Iris Flower Visualization ────────────────────────────────
def plot_interactive_iris_flower(
    sepal_length: float,
    sepal_width: float,
    petal_length: float,
    petal_width: float,
    predicted_species: str = "Setosa",
) -> plt.Figure:
    """
    Draws a realistic 2D botanical vector silhouette of an iris flower
    with labeled measurements. Left panel = anatomical diagram.
    Right panel = polar silhouette.
    """
    sp_color = SPECIES_COLORS.get(predicted_species, CYAN)
    sp_light = sp_color + "55"  # semi-transparent

    fig, (ax_bot, ax_polar) = plt.subplots(
        1, 2,
        figsize=(11, 6),
        facecolor=BG_CANVAS,
        gridspec_kw={"width_ratios": [1.1, 0.9]},
    )

    # ── Left: Anatomical diagram ────────────────────────────────────────────
    ax_bot.set_facecolor(BG_CARD)
    ax_bot.set_xlim(-3.5, 3.5)
    ax_bot.set_ylim(-3.5, 5.5)
    ax_bot.set_aspect("equal")
    ax_bot.axis("off")
    ax_bot.set_title("Iris Flower — Anatomical Diagram", color=TEXT_HI, fontsize=11, fontweight="bold")

    sl = min(sepal_length / 8.0, 1.0)   # scale 0-1
    sw = min(sepal_width  / 6.0, 1.0)
    pl = min(petal_length / 8.0, 1.0)
    pw = min(petal_width  / 4.0, 1.0)

    SEPAL_H = 2.2 + sl * 1.4   # height
    SEPAL_W = 0.65 + sw * 0.7  # half-width
    PETAL_H = 1.1 + pl * 1.6
    PETAL_W = 0.4  + pw * 0.6

    sepal_angles = [90, 210, 330]     # "falls" (sepals at top + two lower)
    petal_angles = [30, 150, 270]     # "standards" (petals between sepals)

    # Draw 3 sepals ("falls")
    for ang in sepal_angles:
        rad = np.deg2rad(ang)
        dx, dy = np.cos(rad), np.sin(rad)
        cx = dx * (SEPAL_H * 0.5)
        cy = dy * (SEPAL_H * 0.5)
        ell = Ellipse(
            (cx, cy),
            width=SEPAL_W * 2,
            height=SEPAL_H,
            angle=ang - 90,
            facecolor=sp_color + "88",
            edgecolor=sp_color,
            linewidth=1.8,
            zorder=2,
        )
        ax_bot.add_patch(ell)

    # Sepal label (one arrow)
    ax_bot.annotate(
        "Sepal (falls)",
        xy=(np.cos(np.deg2rad(90)) * SEPAL_H * 0.75,
            np.sin(np.deg2rad(90)) * SEPAL_H * 0.75),
        xytext=(2.5, 4.0),
        color=TEXT_HI, fontsize=8.5,
        arrowprops=dict(arrowstyle="->", color=TEXT_LO, lw=1.2),
    )

    # Draw 3 petals ("standards")
    for ang in petal_angles:
        rad = np.deg2rad(ang)
        dx, dy = np.cos(rad), np.sin(rad)
        cx = dx * (PETAL_H * 0.45)
        cy = dy * (PETAL_H * 0.45)
        ell = Ellipse(
            (cx, cy),
            width=PETAL_W * 2,
            height=PETAL_H,
            angle=ang - 90,
            facecolor=sp_color + "CC",
            edgecolor=TEXT_HI,
            linewidth=1.5,
            zorder=3,
        )
        ax_bot.add_patch(ell)

    # Petal label (one arrow)
    ax_bot.annotate(
        "Petal (standards)",
        xy=(np.cos(np.deg2rad(30)) * PETAL_H * 0.6,
            np.sin(np.deg2rad(30)) * PETAL_H * 0.6),
        xytext=(2.5, 2.5),
        color=TEXT_HI, fontsize=8.5,
        arrowprops=dict(arrowstyle="->", color=TEXT_LO, lw=1.2),
    )

    # Central circle (receptacle)
    center_circ = Circle((0, 0), 0.38, color=EMERALD, zorder=4, ec=TEXT_HI, lw=1.5)
    ax_bot.add_patch(center_circ)
    ax_bot.text(0, 0, "✿", ha="center", va="center", fontsize=12, color=BG_CANVAS, zorder=5)

    # Dimension callouts
    dim_texts = [
        f"SL = {sepal_length:.1f} cm",
        f"SW = {sepal_width:.1f} cm",
        f"PL = {petal_length:.1f} cm",
        f"PW = {petal_width:.1f} cm",
    ]
    for i, txt in enumerate(dim_texts):
        ax_bot.text(-3.3, 4.8 - i * 0.55, txt, color=TEXT_LO, fontsize=8.5,
                    fontfamily="monospace")

    # Species badge
    ax_bot.text(0, -3.2, f"Species: {predicted_species}",
                ha="center", va="center", fontsize=10, color=sp_color,
                fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.4", facecolor=BG_CARD2,
                          edgecolor=sp_color, linewidth=1.5))

    # ── Right: Polar silhouette ─────────────────────────────────────────────
    ax_polar.remove()
    ax_polar = fig.add_subplot(1, 2, 2, projection="polar", facecolor=BG_CARD)
    ax_polar.set_facecolor(BG_CARD)

    dims    = [sepal_length, sepal_width, petal_length, petal_width]
    labels  = ["Sepal\nLength", "Sepal\nWidth", "Petal\nLength", "Petal\nWidth"]
    maxvals = [8.0, 5.0, 7.0, 3.0]
    norm    = [d / m for d, m in zip(dims, maxvals)]
    N       = len(dims)
    angles  = [n / N * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    norm   += norm[:1]

    ax_polar.plot(angles, norm, "o-", color=sp_color, linewidth=2.2, markersize=8,
                  markerfacecolor=TEXT_HI, markeredgecolor=sp_color)
    ax_polar.fill(angles, norm, alpha=0.28, color=sp_color)
    ax_polar.set_xticks(angles[:-1])
    ax_polar.set_xticklabels(labels, color=TEXT_HI, fontsize=8.5)
    ax_polar.set_ylim(0, 1.05)
    ax_polar.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax_polar.set_yticklabels(["25%", "50%", "75%", "100%"], color=TEXT_LO, fontsize=7)
    ax_polar.tick_params(colors=TEXT_LO)
    ax_polar.spines["polar"].set_edgecolor(BORDER_COL)
    ax_polar.grid(color=BORDER_COL, alpha=0.4)
    ax_polar.set_title("Dimension Radar", color=TEXT_HI, fontsize=10, fontweight="bold", pad=18)

    fig.suptitle(
        f"Iris {predicted_species} — Interactive Botanical Visualization",
        color=TEXT_HI, fontsize=12, fontweight="bold", y=1.01,
    )
    fig.tight_layout()
    return fig
