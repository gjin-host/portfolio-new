import streamlit as st
from streamlit_theme import st_theme

st.title("Educational Background")
st.divider()

with st.container(horizontal=True, vertical_alignment="center"):
    if st.context.theme.type == "dark":
        st.image("svg/wh/university.svg", width=70)
    else:
        st.image("svg/bl/university.svg", width=70)
    with st.container():
        st.subheader("Bachelor of Science; Major in Computer Science, Minor in Mathematics")
        st.text("08/2022 - PRESENT")
        st.text("Honors program member, ASU treasurer, CS club member, ASME attendee. Chairperson and honors program "
                "scholarship recipient. GPA: 3.8/4.0")
        classes = ["Mobile App Development", "Software Engineering", "Assembly Language", "Digital Systems Design", "Machine Learning",
                   "Java I-II", "Systems Programming", "Data Structures", "Algorithms",
                   "Artificial Intelligence", "Linear Algebra and Probability", "Calculus I-III", "Discrete Mathematics"]
        st.pills("Coursework:", classes)
st.divider()

st_theme()