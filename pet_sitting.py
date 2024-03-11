import streamlit as st
import datetime
import requests
import random

# Create the design of the pet sitting page
# Create a selection box for animal preference
def selectionbox():
    option = st.selectbox(
        'What type of animal you would like to sit?',
        ('Cat', 'Dog', 'Others'))
    if option == 'Cat':
        st.write('You selected 🐈')
        st.button("Cat Match",
                  help="Click to get a cat match",
                  on_click=place_cat_image)
    if option == 'Dog':
        st.write('You selected 🐕')
        st.button("Dog Match",
                  help="Click to get a dog match",
                  on_click=place_dog_image)
    if option == 'Others':
        st.write('You selected 🐻')
        st.button("Special Match",
                  help="Click to get a special match",
                  on_click=place_other_image)

# Definition for fetching cat matches
def get_content():
    """Access the API and get the images URL"""
    contents = requests.get('https://cataas.com//cat')
    # contents = requests.get('https://cataas.com//cat/gif')
    return contents.content

# Definition for fetching dog matches
def get_content2():
   """Makes GET request to https://dog.ceo/dog-api/ to fetch a random dog images URL"""
   response = requests.get("https://dog.ceo/api/breeds/image/random")
   if response.status_code == 200:
       data = response.json()
       return data.get("message")
   else:
       return None

# Definition for fetching other matches
def get_content3():
    """Access the API and get the images URL"""
    contents = requests.get('https://placebear.com/g/200/300')
    return contents.content

# Random pet profiles to the matching process
def pet_info():
    info=['''Animal's name: Jojo<br>  
           Animal's personality: Calm<br>  
           Owner's name: Joey<br>  
           <br>Profile: I like people rubbing my tummy. Do not touch my ass though! I will bite.
           ''',
          '''Animal's name: Kitty<br>  
                 Animal's personality: Passionate<br>  
                 Owner's name: Simon<br>  
                 <br>Profile: Feel free to give me treat :)
                 ''',
          '''Animal's name: Momo<br>  
                           Animal's personality: Sensitive<br>  
                           Owner's name: Ariel<br>  
                           <br>Profile: I might overreact when there is loud sound
                           '''
          ]
    return random.choice(info)

# Definition for accepting or declining the match
def confirm_deny_button():
    # Create two columns
    col1, col2 = st.columns(2)

    # Accept match
    col1.button("Confirm",
              on_click=yes)

    # Decline match
    col2.button("Deny",
              on_click=no)

# The responses to the user's choice
def yes():
    st.write('You have registered for a pet sitting volunteer work 🥰!!!')

def no():
    st.write('You have denied that match 🥲')

# Definition to place random cat image for the matches
def place_cat_image():
    write_pet_info = pet_info()
    col1, col2 = st.columns(2)

    """Place the cat images from the cataas.com API"""
    cat_image = get_content()
    col1.image(cat_image, width=200, caption='This is your match!!')
    col2.write(write_pet_info, unsafe_allow_html=True)
    st.subheader('''
    :blue[You found your cat match!]''')
    confirm_deny_button()

# Definition to place random dog image for the matches
def place_dog_image():
    write_pet_info = pet_info()
    col1, col2 = st.columns(2)
    dog_image = get_content2()
    col1.image(dog_image, width=200, caption='This is your match!!')
    col2.write(write_pet_info ,unsafe_allow_html=True)
    st.subheader('''
    :blue[You found your dog match!]''')
    confirm_deny_button()

# Definition to place other image for the matches
def place_other_image():
    # Create two columns
    col1, col2 = st.columns(2)
    other_image = get_content3()
    col1.image(other_image, width=200, caption='This is your match!!')
    col2.write('''
    Animal's name: Teddy  
      
    Animal's personality: Playful  
      
    Owner's name: The National Zoo  
      
    Profile: I like HONEY 
    ''')
    st.subheader('''
    :blue[You found a match? Oh no no no, this is just a joke]''')

# Create the parameter for the user's pet sitting preferences
# Ask the user for the area range
def area_range():
   # code to add a slider
   score = st.slider("Enter your km range:",
                     min_value=0,
                     max_value=100,
                     # this is the value the user sees when the app is opened
                     value=10
                     )
   if score:
       st.write("Your range is", score, "km")

# Ask the user for the date
def calender():
    d = st.date_input("When would you be free?", datetime.date(2024, 1, 1))
    st.write('Your have register for a pet sitting on:', d)

# Ask the user for the time
def time():
    t = st.time_input('Set a time for', datetime.time(8, 45))
    st.write('Time is set for', t)

# Adjust the dsign of the widgets to the page
def pet_sitting():
    col1, col2, col3 = st.columns(3)

    with col1:
       st.header("🏠")
       st.write("In what area are you available?")
       area_range()

    with col2:
       st.header("📅")
       st.write("Which day are you available?")
       calender()

    with col3:
       st.header("🕗")
       st.write("What time are you available?")
       time()