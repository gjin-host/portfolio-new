import streamlit as st

st.title("Contact Information")

st.markdown("Email is the quickest way to get ahold of me, feel free to reach out with any inquiries!")

with st.container(horizontal=True):
    st.link_button("Email", "mailto:gjin.contact@gmail.com", icon=":material/mail:")
    st.link_button("GitHub", "https://github.com/gjinrexhaj")
    st.link_button("LinkedIn", "https://www.linkedin.com/in/gjinrexhaj/")
