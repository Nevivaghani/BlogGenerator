import streamlit as st
import requests

# Streamlit UI
st.title("LLaMA 2 Blog Generator")
st.write("Generate AI-powered blog content with LLaMA 2!")

prompt = st.text_area("Enter a prompt for the blog")

if st.button("Generate Blog"):
    if prompt:
        response = requests.post("http://127.0.0.1:8000/generate", json={"prompt": prompt}, timeout=120)
        print(response.json())
        
        if response.status_code == 200:
            st.write("### Generated Blog:")
            st.write(response.json()["blog"])
        else:
            st.error("Error generating blog content")
    else:
        st.warning("Please enter a prompt")

