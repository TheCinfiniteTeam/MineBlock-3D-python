#encoding:utf-8
import com.github.thecinfiniteteam.mineblock.mineblock.message.api_io as msg_io
import sys,pygame,tkinter,numbers

MINEBLOCK_ID = "mineblock"
MINEBLOCK_NAME = "MineBlock"
MINEBLOCK_VERSION = "1.0.0"
class mineblock():
    def __init__(self):
        self.MINEBLOCK_ID = "mineblock"
        self.MINEBLOCK_NAME = "MineBlock"
        self.MINEBLOCK_VERSION = "1.0.0"
    def gameinit(self):
        return True
    def gameloader(self):
        return True;
    def worldinit(self):
        return True
    def worldloader(self):
        return True
    def dataloader(self):
        return True
    def worldsave(self):
        return True
    def datasave(self):
        return True
    def __exit__(self):
        pygame.quit()
        tkinter._exit()
        sys.exit()
