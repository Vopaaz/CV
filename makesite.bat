@echo off

set root=%cd%

echo Copying files to site directory
copy "experience.json" "site/src/assets/experience.json"
copy "en\resume-EN-verbose.pdf" "site\public\pdf\resume-EN-verbose.pdf"
copy "en\resume-EN.pdf" "site\public\pdf\resume-EN.pdf"
copy "zh\resume-ZH-verbose.pdf" "site\public\pdf\resume-ZH-verbose.pdf"
copy "zh\resume-ZH.pdf" "site\public\pdf\resume-ZH.pdf"

echo files copied to site directory

echo Deploy the website
cd %root%/site
call deploy.bat

cd %root%
