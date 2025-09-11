import streamlit as st
import pandas as pd

st.title("Welcome to My Website!")
st.divider()

st.markdown("Hey there 👋")
st.markdown("My name is **Gjin Rexhaj**, and I am a fourth-year university student. I am currently pursuing a Bachelor of "
            "Science; Majoring in Computer Science and minoring in Mathematics.")

st.markdown("I'm a passionate developer whose interest and experience spans across multiple different subsets within CS. "
            "Follow my [GitHub profile](https://github.com/gjinrexhaj)!")


st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("Take a look around! You can browse all of the contents of this website by navigating via the sidebar.")

with st.container(horizontal=True):
    if st.button("Get in touch", type="primary"):
        st.switch_page("contact.py")
    if st.button("View my projects"):
        st.switch_page("projects.py")

