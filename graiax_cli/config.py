import yaml
import os


def config(path,addr,key,socket,qid):
    if not os.path.isdir(path):
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


        
    
