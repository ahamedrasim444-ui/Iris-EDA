# 🌸 Multidimensional Exploratory Data Analysis of the Iris Dataset
### Utilizing NumPy, Pandas, and Matplotlib
**Department of Computer Science & Engineering | CSE Mini-Project**

---

## 📌 Project Overview
This project presents an interactive, high-performance web dashboard engineered in **Python 3.10+** and **Streamlit** for multi-attribute exploratory data analysis (EDA) of the classic 1936 Fisher Iris botanical dataset. 

It demonstrates foundational data science, linear algebra, and visual analytics principles using:
- **Pandas**: Multi-criteria slicing, groupby aggregations, descriptive metrics, and feature engineering.
- **NumPy**: Sample covariance matrix calculations, correlation tensors, class mean centroid vectors, eigen-decomposition, and live nearest-centroid classification via Euclidean metric distance.
- **Matplotlib**: Publication-quality annotated heatmaps, bivariate cluster scatter plots with convex hull decision boundaries, and 4-panel distribution histograms.
- **Easter Egg**: Functional Python `import antigravity` toggle with interactive floating animations and homage to XKCD #353.

---

## 👥 Project Team & Academic Credentials

- **Institution:** Department of Computer Science & Engineering
- **Course:** Data Science & Multidimensional Analytics (CS601)
- **Faculty Guide:** Prof. Keerthana, Department of Computer Science & Engineering

| S.No. | Student Name | Project Contribution & Role |
| :---: | :--- | :--- |
| **1** | **Balaji (Team Lead)** | **Project Lead & System Architecture** |
| **2** | **Ahamed Rasim** | **Data Pipeline & Pandas Engineering** |
| **3** | **Kishore Kumar** | **NumPy Mathematical & Linear Algebra Engine** |
| **4** | **Aadthiyan** | **Matplotlib Visual Analytics & Frontend UI** |

---

## 📐 Mathematical Formulations

### 1. Sample Covariance Matrix ($\mathbf{\Sigma}$)
Given data matrix $\mathbf{X} \in \mathbb{R}^{n \times 4}$, the empirical mean vector is $\mathbf{\mu} = \frac{1}{n} \sum_{i=1}^n \mathbf{x}_i$. The centered data matrix is:
$$\mathbf{X}_{\text{centered}} = \mathbf{X} - \mathbf{1} \mathbf{\mu}^T$$
The unbiased sample covariance tensor is evaluated via matrix multiplication:
$$\mathbf{\Sigma} = \frac{1}{n - 1} \mathbf{X}_{\text{centered}}^T \mathbf{X}_{\text{centered}}$$

### 2. Pearson Correlation Matrix ($\mathbf{R}$)
Normalized via the standard deviations matrix $\mathbf{D} = \text{diag}(\mathbf{\Sigma})^{1/2}$:
$$\mathbf{R}_{ij} = \frac{\mathbf{\Sigma}_{ij}}{\sigma_i \sigma_j} \quad \Longleftrightarrow \quad \mathbf{R} = \mathbf{D}^{-1} \mathbf{\Sigma} \mathbf{D}^{-1}$$

### 3. Principal Eigen-Decomposition
$$\mathbf{\Sigma} \mathbf{v}_i = \lambda_i \mathbf{v}_i$$
The explained variance ratio for component $i$ is:
$$\text{Variance Explained}(\%) = \frac{\lambda_i}{\sum_{j=1}^4 \lambda_j} \times 100\%$$

### 4. Live Nearest-Centroid Classifier
Given a user query vector $\mathbf{x} = [SL, SW, PL, PW]^T$ and class mean centroids $\mathbf{\mu}_k$ for $k \in \{\text{Setosa}, \text{Versicolor}, \text{Virginica}\}$:
$$\hat{y} = \arg\min_{k} \|\mathbf{x} - \mathbf{\mu}_k\|_2 = \arg\min_{k} \sqrt{\sum_{j=1}^4 (x_j - \mu_{k,j})^2}$$

