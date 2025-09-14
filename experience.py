import streamlit as st
from streamlit_theme import st_theme

st.title("Professional Experience")
st.divider()

with st.container(horizontal=True, vertical_alignment="center"):
    if st.context.theme.type == "dark":
        st.image("svg/wh/coder.svg", width=100)
    else:
        st.image("svg/bl/coder.svg", width=100)
    with st.container():
        st.subheader("Coding Instructor")
        st.text("03/2025 - PRESENT")
        st.text("Working as an instructor tasked with mentoring and teaching students fundamental programming concepts  "
                "via project-based learning.")
        skills = ["Unity", "Java", "C#", "Godot", "Python", "Gamemaker", "Scratch"]
        st.pills("Technologies:", skills)

st.divider()
with st.container(horizontal=True, vertical_alignment="center"):
    if st.context.theme.type == "dark":
        st.image("svg/wh/SAT.svg", width=100)
    else:
        st.image("svg/bl/SAT.svg", width=100)
    with st.container():
        st.subheader("Firmware Engineering Intern")
        st.text("05/2024 - 08/2024")
        st.text("Multi-faceted role which dealt with IoT solutions research and testing, and developing algorithms for "
                "radar sensor vector stabilization.")
        skills = ["Python", "PyQt5", "Jira", "Confluence", "Bitbucket"]
        st.pills("Technologies:", skills)
st.divider()

st_theme()