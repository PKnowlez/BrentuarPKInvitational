import streamlit as st
import base64
from pathlib import Path

def get_image_as_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_path = Path("./Images/f1-logo.png")
f1_img_base64 = get_image_as_base64(img_path)
img_path = Path("./Images/halo-logo.png")
halo_img_base64 = get_image_as_base64(img_path)
img_path = Path("./Images/f1-logo.png")
f1_img_base64 = get_image_as_base64(img_path)

def page():
    with st.expander(f"![Logo](data:image/png;base64,{f1_img_base64})"):
        st.subheader("Formula 1 2025 Regulations")
    with st.expander(f"![Logo](data:image/png;base64,{halo_img_base64})"):
        st.subheader("Halo Infinite Regulations")
    