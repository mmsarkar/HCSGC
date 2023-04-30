# where the user input will be gotten
import streamlit as st
#from tkinter import *
#from tkinter.ttk import *
import gspread

#def nextPage():
#    ws.destroy()
#   import SubmittedPage

st.title("Create a Profile")

#create the profile
# take user input

#get name
st.write("Name")
userName = st.text_input('*Input your first and last Name*')

#get email
st.write("Email")
email = st.text_input("*Input your email*")

#get phone number
st.write("Phone number (no dashes or slashes)")
phoneNum = st.number_input("*Phone number (ex. 9999999999)*")

#get location / city
st.write("What city are you from?")
location = st.selectbox("*Choose an option:*", ['Riverside', 'Other'])

#get number of cs courses taken
st.write("How many computer science courses have you taken? These can be in college, coursera, or any other course.")
courses = st.number_input()

#get number of hackathons
st.write("How many hackathons have you been to?")
hackNum = st.number_input()

#submitted button
isFinished = st.button('Submit')

if isFinished == True:
    st.write("Your profile has been recorded! Please log in on the Log In page.")
