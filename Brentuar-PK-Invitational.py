import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import plotly.express as px
import Sidebar, HomePage, GamesRegulations, Season1

## ----- App Format ----- ##
st.set_page_config(page_title="Home Page", initial_sidebar_state="collapsed", layout="wide")

APP_NAME = "Brentuar PK Invitational" 

st.markdown(
    f"""
    <meta name="application-name" content="{APP_NAME}">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="{APP_NAME}">
    <meta name="mobile-web-app-capable" content="yes">
    """,
    unsafe_allow_html=True
)

selection = Sidebar.Sidebar()

if selection == "Home Page":
    HomePage.page()
elif selection == "Games & Regulations":
    GamesRegulations.page()
elif selection == "Season 1":
    Season1.page()
else:
    st.subheader("Welcome to the Brentuar PK Invitational")