#サインスマート 1.8″ TFT カラー LCD用のグラフィックライブラリ

Pyshon言語で使用できるサインスマート1.8″TFT カラーLCD用のグラフィックライブラリを作成しました。サインスマート1.8″TFT カラーLCDは、Raspberry Pi 3とSPIで接続します。作成するグラフィックライブラリは、任意の色での描画を可能とし、描画できる図形を次に示します。

* 直線
* 四角形および四角形の塗りつぶし
* 円形および円形の塗りつぶし

Raspberry PI 3とサインスマート 1.8インチ LCDの接続は、SPIを使用します。Raspberry PI 3とサインスマート 1.8インチ LCD間の信号線の接続およびSPIの設定方法については、「[Raspberry PI 3でサインスマート 1.8″ LCDの表示](http://tomosoft.jp/design/?p=7944)」を参照してください。

##グラフィックライブラリ

サインスマート 1.8″ TFT カラー LCD用のグラフィックライブラリは、サインスマートLCDライブラリ「ST7735」とグラフィック基本ライブラリ「Graphic」の2つのクラスから構成されます。このグラフィックライブラリを使用することで、インスマート 1.8インチ LCD上に任意の色で直線、四角形、円が描画できます。また、四角形、円については任意の色で塗りつぶしが可能です。

###サインスマートLCDクラス「ST7735」

###グラフィック基本クラス「Graphic」

##サンプルプログラムの実行

Raspberry Piで次のコマンドでサンプルプログラムを実行します。次のようにサインスマート 1.8″ TFT カラー LCD上に、一本の直線、二個の円形（一個は塗りつぶし）、二個の四角形（一個は塗りつぶし）が描画されます。
<div align="center" ><img src="https://github.com/tomosoft-jp/SainSmartLcd/master/lcd02.jpg"></div>
