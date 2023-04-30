#RESOURCES PAGE

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

