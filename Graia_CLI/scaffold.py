import requests
import os
from pathlib import Path

def init_tool(path):
    path = Path(path)
    if not path.is_dir():
        os.mkdir(path)
    os.chdir(path)
    botpy = requests.get("https://pan-1302360504.cos.ap-chengdu.myqcloud.com/share/HelloGraia.py")
    with open(f"bot.py",mode="w",encoding="utf-8") as f:
        f.write(str(botpy.content.decode("utf-8")))

