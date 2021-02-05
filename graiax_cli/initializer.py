import os
import yaml
import template

class Initializer(object):
    """交互式初始化项目"""

    def config(self, auth_key: str, websocket: bool, qq: str, addr: str='http://localhost:8080'):
        config = yaml.dump({'addr': addr, 'authKey': auth_key, 'websocket': websocket, 'qq': int(qq)},
                            Dumper=yaml.SafeDumper)
        with open('./config.yaml', 'w') as f:
            f.write(config)
        
    def run(self):
        path = input('希望初始化的目录：')
        if not os.path.isdir(path):
            os.mkdir(path)
        os.chdir(path)
        if not 'config.yaml' in os.listdir():
            addr = input('httpapi 服务运行的地址：')
            auth_key = input('authKey：')
            websocket = input('是否使用websocket(是/否)：')
            if websocket == '是':
                websocket = True
            else:
                websocket = False
            qq = input('你的机器人qq号：')
            config(addr=addr, auth_key=auth_key, websocket=websocket, qq=qq)
        with open('app.py', 'w+') as f:
            f.write(template.template)
        with open('bot.py', 'w+') as f:
            f.write(template.bot)