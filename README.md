# サインスマート 1.8″ TFT カラー LCD用のグラフィックライブラリ

Pyshon言語で使用できるサインスマート1.8″TFT カラーLCD用のグラフィックライブラリを作成しました。サインスマート1.8″TFT カラーLCDは、Raspberry Pi 3とSPIで接続します。作成するグラフィックライブラリは、任意の色での描画を可能とし、描画できる図形を次に示します。

* 直線
* 四角形および四角形の塗りつぶし
* 円形および円形の塗りつぶし

Raspberry PI 3とサインスマート 1.8インチ LCDの接続は、SPIを使用します。Raspberry PI 3とサインスマート 1.8インチ LCD間の信号線の接続およびSPIの設定方法については、「[Raspberry PI 3でサインスマート 1.8″ LCDの表示](http://tomosoft.jp/design/?p=7944)」を参照してください。

## グラフィックライブラリ

サインスマート 1.8″ TFT カラー LCD用のグラフィックライブラリは、サインスマートLCDライブラリ「ST7735」とグラフィック基本ライブラリ「」の2つのクラスから構成されます。このグラフィックライブラリを使用することで、インスマート 1.8インチ LCD上に任意の色で直線、四角形、円が描画できます。また、四角形、円については任意の色で塗りつぶしが可能です。また、各メソッドは、パラメータで指定された位置について、エラーチェックを行い、サインスマート 1.8″ TFT カラー LCDの画面サイズの外側を指定している場合は、エラーメッセージを表示します。

```
 【カラーコード】
 　RGBそれぞれ８ビットの値になります。
 　例：
    　BLACK   ： 0x000000
    　BLUE    ： 0x0000FF
    　RED     ： 0xFF0000
    　GREEN   ： 0x008000
    　CYAN    ： 0x00FFFF
    　MAGENTA ： 0xFF00FF
    　YELLOW  ： 0xFFFF00
    　WHITE   ： 0xFFFFFF
```

### サインスマートLCDクラス「ST7735」
サインスマートLCDクラス「ST7735」は、サインスマート 1.8″ LCDに実装されているコントローラ「ST7735R」に対して、制御レジスタやデータレジスタおよび描画用メモリに書き込むクラスです。
<dl>
<dt>__init__(width, height)<br>
　width, height：サインスマート 1.8″ LCDの表示画面のドット幅と高さ
</dt>
<dd>インスタンス化するときに、サインスマート 1.8″ TFT カラー LCDの画面サイズをパラメータとして受け取ります。インスタンス化されたときに、次のコードでLCDコントローラIC「ST7735R」のリセット、py-spidevのインスタンス化およびオープン、LCDコントローラIC「ST7735R」のレジスタ設定などを行います。</dd>

<dt>write_cmd(cmd)<br>
　cmd：コマンドレジスタに書き込むデータ
<dd>write_cmdメソッドは、コマンドレジスタにパラメータで与えられた値をxfer2メソッドで書き込みます。</dd>

<dt>write_data(data)<br>
　data：データレジスタに書き込むデータ</dt>
<dd>write_dataメソッドは、データレジスタにパラメータで与えられた値をxfer2メソッドで書き込みます。</dd>

<dt>write(cmd)<br>
　cmd：リスト形式、[0]コマンドレジスタに書き込むデータ、[1～]データレジスタに書き込むデータ</dt>
<dd>writeメソッドは、コマンドレジスタにパラメータで与えられた最初の値をxfer2メソッドで書き込みます。次に、データレジスタにパラメータで与えられた残りの値をxfer2メソッドで書き込みます。</dd>

<dt>dot(x, y, color)<br>
　x, y：x, yピクセル位置<br>
　color：カラーコード</dt>
<dd>dotメソッドは、指定されたｘ、ｙ位置に対応する位置にパラメータで与えられたカラーコードでドットを表示します。</dd>

<dt>sendbuf()</dt>
<dd>sendbufメソッドは、作成した描画データをxfer2メソッドで書き込みます。</dd>
</dl>

### グラフィック基本クラス「Graphic」
グラフィック基本クラス「Graphic」は、グラフィックの基本図形（直線、四角形、円形）を描画するクラスです。
<dl>
<dt>__init__(pst7735)<br>
　pst7735：サインスマートLCDクラス「ST7735」のインスタンス</dt>
<dd>インスタンス化するときに、サインスマートLCDクラス「ST7735」のインスタンスを受け取ります。</dd>

<dt>drawline(x0p, y0p, x1p, y1p, color)<br>
　x0p, y0p：開始x, yピクセル位置<br>
　x1p, y1p：終了x, yピクセル位置<br>
　color：カラーコード</dt>
<dd>drawlineメソッドは、直線を描画します。</dd>

<dt>drawrect(x, y, w, h, color)<br>
　x, y：左上のx, yピクセル位置<br>
　w, h：描画する幅と高さ<br>
　color：カラーコード</dt>
<dd>drawrectメソッドは、四角形を描画します。</dd>

<dt>fillrect(x, y, w, h, color)<br>
　x, y：左上のx, yピクセル位置<br>
　w, h：塗りつぶす幅と高さ<br>
　color：カラーコード</dt>
<dd>fillrectメソッドは、指定された位置から、指定された幅と高さの領域を塗りつぶします。</dd>

<dt>fillscreen(color)<br>
　color：カラーコード</dt>
<dd>fillscreenメソッドは、サインスマート 1.8″ TFT カラー LCDの画面を塗りつぶします。</dd>

<dt>drawcircle(x0, y0, r, color)<br>
　x0, y0：円中心のx, yピクセル位置<br>
　r：半径ピクセル値<br>
　color：カラーコード</dt>
<dd>drawcircleメソッドは、円形を描画します。</dd>

<dt>drawcirclehelper(x0, y0, r, cornername, color)<br>
　x0, y0：丸み中心のx, yピクセル位置<br>
　r：半径ピクセル値<br>
　cornername：描画する角<br>
　　1: top left<br>
　　2: top right<br>
　　4: bottom right<br>
　　8: bottom left<br>
　color：カラーコード</dt>
<dd>drawcirclehelperメソッドは、角の丸みを描画します。</dd>

<dt>fillcirclehelper(x0, y0, r, cornername, delta, color)<br>
　x0, y0：丸み中心のx, yピクセル位置<br>
　r：半径ピクセル値<br>
　cornername：描画する角<br>
　　1: left half<br>
　　2: right half<br>
　delta：それぞれの1/4間を長さの拡張<br>
　color：カラーコード</dt>
<dd>fillcirclehelperメソッドは、角の丸みを塗りつぶします。</dd>

<dt>fillcircle(x0, y0, r, color)<br>
　x0, y0：円中心のx, yピクセル位置 <br>
　r：半径ピクセル値 <br>
　color：カラーコード</dt>
<dd>fillcircleメソッドは、円形を塗りつぶします。</dd>

</dl>
## サンプルプログラムの実行

Raspberry Piで次のコマンドでサンプルプログラムを実行します。

```
python Graphic.py
```

次のようにサインスマート 1.8″ TFT カラー LCD上に、一本の直線、二個の円形（一個は塗りつぶし）、二個の四角形（一個は塗りつぶし）が描画されます。
<div align="center" ><img src="https://tomosoft.jp/github/SainSmartLcd/lcd02.jpg"></div>
