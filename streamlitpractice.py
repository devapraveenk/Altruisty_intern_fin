import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def feedback():
    if not os.path.exists("altruisty-intern-183af2e62cbb.json"):
        st.error("Firebase credential file 'firebase.json' not found.")
        st.stop()

    if not firebase_admin._apps:
        cred = credentials.Certificate("altruisty-intern-183af2e62cbb.json")
        try:
            firebase_admin.initialize_app(cred)
        except ValueError:
            st.error("Firebase app already initialized. Please ensure that you're not initializing Firebase multiple times.")
            st.stop()


    db = firestore.client()
    st.title("Feedback Form")

    # Collect feedback details
    name = st.text_input("Name")
    phone_number = st.text_input("Phone Number")
    email = st.text_input("Email")
    website_rating = st.slider("Rate the model(1-5)", min_value=1, max_value=5)
    suggestions = st.text_area("Suggestions")
    expectation = st.text_area("Expectation in service")
    improvements = st.text_area("How can we improve?")
    service_rating = st.slider("Rate the model(1-5)", min_value=0, max_value=5)


    # Submit button
    if st.button("Submit"):
        # Store data in Firebase
        data = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "website_rating": website_rating,
            "suggestions": suggestions,
            "service_rating": service_rating,
            "expectation": expectation,
            "improvements": improvements
        }
        db.collection("project_details").add(data)
        st.success("feedback submitted successfully!")
