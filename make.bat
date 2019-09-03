@echo off

set root=%cd%

cd %root%/en
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-EN-verbose.tex"
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-EN-verbose.tex"
echo EN-verbose: FINISHED

cd %root%/en
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-EN.tex"
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-EN.tex"
echo EN: FINISHED

cd %root%/zh
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-ZH-verbose.tex"
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-ZH-verbose.tex"
echo ZH-VERBOSE: FINISHED

cd %root%/zh
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-ZH.tex"
lualatex -synctex=1 -interaction=nonstopmode --shell-escape "./CV-ZH.tex"
echo ZH: FINISHED
