#!/usr/bin/python3

import os
import sys
import typer
from commands.installer import Installer
from commands.initializer import Initializer

app = typer.Typer()

installer = Installer(app)
@app.command()
def init():
    """交互式初始化Graia项目"""
    initializer = Initializer()
    initializer.run()
    
    
if __name__ == '__main__':
    app()
