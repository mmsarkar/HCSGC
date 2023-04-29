#WELCOME PAGE

import streamlit as st


st.set_page_config(
    page_title="Hacker CS Girls In Code",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="expanded",

    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

#st.title("Home")
#st.subheader("Hacker CS Girls in Code")

#st.write("hot cs girlies cult")