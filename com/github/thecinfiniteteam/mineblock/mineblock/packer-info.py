#encoding:utf-8
import com.github.thecinfiniteteam.mineblock.mineblock.api.addonLoader as addload
from com.github.thecinfiniteteam.mineblock.mineblock.api.author import Author
@Author(["TheCinfiniteTeam","chenjj100419"])
def getPacker_info():
    return "mineblock"
class packer_info(addload.addonLoader):
    def getPacker_maininfo(self):
        return {"id":self.mineblockId,"name":self.mineblockName,"class":self.mineblockClass,"authorlist":self.mineblockAuthorList,"version":self.mineblockVersion,"isV":self.isV}