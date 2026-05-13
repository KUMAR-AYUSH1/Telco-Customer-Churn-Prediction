import streamlit as st
import requests


st.title("Telco Customer Churn Prediction ")

st.write("Enter the customer details to predict churn.")


partner = st.sidebar.radio("Partner", ("Yes", "No"))
senior_citizen = st.sidebar.radio("Senior Citizen", ("Yes", "No"))
internet_service = st.sidebar.radio("Internet Service", ("DSL", "Fiber optic", "No"))
payment_method = st.sidebar.radio("Payment Method", ("Mailed check", "Bank transfer (automatic)", "Credit card (automatic)", "Electronic check"))
paperless_billing = st.sidebar.radio("Paperless Billing", ("Yes", "No"))
monthly_charges = st.number_input("Monthly Charges",max_value=120,min_value=18)
streaming_movies = st.sidebar.radio("Streaming Movies", ("Yes", "No"))
device_protection = st.sidebar.radio("Device Protection", ("Yes", "No"))
contract = st.sidebar.radio("Contract", ("Month-to-month", "Two year", "One year"))
tenure = st.number_input("Tenure",step=1,min_value=1,max_value=100)
dependents = st.sidebar.radio("Dependents", ("Yes", "No"))

data = {
    'Partner': partner,
    'SeniorCitizen': senior_citizen,
    'InternetService': internet_service,
    'PaymentMethod': payment_method,
    'PaperlessBilling': paperless_billing,
    'MonthlyCharges': monthly_charges,
    'StreamingMovies': streaming_movies,
    'DeviceProtection': device_protection,
    'Contract': contract,
    'tenure': tenure,
    'Dependents': dependents
}

response = requests.post('http://127.0.0.1:8000/predict', json=data)

if response.status_code == 200:
    result = response.json()
    # Display the prediction result
    st.write("Churn:", result['churn'])
    st.write("Churn Probability:", result['churn_probability'],"%")
    st.write("Discount:", result['discount'])
else:
    st.write("Error:", response.status_code)