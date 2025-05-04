# Multiple Disease Prediction System

A comprehensive health assistant application that predicts multiple diseases using machine learning models. The system currently supports predictions for Diabetes, Heart Disease, and Parkinson's Disease.

## Features

- **Multiple Disease Prediction**: Predicts three different diseases:
  - Diabetes
  - Heart Disease
  - Parkinson's Disease
- **User-friendly Interface**: Built with Streamlit for an intuitive user experience
- **RESTful API**: FastAPI backend for model predictions
- **Real-time Predictions**: Instant results based on user input

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **API Communication**: requests

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MohamedREDA-24/Different_disease_system.git
cd Different_disease_system
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the FastAPI backend server:
```bash
uvicorn api:app --reload
```

2. In a new terminal, start the Streamlit frontend:
```bash
streamlit run app.py
```

3. Open your web browser and navigate to `http://localhost:8501`

## Project Structure

- `app.py`: Streamlit frontend application
- `api.py`: FastAPI backend server
- `requirements.txt`: Project dependencies
- `Saved Models/`: Directory containing trained machine learning models
- `Ml_Notebooks/`: Jupyter notebooks for model development and training

