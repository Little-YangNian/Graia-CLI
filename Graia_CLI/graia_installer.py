import typer

def good_echo(text):
    typer.echo(typer.style(text,fg=typer.colors.BRIGHT_GREEN,bold=True))

def bad_echo(text):
    typer.echo(typer.style(text,fg=typer.colors.RED,bold=True))

def normal_echo(text):
    typer.echo(typer.style(text,fg=typer.colors.WHITE,bold=True))

class Graia_installer():
    
    def __init__(self):
        self.py_path=sys.executable
    
    def install(self):
        good_echo("开始安装Graia")
        commands = f"{self.py_path} -m pip install graia-application-mirai"
        os.system(commands)
        try:
            import graia.application
            good_echo("安装成功，前往Github查看文档")
        except:
            bad_echo("安装失败")
    
    def upgrade(self):
        os.system(f"{self.py_path} -m pip install graia-application-mirai -U")
        try:                
            import graia.application    
            good_echo("更新成功")
        except:                                         
            bad_echo("更新失败")
    
    def install_v(self,v):
        os.system(f"{self.py_path} -m pip install graia-application-mirai=={v}")
