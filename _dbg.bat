@echo off
cd %~dp0
call _Compile.bat
move "%~dp0ApexOverlayManager.exe" "%~dp0_Debug"
echo.
echo �v���Z�X�ǐՂ���o�R�ŃA�v���P�[�V�������N��
echo.
set /P Arg="�N���������w��: "
echo.
_Resources\Debug\ProcessTsuisekiKunNN.exe "%~dp0_Debug\ApexOverlayManager.exe" "%Arg%"