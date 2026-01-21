import streamlit as st
from PIL import Image

logo = Image.open("./Images/logo.png")

def Sidebar():
    with st.sidebar:
        st.image(logo)

        selection = st.selectbox("Select Page", ["Home Page", "Games & Regulations", "Season 1"])

    return selection