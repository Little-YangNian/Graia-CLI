import click

try:
    import pip
except ImportError:
    print('如果你连pip都没有，那别用python了')

things = {
    'app': 'graia-application-mirai',
    'saya': 'graia-saya',
    'scheduler': 'graia-scheduler',
}


class Install():
    def __init__(self, thing, version, upgrade):
        pip_cmd = ['install']
        if version is not None:
            self.version = '==' + version
        else:
            self.version = ''
        if thing == ():
            click.echo('Nothing to get,application will be installed')
            pip_cmd.append(things['app'] + self.version)
        elif thing in things.keys():
            pip_cmd.append(things[thing] + self.version)
        else:
            click.echo('This maybe not graia project or it meet some wrong')
            quit()

        if upgrade:
            pip_cmd.append('-U')
        else:
            pass
        self.cmd = pip_cmd

    def install(self):
        stats_code = pip.main(self.cmd)
        if stats_code != 0:
            print("安装失败")
        elif stats_code == 0:
            print('安装成功')
        else:
            print('????????????????????????')


@click.command('install')
@click.argument('get', nargs=-1)
@click.option('--upgrade', default=False, help='upgrade things')
@click.option('--version', default=None, help='install version')
def main(get, upgrade, version):
    ir = Install(get[0], version, upgrade)
    ir.install()
