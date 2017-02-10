#サインスマート 1.8″ TFT カラー LCD用のグラフィックライブラリ

Pyshon言語で使用できるサインスマート1.8″TFT カラーLCD用のグラフィックライブラリを作成しました。サインスマート1.8″TFT カラーLCDは、Raspberry Pi 3とSPIで接続します。作成するグラフィックライブラリは、任意の色での描画を可能とし、描画できる図形を次に示します。

* 直線
* 四角形および四角形の塗りつぶし
* 円形および円形の塗りつぶし

Raspberry PI 3とサインスマート 1.8インチ LCDの接続は、SPIを使用します。Raspberry PI 3とサインスマート 1.8インチ LCD間の信号線の接続およびSPIの設定方法については、「[Raspberry PI 3でサインスマート 1.8″ LCDの表示](http://tomosoft.jp/design/?p=7944)」を参照してください。

##グラフィックライブラリ

サインスマート 1.8″ TFT カラー LCD用のグラフィックライブラリは、サインスマートLCDライブラリ「ST7735」とグラフィック基本ライブラリ「」の2つのクラスから構成されます。このグラフィックライブラリを使用することで、インスマート 1.8インチ LCD上に任意の色で直線、四角形、円が描画できます。また、四角形、円については任意の色で塗りつぶしが可能です。

###サインスマートLCDクラス「ST7735」
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

###グラフィック基本クラス「Graphic」
<dl>
<dt>__init__(pst7735)<br>
　pst7735：サインスマートLCDクラス「ST7735」のインスタンス</dt>
<dd>インスタンス化するときに、サインスマートLCDクラス「ST7735」のインスタンスをパラメータとして受け取ります。この情報を使って、サインスマート 1.8″ TFT カラー LCDの画面サイズを取得し、dotメソッドを呼び出します。また、各メソッドは、パラメータで指定された位置について、エラーチェックを行い、サインスマート 1.8″ TFT カラー LCDの画面サイズの外側を指定している場合は、エラーメッセージを表示します。</dd>

<dt>drawline(x0p, y0p, x1p, y1p, color)<br>
　x0p, y0p：開始x, yピクセル位置<br>
　x1p, y1p：終了x, yピクセル位置<br>
　color：カラーコード</dt>
<dd>drawlineメソッドは、与えられた始点と終点の間に連続した点を置き、近似的な直線を引くためのアルゴリズム「ブレゼンハムのアルゴリズム」を使用します。</dd>

<dt>drawrect(x, y, w, h, color)<br>
　x, y：左上のx, yピクセル位置<br>
　w, h：描画する幅と高さ<br>
　color：カラーコード</dt>
<dd>drawrectメソッドは、drawlineメソッドを使用して描画します。</dd>

<dt>fillrect(x, y, w, h, color)<br>
　x, y：左上のx, yピクセル位置<br>
　w, h：塗りつぶす幅と高さ<br>
　color：カラーコード</dt>
<dd>fillrectメソッドは、dotメソッドを使用して、指定された位置から、指定された幅と高さの領域を指定された色で塗りつぶします。</dd>

<dt>fillscreen(color)<br>
　color：カラーコード</dt>
<dd>fillscreenメソッドは、サインスマート 1.8″ TFT カラー LCDの画面サイズをパラメータに、fillrectメソッドを呼び出します。</dd>

<dt>drawcircle(x0, y0, r, color)<br>
　x0, y0：円中心のx, yピクセル位置<br>
　r：半径ピクセル値<br>
　color：カラーコード</dt>
<dd>drawcircleメソッドは、処理時間を節約するために、円を描画する関数は、x'=-y, y'=xという微分公式をうまく利用し、円形の対称性を利用して、円周上の座標を八分の一だけを計算します。</dd>

<dt>drawcirclehelper(x0, y0, r, cornername, color)<br>
　x0, y0：丸み中心のx, yピクセル位置<br>
　r：半径ピクセル値<br>
　cornername<br>
　color：カラーコード</dt>
<dd>drawcirclehelperメソッドは、角の丸みを描画します。</dd>

<dt>fillcirclehelper(x0, y0, r, cornername, delta, color)<br>
　x0, y0：丸み中心のx, yピクセル位置<br>
　r：半径ピクセル値<br>
　cornername<br>
　delta<br>
　color：カラーコード</dt>
<dd>fillcirclehelperメソッドは、角の丸みを塗りつぶします。</dd>

<dt>fillcircle(x0, y0, r, color)<br>
　x0, y0：円中心のx, yピクセル位置 <br>
　r：半径ピクセル値 <br>
　color：カラーコード</dt>
<dd>fillcircleメソッドは、drawlineメソッドで直線を縦に引き、fillcirclehelperメソッドで半円を塗りつぶします。</dd>

</dl>
##サンプルプログラムの実行

Raspberry Piで次のコマンドでサンプルプログラムを実行します。

```
python Graphic.py
```

次のようにサインスマート 1.8″ TFT カラー LCD上に、一本の直線、二個の円形（一個は塗りつぶし）、二個の四角形（一個は塗りつぶし）が描画されます。
<div align="center" ><img src="https://github.com/tomosoft-jp/SainSmartLcd/blob/master/images/lcd02.jpg"></div>
