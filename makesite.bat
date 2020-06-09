@echo off

set root=%cd%

echo Copying files to site directory
copy "experience.json" "site/src/assets/experience.json"
copy "en\CV-EN-verbose.pdf" "site\public\pdf\CV-EN-verbose.pdf"
copy "en\CV-EN.pdf" "site\public\pdf\CV-EN.pdf"
copy "zh\CV-ZH-verbose.pdf" "site\public\pdf\CV-ZH-verbose.pdf"
copy "zh\CV-ZH.pdf" "site\public\pdf\CV-ZH.pdf"

echo files copied to site directory

echo Deploy the website
cd %root%/site
call deploy.bat

cd %root%
