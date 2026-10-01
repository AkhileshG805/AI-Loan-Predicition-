@echo off
title LoanAI — Credit Underwriting Decision Support System
echo ========================================================
echo   LoanAI — Decision Support System Launcher
echo ========================================================
echo.

cd /d "%~dp0"

REM Check for portable python in scratch directory
if exist "..\python_embed\python.exe" (
    echo [INFO] Using portable Python environment...
    start http://127.0.0.1:5000
    "..\python_embed\python.exe" app.py
    goto end
)

REM Check for system python
python --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [INFO] Using system Python...
    start http://127.0.0.1:5000
    python app.py
    goto end
)

echo [ERROR] Python was not detected on this machine.
echo Please run python app.py manually or ensure Python is installed.
pause

:end
