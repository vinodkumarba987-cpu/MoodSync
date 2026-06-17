@echo off
REM MoodSync Setup Script for Windows

echo 🎵 MoodSync - Setup Script
echo ===========================
echo.

REM Check Python version
echo ✓ Checking Python version...
python --version

REM Create virtual environment
echo ✓ Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo ✓ Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo ✓ Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo ✓ Installing dependencies...
pip install -r requirements.txt

REM Create directories
echo ✓ Creating necessary directories...
if not exist database mkdir database
if not exist models mkdir models
if not exist datasets mkdir datasets
if not exist songs mkdir songs
if not exist reports mkdir reports
if not exist logs mkdir logs
if not exist assets mkdir assets

REM Initialize database
echo ✓ Initializing database...
python -c "from database.db import init_db; init_db()"

REM Create .env file
if not exist .env (
    echo ✓ Creating .env file...
    copy .env.example .env
    echo ⚠️  Please update .env with your configuration
)

echo.
echo ✅ Setup completed successfully!
echo.
echo To run MoodSync, use:
echo   venv\Scripts\activate.bat
echo   streamlit run app.py
echo.
echo The app will be available at: http://localhost:8501
pause
