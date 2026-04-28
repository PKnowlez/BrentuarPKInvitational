import streamlit as st
from PIL import Image
import Background
from Season1News import news

logo_no_laurel = Image.open("./Images/logo-no-laurel.png")

def page():
    st.image(logo_no_laurel)
    st.divider()

    news()

    Background.page()