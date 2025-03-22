from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Load ML Models
working_dir = os.path.dirname(os.path.abspath(__file__))
models_path = {
    'diabetes': f'{working_dir}/Saved Models/diabetes_model.sav',
    'heart': f'{working_dir}/Saved Models/heart_disease_model.sav',
    'parkinsons': f'{working_dir}/Saved Models/parkinsons_model.sav'
}

models = {
    name: pickle.load(open(path, 'rb'))
    for name, path in models_path.items()
}

# Pydantic Models for Input Validation
class DiabetesInput(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float

class HeartInput(BaseModel):
    age: float
    sex: float
    cp: float
    trestbps: float
    chol: float
    fbs: float
    restecg: float
    thalach: float
    exang: float
    oldpeak: float
    slope: float
    ca: float
    thal: float

class ParkinsonsInput(BaseModel):
    fo: float
    fhi: float
    flo: float
    Jitter_percent: float
    Jitter_Abs: float
    RAP: float
    PPQ: float
    DDP: float
    Shimmer: float
    Shimmer_dB: float
    APQ3: float
    APQ5: float
    APQ: float
    DDA: float
    NHR: float
    HNR: float
    RPDE: float
    DFA: float
    spread1: float
    spread2: float
    D2: float
    PPE: float

# API Endpoints
@app.post("/predict/diabetes")
def predict_diabetes(data: DiabetesInput):
    features = list(data.dict().values())
    prediction = models['diabetes'].predict([features])[0]
    return {"prediction": int(prediction)}

@app.post("/predict/heart")
def predict_heart(data: HeartInput):
    features = list(data.dict().values())
    prediction = models['heart'].predict([features])[0]
    return {"prediction": int(prediction)}

@app.post("/predict/parkinsons")
def predict_parkinsons(data: ParkinsonsInput):
    features = list(data.dict().values())
    prediction = models['parkinsons'].predict([features])[0]
    return {"prediction": int(prediction)}

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Health Assistant API!"}