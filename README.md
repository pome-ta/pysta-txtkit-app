# pysta-txtkit-app


Practice textkit-app with Pythonista

[Pythonista](http://omz-software.com/pythonista/) の`objc_util` を使い、Objective-C の理解と、 `TextKit` の理解ができるようにする。


## Basic Data
- iPhone
	- iPhone 11
	- iOS 13.2

- Pythonista
	- ver_3.2


## Gole🏁
### Text(Coding) Editor をつくる
  - Syntax Highlight
  - Line Numbers
  - Auto Complete

特別な縛りはないけども、全部iPhone（or iPad）のみで検証予定（git も含めて）







--- 以下日記 ---

# 2019/11/05

## todo

- font 設定
- lineNumbers したい
	- どこに設置？
		- ui.view に？
		- text.view に？
			- サブクラス化が必要かもね
	- 文字選択しても、選択されないように
	- メインのtext.view のスクロールと連動
	- 色々なナレッジを検索
		- storyboard 使わない時の呼び出し
			- 書換え方を調べないと
- 実はstash って、swipe 文字移動できるのね、、、
	- どこでできてるのか調べないと、、、




# 2019/11/04

## 実験時メモ（気付き）

### `v.txt.hoge()`
- `text='fuga'` -> 🙆‍♂️
- `font=()` -> 🙅‍♂️

### class
- `self` つけると、外から呼び出せる

### Dark Keyboard
- `self.txt.setKeyboardAppearance_(sel('_dark'))`

### `ObjCInstance(self)`
- 変数で呼び出すと、2回目に実行すると落ちる
	- 変数に`.autorelease()` をつけても🙅‍♂️
	- 変数化しないようにしてる




# 2019/11/03

## 進捗

時系列がバラバラだけども、状況を列記

- `ObjCClass('UITextView')`
	- main のview サイズで描画ができた
		- 創造神のomz氏のgist より参照 ->[CodeEditor Demo.py](https://gist.github.com/omz/6762c1e55e8c3a596637)
			- `flex_width, flex_height = (1<<1), (1<<4)`
			- `editor_view.setAutoresizingMask_(flex_width|flex_height)`
	- 仮テキスト流す
		- 青空文庫 [川端康成へ](https://www.aozora.gr.jp/cards/000035/files/1607_13766.html) （深い意味はない）
		- 編集時に、keyboard にテキストが隠れる



## Pythonista クラスか、既存クラスか
- Syntax Highlight のことを考えると
	- 実装が楽なのはPythonista
		- 汎用性がない
		- 内部を知るので時間がかかる
	- objc クラスから
		- 実装が大変そう
		- 基本的な正解より、情報を集めた内容による
		- objc-util やと大変(面倒)やない？
	- ui モジュールから
		- 画面調整とか楽そう
		- どんなtextview か、中身が謎

## 進め方想定(ランダム)

- objc からtextview を、呼び出す
	- フル画面で描画
- キャレット位置取得
	- 今後移動できるように
		- Pythonista のui.textview はガバガバ
- objc の言語理解
	- github のFramework やサイト上のtips をコンバート
- UIKit の把握
	- apple のwwdc の動画観まくる？
- undo redo の実装
- 適当な言葉に、 highlight さす
- LineNumber つける

## モヤり

- 多分GitHub の使い方ちゃんと理解してない🤗
- Markdown の書き方が酷い😂
	- 多分使い方あってない（言語としての活用フォームじゃない）

- （この）テキスト編集を[iVim](https://github.com/terrychou/iVim) （[App Store](https://apps.apple.com/jp/app/ivim/id1266544660)）でしたひ。。。
	- iOS13 になってから、フォルダapp の扱い方が変わったみたいで連携面倒、、、、

- Play js も気になるお年頃なので、この辺で😜


# 2019/11/02

## 1st commit

## ui.View
- Pythonista モジュールの`ui.View` を使用
	- 背景を赤
	- サブクラスで、インスタンス化
		- `ObjCInstance( )`


## debug


ui の状況を知るために、以下で`(p)print` 吐き出し

- Python の関数
	- `dir( )`
	- `vars( )`
- objc より
	- `._ivarDescription( )`
	- `._shortMethodDescription( )`
	- `._methodDescription( )`
	- `.recursiveDescription( )`
	- `._autolayoutTrace( )`

4000行と5000行と、状況により結果が違う🤔再現性が難しくdiff も面倒なので、5000で着地

- `chk=ObjCInstance(self)`
- `chk=ObjCInstance(self._objc_ptr)`

たぶん（たぶん）結果は、同じ🤗


## git とGitHub の連携

どうも要領が掴めない、、、まぁ自分だけやからええやろ😂



でも、日毎にフォルダ作ると完全に意味ないよね？🤔branch 切るの面倒😂😂😂
