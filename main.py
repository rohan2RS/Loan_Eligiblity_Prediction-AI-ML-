import streamlit as st
import pickle
import numpy as np



# Load model with caching
@st.cache_data
def load_model():
    return pickle.load(open('loan_prediction_model.pkl', 'rb'))

model = load_model()

st.title("Loan Approval Prediction App")

# Input fields
gender = st.selectbox("Gender", ['Male', 'Female'])
married = st.selectbox("Married", ['Yes', 'No'])
dependents = st.selectbox("Dependents", ['0', '1', '2', '3+'])
education = st.selectbox("Education", ['Graduate', 'Not Graduate'])
self_employed = st.selectbox("Self Employed", ['Yes', 'No'])
applicant_income = st.number_input("Applicant Income")
coapplicant_income = st.number_input("Co applicant Income")
loan_amount = st.number_input("Loan Amount")
loan_term = st.selectbox("Loan Term", [360.0, 120.0, 180.0, 240.0])
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ['Urban', 'Rural', 'Semiurban'])

# Convert inputs to model format
input_data = np.array([[
    0 if gender == 'Female' else 1,
    1 if married == 'Yes' else 0,
    {'0': 0, '1': 1, '2': 2, '3+': 3}[dependents],
    0 if education == 'Graduate' else 1,
    1 if self_employed == 'Yes' else 0,
    applicant_income,
    coapplicant_income,
    loan_amount,
    loan_term,
    credit_history,
    {'Urban': 2, 'Rural': 0, 'Semiurban': 1}[property_area]
]]).reshape(1, -1)

if st.button("Predict Loan Approval"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Not Approved")


print(model.n_features_in_)
