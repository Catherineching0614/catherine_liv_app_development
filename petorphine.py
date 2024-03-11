import streamlit as st
from track_a_pet import map, location
from pet_sitting import pet_sitting, selectionbox
from homepage import homepage
from login import loginpage

# Set the page config info
st.set_page_config(
    page_title="Petorphine",
    page_icon="🐶")

# Definition to display successfully saved changes
def save_changes():
    st.success("Changes saved successfully!")

# Creating a side menu bar
menu = ["Home Page", "Pet Sitting", "Track a Pet", "My Profile", "Login"]
choice = st.sidebar.selectbox("Menu", menu)

# Create the homepage
if choice == "Home Page":
    st.image("images/petorphine.png")
    st.header("PETORPHINE 🐱 🐶")
    # some fun balloons
    st.balloons()
    homepage()


# Create the pet sitting page
elif choice == "Pet Sitting":
    st.header("Welcome to Pet Sitting")#, divider='blue')
    st.image("images/banner.png")
    st.subheader("", divider='blue')
    st.subheader("Find a home to sit a pet:")
    pet_sitting()
    selectionbox()

# Create the track a pet page
elif choice == "Track a Pet":
    st.header("Track a Pet and get your Petorphine", divider='blue')
    st.subheader("Pets nearby:")
    map()
    st.subheader("Share your pets location:")
    location()

# Create the my profile page
elif choice == "My Profile":
    st.header("My Profile", divider='blue')
    # Create a file uploading gadget
    file_upload = st.file_uploader("Upload a photo")
    # Create a widget able to take photo
    camera_upload = st.camera_input("or Take a photo")
    # Create a function to respond when files are uploaded successfully
    photo_uploaded_successfully = False
    if file_upload or camera_upload:
        photo_uploaded_successfully = True
        st.success("Photos are uploaded successfully")

    # Create boxes for user input
    st.text_input("Animal's Name")
    st.text_input("Animal's Personality")
    st.text_input("Owner's Name")
    st.text_input("Profile (Special Notes)")
    st.button("Save Changes", on_click=save_changes)

# Create the login page
elif choice == "Login":
    loginpage()
