# Green-Skills AI Internship Project  
## Path-Dependent Energy Stress Modeling for Lithium-Ion Battery Packs

An end-to-end, research-grade AI framework that models lithium-ion battery
degradation as a **path-dependent functional learning problem**, moving
beyond traditional cycle-counting and energy-throughput approaches.

This repository integrates **data science, machine learning, functional deep
learning (DeepONet), explainability, and AI-driven analytics** to quantify
battery stress based on *how* energy flows through a battery—not just how
much.

---

## 🔬 Project Motivation

Traditional battery aging models assume:

> Same energy throughput ⇒ Same degradation

This assumption is fundamentally flawed.

**Same Ah ≠ Same Damage**

High-frequency current fluctuations, sharp spikes, and pulsed loads degrade
batteries faster—even when total energy usage is identical.

This project introduces a **Stress Functional Learning Framework** that:

- Learns degradation directly from current waveforms  
- Captures path dependence in battery aging  
- Identifies toxic load shapes  
- Predicts capacity fade and remaining useful life  
- Constructs a Safe vs Dangerous operating envelope  

---

## 🎯 Objectives

- Replace cycle counting with stress-based degradation modeling  
- Learn degradation physics directly from data  
- Capture path dependence in lithium-ion aging  
- Combine ML, Deep Learning, and physics-informed constraints  
- Deliver interpretable insights for Battery Management Systems (BMS)  

---

## 🧠 Core Concept: Stress as a Functional

Battery degradation is modeled as a functional:

\[
D[I(t)] = \int f(I(t), \frac{dI}{dt}) \, dt
\]

Where:

- **I(t)** → current profile  
- **dI/dt** → current rate (stress amplifier)  
- **D** → learned degradation / stress  

This replaces heuristic degradation models with **data-driven physics learning**.

---

## 📁 Repository Structure

```

batteryguard-ai/
│
├── data/
│   ├── raw/
│   │   └── battery_data.csv
│   │
│   ├── processed/
│   │   ├── cycles.csv
│   │   ├── stress_features.csv
│   │   └── capacity_fade.csv
│
├── preprocessing/
│   ├── signal_cleaning.py
│   ├── cycle_extraction.py
│   └── derivatives.py
│
├── features/
│   └── load_shape_features.py
│
├── models/
│   ├── degradation_ml.py
│   ├── anomaly_models.py
│   ├── rul_models.py
│   └── stress_deeponet.py
│
├── xai/
│   ├── shap_analysis.py
│   └── stress_attribution.py
│
├── safety/
│   ├── early_warning.py
│   └── risk_scoring.py
│
├── analytics/
│   ├── cell_pack_loss.py
│   └── reporting.py
│
├── chatbot/
│   └── assistant.py
│
├── app/
│   └── streamlit_app.py
│
├── notebooks/
│   └── green_ai_project.ipynb
│
├── main.py
├── config.yaml
├── requirements.txt
├── .gitignore
└── README.md

````

Each module maps directly to a conceptual block in the modeling pipeline.

---

## 📊 Dataset Description

### Real Battery Data (EV Lab)

Collected from a battery test bench:

- Current (A)  
- Voltage (V)  
- Temperature (°C)  
- Capacity (Ah)  
- Time (timestamps)  
- Cycle number  
- Charge / Discharge state  

### Synthetic Data (Fallback)

Used when real data is incomplete:

- Sinusoidal loads  
- Pulsed current profiles  
- High-frequency noisy loads  
- Realistic EV driving patterns  

---

## 🔧 Data Preprocessing

- Missing value handling  
- Time-series resampling  
- Cycle segmentation  
- Numerical differentiation (dI/dt)  
- Normalization & scaling  
- Capacity drop computation  

---

## ⚙️ Feature Engineering: Load Shape Toxicity

Each cycle is summarized using four physically meaningful coefficients:

| Feature | Definition | Interpretation |
|------|-----------|---------------|
| C1 | mean(I) | Average stress level |
| C2 | mean(dI/dt) | Spike-induced damage |
| C3 | std(I) | Oscillation amplitude |
| C4 | mean(I²) | Energy-weighted stress |

These features power both ML models and interpretability analysis.

---

## 📈 Exploratory Data Analysis (EDA)

- Correlation heatmaps  
- Stress vs capacity plots  
- Cycle-wise degradation trends  
- Cluster visualization of load shapes  

**Key Insight:**  
Current derivative (dI/dt) correlates more strongly with degradation than
energy throughput alone.

---

## 🤖 Machine Learning Models

### Regression (Capacity Fade Prediction)

- Linear Regression  
- Random Forest Regressor  
- Support Vector Regressor (SVR)  

### Unsupervised Learning

- KMeans clustering  
- Pattern discovery in load shapes  

---

## 🧬 Deep Learning: Neural Operator (DeepONet)

### Why DeepONet?

DeepONet is designed for **Function → Scalar mappings**, which exactly matches:

\[
I(t) \rightarrow \text{Stress / Degradation}
\]

### Architecture

- **Branch Network**: Learns waveform & derivative behavior  
- **Trunk Network**: Learns time dependence  
- Elementwise product + summation  

### Physics-Informed Loss

\[
\mathcal{L} = \text{MSE} + \lambda \cdot \mathbb{E}[(dI/dt)^2]
\]

This enforces:

- Smoothness  
- Physical plausibility  
- Numerical stability  

---

## 🛡 Stress & Safety Modeling

For each cycle:

- Stress value is predicted  
- Equivalent Stress Cycles (ESC) computed  
- Cycles classified as:
  - **Safe**
  - **Dangerous**

Thresholds use percentile-based stress limits.

---

## 💬 AI Chatbot Interface

A lightweight analytics chatbot enables natural-language queries:

Examples:

- “What is the mean stress?”  
- “Which cycles are dangerous?”  
- “Show stress vs capacity plot”  
- “Cluster-wise statistics”  

Demonstrates AI-powered battery analytics.

---

## 🌐 Streamlit Research Dashboard

An interactive dashboard allows:

- Dataset upload  
- Stress visualization  
- Safe vs dangerous cycle identification  
- Capacity fade & RUL insights  

Run locally:

```bash
streamlit run app/streamlit_app.py
````

---

## 🧪 Tech Stack

### Programming & Data

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* Random Forest
* SVR
* KMeans

### Deep Learning

* PyTorch
* Neural Operators (DeepONet)

### AI / NLP

* Rule-based chatbot
* GPT-style extensibility

---

## 🔍 Key Findings

* Battery stress is **path-dependent**, not cycle-dependent
* High dI/dt causes disproportionate damage
* ESC outperforms raw cycle count
* Neural Operators learn degradation functionals effectively
* ML models identify toxic load shapes

---

## 🚀 Applications

* Electric Vehicle Battery Management Systems (BMS)
* Smart charging optimization
* Energy storage systems
* Predictive maintenance
* Warranty & lifecycle estimation
* Safety envelope monitoring

---

## 🔮 Future Work

* Multi-physics coupling (thermal + electrochemical)
* Transformer-based sequence models
* Online BMS deployment
* Real-time stress-aware charging control

---

## ⭐ Final Note

This project demonstrates a **next-generation AI framework** for
lithium-ion battery degradation modeling by:

* Learning degradation physics from data
* Modeling stress as a functional
* Integrating ML, DL, XAI, and analytics

**If you find this project useful, consider starring the repository.**

```

