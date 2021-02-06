#!/usr/bin/python3

import os
import sys
import typer
import inspect
import importlib
import .commands

app = typer.Typer()

def load_commands(app: typer.Typer):
    """加载命令"""
    pack_path = commands.__path__[0]
    mods = [file[:-3] for file in os.listdir(pack_path) if file.endswith('.py') and file !='__init__.py']
    #pack_path = 'commands'
    pack_path = '.commands'
    for mod in mods:
        module = importlib.import_module(f'.{mod}', pack_path)
        exec(f'{mod} = module.{mod.capitalize()}(app)')

def main():
    load_commands(app)

if __name__ == '__main__':
    main()
    app()
