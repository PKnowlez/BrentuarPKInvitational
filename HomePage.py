import streamlit as st
from PIL import Image
import base64

logo_no_laurel = Image.open("./Images/logo-no-laurel.png")

def page():
    st.image(logo_no_laurel)
    st.divider()

    def get_base64(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    bin_str = get_base64('./Images/logo-background.png')

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-attachment: fixed;
            background-size: cover;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )