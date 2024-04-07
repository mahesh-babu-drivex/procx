import streamlit as st

# Set background image
background_image = 'https://mfiles.alphacoders.com/101/1011744.png'
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('{background_image}');
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Container style
container_style = """
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: rgba(255, 255, 255, 0.4);
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
"""

# App icon
icon_url = 'https://procx.drivex.dev/loginPage/procx-logo.png'

# Title and content
st.markdown(
    f"""
    <div style="{container_style}">
        <img src="{icon_url}" alt="App Icon" width="200" style="margin-bottom: 20px;">
        <div style="text-align: center; color: orange;">
            <p style="color: black;">Download our mobile app to stay connected</p>
            <p style="color: red;"><span style="color: red;">*</span> Only for Android users</p>
            <a href="https://drive.usercontent.google.com/download?id=1l00hPKlh7BV_uLNnclX0IxAHqH5icYd-&export=download&authuser=0" style="background-color: #007bff; color: #fff; padding: 10px 20px; border-radius: 5px; text-decoration: none; transition: background-color 0.3s; margin-bottom: 20px; display: inline-block;" target="_blank">Download Mobile App</a>
        </div>
        <div style="text-align: center; color: orange;">
            <p style="color: black;">Click on ProcX website:</p>
            <p style="color: red;"><span style="color: red;">*</span> Only for ProcX admins</p>
            <a href="https://procx.drivex.in/" style="background-color: #007bff; color: #fff; padding: 10px 20px; border-radius: 5px; text-decoration: none; transition: background-color 0.3s;" target="_blank">ProcX Web</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
