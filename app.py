import streamlit as st
from datetime import datetime
from Hello import quiz,move
import firebase_admin
from firebase_admin import credentials, auth
from chatbot import re
from app1 import base
import os

st.set_page_config(page_title="Altruisty Guide",page_icon="book",layout="wide")
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



def main():
    
    st.title("Welcome to Altruisty StartUp Launchpad")

    # with st.sidebar:
    #     st.image('Logo.png')
    

    
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    def input():
        try:
            user=auth.get_user_by_email(email)
            # st.success('login Successfully')
            st.session_state.username = user.uid
            st.session_state.useremail = user.email

            st.session_state.signedout= True 
            st. session_state.signout= True

            

        except:

            st.warning('Login Failed')
    def output():
        st. session_state.signout = False
        st.session_state.signedout = False
        st. session_state. username =''
        
    if 'signedout' not in st.session_state:
        st. session_state.signedout = False
    if 'signout' not in st.session_state:
        st. session_state.signout = False

    if not st. session_state['signedout']:
        choice = st. selectbox ("Login/Signup", ['Login', 'Sign Up'])

        if choice=='Login':
            email=st.text_input('Email Address')
            password = st. text_input('Password', type='password')
            st. button( 'Login',on_click=input)
        else:
            email=st.text_input ("Email Address")
            password= st.text_input('Password',type='password')
            username = st. text_input('Enter your unique username' )
            if st.button("Create my account" ):
                user = auth. create_user(email = email, password = password, uid=username)
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
    
    if st.session_state.signout:
        # with st.sidebar:
        #     st.info('Welcome To Altruisty')
        #     st.button("Sign Out",on_click=output)
        
    
        base()
            # if c:
            #     with st.sidebar:
            #         st.button("Sign Out",on_click=output)



if __name__ == "__main__":
    main()
