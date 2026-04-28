import streamlit as st
import Background
import pandas as pd
import base64
from pathlib import Path
from Season1News import news
from Articles import Article1

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
    tab1, tab2, tab3, tab4 = st.tabs(["News","The Teams","Schedule","Results"])
    
    with tab1:
        news()
        Article1.article()
         
    with tab2:
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
            role = ["IGL","","",""]
            Brentuar = ["Brentuar","PretZilla","Queen","Newman"]
            pk = ["PK","Joshua Rosario","Eddie Tavera Jr.","Josh Anderson"]
            data = {
                "Role": role,
                "Team Brentuar": Brentuar,
                "Team PK": pk
            }
            df = pd.DataFrame(data)
            st.dataframe(df, hide_index=True)
        with st.expander(f"![Logo](data:image/png;base64,{f1_img_base64})"):
            role = ["IGL","","",""]
            Brentuar = ["Brentuar","Newman","Nick Beglin","Erick Tavera"]
            pk = ["PK","Josh Anderson","Josh Crane","Josh Rosario"]
            data = {
                "Role": role,
                "Team Brentuar": Brentuar,
                "Team PK": pk
            }
            df = pd.DataFrame(data)
            st.dataframe(df, hide_index=True)
        with st.expander(f"![Logo](data:image/png;base64,{halo_img_base64})"):
            role = ["IGL","","",""]
            Brentuar = ["Brentuar","Grayson Simmons","Erick Tavera","TBD"]
            pk = ["Connor Boyd","PK","Josh Anderson","Eddie Tavera Jr."]
            data = {
                "Role": role,
                "Team Brentuar": Brentuar,
                "Team PK": pk
            }
            df = pd.DataFrame(data)
            st.dataframe(df, hide_index=True)

    with tab3:
        event = ["Fall Guys","Halo Infinite","F1 25"]
        date = ["Wednesday April 29, 2026","Wednesday May 6, 2026","Wedesday May 13, 2026"]
        data = {
            "Event": event,
            "Date": date
        }
        df = pd.DataFrame(data)
        st.dataframe(df, hide_index=True)

    with tab4:
        st.markdown('''coming soon''')
        #TODO Individuals Bar Graph Per Game
        #TODO Individuals Line Chart
        #TODO Team Stacked Bar Chart (each game is a stack portion)
        #TODO Team Line Chart

    Background.page()