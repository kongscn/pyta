@echo off
echo start plotting...
cd Rfiles
rscript DJIA.R > maketex-out.log
cd ..
echo start building doc...
D:\texlive\bin\win32\lualatex.exe _main.tex >> maketex-out.log
echo start 2nd pass...
D:\texlive\bin\win32\lualatex.exe _main.tex >> maketex-out.log
echo start 3rd pass...
D:\texlive\bin\win32\lualatex.exe _main.tex >> maketex-out.log

del demo-proj.pdf
rename _main.pdf demo-proj.pdf

echo renamed to demo-proj.pdf
pause