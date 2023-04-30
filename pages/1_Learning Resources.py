#RESOURCES PAGE

import streamlit as st
import gspread
import pandas as pd
from gspread_dataframe import get_as_dataframe, set_with_dataframe

st.set_page_config(
    page_title="Learning Resources"
)


#connect to the google sheet
gc = gspread.oauth(
    credentials_filename='path/to/the/credentials.json',
    authorized_user_filename='path/to/the/authorized_user.json'
)

sheet_id = "1L8WY2GKSypZH5pKJIis7Y6LKV2zY1IJO4PvtQxmQsZA"
sheet_name = "Language Resources"
#url = f"<https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}>"
#df = pd.read_csv(url, dtype=str).fillna("")

spreadSheet = gc.open_by_key(sheet_id)
learnWS = spreadSheet.get_worksheet(0)

#st.write(df)

st.title("Resources")

st.header("Learn a language!")
languageChoice = st.selectbox(
       "Choose a language:", 
       ("C++", "C", "Python", "Java", "JavaScript", "Swift", "R"),)
if languageChoice == "C++":
    st.subheader("Resources for C++")

    installLink = learnWS.acell('D7').value
    shortName = learnWS.acell('E7').value
    shortLink = learnWS.acell('F7').value
    shortLength = learnWS.acell('G7').value
    shortPaid = learnWS.acell('H7').value
    longName = learnWS.acell('I7').value
    longLink = learnWS.acell('J7').value
    longLength = learnWS.acell('K7').value
    longPaid = learnWS.acell('L7').value

    st.write("Install C++")

if languageChoice == "C":
    st.subheader("Resources for C")

if languageChoice == "Python":
    st.subheader("Resources for Python")
if languageChoice == "Java":
    st.subheader("Resources for Java")
if languageChoice == "JavaScript":
    st.subheader("Resources for JavaScript")
if languageChoice == "Swift":
    st.subheader("Resources for Swift")
if languageChoice == "R":
    st.subheader("Resources for R")

st.header("Learn about softwares!")
swChoice = st.selectbox(
       "Choose a topic:", 
       ("GitHub", "streamlit", "react.js", "visual studio code", "vim"),)
if swChoice == "GitHub":
    st.subheader("Resources for GitHub")
if swChoice == "streamlit":
    st.subheader("Resources for streamlit")
if swChoice == "react.js":
    st.subheader("Resources for react.js")
if swChoice == "visual studio code":
    st.subheader("Resources for visual studio code")
if swChoice == "vim":
    st.subheader("Resources for vim")

import streamlit as st
import gspread
import pandas as pd
from gspread_dataframe import get_as_dataframe, set_with_dataframe

st.set_page_config(
    title="Learning Resources"
)


#connect to the google sheet
gc = gspread.oauth(
    credentials_filename='path/to/the/credentials.json',
    authorized_user_filename='path/to/the/authorized_user.json'
)

sheet_id = "1L8WY2GKSypZH5pKJIis7Y6LKV2zY1IJO4PvtQxmQsZA"
sheet_name = "Language Resources"
#url = f"<https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}>"
#df = pd.read_csv(url, dtype=str).fillna("")

spreadSheet = gc.open_by_key(sheet_id)
learnWS = spreadSheet.get_worksheet(0)

#st.write(df)

st.title("Resources")

st.header("Learn a language!")
languageChoice = st.selectbox(
       "Choose a language:", 
       ("C++", "C", "Python", "Java", "JavaScript", "Swift", "R"),)
if languageChoice == "C++":
    st.subheader("Resources for C++")