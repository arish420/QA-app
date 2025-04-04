import os

# OpenAI API Key
OPENAI_API_KEY = ""  # Replace with your API key


# Application Settings 
APP_TITLE = "Document Q&A Generator"
APP_DESCRIPTION = "Upload a document to extract questions and generate AI answers"

# File Settings 
ALLOWED_EXTENSIONS = ['pdf', 'docx']
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
 
# Tesseract Path (update based on OS)
TESSERACT_PATH = '/usr/bin/tesseract'  # Linux/Mac
# TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows
