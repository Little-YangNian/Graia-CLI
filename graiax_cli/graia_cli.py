#! python3

from .scaffold import init_tool
from .scaffold import init_config
import typer
import sys
import os
from .graia_installer import GraiaInstaller
from .config import config as cf

def good_echo(text):
    typer.echo(typer.style(text,fg=typer.colors.BRIGHT_GREEN,bold=True))

def bad_echo(text):
    typer.echo(typer.style(text,fg=typer.colors.RED,bold=True))

def normal_echo(text):
    typer.echo(typer.style(text,fg=typer.colors.WHITE,bold=True))

app = typer.Typer()

@app.command()
def install(
        install: bool=False,installv:str= typer.Argument(""),upgrade: bool=False
        ):

    """ 
    graiax install --install 安装Graia  可选参数版本号
    
    graiax install --upgrade 更新Graia
    
    """ 
    
    installer = GraiaInstaller()
    
    if upgrade:
        installer.upgrade()
    
    if install:
        installer.install()
        if installv != "":
            installer.install_v(installv)

@app.command()
def init(path: str = typer.Argument(...),
        c:bool=False):
    
    """
    graiax init [path]
    """
    if c:
        init_config(path)
    else:
        normal_echo(path)
        init_tool(path)
        normal_echo("OK")
@app.command()
def config(path: str = typer.Argument(...),
        url: str= typer.Option(...),
        qid: str= typer.Option(...),
        key: str= typer.Option(...)
        ,websocket: str= typer.Option(...)):
    cf(path,url,key,websocket,qid)

if __name__ == "__main__":
    app()
