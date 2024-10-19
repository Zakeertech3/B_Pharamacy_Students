import streamlit as st
from utils.drug_utils import get_drug_info
from utils.mcq_utils import get_mcq_data
import random

# Title of the app
st.title("B. Pharmacy Student Helper")

# Sidebar for navigation
st.sidebar.title("Navigation")
menu = ["Home", "Drug Database", "Flashcards", "Study Resources", "Exam Preparation", "Career Advice"]
choice = st.sidebar.selectbox("Select a feature", menu)

# Home Section
if choice == "Home":
    st.subheader("Welcome to the B. Pharmacy Student Helper App")
    st.write("This app provides valuable resources for B. Pharmacy students to aid their studies.")

# Drug Database Section
if choice == "Drug Database":
    st.subheader("Search Drug Information")
    drug = st.text_input("Enter Drug Name")
    if drug:
        result = get_drug_info(drug)
        if result is not None:
            st.write(result)
        else:
            st.write(f"No data found for {drug}")

# Flashcards Section
if choice == "Flashcards":
    st.subheader("Flashcards for Learning Drugs")
    mcq_data = get_mcq_data()
    question, details = random.choice(list(mcq_data.items()))
    st.write(f"Question: {question}")
    answer = st.radio("Choose an answer:", details['options'])
    if st.button("Check Answer"):
        if answer == details['answer']:
            st.write("Correct!")
        else:
            st.write(f"Incorrect. The correct answer is {details['answer']}.")

# Study Resources Section
if choice == "Study Resources":
    st.subheader("Useful Study Resources")
    st.write("Here are some useful links for studying:")
    st.markdown("[Pharmacology Textbook](https://example.com)")
    st.markdown("[B. Pharmacy Notes](https://example.com)")

# Exam Preparation Section
if choice == "Exam Preparation":
    st.subheader("Practice with Exam Questions")
    # Here you can add more MCQ-related code
    st.write("Example questions and answers will be shown here.")

# Career Advice Section
if choice == "Career Advice":
    st.subheader("Pharmacy Career Tips")
    st.write("Career tips, job opportunities, and internships.")