Proximity confidence scores are computed via normalized softmax over inverse distance:
$$w_k = \frac{\exp(-d_k / T)}{\sum_j \exp(-d_j / T)} \times 100\%$$

---

## 🚀 Key Dashboard Features

### 🎛️ Sidebar Controls
- **Team Information:** Expandable card listing all 4 team members, USNs, roles, and faculty guide.
- **Multiselect Species Filter:** Dynamically select any combination of `Setosa`, `Versicolor`, and `Virginica`.
- **4 Dimensional Range Sliders:** Slices the dataset in real-time across Sepal Length, Sepal Width, Petal Length, and Petal Width.
- **Python Easter Egg:** `🚀 import antigravity` toggle triggering custom floating CSS animations and comic reference.

### 📑 Main Dashboard Tabs
1. **Tab 1: Dataset Explorer & Pandas Aggregations**
   - Interactive data table with keyword searching and CSV export.
   - Engineered features: Petal Aspect Ratio ($PL/PW$), Sepal Aspect Ratio ($SL/SW$), Petal Area Proxy, Sepal Area Proxy.
   - Comprehensive summary statistics (mean, std, IQR, skewness, kurtosis).
   - Stratified Pandas GroupBy aggregations.
2. **Tab 2: NumPy Mathematical Engine**
   - LaTeX mathematical formula callout boxes.
   - 4x4 Sample Covariance Heatmap with numerical precision verification vs. `np.cov` ($< 10^{-15}$).
   - 4x4 Pearson Correlation Diverging Heatmap.
   - Class Mean Centroids table.
   - Eigenvalues and Percentage of Explained Variance table.
3. **Tab 3: Visual Analytics Suite**
   - High-resolution Matplotlib bivariate scatter plot with customizable X and Y axes.
   - Convex Hull decision boundaries calculated in pure NumPy.
   - Centroid star markers ($\star$) with coordinate labels.
   - 4-Panel distribution histogram grid with species-stratified frequencies and mean indicator lines.
4. **Tab 4: Interactive Centroid Predictor**
   - 4 Interactive dimension sliders for real-time testing.
   - Quick preset profile buttons: *"Typical Setosa"*, *"Typical Versicolor"*, *"Typical Virginica"*.
   - Live prediction status box with species color badge and confidence score.
   - Metric comparison horizontal bar chart (Euclidean Distances vs. Softmax Proximity).
   - 2D Query Point Space Projection showing exactly where the test point lands relative to clusters and centroids.

---

## 🛠️ Tech Stack & Directory Structure

- **Python:** 3.10+ (tested on Python 3.13)
- **Frontend / Framework:** Streamlit 1.35+
- **Array Math & Algebra:** NumPy 1.24+
- **Data Wrangling:** Pandas 2.0+
- **Custom Visuals:** Matplotlib 3.8+

```
iris_eda_streamlit_dashboard/
├── app.py                 # Main Streamlit dashboard application
├── data_engine.py         # Pure NumPy mathematical engine & Pandas logic
├── visualizations.py      # High-DPI Matplotlib heatmaps & scatter plots
├── styles.py              # Custom CSS styles, theme cards, and Easter Egg
├── test_engine.py         # Automated test suite (100% test coverage)
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── data/
    └── iris.csv           # Offline-first bundled Iris dataset (150 samples)
```

---

## 💻 Installation & Execution

### 1. Clone or Open the Project
```bash
cd iris_eda_streamlit_dashboard
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Automated Test Suite
```bash
python test_engine.py
```

### 4. Launch the Streamlit Dashboard
```bash
streamlit run app.py
```
*Alternatively, with module runner:*
```bash
python -m streamlit run app.py
```

Open your browser at `http://localhost:8501`.

---

## 📜 Academic Acknowledgments
Dataset original reference:
> Fisher, R. A. (1936). *The use of multiple measurements in taxonomic problems.* Annals of Eugenics, 7(2), 179-188.
