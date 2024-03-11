import streamlit as st
import pandas as pd
import numpy as np

# Create the design of the track a pet page
# Create a definition that places a map that simulates the location of pets
def map():
    df = pd.DataFrame(
        np.random.randn(100, 2) / [80, 50] + [53.56, 9.99],
        columns=['lat', 'lon'])
    st.map(df)

# Create a definition that allows the user to share their location
def location():
    # Place a toggle button
    on = st.toggle('Show your location?')
    if on:
        st.write('📌🗺️ Other users might be on their way to visit you!')
    else:
        st.write('⛔📌🗺️ GPS is off, enjoy your comfort alone walk!')