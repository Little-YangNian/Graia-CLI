#!/usr/bin/python3

import os
import sys
import typer
import inspect
import importlib
#from graiax_cli import commands
import commands

app = typer.Typer()

def load_commands(app: typer.Typer):
    """加载命令
    
    从commands文件夹中导入所有非'_'下划线开头的.py文件，
    并创建为文件名对应首字母大写的类的实例，传入typer.Typer对象，
    命令注册逻辑应在对应类中处理

    Args:
        app: 主Typer对象
    """
    pack_path = commands.__path__[0]
    mods = [file[:-3] 
                for file in os.listdir(pack_path) 
                    if file.endswith('.py') and not file.startswith('_')]
    pack_path = 'commands'
    #pack_path = 'graiax_cli.commands'
    for mod in mods:
        module = importlib.import_module(f'.{mod}', pack_path)
        exec(f'{mod} = module.{mod.capitalize()}(app)')

load_commands(app)

if __name__ == '__main__':
    app()
