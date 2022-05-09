@echo off
rd /q %~dp0build
call apexoverlaymanager_build\Scripts\activate
pyinstaller main.py -F
pause