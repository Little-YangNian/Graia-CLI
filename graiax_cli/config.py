import yaml
import pathlib
import os


def config(path,addr,key,socket,qid):
    path = pathlib.Path(path)
    if not path.is_dir():
        os.mkdir(path)
    if socket.lower() == "true":
        socket = True
    else:
        socket = False
    main_config = yaml.dump(
            {"addr":addr,"authkey":key,"websocket":socket,"qid":int(qid)},
            Dumper=yaml.SafeDumper)
    os.chdir(path)
    with open("config.yaml",mode="w") as f:
        f.write(main_config)


        
    
