import ui
from objc_util import ObjCInstance,ObjCClass,CGRect,CGPoint,CGSize

from pprint import pprint

def pdbg(obj):
  def pPass():
    print('--- Pass ----')
  print('# --- name______')
  try:
    pprint(obj)
  except:
    pPass()
  print('# --- vars( )______')
  try:
    pprint(vars(obj))
  except:
    pPass()
  print('# --- dir( )______')
  try:
    pprint(dir(obj))
  except:
    pPass()
  
  # todo: 落ちる時は落ちる
  print('# --- ivarDescription')
  try:
    #pass
    pprint(obj._ivarDescription())
  except:
    pPass()
  print('# --- shortMethodDescription')
  try:
    pprint(obj._shortMethodDescription())
  except:
    pPass()
  print('# --- methodDescription')
  try:
    pprint(obj._methodDescription())
  except:
    pPass()
  
  print('# --- recursiveDescription')
  try:
    pprint(obj.recursiveDescription())
  except:
    pPass()
  print('# --- autolayoutTrace')
  try:
    pprint(obj._autolayoutTrace())
  except:
    pPass()

# --- mainClass
class MainView(ui.View):
  def __init__(self,*args, **kwargs):
    # todo: おまじないになっとる
    super().__init__(self, *args, **kwargs)
    self.bg_color='red'
    self.selfIns = ObjCInstance(self)
    
    
    initFrame = CGRect(CGPoint(0, 0), CGSize(self.width, self.height))
    # fullViewSize
    flex_w, flex_h = (1<<1), (1<<4)
    
    
    uiTextView = ObjCClass('UITextView').alloc()
    self.uiTV = uiTextView
    self.uiTV.initWithFrame_(initFrame)
    self.uiTV.setAutoresizingMask_(flex_w|flex_h)
    self.uiTV.returnKeyType=10
    self.selfIns.addSubview_(self.uiTV)
    
    

v=MainView()
v.present()
pdbg(v.uiTV)

