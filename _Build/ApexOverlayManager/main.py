import argparse
from re import sub
import subprocess
import time

#import pyocr
from obswebsocket import obsws, requests

name = "ApexOverlayManager"
version = "0.1.0"
author = "Milkeyyy"

print(f"{name} Version {version}\nCreated by {author}")

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
print(f"Connect: {host}:{port}")

while loopv == True:
	ocr_r = subprocess.run([r"OCRCapture.exe"], shell=True, text=True, stdout=subprocess.PIPE)
	if ocr_r.stdout == "True":
		print(f"オーバーレイ有効化 ({ocr_r.stdout})")
		switch_overlay(True)
	else:
		print(f"オーバーレイ無効化 ({ocr_r.stdout})")
		switch_overlay(False)

	#time.sleep(1)

#オーバーレイを有効化/無効化
#print(f"Render: {args.render}")
#if args.render == "True":
#	eneble_overlay()
#elif args.render == "False":
#	disable_overlay()

#OBSから切断する
obs.disconnect
