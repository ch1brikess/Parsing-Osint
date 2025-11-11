@echo off
setlocal enabledelayedexpansion

set "RED=[31m"
set "GREEN=[32m"
set "YELLOW=[33m"
set "RESET=[0m"

if "%~1"=="" (
    echo !RED![sudo] Usage: sudo command [args]!RESET!
    echo Examples:
    echo   sudo net start wuauserv
    echo   sudo sc query sshd
    echo   sudo reg add HKLM\Software\Test
    exit /b 1
)

:: Проверка прав администратора
net session >nul 2>&1
if %errorlevel% equ 0 (
    echo !GREEN![sudo] Already running as administrator!RESET!
    %*
    exit /b 0
)

set "FULL_CMD=%*"
set "CMD_PATH=%~1"

:: Поиск полного пути к команде
where "!CMD_PATH!" >nul 2>&1
if !errorlevel! equ 0 (
    for /f "delims=" %%I in ('where "!CMD_PATH!"') do set "CMD_PATH=%%I"
)

echo !YELLOW![sudo] Elevating: !FULL_CMD!!RESET!

:: Запуск через PowerShell с UAC
set "PS_CMD=Start-Process cmd -ArgumentList '/c !FULL_CMD!' -Verb RunAs -Wait"
powershell -Command "!PS_CMD!"

endlocal