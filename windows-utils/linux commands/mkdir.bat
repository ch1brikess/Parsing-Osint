@echo off
if "%~1"=="" (
    echo Usage: mkdir dirname
    exit /b 1
)
mkdir "%~1"