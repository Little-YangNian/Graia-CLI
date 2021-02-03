#! python3

from .scaffold import init_tool
import typer
import sys
import os
from .graia_installer import GraiaInstaller

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
    graia install --install 安装Graia  可选参数版本号
    
    graia install --upgrade 更新Graia
    
    """ 
    
    installer = GraiaInstaller()
    
    if upgrade:
        installer.upgrade()
    
    if install:
        installer.install()
        if installv != "":
            installer.install_v(installv)

@app.command()
def init(path:str= typer.Argument(...)):
    
    """
    graia init [path]
    
    init_tool(path)
    normal_echo("OK")
    """

if __name__ == "__main__":
    app()
