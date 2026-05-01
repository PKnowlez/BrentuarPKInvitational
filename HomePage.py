import streamlit as st
from PIL import Image
import Background
from Articles import Article1, Fall_Guys_Article

logo_no_laurel = Image.open("./Images/logo-no-laurel.png")

def page():
    st.image(logo_no_laurel)
    st.divider()

    if 'show_all_content' not in st.session_state:
            st.session_state.show_all_content = False

            #region latest article
            
            Fall_Guys_Article.article()

            #endregion

            # ----------------------------------------------------------------------------------------------------------
            # "Show More/Less" button 
            if not st.session_state.show_all_content:
                if st.button('Show More'):
                    st.session_state.show_all_content = True
                    st.rerun()  # Rerun the app to show everything
            else: 
                if st.button('Show Less'):
                    st.session_state.show_all_content = False
                    st.rerun()

            if st.session_state.show_all_content:
                 
                Article1.article()

    Background.page()