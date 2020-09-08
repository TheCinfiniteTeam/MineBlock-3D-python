#encoding:utf-8
import com.github.thecinfiniteteam.mineblock.mineblock.player.player as player
def hasTags(player,path,uuid):
    try:
        if player.getTags.getTags(path+uuid) == "{}":
            return True;
        elif not player.getTags.getTags(path+uuid) == "{}":
            return False;
    except :
        return {
            'Error':True
        }
        raise OSError('[MineBlock](Error) Player.hasTags function')
