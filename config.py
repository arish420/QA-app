import os

# OpenAI API Key
OPENAI_API_KEY = "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"  # Replace with your API key


# Application Settings 
APP_TITLE = "Document Q&A Generator"
APP_DESCRIPTION = "Upload a document to extract questions and generate AI answers"

# File Settings 
ALLOWED_EXTENSIONS = ['pdf', 'docx']
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
 
# Tesseract Path (update based on OS)
TESSERACT_PATH = '/usr/bin/tesseract'  # Linux/Mac
# TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows
