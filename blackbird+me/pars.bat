@echo off
setlocal

cd /d "%~dp0"

if "%~1"=="" (
    python main.py --help
    pause
    exit
) 

python main.py %*

pause