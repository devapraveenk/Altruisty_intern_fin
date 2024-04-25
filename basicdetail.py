import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

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

def Basic_Details():
    st.title("Project Information")


    name = st.text_input("Name")
    phone_number = st.text_input("Phone Number")
    email = st.text_input("E-Mail")
    project_domain = st.text_input("Project Domain")
    project_title = st.text_input("Project Title")
    project_description = st.text_area("Project Description")
    user_photo = st.file_uploader("Upload Photo")
    company_logo = st.file_uploader("Upload Company Logo")

    if st.button("Submit"):
        data = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "project_domain": project_domain,
            "project_title": project_title,
            "project_description": project_description
        }
        if user_photo:
            pass
        if company_logo:
            pass
        db.collection("project_details").add(data)
        st.success("Project details submitted successfully!")
