import ui
from objc_util import *
from pprint import pprint

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
    #pprint(obj._ivarDescription())
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







class MainView(ui.View):
  def __init__(self,*args, **kwargs):
    self.bg_color='red'
    
    f = CGRect(CGPoint(0, 0), CGSize(self.width, self.height))
    uitextview=ObjCClass('UITextView')
    
    # font 呼び出し
    uifont=ObjCClass('UIFont')
    tFnt=uifont.fontWithName_size_('Source Code Pro',16)
    #pprint(dir(uifont))
    
    
    
    # とりあえずのサイズで生成
    self.ed_view=uitextview.alloc().initWithFrame_(f)
    
    # ここで、textview を最大化
    flex_width, flex_height = (1<<1), (1<<4)
    self.ed_view.setAutoresizingMask_(flex_width|flex_height)
    # 大文字にしない
    self.ed_view.setAutocapitalizationType_(0)
    #pprint(dir(self.ed_view))
    
    # font 設定
    self.ed_view.font=tFnt
    
    keyboardToolbar=ObjCClass('UIToolbar').alloc().init()
    keyboardToolbar.sizeToFit()
    flexBarButton=ObjCClass('UIBarButtonItem').alloc().initWithBarButtonSystemItem_target_action_(2,None,None)
    doneBarButton=ObjCClass('UIBarButtonItem').alloc().initWithBarButtonSystemItem_target_action_(0,self.ed_view,sel('endEditing:')) 
    keyboardToolbar.items = [flexBarButton, doneBarButton]
    
    
    #uitoolbar.alloc().init()
    #uitoolbar.sizeToFit()
    #pdbg(uitoolbar)
    #self.ed_view.inputAccessoryView= keyboardToolbar
    self.ed_view.setInputAccessoryView_(keyboardToolbar)
    
    
    
    
    
    # dark
    self.ed_view.setKeyboardAppearance_(sel('_dark'))
    self.ed_view.autorelease()
    
    ObjCInstance(self).addSubview_(self.ed_view)
    
    

  


v=MainView()
#v.txt.font=('Ubuntu Mono',14)
v.ed_view.text='''\
1oil0
あなたは文藝春秋九月号に私への悪口を書いて居られる。「前略。――なるほど、道化の華の方が作者の生活や文学観を一杯に盛っているが、私見によれば、作者目下の生活に厭いやな雲ありて、才能の素直に発せざる憾うらみあった。」
　おたがいに下手な嘘はつかないことにしよう。私はあなたの文章を本屋の店頭で読み、たいへん不愉快であった。これでみると、まるであなたひとりで芥川賞をきめたように思われます。これは、あなたの文章ではない。きっと誰かに書かされた文章にちがいない。しかもあなたはそれをあらわに見せつけようと努力さえしている。「道化の華」は、三年前、私、二十四歳の夏に書いたものである。「海」という題であった。友人の今官一、伊馬鵜平うへいに読んでもらったが、それは、現在のものにくらべて、たいへん素朴な形式で、作中の「僕」という男の独白なぞは全くなかったのである。物語だけをきちんとまとめあげたものであった。そのとしの秋、ジッドのドストエフスキイ論を御近所の赤松月船氏より借りて読んで考えさせられ、私のその原始的な端正でさえあった「海」という作品をずたずたに切りきざんで、「僕」という男の顔を作中の随所に出没させ、日本にまだない小説だと友人間に威張ってまわった。友人の中村地平、久保隆一郎、それから御近所の井伏さんにも読んでもらって、評判がよい。元気を得て、さらに手を入れ、消し去り書き加え、五回ほど清書し直して、それから大事に押入れの紙袋の中にしまって置いた。今年の正月ごろ友人の檀一雄がそれを読み、これは、君、傑作だ、どこかの雑誌社へ持ち込め、僕は川端康成氏のところへたのみに行ってみる。川端氏なら、きっとこの作品が判るにちがいない、と言った。
　そのうちに私は小説に行きづまり、謂いわば野ざらしを心に、旅に出た。それが小さい騒ぎになった。
　どんなに兄貴からののしられてもいいから、五百円だけ借りたい。そうしてもういちど、やってみよう、私は東京へかえった。友人たちの骨折りのおかげで私は兄貴から、これから二三年のあいだ、月々、五十円のお金をもらえることになった。私はさっそく貸家を捜しまわっているうちに、盲腸炎を起し阿佐ヶ谷の篠原病院に収容された。膿うみが腹膜にこぼれていて、少し手おくれであった。入院は今年の四月四日のことである。中谷孝雄が見舞いに来た。日本浪曼派へはいろう、そのお土産として「道化の華」を発表しよう。そんな話をした。「道化の華」は檀一雄の手許てもとにあった。檀一雄はなおも川端氏のところへ持って行ったらいいのだがなぞと主張していた。私は切開した腹部のいたみで、一寸もうごけなかった。そのうちに私は肺をわるくした。意識不明の日がつづいた。医者は責任を持てないと、言っていたと、あとで女房が教えて呉くれた。まる一月その外科の病院に寝たきりで、頭をもたげることさえようようであった。私は五月に世田谷区経堂の内科の病院に移された。ここに二カ月いた。七月一日、病院の組織がかわり職員も全部交代するとかで、患者もみんな追い出されるような始末であった。私は兄貴と、それから兄貴の知人である北芳四郎という洋服屋と二人で相談してきめて呉れた、千葉県船橋の土地へ移された。終日籐椅子とういすに寝そべり、朝夕軽い散歩をする。一週間に一度ずつ東京から医者が来る。その生活が二カ月ほどつづいて、八月の末、文藝春秋を本屋の店頭で読んだところが、あなたの文章があった。「作者目下の生活に厭な雲ありて、云々。」事実、私は憤怒に燃えた。幾夜も寝苦しい思いをした。
　小鳥を飼い、舞踏を見るのがそんなに立派な生活なのか。刺す。そうも思った。大悪党だと思った。そのうちに、ふとあなたの私に対するネルリのような、ひねこびた熱い強烈な愛情をずっと奥底に感じた。ちがう。ちがうと首をふったが、その、冷く装うてはいるが、ドストエフスキイふうのはげしく錯乱したあなたの愛情が私のからだをかっかっとほてらせた。そうして、それはあなたにはなんにも気づかぬことだ。
　私はいま、あなたと智慧ちえくらべをしようとしているのではありません。私は、あなたのあの文章の中に「世間」を感じ、「金銭関係」のせつなさを嗅かいだ。私はそれを二三のひたむきな読者に知らせたいだけなのです。それは知らせなければならないことです。私たちは、もうそろそろ、にんじゅうの徳の美しさは疑いはじめているのだ。
　菊池寛氏が、「まあ、それでもよかった。無難でよかった。」とにこにこ笑いながらハンケチで額の汗を拭っている光景を思うと、私は他意なく微笑ほほえむ。ほんとによかったと思われる。芥川龍之介を少し可哀そうに思ったが、なに、これも「世間」だ。石川氏は立派な生活人だ。その点で彼は深く真正面に努めている。
　ただ私は残念なのだ。川端康成の、さりげなさそうに装って、装い切れなかった嘘が、残念でならないのだ。こんな筈ではなかった。たしかに、こんな筈ではなかったのだ。あなたは、作家というものは「間抜け」の中で生きているものだということを、もっとはっきり意識してかからなければいけない。
'''
v.present()

