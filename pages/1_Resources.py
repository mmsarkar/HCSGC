#RESOURCES PAGE

import streamlit as st
#import gspread
import pandas as pd
#from gspread_dataframe import get_as_dataframe, set_with_dataframe

st.set_page_config(
    page_title="Learning Resources"
)

st.title("Resources")


#had to manually enter in data bc api wasnt working

#learn a language!
st.header("Learn a language!")
languageChoice = st.selectbox(
       "Choose a language:", 
       ("C++", "C", "Python", "Java", "JavaScript", "Swift", "R"),)
if languageChoice == "C++":
    st.subheader("Resources for C++")
    st.write("Download the needed C++ compilers [here](https://gist.github.com/hugoledoux/2e91ed3efbfa8ca5da1ea27e522d2b34)")
    st.write("---") 
    st.write("Consider taking this shorter course: [C++ Essential Training](https://www.linkedin.com/learning-login/share?account=26135898&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fc-plus-plus-essential-training-15106801%3Ftrk%3Dshare_ent_url%26shareId%3DunMtnNavS%252BmCdQHQHm8Brg%253D%253D)")
    st.write("Free, for college students")
    st.write("---") 
    st.write("Consider taking this longer course: [Learn C++](https://www.codecademy.com/learn/learn-c-plus-plus)")
    st.write("Length: 25 hours")
    st.write("Free")
if languageChoice == "C":
    st.subheader("Resources for C")
    st.write("---") 
    st.write("Consider taking this shorter course: [C Programming](https://youtu.be/KJgsSFOSQv0)")
    st.write("Length: 4 hours")
    st.write("Free")

    st.write("---") 
    st.write("Consider taking this longer course: [Introductory C Programming](https://youtu.be/KJgsSFOSQv0)")
    st.write("Length: 5 months")
    st.write("Free, + a certificate")
if languageChoice == "Python":
    st.subheader("Resources for Python")
    st.write("Download the needed Python compilers [here](https://wiki.python.org/moin/BeginnersGuide/Download)")
    st.write("---") 
    st.write("Consider taking this shorter course: [Python Full Course for Beginners](https://youtu.be/_uQrJ0TkZlc)")
    st.write("Length: 6 hours")
    st.write("Free")

    st.write("---") 
    st.write("Consider taking this longer course: [Learn Python 3](https://www.codecademy.com/learn/learn-python-3)")
    st.write("Length: 25 hours")
    st.write("Free")
if languageChoice == "Java":
    st.subheader("Resources for Java")
    st.write("Download the needed Java compilers [here](https://www.java.com/en/download/help/log_files.html)")
    st.write("---") 
    st.write("Consider taking this shorter course: [Java Tutorial for Beginners](https://youtu.be/eIrMbAQSU34)")
    st.write("Length: 2.5 hours")
    st.write("Free")

    st.write("---") 
    st.write("Consider taking this longer course: [Learn Java](https://www.codecademy.com/learn/learn-java)")
    st.write("Length: 25 hours")
    st.write("Free")
if languageChoice == "JavaScript":
    st.subheader("Resources for JavaScript")
    st.write("Download the needed JavaScript compilers [here](https://launchschool.com/books/javascript/read/preparations)")
    st.write("---") 
    st.write("Consider taking this shorter course: [Learn Javascript - Full Course for Beginners](https://youtu.be/PkZNo7MFNFg)")
    st.write("Length: 3 hours")
    st.write("Free")

    st.write("---") 
    st.write("Consider taking this longer course: [Learn Javascript](https://www.codecademy.com/learn/introduction-to-javascript)")
    st.write("Length: 20 hours")
    st.write("Free")
if languageChoice == "R":
    st.subheader("Resources for R")
    st.write("Download the needed R compilers [here](https://cran.r-project.org/)")
    st.write("---") 
    st.write("Consider taking this shorter course: [R Programming Tutorial](https://youtu.be/_V8eKsto3Ug)")
    st.write("Length: 2 hours")
    st.write("Free")

    st.write("---") 
    st.write("Consider taking this longer course: [R Programming](https://www.coursera.org/learn/r-programming)")
    st.write("Length: 57 hours")
    st.write("Free, plus a certificate")
if languageChoice == "Swift":
    st.subheader("Resources for Swift")
    st.write("Download the needed Swift compilers [here](https://www.swift.org/download/)")
    st.write("---") 
    st.write("Consider taking this shorter course: [Swift Programming Tutorial for Beginners](https://www.youtube.com/live/Ulp1Kimblg0?feature=share)")
    st.write("Length: 3 hours")
    st.write("Free")

    st.write("---") 
    st.write("Consider taking this longer course: [Learn Swift](https://www.codecademy.com/learn/learn-swift)")
    st.write("Length: 25 hours")
    st.write("Free")



#learn about softwares!
st.header("Learn about softwares!")
swChoice = st.selectbox(
       "Choose a topic:", 
       ("GitHub", "streamlit", "React", "Visual Studio Code", "vim"),)
if swChoice == "GitHub":
    st.subheader("Resources for GitHub")
    st.write("Install it [here](https://github.com/git-guides/install-git)")
    st.write("---") 
    st.write("Try this tutorial: [Hello World](https://docs.github.com/en/get-started/quickstart/hello-world)")
