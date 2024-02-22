import streamlit as st

# Define the layout and styling
st.markdown(
"""
<style>
.button-description {
    font-size: 16px;
    margin-bottom: 10px;
    color: #555;
    font-style: italic;
}
.button-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 30px;
}
.button {
    padding: 10px 20px;
    font-size: 18px;
    margin-bottom: 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}
.button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)

# Add a two-line description before each button
st.markdown("<div class='button-container'>", unsafe_allow_html=True)

if st.button("Home", key="home_button", help="Go back to the main page"):
    st.switch_page("app.py")

st.markdown("<div class='button-description'>Click the button below to summarize YouTube videos:<br/>Summarize the content of YouTube videos for quick understanding.</div>", unsafe_allow_html=True)
if st.button("Youtube Video Summarizer", key="yt_button", help="Summarize YouTube videos"):
    st.switch_page("pages/yt_summarizer.py")

st.markdown("<div class='button-description'>Click the button below to summarize content of PDF files:<br/>Generate a summary of the content present in PDF documents.</div>", unsafe_allow_html=True)
if st.button("PDF File Content Summarizer", key="pdf_button", help="Summarize PDF files"):
    st.switch_page("pages/content_summarizer.py")

st.markdown("<div class='button-description'>Click the button below to interact with a multimodal chatbot:<br/>Engage in conversation with a chatbot capable of processing text, images, and more.</div>", unsafe_allow_html=True)
if st.button("Multimodal Chatbot", key="chatbot_button", help="Interact with a multimodal chatbot"):
    st.switch_page("pages/multimodal_chatbot.py")

st.markdown("</div>", unsafe_allow_html=True)
