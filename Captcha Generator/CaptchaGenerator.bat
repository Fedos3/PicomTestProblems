@Echo Off
Setlocal
color 0a
set "Source=%~dp0"
cd /d "%~dp0"

echo %Source% 
set MIN=10000
set MAX=99999
set /a R=MIN+(MAX)*%random%/32768 

magick convert -size 256x128 gradient:white-red -font Corsiva -pointsize 64 ^
          -tile gradient:red-white  -annotate +20+80 %R%  -swirl 90  -blur 2x3  captcha.jpg
start captcha.jpg
cls
echo. 
echo  Done! Captcha - %R%
echo.

pause


	