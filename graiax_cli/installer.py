import typer
import os
import sys


class Installer(object):
    """安装类
    
    Attributes:
        py_path: python解释器路径
        package: 安装包名
    """
    def __init__(self, package: str='graia-application-mirai'):
        self.py_path = sys.executable
        self.package = package
    
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