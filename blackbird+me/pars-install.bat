@echo off
setlocal

cd /d "%~dp0"

python --version
pip install -r requirements.txt
python main.py --setup-ai