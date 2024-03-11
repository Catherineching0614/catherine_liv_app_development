import streamlit as st
import firebase_admin #don't forget to install :)
from firebase_admin import credentials
from firebase_admin import auth

# The file that links to firebase and retrieves the user info
cred = credentials.Certificate("petorphine-0e63b8bb9433.json")
firebase_admin.initialize_app(cred)

# The code to check the user's login info or if they still need to sign up
def login():
    try:
        auth.get_user_by_email(email)
        st.success("You are logged in")
    except:
        st.warning("Log in failed")

# Create the design of the login page
def loginpage():
    global email
    st.title("Welcome to :blue[Petorphine]")

    # Create a selection box
    choice = st.selectbox("Login/Signup", ["Login","Sign Up"])

    # Login info for signed up users
    if choice == "Login":
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        st.button("Login", on_click=login)

    # Sign up info for new users
    else:
        st.selectbox("University", ["Leuphana University", "Hamburg Media School"])
        email = st.text_input("Email Address")
        username = st.text_input("Enter your username")
        password = st.text_input("Password", type="password")
        if st.button("Create Account"):
            auth.create_user(email=email, uid=username, password=password)
            st.success("Account created successfully!")
            st.markdown("Please log in using your email and password")
            st.balloons()