#!/bin/bash
echo "Setting up environment..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi
 
# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Ensure dependencies are installed
echo "Checking dependencies..."
pip install -r requirements.txt

# Make sure python-dotenv is installed
pip install python-dotenv

# Run the application
echo "Starting application..."
streamlit run app.py
