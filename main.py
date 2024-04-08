import streamlit as st

# Set background image
background_image = ""
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('{background_image}');
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True,
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
    height:410px;
"""

# App icon
icon_url = "https://procx.drivex.dev/loginPage/procx-logo.png"

# Title and content
st.markdown(
    f"""
    <div style="{container_style}">
        <img src="{icon_url}" alt="App Icon" width="200" style="margin-bottom: 20px;">
        <div style="text-align: center; color: orange;">
            <p style="color: black;">Download our mobile app to stay connected</p>
            <p style="color: red;"><span style="color: red;">*</span> Only for Android users</p>
            <a href="https://drive.google.com/drive/folders/176QNjHtYKVNywe_zY-Um5Go7n4OgH4x8?usp=drive_link" style="background: linear-gradient(88deg,
                #e63c32 0%,
                #e94a2e 9%,
                #ee5e29 24%,
                #f16d25 42%,
                #f37523 64%,
                #f47823 100%); color: #fff; padding: 10px 20px; border-radius: 5px; text-decoration: none; transition: background-color 0.3s; margin-bottom: 20px; display: inline-block;" target="_blank">Download Mobile App</a>
        </div>
        <div style="text-align: center; color: orange;">
            <p style="color: black;">Click on ProcX website:</p>
            <p style="color: red;"><span style="color: red;">*</span> Only for ProcX admins</p>
            <a href="https://procx.drivex.in/" style="background: linear-gradient(88deg,
                #e63c32 0%,
                #e94a2e 9%,
                #ee5e29 24%,
                #f16d25 42%,
                #f37523 64%,
                #f47823 100%); color: #fff; padding: 10px 20px; border-radius: 5px; text-decoration: none; transition: background-color 0.3s;" target="_blank">ProcX Web</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Login and Feedback divs
st.markdown(
    f"""
    <div style="{container_style} display: flex; flex-direction: row;">
        <div style="text-align: center; color: orange; flex-grow: 1; margin-right: 10px;">
            <div style="background-color: rgba(255, 255, 255, 0.4); padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); margin-bottom: 30px; height:238px">
                <h6>Login Credentials</h2>
                <p style="color: purple;">For Login Credentials please contact- <br> <span  style="color: black;">Rishab, <a href="tel:908376373838">9548494539</a>, <a href="mailto:rishab.giri@drivex.in">rishab.giri@drivex.in</a> </span><br> or<br><span style="color: black;"> Durgaprasad, <a href="tel:8885456932">8885456932</a>, <a href="mailto:durga.rayudu@drivex.in ">durga.rayudu@drivex.in</a></p></span>
            </div>
        </div>
        <div style="text-align: center; color: orange; flex-grow: 1; margin-left: 10px;">
            <div style="background-color: rgba(255, 255, 255, 0.4); padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); margin-bottom: 30px; height:235px">
                <h6 style="padding-top:35px">Feedback</h2>
                <p style="color: purple;">Please click on the below link to share your feedback<br> <a href="https://forms.gle/hsMufT6vbGttqixw6" target="_blank">Click here</a></p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
