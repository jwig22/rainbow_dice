import streamlit as st

st.set_page_config(
    page_title="Rainbow Dice Intro",
    page_icon="🎲",
)

st.sidebar.success('Select "Game" above To Get Started Playing')

st.title('Rainbow Dice')
st.header('How To Play')
st.markdown(
    """
    First, you'll need to either have the proper marking cards for this game until multiple users and
    in-app cards are suppored here. The object of the game is to get as many of your squares marked on
    on each row as possible (exept for penalties) to score max points. Each line of numbers must be 
    marked from **_left_ to _right_** only. Once a number has been marked on a line, all unmarked numbers
    to the left are no longer useable.
"""
)
