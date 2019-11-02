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
