import streamlit as st

pages = {
    "Portfolio": [
        st.Page("about.py", title="About me", icon=":material/info:"),
        st.Page("experience.py", title="Experience", icon=":material/work:"),
        st.Page("education.py", title="Education", icon=":material/school:"),
        st.Page("projects.py", title="Projects", icon=":material/terminal:"),
        st.Page("volunteering.py", title="Volunteer"),
    ],
    "Social": [
        st.Page("contact.py", title="Contact", icon=":material/mail:"),
        st.Page("blog.py", title="Blog", icon=":material/chat_bubble:"),
    ],
}

pg = st.navigation(pages)
pg.run()