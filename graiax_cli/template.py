template=r'''from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
import asyncio
import yaml

with open('config.yaml', 'r') as f:
    configs = yaml.load(f, Loader=yaml.Loader)
qid = int(configs['qq'])
address = str(configs['addr'])
key = str(configs['authKey'])
socket = bool(configs['websocket'])

loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host=address,
        authKey=key,
        account=qid,
        websocket=socket
    )
)
'''

bot=r'''from app import bcc
from app import app

app.launch_blocking()
'''