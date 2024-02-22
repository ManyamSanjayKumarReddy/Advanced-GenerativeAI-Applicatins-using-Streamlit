import streamlit as st

if st.button("Home"):
    st.switch_page("main.py")
if st.button("Youtube Video Summarizer"):
    st.switch_page("pages/yt_summarizer.py")
if st.button("PDF File Content Summarizer"):
    st.switch_page("pages/content_summarizer.py")