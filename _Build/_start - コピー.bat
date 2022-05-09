@echo off
rem ----------各種設定項目----------
rem ↓WebSocketのポート番号↓
set port=4444
rem ↓WebSocketのパスワード↓
set password=5555
rem ↓シーン名 (日本語は使用しないでください)↓
set scene=ApexOverlayTest
rem ↓ソース名 (日本語は使用しないでください)↓
set source=Overlay
rem --------------------------------

main.exe --port %port% --password %password% --scene %scene% --source %source%