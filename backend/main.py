from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas  import BatteryInput, PredictionOutput
from fastapi.responses import FileResponse
import numpy as np

import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rf_model = joblib.load(os.path.join(BASE_DIR, 'models', 'saved', 'rf_model.pkl'))
xgb_model = joblib.load(os.path.join(BASE_DIR, 'models', 'saved', 'xgb_model.pkl'))
print("Models loaded successfully!")

app = FastAPI(title="Battery Degradation API")

# allows React frontend to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "running", "message": "Battery API is online"}

@app.get("/plots/{plot_name}")
def get_plot(plot_name: str):
    plot_path = os.path.join(BASE_DIR, 'outputs', 'plots', f'{plot_name}.png')
    print(f"Looking for plot at: {plot_path}")  # add this
    if not os.path.exists(plot_path):
        raise HTTPException(status_code=404, detail="Plot not found")
    return FileResponse(plot_path, media_type="image/png")

@app.post("/predict", response_model=PredictionOutput)
def predict(data: BatteryInput):
    # prepare input features
    features = np.array([[
        data.C1, data.C2, data.C3,
        data.C4, data.min_voltage
    ]])

    # predict capacity
    capacity = float(rf_model.predict(features)[0])

    # calculate RUL
    eol_capacity = 1.4
    RUL = max(0, int((capacity - eol_capacity) * 200))

    # determine stress level
    c1_abs = abs(data.C1)
    if c1_abs < 0.000027:
        stress_level = "low"
    elif c1_abs < 0.000035:
        stress_level = "medium"
    else:
        stress_level = "high"

    # determine health status
    if capacity >= 1.6:
        health_status = "Safe"
    elif capacity >= 1.4:
        health_status = "Warning"
    else:
        health_status = "Dangerous"

    return PredictionOutput(
        capacity=round(capacity, 4),
        RUL=RUL,
        stress_level=stress_level,
        health_status=health_status
    )

