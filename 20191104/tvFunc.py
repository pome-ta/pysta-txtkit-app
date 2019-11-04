import ui

class V(ui.View):
  def __init__(self):
    self.bg_color='red'
    self.tv=ui.TextView()
    self.tv.flex='WH'
    self.add_subview(self.tv)

v=V()
v.tv.font=('Source Code Pro',16)
v.tv.text='あああ、ghjbxd\nilo01'
v.present()
