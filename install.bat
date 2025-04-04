@echo off
echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
 
echo Ensuring all dependencies are correctly installed...
pip install python-dotenv openai==0.28.0 --force-reinstall
 
echo Installation complete!
pause 
