import requests
import os

def InitTool(path):
    os.chdir(path)
    botpy = requests.get("https://pan-1302360504.cos.ap-chengdu.myqcloud.com/share/HelloGraia.py")
    with open(f"bot.py",mode="w",encoding="utf-8") as f:
        f.write(str(botpy.content.decode("utf-8")))

