@echo off
cd %~dp0
call _Compile_Updater.bat
move "%~dp0AOM_Updater.exe" "%~dp0_Debug"
echo.
echo �v���Z�X�ǐՂ���o�R�ŃA�v���P�[�V�������N��
echo.
set /P Arg="�N���������w��: "
echo.
_Resources\Debug\ProcessTsuisekiKunNN.exe "%~dp0_Debug\AOM_Updater.exe" "%Arg%"