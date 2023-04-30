#CALENDAR PAGE

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Events"
)

st.title("Upcoming Events")


st.header("Upcoming Awards and Scholarships")
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "Scholarship": [ "Nucamp + Google Cloud Women in Tech ", "BHW Scholarship", "Drone Technology College Scholarship", "SMART Scholarship", "Planatir Women in Technology"],
            "Links": ["https://www.nucamp.co/scholarships/googlewomenintech?cn=&cs=&utm_source=google&utm_medium=paid&utm_campaign=search&utm_content=&utm_term=&utm_keyword=women%20in%20tech%20scholarship&gad=1&gclid=CjwKCAjwo7iiBhAEEiwAsIxQESIqBy3j1ZRPu87y3pBbW2wIy19AhLc8XJf_Em3kezOI4JvXQWLxKBoC_BsQAvD_BwE", "https://thebhwgroup.com/scholarship", "https://www.dronepilotgroundschool.com/scholarship/#college", "https://www.smartscholarship.org/smart?id=smart_index", "https://www.palantir.com/careers/students/scholarship/wit-north-america/"],
            "Money": ["Up to 25% of tution", "$3k", "$1k", "100% of tuition", "$7k"],
            "Deadline": ["Before fund is depleted", "4/15", "5/31", "12/1", "January"],
        }
    )

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=st.session_state.use_container_width)


#col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

