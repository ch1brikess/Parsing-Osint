@echo off
if "%~1"=="" (
    echo Usage: cat filename
    exit /b 1
)
type "%~1"