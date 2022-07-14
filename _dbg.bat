@echo off
cd %~dp0
call _Compile_Updater.bat
move "%~dp0AOM_Updater.exe" "%~dp0_Debug"
echo.
echo プロセス追跡くん経由でアプリケーションを起動
echo.
set /P Arg="起動引数を指定: "
echo.
_Resources\Debug\ProcessTsuisekiKunNN.exe "%~dp0_Debug\AOM_Updater.exe" "%Arg%"