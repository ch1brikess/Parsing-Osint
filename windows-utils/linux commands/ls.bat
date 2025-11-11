@echo off
setlocal enabledelayedexpansion

set "BLUE=[34m"
set "GREEN=[32m"
set "RED=[31m"
set "YELLOW=[33m"
set "RESET=[0m"

if "%~1"=="" (
    set "path=."
) else (
    set "path=%~1"
)

for /f "delims=" %%i in ('dir /b /a "!path!" 2^>nul') do (
    if exist "!path!\%%i\" (
        echo !BLUE!%%i!RESET!
    ) else (
        echo %%i
    )
)
endlocal