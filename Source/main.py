import argparse
from re import sub
import subprocess
import time
import json

#import pyocr
from obswebsocket import obsws, requests

name = "ApexOverlayManager"
version = "0.1.0"
author = "Milkeyyy"

print(f"\n{name} Version {version}\nCreated by {author}\n")

#引数ぱーさー
parser = argparse.ArgumentParser()
parser.add_argument("--port", help="WebSocket Port",
					type=int,required=True)
parser.add_argument("--password", help="WebSocket Password",
					type=str,required=True)
parser.add_argument("--scene", help="Scene Name",
					type=str,required=True)
parser.add_argument("--source", help="Overlay Source Name",
					type=str,required=True)
parser.add_argument("--render", help="Render",
					type=str,required=False)
args = parser.parse_args()

host = "localhost"
port = args.port
password = args.password
scene = args.scene
source = args.source
loopv = True

#コンフィグを読み込み
config_open = open("Config.json", "r", encoding="UTF-8")
config = json.load(config_open)
print(f"コンフィグを読み込みました: {config}\n")

def switch_overlay(render):
	response = obs.call(requests.SetSceneItemRender(source,render,scene))
	print(f"	{response}")

def eneble_overlay():
	response = obs.call(requests.SetSceneItemRender(source,True,scene))
	print(response)

def disable_overlay():
	response = obs.call(requests.SetSceneItemRender(source,False,scene))
	print(response)

#OBSに接続する
obs = obsws(host,port,password)
obs.connect()
print(f"OBS WebSocketと接続: {host}:{port}\n-準備完了-")

while loopv == True:
	#画面をキャプチャー
	ocr_c = subprocess.run([r"OCRScreenCaptureHelper.exe"], shell=True, text=True, stdout=subprocess.PIPE)
	#print(f"キャプチャー画像: {ocr_c.stdout}")

	#キャプチャーした画像から文字認識
	ocr_w = subprocess.run([r"OCRWorker.exe", ocr_c.stdout], shell=True, text=True, stdout=subprocess.PIPE)
	ocr_w_text = ocr_w.stdout.rstrip("\n")

	detect = False
	sourcerender = obs.call(requests.GetSceneItemProperties(source,scene)).datain["visible"]
	for w in config["ListOfWordToDetect"]:
		if w in ocr_w_text:
			detect = True
			break

	#単語を検知できたらオーバーレイを有効化
	if detect == True:
		if sourcerender is False:
			print(f"\nオーバーレイ有効化 | 検知文字: {ocr_w_text}")
			switch_overlay(True)
	else:
		if sourcerender is True:
			print(f"\nオーバーレイ無効化 | 検知文字: {ocr_w_text}")
			switch_overlay(False)

	#time.sleep(0.1)

#オーバーレイを有効化/無効化
#print(f"Render: {args.render}")
#if args.render == "True":
#	eneble_overlay()
#elif args.render == "False":
#	disable_overlay()

#OBSから切断する
obs.disconnect
