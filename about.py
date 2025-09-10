import streamlit as st

st.title("About Me")

st.markdown("Hey there! 👋")
st.markdown("My name is **Gjin Rexhaj**, and I am a third-year university student. I am currently pursuing a Bachelor of "
            "Science; Majoring in Computer Science and minoring in Mathematics.")

st.markdown("I'm a passionate developer whose interest and experience spans across multiple different subsets within CS. "
            "Follow me on GitHub!")

if st.button("Get in touch"):
    st.switch_page("contact.py")