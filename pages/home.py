#WELCOME PAGE

import streamlit as st

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

#_create_option(
#    "theme.primaryColor"
#    description="FFE5EC"
#)

from streamlit_extras.let_it_rain import rain

rain(
    emoji="💻",
    font_size=54,
    falling_speed=7,
    animation_length=4,
)

st.title("hack.her\n")
st.subheader("👋 Hi there!")
st.subheader("💻 Welcome to the official hacking hub for girls who like to code!\n")

st.write("A safe space for girls interested in computer science to build their computer science skillset, ")
st.write("find resources to learn more about different coding languages, gain information about hackathons, ")
st.write("and most importantly, connect with other girls with the same passions.\n")

#st.image(https://today.ttu.edu/posts/2021/09/Images/Woman-Computer-2-lg.jpg)