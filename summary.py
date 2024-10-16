import streamlit as st
from transformers import pipeline

# Title of the app
st.title("Text Summarization App")

# Instructions
st.write("""
This application uses the Falconsai/text_summarization model to generate summaries of input text. 
Simply paste a long paragraph, and it will return a concise summary.
""")

# Input text box
input_text = st.text_area("Enter the text you want to summarize", height=200)

# Summarization pipeline
@st.cache_resource
def load_summarization_model():
    return pipeline("summarization", model="Falconsai/text_summarization")

summarizer = load_summarization_model()

# Button to trigger summarization
if st.button("Summarize"):
    if input_text.strip() != "":
        with st.spinner("Summarizing..."):
            summary = summarizer(input_text)[0]['summary_text']
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")

# Footer
st.write("Made with Streamlit and Transformers 🤗")
