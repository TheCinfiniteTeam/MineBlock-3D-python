#encoding:utf-8
def hasTags(player):
    try:
        if player.getTags == "{}":
            return True;
        elif not player.getTags == "{}":
            return False;
    except :
        return {
            'Error':True
        }
        raise TypeError('[MineBlock](Error) Player.hasTags function')
