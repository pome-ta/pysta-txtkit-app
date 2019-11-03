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

> 2019/11/03

# Pythonista クラスか、既存クラスか
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

# モヤり

- 多分GitHub の使い方ちゃんと理解してない🤗
- Markdown の書き方が酷い😂
	- 多分使い方あってない（言語としての活用フォームじゃない）


> 2019/11/02

# 1st commit

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
