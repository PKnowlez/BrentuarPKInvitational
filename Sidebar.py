import streamlit as st
from PIL import Image

logo = Image.open("./Images/logo.png")
brentuar = Image.open("./Images/brentuar-logo.png")
pk = Image.open("./Images/pk-logo.png")

def Sidebar():
    with st.sidebar:
        st.image(logo)

        selection = st.selectbox("Select Page", ["Home Page", "Games & Regulations", "Season 1"])
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(brentuar)
        with col2:
            st.image(pk)

        link_text = "WATCH LIVE"
        link_url = "https://twitch.tv/brentuar/"
        st.markdown(f'<a href="{link_url}" target="_blank">{link_text}</a>', unsafe_allow_html=True)

    return selection