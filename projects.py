import streamlit as st

st.title("Software Engineering Projects")
st.divider()

with st.container(horizontal=True, vertical_alignment="center"):
    with st.container():
        st.subheader("java-neural-network")
        st.text("Implemented a fully parameterized Neural Network engine from scratch in Java, complete with mutation "
                "and gradient descent training methods. Ships with a front-end visualizer I built using Java Swing. ")
        tech = ["Machine Learning", "Java", "Java Swing", "AWT", "Maven"]
        st.pills("Technologies:", tech)
        st.link_button("View source code", "https://github.com/gjinrexhaj/java-neural-network", type="primary", icon=":material/code:")
    with st.container():
        st.image("image/java-neural-net.png")

st.divider()
with st.container(horizontal=True, vertical_alignment="center"):
    with st.container():
        st.subheader("ticket-finder")
        st.text("A native android application which allows a user to search for tickets based on category and location, "
                "and optionally storing their favorites within an account. ")
        tech = ["Kotlin", "Android", "Firebase Firestore", "Ticketmaster discovery API"]
        st.pills("Technologies:", tech)
        st.link_button("View source code", "https://github.com/gjinrexhaj/ticket-finder", type="primary", icon=":material/code:")
    with st.container():
        st.image("image/ticket-finder.gif")

st.divider()
with st.container(horizontal=True, vertical_alignment="center"):
    with st.container():
        st.subheader("cellular-automata")
        st.text("An open-source cellular automata engine built with C, C++, and raylib")
        tech = ["C", "C++", "Raylib", "Raygui", "CMake"]
        st.pills("Technologies:", tech)
        with st.container(horizontal=True):
            st.link_button("View source code", "https://github.com/gjinrexhaj/cellular-automata", type="primary", icon=":material/code:")
            st.link_button("Video showcase", "https://www.youtube.com/watch?v=qYmX0MMCitA")
    with st.container():
        st.image("image/cellular-automata.gif")

st.divider()
with st.container(horizontal=True, vertical_alignment="center"):
    with st.container():
        st.subheader("cli-snake-game")
        st.text("A command-line snake game written entirely in C with curses.h, targeting UNIX systems")
        tech = ["C", "Curses", "UNIX"]
        st.pills("Technologies:", tech)
        st.link_button("View source code", "https://github.com/gjinrexhaj/cli-snake-game", type="primary", icon=":material/code:")
    with st.container():
        st.image("image/cli-snake-game.gif")

st.divider()
with st.container(horizontal=True, vertical_alignment="center"):
    with st.container():
        st.subheader("sierpinski-fractal-generator")
        st.text("A Java GUI program which renders an \"nth\" order Sierpinski gasket. The canvas size and degree of the "
                "rendered Sierpinski gasket are user-specified.")
        tech = ["Java", "Java Swing", "Java AWT"]
        st.pills("Technologies:", tech)
        st.link_button("View source code", "https://github.com/gjinrexhaj/sierpinski-fractal-generator", type="primary", icon=":material/code:")
    with st.container():
        st.image("image/sierpinski-fractal-generator.png")

st.divider()
with st.container(horizontal=True, vertical_alignment="center"):
    with st.container():
        st.subheader("graphing-calculator")
        st.text("A graphing calculator written in Python capable of plotting user-specifiable arbitrary mathematical "
                "functions. Currently implemented with PySide6 and matplotlib. ")
        tech = ["Python", "PySide6", "matplotlib"]
        st.pills("Technologies:", tech)
        st.link_button("View source code", "https://github.com/gjinrexhaj/graphing-calculator", type="primary", icon=":material/code:")

st.divider()