if swChoice == "streamlit":
    st.subheader("Resources for streamlit")
    st.write("Install it [here](https://docs.streamlit.io/library/get-started/installation)")
    st.write("---") 
    st.write("Try this tutorial: [Main Concepts](https://docs.streamlit.io/library/get-started/main-concepts)")
if swChoice == "React":
    st.subheader("Resources for React")
    st.write("Install it [here] (https://react.dev/learn/installation)")
    st.write("---") 
    st.write("Try this tutorial: [Quick Start](https://react.dev/learn)")
if swChoice == "Visual Studio Code":
    st.subheader("Resources for Visual Studio Code")
    st.write("Install it [here] (https://code.visualstudio.com/docs/setup/setup-overview)")
    st.write("---") 
    st.write("Try this tutorial: [Getting Started With Visual Studio Code](https://code.visualstudio.com/docs/introvideos/basics)")
if swChoice == "vim":
    st.subheader("vim")
    st.write("Install it [here] (https://www.tutorialspoint.com/vim/vim_installation_and_configuration.htm)")
    st.write("---") 
    st.write("Try this tutorial: [Vim 101: A Beginners Guide to Vim](https://www.linuxfoundation.org/blog/blog/classic-sysadmin-vim-101-a-beginners-guide-to-vim)")

#Learn about relevant majors
st.header("Learn about relevant majors!")
majorChoice = st.selectbox(
       "Choose a major:", 
       ("Computer Engineering", "Computer Science", "Computer Science with Business Applications", "Data Science (engineering)", "Data Science (science)", "Electrical Engineering", "Unmanned Aerial Systems at UCR"),)
if majorChoice == "Computer Engineering":
    st.write("Check out this [course plan](https://student.engr.ucr.edu/sites/default/files/2019-04/2018_cen.pdf)")
if majorChoice == "Computer Science":
    st.write("Check out this [course plan](https://student.engr.ucr.edu/sites/default/files/2019-04/2018_encs_2.pdf)")
if majorChoice == "Computer Science with Business Applications":
    st.write("Check out this [course plan](https://student.engr.ucr.edu/sites/default/files/2019-04/2018_csba.pdf)")
if majorChoice == "Data Science (engineering)":
    st.write("Check out this [course plan](https://datascience.ucr.edu/sites/default/files/2020-09/BCOE-2020%20Data%20Science.pdf)")
if majorChoice == "Data Science (science)":
    st.write("Check out this [course plan](https://datascience.ucr.edu/sites/default/files/2020-09/2020%20Data%20Science-CNAS.pdf?_gl=1*1b2eys3*_ga*NDI2MjQyMDQ4LjE2Nzc0ODE4MjQ.*_ga_Z1RGSBHBF7*MTY3NzQ4MTgyNC4xLjEuMTY3NzQ4MTkxMC4wLjAuMA..*_ga_S8BZQKWST2*MTY3NzQ4MTgyNC4xLjEuMTY3NzQ4MTkxMC4wLjAuMA..)")
if majorChoice == "Electrical Engineering":
    st.write("Check out this [course plan](https://student.engr.ucr.edu/sites/default/files/2019-10/2019_elen.pdf)")
if majorChoice == "Computational Mathematics":
    st.write("Check out this [course plan](https://cnasstudent.ucr.edu/sites/default/files/2023-02/math_bs_all_degreesummary_sheets_2022-_-previous.pdf)")
if majorChoice == "Robotics Engineering":
    st.write("Check out this [course plan](https://student.engr.ucr.edu/sites/default/files/2022-10/2022_robotics.pdf)")

#Learn about relevant majors
st.header("Learn about relevant clubs (UCR-specific only for now)!")
clubChoice = st.selectbox(
       "Choose a club:", 
       ("Competitive Coding Club", "Gamespawn at UCR", "Google Developers Student Club", "High Performance Computing Club", "Highlander Gaming", "Institute of Electrical and Electronics Engineers", "Computational Mathematics", "Robotics Engineering"),)
if clubChoice == "Competitive Coding Club":
    st.write("Check out this [club](https://highlanderlink.ucr.edu/organization/ccc)")
if clubChoice == "Gamespawn at UCR":
    st.write("Check out this [club](https://highlanderlink.ucr.edu/organization/gamespawn)")
if clubChoice == "Google Developers Student Club":
    st.write("Check out this [club](https://highlanderlink.ucr.edu/organization/gdsc)")
if clubChoice == "High Performance Computing Club":
    st.write("Check out this [club](https://highlanderlink.ucr.edu/organization/hpcc)")
if clubChoice == "Highlander Gaming":
    st.write("Check out this [club](https://highlanderlink.ucr.edu/organization/highlandergaming)")
if clubChoice == "Institute of Electrical and Electronics Engineers":
    st.write("Check out this [club](https://highlanderlink.ucr.edu/organization/ieee)")
if clubChoice == "Unmanned Aerial Systems at UCR":
    st.write("Check out this [club](https://highlanderlink.ucr.edu/organization/ucruas)")
