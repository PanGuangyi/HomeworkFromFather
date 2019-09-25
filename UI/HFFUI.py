import os
import wx
from wx import xrc
from tasks.HomeworkCreator import HomeworkCreator
import pdb

class Config():
    def __init__(self):
        pass
    
    def get_configs(self,task):
        pass

class HFF(wx.App):

    def OnInit(self):
        self.res = xrc.XmlResource(os.path.join(os.path.abspath(os.path.dirname(__file__)),'HFFUI.xrc'))        
        self.init_frame()
        return True

    def init_frame(self):
        self.frame = self.res.LoadFrame(None, 'HFFFrame')
        if self.frame is None:
            pdb.set_trace()

        self.frame.Bind(wx.EVT_BUTTON, self.Onbtn_Math_ShuZiShuXie, id=xrc.XRCID('btn_Math_ShuZiShuXie'))
        self.frame.Show()

    def Onbtn_Math_ShuZiShuXie(self, evt):
        cfg = Config()
        cfg_items = cfg.get_configs("Math_ShuZiShuXie")
        
        hwc = HomeworkCreator("Math_ShuZiShuXie")
        
        
        
def ShowUI():
    app = HFF(False)
    app.MainLoop()
        

if __name__ == '__main__':
    app = HFF(False)
    app.MainLoop()