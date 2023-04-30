#WELCOME PAGE

import streamlit as st
from st_on_hover_tabs import on_hover_tabs

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'Learn', 'Calendar', 'Profile', 'Code'])



st.title("Home")
st.subheader("Hacker CS Girls in Code")

st.write("hot cs girlies cult")