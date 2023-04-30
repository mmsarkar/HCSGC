import pandas as pd
import streamlit as st

# read in data from google sheet
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

    
df = load_data(st.secrets["public_gsheets_url"])

#printed results
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}")