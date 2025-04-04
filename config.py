import os
import streamlit as st

# OpenAI API Key - Try to get from environment or secrets
try:
    OPENAI_API_KEY = st.secrets.get("openai", {}).get("api_key", os.environ.get("OPENAI_API_KEY", ""))
except:
    # Fallback to environment variable only if secrets access fails
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

# Application Settings 
APP_TITLE = "Document Q&A Generator"
APP_DESCRIPTION = "Upload a document to extract questions and generate AI answers"

# File Settings 
ALLOWED_EXTENSIONS = ['pdf', 'docx']
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
 
# Tesseract Path (update based on OS)
TESSERACT_PATH = '/usr/bin/tesseract'  # Linux/Mac
# TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows
