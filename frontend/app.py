# from flask import Flask
# from flask_cors import CORS
# from routes import generate_bp  # Import routes

# app = Flask(__name__)
# CORS(app)

# # Register blueprints
# app.register_blueprint(generate_bp)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000, debug=True)

import streamlit as st
import requests

st.title("AI-Powered Blog Generator")

prompt = st.text_area("Enter a blog topic or idea:")

if st.button("Generate Blog"):
    if prompt.strip():
        response = requests.post("http://127.0.0.1:8000/generate", json={"prompt": prompt})
        if response.status_code == 200:
            st.write(response.json()["blog"])
        else:
            st.error("Error generating blog. Try again.")
    else:
        st.warning("Please enter a prompt.")
