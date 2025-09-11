import streamlit as st
from streamlit_theme import st_theme

st.title("Volunteer Work")
st.divider()

with st.container(horizontal=True, vertical_alignment="center"):
    if st.context.theme.type == "dark":
        st.image("svg/wh/presentation.svg", width=70)
    else:
        st.image("svg/bl/presentation.svg", width=70)
    with st.container():
        st.subheader("Engineering Colloquia Series Presentation")
        st.text("04/2025")
        st.text("Gave a presentation under mentorship of a researcher at a University. The presentation introduced and "
                "explained Agentic AI, and multi-agent AI systems to a broad audience of academic scholars.")


st.divider()
with st.container(horizontal=True, vertical_alignment="center"):
    if st.context.theme.type == "dark":
        st.image("svg/wh/plane.svg", width=70)
    else:
        st.image("svg/bl/plane.svg", width=70)
    with st.container():
        st.subheader("Aircraft Technician Volunteer Work")
        st.text("06/2022 - 08/2022")
        st.text("Volunteered at a local aircraft technician facility. Workload dealt with the ordering, assembly, and "
                "installation of wiring harnesses and advanced avionics systems for small form-factor propeller "
                "engine aircraft.")


st.divider()

st_theme()

