#RESOURCES PAGE

import streamlit as st
import gspread
import pandas as pd
from gspread_dataframe import get_as_dataframe, set_with_dataframe

st.set_page_config(
    page_title="Learning Resources"
)

#connect to the google sheet
credentials = {
  "type": "service_account",
  "project_id": "hack-her-database",
  "private_key_id": "62d17b229f841c8252e09a86d83c03089f3d6517",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCH1TncNx6f/F0d\nOTdkHJoHddzKSIZLFCaW9ANbO1qgnPX2zmyXWWy3MX6qCOrvOnr4oLViVXHAr/7I\n7UkBAFMFj3gJHvmxu6JTs59SDg6eaTGWhx2RaF1Hm0Cv3MCdpzg0Hlnc+BbBPwkF\nvLKwJ94dD2e385lybmOLdQMNfIhIIKaUm3U47ghFBHPSRU+z1W5CWCC4uPDlPrZg\nF6ffTLUJYh6ephGOvTzY1eO5ajv4P5Vzs3e4to6g+3xhaRa31DsW+I+rV/DVfwH1\n8/MApqeMPZXaPrfHZtUFJr3EAD+7UOymv3tNv7jeFbQcTg6FSlmoJuD3ZxXKuCTl\nE+XWIzgdAgMBAAECggEAIfBmB58CGOlefqnILEx1M/4AD871Nxcu2TLZD9eRumXd\nkzBas6pVXqSQSH337ZRIG41UJODCjmmrGJspTYW+OLpzPJwvuXfvhEhyO3dlsbEJ\nAdp6ydUw0W56SDa5LesVQPiAbZTTYq+UWomegCNF/S7XNIA6S/xHBRZUj+8YwiSB\nKNAfTIzl/4TRV8i0b4eD/VjKrx2GnyTGOVJ8/6SzlUA3oBrKqK9VmmqoHn1NUt5H\noZBAR/GgpnK7xXbFXavkA1WmBHnYnFfQK8fFoUyvssnlvaHWmVVlXw/9ANMb6SyV\nufj5QAa4t67ywF68VZ6kcZ2u93qZYfrUl/+84SudwQKBgQC9BIUHIZ1O6+YaCgyy\nGOE+F4KYUu7NOCSh90+cJSfkt+JTsHrZIovX7794VcdNNJW4d2NL2kS3a3+Snd+k\nJvYv7+mB7UsrIVDp33LxzZV1bXCLpQdGSQbVq5cLJAh5fLPN7y1eM781UCN2R/7N\nFG4M9sUStECKxl4hMvO5+z2EMQKBgQC399fk2VM3gTC46zFXtC/ufiYfm2zXm7oN\nb2ohPKRdWYW4QkFge+uh8qq6Gh7o8in9AXFdKJiiSb06EgpRXm3spd49eEOBDcT/\nQKMoXEm6FAUj+rjmxi4dg/g5D58G0o/xQvLp0sqc/+eamBTWaGMzaMsWvLFfF9vn\nqt3TAsVTrQKBgQCjw5+yDwipES96jgxz3aSBVIM8kFYADc2HWqtp4LNQsZTw5214\nZTr+KuUcUE1t8cpqWV35oTF6LTQJhqj2Ix+XZuhMPpiq1KGzD3saTwFYDSq+govr\n9Gdshs9FwsFo6IcsPDZ1cKYQfc9LspLrgfDbYI5cZzmoQrfZUbjjAO9KcQKBgQCR\nwVfYBSedjknf+Ne7ORPQzTm/SRFPMh6SjndzpexD2a3McxIBM61ZPj5t/EwJG/SQ\ndBgxSvzDd9DotWpfVYWaPUB7S1GQaixuX/PlAlmXiE0aWIcusE3RLMH505qXeTR6\nXiS/hTbqdQY2wc+goEwYayqc9RtC0FB2mDXv/P4CcQKBgQCqF+RzbJ+7SR+vOwAQ\nL15w+wX2IKroXYT0uyb9esbEJUnLOzuLVMNKWEs7TBN6oZT46MnncVAYroRQNic5\nHR0s3Nd2bpgb6iTgcSsZSGNsUKZQFq+rvl6y1zgpWgvBmUbjFroHnMQwjrCTO6cL\nBwOm3lTUDWE91phGG1Rk5JFOlg==\n-----END PRIVATE KEY-----\n",
  "client_email": "googlesheetshack@hack-her-database.iam.gserviceaccount.com",
  "client_id": "107661966123414012146",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/googlesheetshack%40hack-her-database.iam.gserviceaccount.com"
}

gc, authorized_user = gspread.oauth_from_dict(credentials)


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

