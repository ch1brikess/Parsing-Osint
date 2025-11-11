@echo off
setlocal enabledelayedexpansion

chcp 65001 >nul
set "FILE=%~1"

if "!FILE!"=="" (
    set /p FILE="File name: "
)

if not exist "!FILE!" (
    echo Creating new file: !FILE!
    echo.
)

:edit
cls
echo [Nano for Windows] - !FILE! - Use F1 to Exit
echo ===========================================
if exist "!FILE!" type "!FILE!"
echo.
echo ===========================================
echo F1: Exit

choice /c 12 /n >nul
if errorlevel 1 goto :exit

:save
if not exist "!FILE!" (
    echo. > "!FILE!"
)
echo File saved: !FILE!
goto :exit

:exit
endlocal