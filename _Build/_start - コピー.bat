@echo off
rem ----------�e��ݒ荀��----------
rem ��WebSocket�̃|�[�g�ԍ���
set port=4444
rem ��WebSocket�̃p�X���[�h��
set password=5555
rem ���V�[���� (���{��͎g�p���Ȃ��ł�������)��
set scene=ApexOverlayTest
rem ���\�[�X�� (���{��͎g�p���Ȃ��ł�������)��
set source=Overlay
rem --------------------------------

main.exe --port %port% --password %password% --scene %scene% --source %source%