@echo off

call python render-experiences.py
call python render-mains.py

copy experience.json site/src/assets/experience.json

set root=%cd%
set silentfile=silent.aux

cd %root%/en
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-EN-verbose.tex" > %silentfile%
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-EN-verbose.tex" > %silentfile%
if errorlevel 1 ( echo [ATTENTION] EN-verbose: FAILED [ATTENTION] ) else ( echo EN-verbose: finished )

cd %root%/en
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-EN.tex" > %silentfile%
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-EN.tex" > %silentfile%
if errorlevel 1 ( echo [ATTENTION] EN: FAILED [ATTENTION] ) else ( echo EN: finished )

cd %root%/zh
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-ZH-verbose.tex" > %silentfile%
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-ZH-verbose.tex" > %silentfile%
if errorlevel 1 ( echo [ATTENTION] ZH-verbose: FAILED [ATTENTION] ) else ( echo ZH-verbose: finished )

cd %root%/zh
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-ZH.tex" > %silentfile%
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-ZH.tex" > %silentfile%
if errorlevel 1 ( echo [ATTENTION] ZH: FAILED [ATTENTION] ) else ( echo ZH: finished )

