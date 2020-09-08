#encoding:utf-8
import com.github.thecinfiniteteam.mineblock.mineblock.player.player as player
import json,os,time
def getTags(path):
    if os.path.isdir(path):
        with open(file=path,mode="a+",encoding="utf-8") as tags_json:
            return json.loads(tags_json.read())
