@echo off
cd %~dp0
call _Compile.bat
move "%~dp0ApexOverlayManager.exe" "%~dp0_Debug"
echo.
echo プロセス追跡くん経由でアプリケーションを起動
echo.
_Resources\Debug\ProcessTsuisekiKunNN.exe "%~dp0_Debug\ApexOverlayManager.exe"
