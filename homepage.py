import streamlit as st

# Create the design for the home page
def homepage():
    st.write('''Can not find anyone to take care of you beloved pet when you need to travel?
            Feeling like some pet-petting energy boost?  
            Welcome!!  
            This is Petorphine, an app to share location for pet-petting experience and pet-sitting work.
            You can share your favourite photos of you and your pet and make new friends with other pet owners!
            '''
            )
    st.header("", divider='blue')
    st.info('View our community gallery:', icon="🖼️")

    # Create columns for the community gallery
    col1, col2, col3 = st.columns(3)

    # Place images
    with col1:
       st.image("images/dog1.jpg")
       st.image("images/cat3.jpg")
       st.image("images/cat4.jpg")

    with col2:
       st.image("images/cat1.jpg")
       st.image("images/dog4.jpg")
       st.image("images/dog3.jpg")
       st.image("images/cat5.jpg")

    with col3:
       st.image("images/dog2.jpg")
       st.image("images/cat2.jpg")
       st.image("images/dog5.jpg")
       st.warning('Loading more...', icon="⏳")

    # Place an info box simulating loading process
    st.info('Get to know our best rated pet sitters!', icon="🐾")

    # Create columns for the best rated pet sitters
    col1, col2 = st.columns(2)

    # Place images and captions
    with col1:
       st.image("images/owner1.jpg", caption='Lara, 23, University Student')
       st.image("images/owner5.jpg", caption='Sabine, 31, Nanny')
       st.image("images/owner3.jpg", caption='Tanya, 29, Writer & Author')
       st.warning('Loading more...', icon="⏳")

    with col2:
       st.image("images/owner2.jpg", caption='Naomi, 27, Flight Attendant')
       st.image("images/owner4.jpg", caption='Jon, 32, Teacher')

    # To finish up the page
    st.header("", divider='blue') #just want a colour divider
    st.subheader("Look for any pets in your area or login to book a pet-sitting service!")
