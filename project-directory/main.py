import streamlit as st

st.title("Credit Scoring Card Application")
st.write("Welcome to the Credit Scoring Card Application!")
st.write("This application allows you to input your financial information and receive a credit score based on our model.")

st.set_page_config(page_title = "Credit Scoring Card", layout = "centered")

st.subheader("Category 1 -------------")
col1, col2, col3 = st.columns(3)
age = col1.number_input("Age", min_value = 18, max_value = 70, value = 28, help = "Please choose your age here")
income = col2.number_input("Icome Annual", min_value = 30000, max_value = 1000000, value = 40000, help = "Your annual income")
loan_amount = col3.number_input("Loan amount", min_value = 1000, max_value = 1000000, value = 10000, help = "Your Loan amount")

st.subheader("Category 2 --------------")
col4, col5, col6 = st.columns(3)
tenure_months = col4.slider("Loan Tenure in months", min_value = 6, max_value = 120, step = 6)
loan_type = col5.radio("Loan Type", ["Secured, Unsecured"])
residence_type = col6.selectbox("Residence property", ["Rent", "Owner", "Mortgage"])

if st.button("Calculate the Score"):
    st.success("Calculations completed")    
