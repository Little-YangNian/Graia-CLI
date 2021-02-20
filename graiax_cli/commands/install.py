import typer
import os
import sys
import logging

class Install(object):
    """安装类
    
    Attributes:
        py_path: python解释器路径
        package: 安装包名
    """
    def __init__(self, app: typer.Typer, package: str='graia-application-mirai'):
        self.py_path = sys.executable

        
        #注册指令
        @app.command()
        def install(name: str=typer.Argument(None), upgrade: bool=False, version: str=typer.Argument(None)):
            """安装Graia系列\n参数application 安装Application\nscheduler 安装Scheduler\nsaya 安装saya\n默认application，选项––upgrade可以更新"""
            things = {
                    "application":"graia-application-mirai",
                    "scheduler":"graia-scheduler",
                    "saya":"graia-saya",
                    "None":"graia-application-mirai"
                    }

            try:
                self.package = things[name.lower()]
            except:
                logging.error("没有")
                quit()
            if upgrade:
                if 0 != self.upgrade():
                    logging.error(u'升级失败')
                    sys.exit(1)
                logging.info(u'升级成功')
        
            else:
                if 0 != self.install(version=version):
                    logging.error(u'安装失败')
                    sys.exit(1)
                logging.info(u'安装成功')
        
    
    def install(self, version: str=None):
        """安装
        
        Args:
            version: (可选)指定安装版本
            
        Returns:
            返回0则成功，其它值则安装失败
        """
        if version == None:
            return self.upgrade()
        else:
            command = f'{self.py_path} -m pip install {self.package}=={version}'
            return os.system(command)
    
    def upgrade(self):
        """更新
        
        Returns:
            0成功，其它值则失败
        """
        command = f'{self.py_path} -m pip install -U {self.package}'
        return os.system(command)
