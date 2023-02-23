@echo off
echo installing and updating discord.py

set /p token=Enter your bot token:

setlocal EnableDelayedExpansion

set "file=bot.py"
set "tempFile=bot_temp.py"

(for /F "delims=" %%i in (!file!) do (
    set "line=%%i"
    set "line=!line:token is here=!token!"
    echo(!line!
)) > !tempFile!

del !file!
ren !tempFile! !file!

echo Token has been inserted into bot.py
