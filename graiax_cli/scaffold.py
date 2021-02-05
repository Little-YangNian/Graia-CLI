import requests
import os


def init_tool(path):
    if not os.path.isdir(path):
        os.mkdir(path)
    os.chdir(path)
    botpy = requests.get("https://pan-1302360504.cos.ap-chengdu.myqcloud.com/share/HelloGraia.py")
    with open(f"bot.py",mode="w",encoding="utf-8") as f:
        f.write(str(botpy.content.decode("utf-8")))

def init_config(path,):
    if not os.path.isdir(path):
        print("你应该先使用graiax config [path]生成配置文件")
    else:
        os.chdir(path)
        try:
            os.mkdir("app")
        except:
            pass
        with open("app/app.py",mode="w") as f:
            apppy = requests.get("https://pan-1302360504.cos.ap-chengdu.myqcloud.com/share/app.py")
            f.write(str(apppy.content.decode("utf-8")))
        with open("bot.py",mode="w") as f:
            f.write("from app.app import bcc\nfrom app.app import app\n\napp.launch_blocking()")
        print("ok")
