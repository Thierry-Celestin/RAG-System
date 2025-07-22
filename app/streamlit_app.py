import streamlit as st
import sys
import os
from pathlib import Path
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

API_URL = "http://localhost:8000"

st.set_page_config(page_title="RAG System - Document Q&A", page_icon="📄", layout="wide")

st.markdown(
    """
    <style>
    .main {background-color: #0e1117;}
    .block-container {padding: 2rem;}
    .title {color: #1DB954; font-size: 2.5rem;}
    .sub-title {color: #39FF14; font-size: 1.5rem; margin-bottom: 1rem;}
    .feature-box {background-color: #0e1117; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;}
    .quick-guide {background-color: #0e1117; padding: 1rem; border-radius: 0.5rem; margin-top: 2rem;}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title">RAG System</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Retriever-Augmented Generation for Document Q&A</p>', unsafe_allow_html=True)


# --- Upload Document Section ---
st.markdown("### 📤 Upload PDF Document")
uploaded_file = st.file_uploader("Upload a PDF file for analysis", type=['pdf'])

if uploaded_file:
    file_path = os.path.join("data", uploaded_file.name)
    os.makedirs("data", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner('Processing the document...'):
        response = requests.post(f"{API_URL}/upload/", files={"file": open(file_path, "rb")})
        if response.status_code == 200:
            st.success("✅ Document processed successfully!")
        else:
            st.error("❌ Failed to process document via API.")

st.markdown("---")

# --- Question Section ---
st.markdown("### ❓ Ask a Question")
question = st.text_input("Enter your question about the uploaded document:")

if question:
    with st.spinner('Generating answer...'):
        response = requests.post(f"{API_URL}/ask/", json={"question": question})
        if response.status_code == 200:
            answer = response.json().get("answer")
            st.success(f"📢 **Answer:** {answer}")
        else:
            st.error("❌ Error in fetching answer. Ensure a document is processed first.")

st.markdown("---")

# --- Features ---
st.markdown('<div class="feature-box"><h4>🚀 Features</h4><ul>'
            '<li>PDF Document Processing</li>'
            '<li>AI-Powered Text Embeddings</li>'
            '<li>Intelligent Q&A System</li>'
            '</ul></div>', unsafe_allow_html=True)

# --- Quick Start Guide ---
st.markdown('<div class="quick-guide"><h4>📚 Quick Start Guide</h4>'
            '<ol>'
            '<li><strong>Upload PDF:</strong> Upload a PDF document to be processed.</li>'
            '<li><strong>Processing:</strong> The system extracts text and creates embeddings for search.</li>'
            '<li><strong>Ask Questions:</strong> Ask any question about the document content and get AI responses.</li>'
            '</ol></div>', unsafe_allow_html=True)
