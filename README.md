# Document Q&A Generator

Extract questions from documents and generate expert answers.

## Installation

### Required System Dependencies

#### Tesseract OCR Installation:
- **Windows**: 
  - Download from: https://github.com/UB-Mannheim/tesseract/wiki
  - Install and add to PATH

- **macOS**:
  ```bash
  brew install tesseract
  ```

- **Linux** (Ubuntu/Debian):
  ```bash
  sudo apt-get update
  sudo apt-get install -y tesseract-ocr
  ```

#### Poppler Installation (for PDF processing):
- **Windows**: Download from https://github.com/oschwartz10612/poppler-windows/releases
- **macOS**: `brew install poppler`
- **Linux**: `sudo apt-get install -y poppler-utils`

### Application Setup

#### Windows:
1. Install Python 3.8 or later from [python.org](https://python.org)
2. Double-click `install.bat`
3. Double-click `run.bat`

#### Mac/Linux:
1. Open Terminal
2. Navigate to app directory:
   ```bash
   cd document_qa_app
   ```
3. Make run script executable:
   ```bash
   chmod +x run.sh
   ```
4. Run the application:
   ```bash
   ./run.sh
   ```

## API Key Setup
You can provide your OpenAI API key in one of three ways:
1. Create a `.env` file by copying `.env.example` and adding your API key
2. Enter your API key in the web interface when prompted
3. Update the `OPENAI_API_KEY` value in `config.py`

## Usage
1. Open web browser to http://localhost:8501
2. Enter your OpenAI API key if not already configured
3. Upload PDF or DOCX file
4. Wait for question extraction
5. Click "Generate Answers" to process
6. Download the Q&A document

## Troubleshooting

### If you see OCR-related errors:
- Make sure Tesseract OCR is properly installed (see installation steps above)
- Verify the Tesseract path in the error message
- On Windows, the default path is usually `C:\Program Files\Tesseract-OCR\tesseract.exe`
- On Mac/Linux, it should be in your PATH (try running `which tesseract` to verify)

### PDF Processing Issues:
- For PDF processing issues, make sure Poppler is properly installed

## Requirements
- Python 3.8+
- Tesseract OCR 
- 2GB RAM minimum
- Internet connection for processing
- OpenAI API key
# QA-app
