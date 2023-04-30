#WELCOME PAGE

import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="hack.her",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.balloons()

st.title("hack.her\n")
st.header("👋 Hi there!")
st.header("💻 Welcome to the official hacking hub for girls who like to code!\n")

def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json")

with st.container(): 
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.subheader("A safe space for girls interested in computer science to:")
    st.write(
      """
      -grow their computer science skillset
      -find resources to learn about different coding languages
      -gain information about hackathons
      -connect with other girls with the same passions
      """  
    )
  with right_column:
    st_lottie(lottie_coding, height = 250, key = "coding")