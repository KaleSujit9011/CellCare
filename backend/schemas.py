from pydantic import BaseModel
from typing import List

class BatteryInput(BaseModel):
    C1: float
    C2: float
    C3: float
    C4: float
    min_voltage: float

class PredictionOutput(BaseModel):
    capacity: float
    RUL: int
    stress_level: str
    health_status: str

class SequencePredictionOutput(BaseModel):
    predicted_capacities: List[float]
    cycles_ahead: int
