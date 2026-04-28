import streamlit as st
from Articles import Article1

def news():
    if 'show_all_content' not in st.session_state:
        st.session_state.show_all_content = False

        #region latest article
        
        Article1.article()

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
            x=0