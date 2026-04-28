import streamlit as st
import base64
from pathlib import Path
import Background
import pandas as pd

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
        st.markdown("Any or all of the modes listed below will be played. A win in any of them will result in the number of points listed. Each team can earn a maximum of 80 points throughout this game event. There will be no cap on individual points for the overall individual scoring.")
        mode = ["Dynamic Duos",
                "Ball Blast",
                "Fall Ball Cup",
                "Royal Fumble",
                "Pegwin Palooza",
                "Jump Around",
                "Duos",
                "Day at the Races",
                "Thin Ice",
                "Solos"]
        points = [10,10,10,10,10,10,10,10,10,20]
        data = {
            "Mode": mode,
            "Points per Win": points
        }
        df = pd.DataFrame(data)
        st.dataframe(df, hide_index=True)
    
    with st.expander(f"![Logo](data:image/png;base64,{f1_img_base64})"):
        st.subheader("Formula 1 2025 Regulations")
        st.markdown("The race will utlize the regulations and rules set within The Alternative's Season 4 F125 season. This specific event will be consist of a Short Qulifying session, a Sprint, and a reverse grid Race set by the results of the Sprint. A team will be capped at 80 points during this game event. There will be no cap on individual points for the overall individual scoring.")
        place = ["1st","2nd","3rd","4th","5th","6th","7th","8th"]
        sprint_points = [8,7,6,5,4,3,2,1]
        race_points = [15,13,11,9,7,5,3,1]
        data = {
            "Position": place,
            "Sprint Points": sprint_points,
            "Race Points": race_points
        }
        df = pd.DataFrame(data)
        st.dataframe(df, hide_index=True)
        st.markdown("A singular bonus point will be awarded for each of the following: Pole Position, Sprint Fastest Lap, Race Fastest Lap, Race Driver of the Day, Race Cleanest Driver, Race Most Overtakes")
    
    with st.expander(f"![Logo](data:image/png;base64,{halo_img_base64})"):
        st.subheader("Halo Infinite Regulations")
        st.markdown("A single FFA Slayer and a single Team Slayer will be played as warmups. The following games will all be played in the order listed below and scoring will be awarded as described. A team will be capped at 80 points during this game event. There will be no cap on individual points for the overall individual scoring.")
        st.markdown("Game Modes: Assault One Bomb, Land Grab, Oddball, Capture the Flag")
        categories = ["Game Mode Win","Kill","Assist","Team Kill + Assist Maximum"]
        halo_points = [10,0.1,0.025,40]
        data = {
            "Category": categories,
            "Points": halo_points,
        }
        df = pd.DataFrame(data)
        st.dataframe(df, hide_index=True)

    Background.page()
    