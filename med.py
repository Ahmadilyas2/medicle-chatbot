# Streamlit app layout
import streamlit as st
from transformers import pipeline

# Load the QA model
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

st.title("Health Symptoms Chatbot")

st.write("Enter your symptoms or questions below, and get a recommendation on whether to see a doctor.")

# User input section
user_input = st.text_input("Describe your symptoms:")

if user_input:
    # Provide a general context
    context = "Please note this is a basic demo and not a medical substitute. Seek professional medical advice."
    
    # Get the answer from the model
    answer = qa_pipeline(question=user_input, context=context)
    
    # Show the answer on the Streamlit app
    st.write("Suggested Advice: ", answer['answer'])

    # Optional: Add a disclaimer
    st.write("**Disclaimer**: This chatbot provides suggestions based on your input. It is not a substitute for professional medical advice.")
