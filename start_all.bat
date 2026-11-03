@echo off
echo Starting Bus Tracking System...

echo Starting Backend Server...
start cmd /k "cd /d %~dp0server && npm run dev"

echo Starting Frontend Client...
start cmd /k "cd /d %~dp0client && npm run dev"

echo Both services are starting in separate windows.
pause
