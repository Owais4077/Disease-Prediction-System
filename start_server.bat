@echo off
echo Disease Prediction System - Windows Startup
echo ==========================================

echo Checking Python installation...
python --version
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo.
echo Installing/Updating requirements...
pip install -r requirements.txt

echo.
echo Running migrations...
python manage.py migrate

echo.
echo Starting Django development server...
echo Server will be available at: http://127.0.0.1:8000/
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver

pause
