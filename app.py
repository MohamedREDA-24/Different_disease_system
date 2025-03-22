import streamlit as st
from streamlit_option_menu import option_menu
import requests

# Streamlit Page Configuration
st.set_page_config(
    page_title="Health Assistant",
    layout="wide",
    page_icon="🧑‍⚕️"
)

# API Configuration
API_URL = "http://localhost:8000"

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Function to validate user inputs
def validate_inputs(inputs):
    try:
        return {k: float(v) for k, v in inputs.items() if v.strip() != ''}
    except ValueError:
        st.error("Please enter valid numerical values for all fields")
        return None

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)
    inputs = {
        'Pregnancies': col1.text_input('Number of Pregnancies'),
        'Glucose': col2.text_input('Glucose Level'),
        'BloodPressure': col3.text_input('Blood Pressure value'),
        'SkinThickness': col1.text_input('Skin Thickness value'),
        'Insulin': col2.text_input('Insulin Level'),
        'BMI': col3.text_input('BMI value'),
        'DiabetesPedigreeFunction': col1.text_input('Diabetes Pedigree Function'),
        'Age': col2.text_input('Age of the Person')
    }

    # Prediction button
    if st.button('Diabetes Test Result'):
        validated = validate_inputs(inputs)
        if validated:
            try:
                response = requests.post(f"{API_URL}/predict/diabetes", json=validated)
                if response.status_code == 200:
                    result = "diabetic" if response.json()['prediction'] else "not diabetic"
                    st.success(f'The person is {result}')
                else:
                    st.error("Prediction failed")
            except requests.ConnectionError:
                st.error("Could not connect to API server")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)
    inputs = {
        'age': col1.text_input('Age'),
        'sex': col2.text_input('Sex (1 = male; 0 = female)'),
        'cp': col3.text_input('Chest Pain types (0-3)'),
        'trestbps': col1.text_input('Resting Blood Pressure'),
        'chol': col2.text_input('Serum Cholestoral in mg/dl'),
        'fbs': col3.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)'),
        'restecg': col1.text_input('Resting Electrocardiographic results (0-2)'),
        'thalach': col2.text_input('Maximum Heart Rate achieved'),
        'exang': col3.text_input('Exercise Induced Angina (1 = yes; 0 = no)'),
        'oldpeak': col1.text_input('ST depression induced by exercise'),
        'slope': col2.text_input('Slope of the peak exercise ST segment (0-2)'),
        'ca': col3.text_input('Major vessels colored by flourosopy (0-3)'),
        'thal': col1.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    }

    # Prediction button
    if st.button('Heart Disease Test Result'):
        validated = validate_inputs(inputs)
        if validated:
            try:
                response = requests.post(f"{API_URL}/predict/heart", json=validated)
                if response.status_code == 200:
                    result = "having heart disease" if response.json()['prediction'] else "not having heart disease"
                    st.success(f'The person is {result}')
                else:
                    st.error("Prediction failed")
            except requests.ConnectionError:
                st.error("Could not connect to API server")

# Parkinson's Prediction Page
if selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")

    # Input fields
    col1, col2, col3, col4, col5 = st.columns(5)
    inputs = {
        'fo': col1.text_input('MDVP:Fo(Hz)'),
        'fhi': col2.text_input('MDVP:Fhi(Hz)'),
        'flo': col3.text_input('MDVP:Flo(Hz)'),
        'Jitter_percent': col4.text_input('MDVP:Jitter(%)'),
        'Jitter_Abs': col5.text_input('MDVP:Jitter(Abs)'),
        'RAP': col1.text_input('MDVP:RAP'),
        'PPQ': col2.text_input('MDVP:PPQ'),
        'DDP': col3.text_input('Jitter:DDP'),
        'Shimmer': col4.text_input('MDVP:Shimmer'),
        'Shimmer_dB': col5.text_input('MDVP:Shimmer(dB)'),
        'APQ3': col1.text_input('Shimmer:APQ3'),
        'APQ5': col2.text_input('Shimmer:APQ5'),
        'APQ': col3.text_input('MDVP:APQ'),
        'DDA': col4.text_input('Shimmer:DDA'),
        'NHR': col5.text_input('NHR'),
        'HNR': col1.text_input('HNR'),
        'RPDE': col2.text_input('RPDE'),
        'DFA': col3.text_input('DFA'),
        'spread1': col4.text_input('spread1'),
        'spread2': col5.text_input('spread2'),
        'D2': col1.text_input('D2'),
        'PPE': col2.text_input('PPE')
    }

    # Prediction button
    if st.button("Parkinson's Test Result"):
        validated = validate_inputs(inputs)
        if validated:
            try:
                response = requests.post(f"{API_URL}/predict/parkinsons", json=validated)
                if response.status_code == 200:
                    result = "having Parkinson's disease" if response.json()['prediction'] else "not having Parkinson's disease"
                    st.success(f'The person is {result}')
                else:
                    st.error("Prediction failed")
            except requests.ConnectionError:
                st.error("Could not connect to API server")