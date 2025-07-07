
import streamlit as st
import os

st.set_page_config(page_title="UrgeCare", layout="wide")

st.sidebar.title("🏥 UrgeCare Navigation")
st.sidebar.page_link("pages/1_Home.py", label="Home")
st.sidebar.page_link("pages/2_Login.py", label="Login")
st.sidebar.page_link("pages/3_Upload.py", label="Upload & OCR")
st.sidebar.page_link("pages/4_AI_Assistant.py", label="AI Assistant")
st.sidebar.page_link("pages/5_History.py", label="Chat History")

st.title("Welcome to UrgeCare 🩺")
st.write("Choose a section from the sidebar to get started.")
