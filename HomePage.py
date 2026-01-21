import streamlit as st
from PIL import Image

logo_no_laurel = Image.open("./Images/logo-no-laurel.png")

def page():
    st.image(logo_no_laurel)
    st.divider()