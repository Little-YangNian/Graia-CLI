#!/usr/bin/python3

import os
import sys
import typer
import logging
from .installer import Installer
from .initializer import Initializer

app = typer.Typer()


@app.command()
def install(upgrade: bool=False, version: str=typer.Argument(None)):
    """安装Graia，--upgrade 升级Graia，可指定版本"""
    
    installer = Installer()
    if upgrade:
        if 0 != installer.upgrade():
            logging.error(u'升级失败')
            sys.exit(1)
        logging.info(u'升级成功')
        
    else:
        if 0 != installer.install(version=version):
            logging.error(u'安装失败')
            sys.exit(1)
        logging.info(u'安装成功')
        

@app.command()
def init():
    """交互式初始化Graia项目"""
    initializer = Initializer()
    initializer.run()
    
    
if __name__ == '__main__':
    app()
