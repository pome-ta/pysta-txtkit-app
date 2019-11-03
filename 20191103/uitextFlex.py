import ui
from objc_util import *
from pprint import pprint

class MainView(ui.View):
  def __init__(self,*args, **kwargs):
    self.bg_color='red'
    
    self.tv=ui.TextView()
    self.tv.flex='WH'
    self.add_subview(self.tv)
    
    
    
    
  def pdbg(self):
    #chk=ObjCInstance(self._objc_ptr)
    chk=ObjCInstance(self.tv)
    
    print('# --- dir( )______')
    pprint(dir(chk))
    print('# --- vars( )______')
    pprint(vars(chk))
    print('# --- name______')
    pprint(chk)
    
    print('# --- ivarDescription')
    pprint(chk._ivarDescription())
    print('# --- shortMethodDescription')
    pprint(chk._shortMethodDescription())
    print('# --- methodDescription')
    pprint(chk._methodDescription())
    
    print('# --- recursiveDescription')
    pprint(chk.recursiveDescription())
    print('# --- autolayoutTrace')
    pprint(chk._autolayoutTrace())
    
  


v=MainView()
#v.tv.text='hogeee'
v.present()
v.pdbg()
