FROM python:3.10-slim

WORKDIR /app

# Install tesseract and other dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \ 
    libleptonica-dev \
    libsm6 \
    libxext6 \
    libxrender-dev \ 
    poppler-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
 
# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Command to run the application
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
