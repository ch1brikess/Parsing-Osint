@echo off
setlocal enabledelayedexpansion

if "%~1"=="" (
    echo Usage: rm [-f] [-r|-R] FILE...
    echo Remove (unlink) the FILE(s).
    echo   -f, --force    ignore nonexistent files and arguments, never prompt
    echo   -r, -R, --recursive   remove directories and their contents recursively
    exit /b 1
)

set "recursive=0"
set "force=0"
set "args="

:argloop
if "%~1"=="" goto :doneargs

if "%~1"=="--help" (
    echo Usage: rm [-f] [-r|-R] FILE...
    echo Remove (unlink) the FILE(s).
    echo   -f, --force    ignore nonexistent files and arguments, never prompt
    echo   -r, -R, --recursive   remove directories and their contents recursively
    exit /b 0
)

if "%~1"=="-f" (
    set "force=1"
    shift
    goto :argloop
)
if "%~1"=="--force" (
    set "force=1"
    shift
    goto :argloop
)

if "%~1"=="-r" (
    set "recursive=1"
    shift
    goto :argloop
)
if "%~1"=="-R" (
    set "recursive=1"
    shift
    goto :argloop
)
if "%~1"=="--recursive" (
    set "recursive=1"
    shift
    goto :argloop
)

goto :doneargs

:doneargs
set "files="
:collectfiles
if "%~1"=="" goto :execute
set "files=!files! "%~1""
shift
goto :collectfiles

:execute
if "!files!"=="" (
    echo rm: missing operand
    echo Try 'rm --help' for more information.
    exit /b 1
)

for %%F in (!files!) do (
    if exist "%%~F" (
        if exist "%%~F\" (
            if "!recursive!"=="1" (
                if "!force!"=="1" (
                    rmdir /s /q "%%~F" >nul 2>&1
                ) else (
                    rmdir /s "%%~F"
                )
            ) else (
                echo rmdir /s "%%~F" would be required. Use -r to remove directories.
                if "!force!"=="0" exit /b 1
            )
        ) else (
            if "!force!"=="1" (
                del "%%~F" >nul 2>&1
            ) else (
                del "%%~F"
            )
        )
    ) else (
        if "!force!"=="0" (
            echo rm: cannot remove '%%~F': No such file or directory
            exit /b 1
        )
    )
)

exit /b 0