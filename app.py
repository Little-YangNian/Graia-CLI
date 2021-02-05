from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
import asyncio
import yaml

config_file = open('config.yaml')
configs = yaml.load(config_file,Loader=yaml.Loader)
qid = int(configs['qid'])
address = str(configs['addr'])
key = str(configs['authkey'])
socket = bool(configs['websocket'])

loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host=address, # 填入 httpapi 服务运行的地址
        authKey=key, # 填入 authKey
        account=qid, # 你的机器人的 qq 号
        websocket=socket # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)
