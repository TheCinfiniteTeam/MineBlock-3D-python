#encoding:utf-8
import os,json,time
def getInfo_json(path):
    with open(file=path,mode="a+",encoding="utf-8") as info_load:
        info = info_load.read(os.path.getsize(path))
        return info

