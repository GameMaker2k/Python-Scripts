@echo off
set PyVer=2.7
set OLDPATH=%PATH%;
FOR /f "tokens=3* delims=	" %%! in ('REG.EXE QUERY "HKEY_LOCAL_MACHINE\SOFTWARE\Python\PythonCore\%PyVer%\InstallPath" /ve ^| Findstr.exe /ri "\<NO NAME\>"') DO set PATH=%PATH%;%%!;
pysmile-gen.bat %1 "Python" | python.exe -b -B -x -
