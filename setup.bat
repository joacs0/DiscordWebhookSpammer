@echo off
echo Installing dependecies...
pip install -r requirements.txt
cls
echo Running WebhookSpammer...
timeout /t 2
py main.py
