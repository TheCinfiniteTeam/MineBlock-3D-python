#encoding:utf-8
import com.github.thecinfiniteteam.mineblock.mineblock.mineblock as mb
class addonLoader():
    def __init__(self):
        self.mineblockClass = mb
        self.mineblockId = self.mineblockClass.MINEBLOCK_ID
        self.mineblockName = self.mineblockClass.MINEBLOCK_NAME
        self.isV = True
        self.mineblockAuthorList = ["TheCinfiniteTeam","chenjj100419"]
        self.mineblockVersion = self.mineblockClass.MINEBLOCK_VERSION
    def Addon(self,ADDON_ID,ADDON_NAME,ADDON_AUTHORLIST,ADDON_VERSION,CLASS):
        isAddonMainClass = True
        addonClass = CLASS
        addonId = ADDON_ID
        addonName = ADDON_NAME
        addonAuthorList = ADDON_AUTHORLIST
        addonVersion = ADDON_VERSION