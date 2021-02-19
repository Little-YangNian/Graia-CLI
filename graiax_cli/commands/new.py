import os
import yaml
import typer
import requests
#from graiax_cli import template

class New(object):
    """交互式初始化项目"""
    
    def __init__(self, app: typer.Typer):

        @app.command()
        def new(type: str=typer.Argument('project')):
            """
            新建Graia项目
            
            type: 项目类型，可选project, plugin
            """
            #self.run()
            pass


    """
    def config(self, auth_key: str, websocket: bool, qq: str, addr: str='http://localhost:8080'):
        config = yaml.dump({'addr': addr, 'authKey': auth_key, 'websocket': websocket, 'qq': int(qq)},
                            Dumper=yaml.SafeDumper)
        with open('./GraiaConfig.yaml', 'w') as f:
            f.write(config)
        
    def run(self):
        path = input('希望初始化的目录：')
        if not os.path.isdir(path):
            os.mkdir(path)
        os.chdir(path)
        if not 'config.yaml' in os.listdir():
            addr = input('httpapi 服务运行的地址：')
            if not addr.startswith('http:\\\\'):
                addr = 'http:\\\\' + addr
            auth_key = input('authKey：')
            websocket = input('是否使用websocket(是/否)：')
            if websocket == '是':
                websocket = True
            else:
                websocket = False
            qq = input('你的机器人qq号：')
            self.config(addr=addr, auth_key=auth_key, websocket=websocket, qq=qq)
        with open('app.py', 'w+') as f:
            f.write(template.app)
        with open('bot.py', 'w+') as f:
            f.write(template.bot)

"""

class TemplateGetClient(object):
    """从指定的网络位置获取项目和插件模板

    Attributes:
        url: 网址
    """
    def __init__(self, url: str):
        self.url = url

    def get(self, type: str):
        pass