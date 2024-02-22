import streamlit as st
import PyPDF2 as pdf
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, pdf_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt + pdf_text)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Prompt Template
input_prompt = """
You are an Expert Summarizer in Tech Field. Now Please Help in Summarizing the given text here in detailed  paragraph's 

Also Provide any Improvements and suggestions from Your End

Note : You Need to give the output in neat bold Manner when ever it is Required and the text is attached here :

{pdf_text}

Summary:

Imporvements : 
"""

def display_upload_ui():
    st.title("PDF Text Summarizer")
    st.text("Extract Text from PDF and Generate Summary")
    uploaded_file = st.file_uploader("Upload Your PDF File", type="pdf", help="Please upload the PDF file")
    return uploaded_file

def display_response(response):
    st.subheader("Summary Generated:")
    st.write(response)

def display_error(message):
    st.subheader("Error:")
    st.error(message)

def main():
    uploaded_file = display_upload_ui()

    submit = st.button("Generate Summary")

    if submit:
        if uploaded_file is not None:
            try:
                pdf_text = input_pdf_text(uploaded_file)
                response = get_gemini_response(input_prompt, pdf_text)
                display_response(response)
            except Exception as e:
                display_error(f"Error processing the file: {str(e)}")
        else:
            display_error("Please upload a file.")

if __name__ == "__main__":
    main()
