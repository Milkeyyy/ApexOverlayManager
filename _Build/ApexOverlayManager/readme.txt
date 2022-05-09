ApexOverlayManager - Version 0.0.1
1. https://github.com/obsproject/obs-websocket/releases/download/4.9.1/obs-websocket-4.9.1-Windows-Installer.exe からインストーラーをダウンロードして、OBS用のWebSocketプラグインをインストールする
2. OBSを起動して、ツールバーの「ツール」から「Websocket サーバー設定」をクリックして、パスワードを設定する(サーバーポートは基本的に変更する必要はありません)
3. Config.json をテキストエディターなどで開いて、「ID」へ自分のIDを設定する(IDは複数に区切って追加することをおすすめします 追加する場合は「"ABC","DEF"」のように「,""」を後ろに追加していってください 例: Milkeyyy_nmGの場合 → "Milkeyyy","nmG")
4. Config.json の「CapturePos」へ解像度に合わせて座標を設定する (1番のモニターからのみキャプチャーできます 1920x1080(初期値)=「176,956,154,41」2560x1440=「235,1275,205,54」)
5. _start.bat をテキストエディターなどで開いて、各種設定項目を設定して保存
6. _start.bat をダブルクリックして起動