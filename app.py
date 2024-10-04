import pickle
import streamlit as st
import numpy as np

# Load the trained model
pickle_in = open('save_model.pkl', 'rb')
classifier = pickle.load(pickle_in)

# Define the function for making predictions
def prediction(Year_Birth, Education, Marital_Status, Kidhome, Teenhome, Recency, Complain, Response, Purchases, Campaign, Incomes, Expense):

    
    # Make prediction
    pred = classifier.predict([[Year_Birth, Education, Marital_Status, Kidhome, Teenhome, Recency, Complain, Response, Purchases, Campaign, Incomes, Expense]])
    return pred

# Main function to create the Streamlit app
def main():
    st.title("Customer Segmentation Prediction")
    
    # Collect user input
    Year_Birth = st.number_input("Year of Birth", min_value=0, max_value=2022, step=1)
    Education = st.selectbox("Education", ["Basic", "Graduated", "PHD"])
    Marital_Status = st.selectbox("Marital Status", ["single", "relationship"])
    Kidhome = st.number_input("Number of Children at Home", min_value=0)
    Teenhome = st.number_input("Number of Teenagers at Home", min_value=0)
    Recency = st.number_input("Recency", min_value=0)
    Complain = st.selectbox("Complain", ["NO", "YES"])
    Response = st.selectbox("Response", ["NO", "YES"])
    Purchases = st.number_input("Number of Purchases", min_value=0)
    Campaign = st.selectbox("Campaign", ["Accepted 0 Campaign", "Accepted 1 Campaign", "Accepted 2 Campaign", "Accepted 3 Campaign", "Accepted 4 Campaign"])
    Incomes = st.selectbox("Incomes", ["Below 25000", "Income 25000-50000", "Income 50000-100000", "Above 100000"])
    Expense = st.selectbox("Expense", ["Below 500", "Expense 500-1000", "Above 1000"])
    
    # Convert categorical inputs to numerical values
    Education = {"Basic": 0, "Graduated": 1, "PHD": 2}[Education]
    Marital_Status = {"single": 0, "relationship": 1}[Marital_Status]
    Complain = {"NO": 0, "YES": 1}[Complain]
    Response = {"NO": 0, "YES": 1}[Response]
    Campaign = {"Accepted 0 Campaign": 0, "Accepted 1 Campaign": 1, "Accepted 2 Campaign": 2, "Accepted 3 Campaign": 3, "Accepted 4 Campaign": 4}[Campaign]
    Incomes = {"Below 25000": 1, "Income 25000-50000": 2, "Income 50000-100000": 3, "Above 100000": 0}[Incomes]
    Expense = {"Below 500": 0, "Expense 500-1000": 1, "Above 1000": 2}[Expense]
    
    # Make prediction
    if st.button("Predict"):
        result = prediction(Year_Birth, Education, Marital_Status, Kidhome, Teenhome, Recency, Complain, Response, Purchases, Campaign, Incomes, Expense)
        st.success(f"The predicted cluster is {result}")

if __name__ == "__main__":
    main()
