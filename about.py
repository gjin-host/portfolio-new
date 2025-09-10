import streamlit as st
import pandas as pd

st.title("About Me")

st.markdown("Hey there! 👋")
st.markdown("My name is **Gjin Rexhaj**, and I am a third-year university student. I am currently pursuing a Bachelor of "
            "Science; Majoring in Computer Science and minoring in Mathematics.")

st.markdown("I'm a passionate developer whose interest and experience spans across multiple different subsets within CS. "
            "Follow my [GitHub profile](https://github.com/gjinrexhaj)!")


st.markdown("")
st.markdown("")
st.markdown("")

st.markdown("Take a look around! You can browse all of the contents of this webpage by navigating via the sidebar.")

with st.container(horizontal=True):
    if st.button("Get in touch"):
        st.switch_page("contact.py")
    if st.button("View my blog"):
        st.switch_page("blog.py")