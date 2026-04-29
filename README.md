<div align="center">

#  CellCare
*Intelligent Battery Health Analytics*

*An end-to-end machine learning ecosystem for predicting lithium-ion battery health, forecasting Remaining Useful Life (RUL), and tracking capacity degradation.*

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E)](https://vitejs.dev/)
<br/>
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-%231E90FF.svg?style=for-the-badge&logo=XGBoost&logoColor=white)](https://xgboost.ai/)
<br/>
[![Vercel](https://img.shields.io/badge/Vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/)
[![Render](https://img.shields.io/badge/Render-%2346E3B7.svg?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

<br/>

[**Live Demo**](https://cellcare-olive.vercel.app/) &nbsp; • &nbsp;
[**Get Started**](#getting-started) &nbsp; • &nbsp;
[**Architecture**](#architecture) &nbsp; • &nbsp;
[**API Reference**](#api-reference) &nbsp; • &nbsp;
[**Report Issue**](https://github.com/KaleSujit9011/Green-Skills-AI-Internship-Project/issues)

</div>

---

##  Table of Contents

- [Overview](#-Overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [API Reference](#-api-reference)
- [Machine Learning Pipeline](#-machine-learning-pipeline)
- [Feature Engineering](#-feature-engineering)
- [Dataset](#-dataset)

---

##  Overview

**CellCare** is an intelligent battery health monitoring system that applies machine learning to predict the degradation of lithium-ion batteries. It ingests raw discharge cycle data, extracts statistical features from current signals, and uses trained models to forecast:

- **Current battery capacity** (Ah)
- **Remaining Useful Life (RUL)** in charge/discharge cycles
- **Health status** — `Safe`, `Warning`, or `Dangerous`
- **Stress level** — `Low`, `Medium`, or `High`
- **Future capacity** for the next 10 cycles (via LSTM)

The system is designed around the **NASA Battery Dataset (B0005)** and is split into a Python/FastAPI backend and a React/Vite frontend dashboard.

---

##  Features

| Feature | Description |
|---|---|
|  **Point Prediction** | Predict battery capacity and RUL from a single discharge cycle's features |
|  **Sequence Forecasting** | Use an LSTM model to forecast capacity for the next 10 charge/discharge cycles |
|  **CSV Upload** | Upload a `.csv` file of cycle data and receive instant predictions |
|  **Health Dashboard** | Visual cards showing health status, RUL, capacity, and stress level |
|  **Technical Dashboard** | View pre-generated analysis plots (capacity fade curves, feature importance, model comparison) |
|  **REST API** | Fully documented FastAPI backend with interactive Swagger UI |

---

##  Architecture

```
┌─────────────────────────────────────────────────────────┐
│      React Frontend (Vite)  —  Deployed on Vercel       │
│  ┌──────────────┐  ┌────────────────────┐  ┌──────────┐ │
│  │  NavBar.jsx  │  │ HealthDashboard.jsx│  │Technical │ │
│  └──────────────┘  │  FileUpload.jsx    │  │Dashboard │ │
│                    └────────────────────┘  └──────────┘ │
└─────────────────────────┬───────────────────────────────┘
                          │ HTTPS (Axios)
                          ▼
┌─────────────────────────────────────────────────────────┐
│      FastAPI Backend (API)  —  Deployed on Render       │
│   /predict   /predict_sequence   /predict_csv           │
│   /predict_sequence_csv          /plots/{name}          │
└────────────┬───────────────────────────────┬────────────┘
             │                               │
    ┌────────▼──────┐               ┌────────▼──────┐
    │  RF + XGBoost │               │ LSTM (PyTorch)│
    │  (joblib .pkl)│               │ (.pth weights)│
    └───────────────┘               └───────────────┘
```

---

##  Tech Stack

### Backend
| Layer | Technology |
|---|---|
| API Framework | FastAPI |
| Server | Uvicorn |
| ML Models | scikit-learn (Random Forest), XGBoost, PyTorch (LSTM) |
| Data Processing | NumPy, Pandas, SciPy |
| Model Serialization | joblib (sklearn/xgb), `torch.save` (LSTM) |
| Validation | Pydantic |

### Frontend
| Layer | Technology |
|---|---|
| Framework | React 19 + Vite |
| HTTP Client | Axios |
| Styling | Inline CSS (React style objects) |
| Build Tool | Vite |

---

##  Project Structure

```
01_CellCare/
├── backend/
│   ├── main.py              # FastAPI app — all API endpoints
│   └── schemas.py           # Pydantic request/response models
│
├── src/
│   ├── data_loader.py       # Load .mat files, extract discharge cycles
│   ├── features.py          # Statistical feature engineering (C1–C4)
│   ├── preprocessing.py     # Data cleaning & normalization
│   ├── models.py            # RF, XGBoost, LSTM training & evaluation
│   └── visualization.py     # Plot generation (saved to outputs/)
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx                        # Root component, page routing
│   │   └── components/
│   │       ├── NavBar.jsx                 # Navigation bar
│   │       ├── HealthDashboard.jsx        # Health status, RUL, capacity cards
│   │       ├── TechnicalDashboard.jsx     # Model analysis plots
│   │       └── FileUpload.jsx             # CSV upload & prediction trigger
│   ├── package.json
│   └── vite.config.js
│
├── data/
│   ├── raw/                 # Original NASA .mat files (B0005.mat, etc.)
│   └── processed/           # Extracted feature CSVs (battery_features.csv)
│
├── models/
│   └── saved/               # Trained model artifacts
│       ├── rf_model.pkl
│       ├── xgb_model.pkl
│       └── lstm_model.pth
│
├── notebooks/
│   └── exploration.ipynb    # EDA and prototyping notebook
│
├── outputs/
│   └── plots/               # Generated PNG plots served by the API
│
├── requirements.txt
└── README.md
```

---

##  Live Environment

The project is fully deployed and accessible over the internet.

- **Frontend (Web App):** Deployed serverlessly via [Vercel](https://cellcare-olive.vercel.app/)
  - URL: `https://cellcare-olive.vercel.app/`
- **Backend (REST API):** Hosted as a Web Service on [Render](https://cellcare-api.onrender.com)
  - Base API URL: `https://cellcare-api.onrender.com`
  - Swagger UI Documentation: `https://cellcare-api.onrender.com/docs`

---

##  Local Development Setup

### Prerequisites

- Python ≥ 3.9
- Node.js ≥ 18
- The NASA Battery Dataset file `B0005.mat` placed in `data/raw/`

---

### Backend Setup

**1. Create and activate a virtual environment:**

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

**2. Install Python dependencies:**

```bash
pip install -r requirements.txt
```

**3. Prepare the data and train the models:**

```bash
# Extract features from raw .mat data
cd src
python data_loader.py

# Train Random Forest, XGBoost, and LSTM models
python models.py
```

> Trained models are saved to `models/saved/` and plots are saved to `outputs/plots/`.

**4. Start the API server:**

```bash
cd backend
uvicorn main:app --reload --port 8000
```

The API will be live at **http://localhost:8000**  
Interactive Swagger docs available at **http://localhost:8000/docs**

---

### Frontend Setup

**1. Install dependencies:**

```bash
cd frontend
npm install
```

**2. Start the development server:**

```bash
npm run dev
```

The React app will be available at **http://localhost:5173**

> Make sure the backend is running on port `8000` before using the frontend.

---

##  API Reference

The Live API is hosted at: `https://cellcare-api.onrender.com`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Health check — confirms the API is running |
| `POST` | `/predict` | Single-cycle prediction (capacity, RUL, health status, stress) |
| `POST` | `/predict_sequence` | LSTM forecast for next 10 cycles from 10 input cycles |
| `POST` | `/predict_csv` | Upload a CSV file for single-cycle prediction |
| `POST` | `/predict_sequence_csv` | Upload a CSV (≥10 rows) for LSTM sequence forecasting |
| `GET` | `/plots/{plot_name}` | Serve a pre-generated analysis plot by name |

### Example: `POST /predict`

**Request Body:**
```json
{
  "C1": 0.000032,
  "C2": 0.010484,
  "C3": -0.717731,
  "C4": 95.203672,
  "min_voltage": 2.612467
}
```

**Response:**
```json
{
  "capacity": 1.7823,
  "RUL": 76,
  "stress_level": "medium",
  "health_status": "Safe"
}
```

### Health Status Thresholds

| Status | Capacity |
|---|---|
| ✅ Safe | ≥ 1.6 Ah |
| ⚠️ Warning | 1.4 – 1.6 Ah |
| 🚨 Dangerous | < 1.4 Ah |

### CSV File Format

Uploaded CSV files must contain the following columns:

```
C1, C2, C3, C4, min_voltage
```

For sequence prediction, the file must have **at least 10 rows** (the first 10 rows are used as the LSTM input window).

---

##  Machine Learning Pipeline

### 1. Random Forest Regressor
- **Task:** Predict battery capacity from single-cycle statistical features
- **Library:** scikit-learn
- **Config:** 100 estimators, `random_state=42`
- **Split:** 70% train / 30% test

### 2. XGBoost Regressor
- **Task:** Capacity prediction (same task as RF, used for comparison)
- **Library:** XGBoost
- **Config:** 100 estimators, `random_state=42`

### 3. LSTM (Long Short-Term Memory)
- **Task:** Forecast the next 10 cycles of battery capacity given 10 historical cycles
- **Library:** PyTorch
- **Architecture:** 2-layer LSTM → Fully Connected layer
  - Input size: 5 features
  - Hidden size: 64
  - Output: 10 future capacity values
- **Training:** 50 epochs, Adam optimizer, MSE loss, lookback = 10, forecast = 10

### Evaluation Metrics
- **MAE** (Mean Absolute Error)
- **R²** (Coefficient of Determination)

---

##  Feature Engineering

Raw current signals from each discharge cycle are transformed into 5 statistical features, which serve as model inputs:

| Feature | Description |
|---|---|
| `C1` | Mean of dI/dt (average rate of current change) |
| `C2` | Standard deviation of dI/dt |
| `C3` | Skewness of dI/dt |
| `C4` | Kurtosis of dI/dt |
| `min_voltage` | Minimum measured terminal voltage during discharge |

> `dI/dt` (rate of change of current with respect to time) captures the dynamic load behaviour of the battery across each cycle.

---

##  Dataset

This project uses the **NASA Randomized Battery Usage Data Set**, specifically battery `B0005`.

- **Source:** [NASA Prognostics Center of Excellence Data Repository](https://www.nasa.gov/content/prognostics-center-of-excellence-data-set-repository)
- **Format:** MATLAB `.mat` files
- **Content:** Charge, discharge, and impedance cycles with measurements of voltage, current, temperature, and capacity

Place the raw `.mat` file at:
```
data/raw/B0005.mat
```

---

##  Author

**Sujit Kale**  
Green Skills AI Internship Project  
[GitHub](https://github.com/KaleSujit9011)

---

*Built with ❤️ using Python, FastAPI, PyTorch, and React.*
