import os
import click
import importlib
os.chdir("graiax_cli")

@click.group()
def group():
    pass


def cli():
    cmdlist = os.listdir('./commands')
    for i in cmdlist:
        if i.endswith('.py') and i != '__init__.py':
            i = i.replace('.py', '')
            cmd = importlib.import_module('graiax_cli.commands.' + i)
            group.add_command(cmd.main)
    return group


app = cli()
if __name__ == '__main__':
    app()
