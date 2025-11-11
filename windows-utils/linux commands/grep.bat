@echo off
setlocal enabledelayedexpansion

set "RED=[31m"
set "RESET=[0m"

if "%~2"=="" (
    findstr "%~1"
) else (
    findstr "%~1" "%~2"
)
endlocal