import ui
from objc_util import *
from pprint import pprint
import os

def pPass():
  print('Pass')
def pdbg(obj):
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
    pass
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


# load classes
UITextView,UIColor,UIFont,UIToolbar,UIBarButtonItem=map(ObjCClass,['UITextView','UIColor','UIFont','UIToolbar','UIBarButtonItem'])



# 文字流し込み
def dummy_txt(path_str):
  d_path=os.path.abspath(path_str)
  with open(d_path,encoding='utf-8') as f:
    d_txt = f.read()
  return d_txt


# --- mainClass
class MainView(ui.View):
  def __init__(self,*args, **kwargs):
    # todo: おまじないになっとる
    super().__init__(self, *args, **kwargs)
    self.bg_color='red'
    
    
    f = CGRect(CGPoint(0, 0), CGSize(self.width, self.height))
    
    # font 呼び出し
    tFnt=UIFont.fontWithName_size_('Source Code Pro',16)
    
    # とりあえずのサイズで生成
    self.ed_view=UITextView.alloc().initWithFrame_(f)
    #self.ed_view.setOpaque_(0)
    
    
    #bg_color = UIColor.color(red=0.0, green=0.0, blue=1.0, alpha=0.5)
    bg_color = UIColor.color(red=1.0, green=1.0, blue=1.0, alpha=1.0)
    
    self.ed_view.setBackgroundColor_(bg_color)
    #pdbg(self.ed_view)
    
    # ここで、textview を最大化
    flex_width, flex_height = (1<<1), (1<<4)
    self.ed_view.setAutoresizingMask_(flex_width|flex_height)
    # 大文字にしない
    self.ed_view.setAutocapitalizationType_(0)
    
    # font 設定
    self.ed_view.font=tFnt
    
    keyboardToolbar=UIToolbar.alloc().init()
    keyboardToolbar.sizeToFit()
    doneBarButton=UIBarButtonItem.alloc().initWithBarButtonSystemItem_target_action_(0,self.ed_view,sel('endEditing:')) 
    #keyboardToolbar.items = [flexBarButton, doneBarButton]
    keyboardToolbar.items = [doneBarButton]
    
    self.ed_view.setInputAccessoryView_(keyboardToolbar)
    
    # dark
    self.ed_view.setKeyboardAppearance_(sel('_dark'))
    self.ed_view.autorelease()
    
    
    
    ObjCInstance(self).addSubview_(self.ed_view)
    
    # todo: リファクタリングも考えなくちゃ
    
  def layout_view(self):
    pass
  def set_font(self):
    pass
  def set_cstmKbd(self):
    pass
    

  


v=MainView()
v.ed_view.text=dummy_txt('dummy.txt')

v.present()

