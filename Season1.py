import streamlit as st
import Background
import pandas as pd
import base64
from pathlib import Path
from Articles import Article1
from Functions import StackedBarChart

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

# Helper function to process sheets for Halo results
def process_sheet(sheet_name):
    df = pd.read_excel('./Brentuar PK Invitational Season 1.xlsx', sheet_name=sheet_name)
    
    # Find the 'Total' column (case-insensitive)
    total_col_name = None
    for col in df.columns:
        if str(col).lower() == 'total':
            total_col_name = col
            break
    
    # If 'Total' column exists, keep only columns up to and including it
    if total_col_name:
        total_col_index = df.columns.get_loc(total_col_name)
        df = df.iloc[:, :total_col_index + 1]
    return df

def page():
    # tab1, tab2, tab3, tab4 = st.tabs(["News","The Teams","Schedule","Results"])
    
    # with tab1:
    #     if 'show_all_content' not in st.session_state:
    #         st.session_state.show_all_content = False

    #         #region latest article
            
    #         Article1.article()

    #         #endregion

    #         # ----------------------------------------------------------------------------------------------------------
    #         # "Show More/Less" button 
    #         if not st.session_state.show_all_content:
    #             if st.button('Show More'):
    #                 st.session_state.show_all_content = True
    #                 st.rerun()  # Rerun the app to show everything
    #         else: 
    #             if st.button('Show Less'):
    #                 st.session_state.show_all_content = False
    #                 st.rerun()

    #         if st.session_state.show_all_content:
                
    #             Article1.article()

    tab2, tab3, tab4 = st.tabs(["The Teams","Schedule","Results"])
         
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
            pk = ["PK","Joshua Rosario","Eddie Tavera Jr.","Connor Boyd"]
            data = {
                "Role": role,
                "Team Brentuar": Brentuar,
                "Team PK": pk
            }
            df = pd.DataFrame(data)
            st.dataframe(df, hide_index=True)
        with st.expander(f"![Logo](data:image/png;base64,{halo_img_base64})"):
            role = ["IGL","","",""]
            Brentuar = ["Brentuar","Grayson Simmons","Erick Tavera","Nick Beglin"]
            pk = ["Connor Boyd","PK","Josh Anderson","Eddie Tavera Jr."]
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
        col1, col2 = st.columns(2)

        with col1:
            with st.popover('Team Results'):
                sheet = pd.read_excel('./Brentuar PK Invitational Season 1.xlsx',sheet_name='Team Results')
                st.dataframe(sheet, hide_index=True)
            sheet = pd.read_excel('./Brentuar PK Invitational Season 1.xlsx',sheet_name='Team Results')
            colors = {
                "Team Brentuar": ["#ff0000","#ff7070","#f5b7b7"],
                "Team PK": ["#0000ff","#8080ff","#ccccff"]
            }
            fig1 = StackedBarChart(sheet,colors,'Team Results')
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            with st.popover('Individual Results'):
                sheet = pd.read_excel('./Brentuar PK Invitational Season 1.xlsx',sheet_name='Individual Results')
                st.dataframe(sheet, hide_index=True)
            sheet = pd.read_excel('./Brentuar PK Invitational Season 1.xlsx',sheet_name='Individual Results')
            colors = {
                "Brentuar": ["#ff0000","#ff7070","#f5b7b7"],
                "Newman": ["#ff0000","#ff7070","#f5b7b7"],
                "PretZilla": ["#ff0000","#ff7070","#f5b7b7"],
                "Queen": ["#ff0000","#ff7070","#f5b7b7"],
                "Nick": ["#ff0000","#ff7070","#f5b7b7"],
                "Erick": ["#ff0000","#ff7070","#f5b7b7"],
                "Grayson": ["#ff0000","#ff7070","#f5b7b7"],
                "PK": ["#0000ff","#8080ff","#ccccff"],
                "Josh Rosario": ["#0000ff","#8080ff","#ccccff"],
                "Connor": ["#0000ff","#8080ff","#ccccff"],
                "Eddie": ["#0000ff","#8080ff","#ccccff"],
                "Josh Crane": ["#0000ff","#8080ff","#ccccff"],
                "Josh Anderson": ["#0000ff","#8080ff","#ccccff"],
            }
            fig1 = StackedBarChart(sheet,colors,'Individual Results')
            st.plotly_chart(fig1, use_container_width=True)

        with st.expander(f"![Logo](data:image/png;base64,{fallguys_img_base64})"):
            sheet = pd.read_excel('./Brentuar PK Invitational Season 1.xlsx',sheet_name='Fall Guys Results')
            st.dataframe(sheet, hide_index=True)

        with st.expander(f"![Logo](data:image/png;base64,{halo_img_base64})"):

            st.subheader('Overall')
            df_overall = process_sheet('Halo Results')
            st.dataframe(df_overall, hide_index=True)

            st.subheader('One Bomb')
            df_aob = process_sheet('Halo Results AOB')
            st.dataframe(df_aob, hide_index=True)

            st.subheader('Land Grab')
            df_lg = process_sheet('Halo Results LG')
            st.dataframe(df_lg, hide_index=True)

            st.subheader('Oddball')
            df_ob = process_sheet('Halo Results OB')
            st.dataframe(df_ob, hide_index=True)

            st.subheader('Capture The Flag')
            df_ctf = process_sheet('Halo Results CTF')
            st.dataframe(df_ctf, hide_index=True)

        with st.expander(f"![Logo](data:image/png;base64,{f1_img_base64})"):
            df_formula1 = process_sheet('Formula 1 Results')
            st.dataframe(df_formula1, hide_index=True)

    Background.page()