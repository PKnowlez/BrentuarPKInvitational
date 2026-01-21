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
img_path = Path("./Images/fallguys-logo.png")
fallguys_img_base64 = get_image_as_base64(img_path)

def page():

    st.markdown(
                """
                <style>
                    /* Target the summary (header) of the expander */
                    [data-testid="stExpander"] summary {
                        padding-top: 5px !important;
                        padding-bottom: 5px !important;
                        min-height: 50px; /* Force a specific height */
                        display: flex;
                        align-items: center;
                    }
                    
                    /* Ensure the title text and logo stay centered */
                    [data-testid="stExpander"] summary p {
                        font-size: 24px !important; /* Optional: Make text larger too */
                        margin-bottom: 0px;
                    }
                </style>
                """,
                unsafe_allow_html=True
    )   
    with st.expander(f"![Logo](data:image/png;base64,{fallguys_img_base64})"):
        st.subheader("Fall Guys Regulations")
    with st.expander(f"![Logo](data:image/png;base64,{f1_img_base64})"):
        st.subheader("Formula 1 2025 Regulations")
    with st.expander(f"![Logo](data:image/png;base64,{halo_img_base64})"):
        st.subheader("Halo Infinite Regulations")
    