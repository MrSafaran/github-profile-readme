import streamlit as st

st.title(":gear: GitHub Profile Generator :gear:")

# Get Personal Info
st.header(":notebook: Personal Info")
with st.expander("Personal Info"):
    col1, col2 = st.columns(2)
    name = col1.text_input("Name")
    phone = col2.text_input("Phone")
    email = col1.text_input("Email")
    website = col2.text_input("Website")
    location = st.text_input("Location")

# Get Social Media
st.header(":iphone: Social Media")
with st.expander("Social Media"):
    st.caption("Enter your social media username (not the url):")
    col1 , col2 = st.columns(2)
    Linkedin = col1.text_input("Linkedin")
    Telegram = col2.text_input("Telegram")
    Instagram = col1.text_input("Instagram")
    Twitter = col2.text_input("Twitter")
    Github = col1.text_input("Github")
    Youtube = col2.text_input("Youtube")
    
