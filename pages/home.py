#WELCOME PAGE

import streamlit as st
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(
    page_title="hack.her",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="expanded",

    #menu_items={
       # 'Learning Resources': 'https://www.extremelycoolapp.com/help',
      #  'Report a bug': "https://www.extremelycoolapp.com/bug",
    #    'About': "# This is a header. This is an *extremely* cool app!"
  #  }
)

st.header("Custom tab component for on-hover navigation bar")
#st.markdown('<style>' + open('./style.css').read() + '<style>', unsafe_allow_html=True)

with st.sidebar:
  tabs = on_hover_tabs(tabName=['Home', 'Learning Resources', 'Calendar', 'Coding Practice', 'Profile'], default_choice = 0)

if tabs == 'Home':
  st.title("Home")
  st.write('Name of option is {}'.format(tabs))

st.balloons()

st.title("hack.her\n")
st.subheader("👋 Hi there!")
st.subheader("💻 Welcome to the official hacking hub for girls who like to code!\n")

st.write("A safe space for girls interested in computer science to build their computer science skillset, ")
st.write("find resources to learn more about different coding languages, gain information about hackathons, ")
st.write("and most importantly, connect with other girls with the same passions.\n")

#st.image(https://today.ttu.edu/posts/2021/09/Images/Woman-Computer-2-lg.jpg)

#sidebar
