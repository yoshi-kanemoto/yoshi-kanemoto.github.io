<HTML>
<HEAD>
<TITLE>TAKE Soft/Graphic Access Counter</TITLE>
</HEAD>
<BODY BGCOLOR=#CCFFCC>

<P ALIGN=RIGHT>
<IMG SRC="../../image/w7.gif" BORDER=0 ALT="7"><IMG SRC="../../image/w3.gif" BORDER=0 ALT="3"><IMG SRC="../../image/w5.gif" BORDER=0 ALT="5">人目
</P>

<CENTER>
<TABLE WIDTH=500 BORDER=0>
<TR ALIGN=CENTER VALIGN=MIDDLE>

<TD WIDTH=100><IMG SRC="../../image/cntr_ico.gif" ALT=" "></TD>

<TD WIDTH=300>
<H2>グラフィックタイプの<BR>
アクセスカウンタ</H2>
</TD>

<TD WIDTH=100><IMG SRC="../../image/cntr_ico.gif" ALT=" "></TD>

</TABLE>
</CENTER>

<HR>
<!------------------------------------------------------>
<H4>目次</H4>
<UL>
<LI><A HREF=#gacf>
    最初のページ用のグラフィックタイプのアクセスカウンタ”gacf”</A>
<LI><A HREF=#gacs>
    ２番目以降のページ用のグラフィックタイプのアクセスカウンタ”gacs”</A>
<LI><A HREF=#gcounter>
    桁毎に表示するグラフィックタイプのアクセスカウンタ”gcounter”</A>
</UL>

<H3><A NAME="gacf">○最初のページ用のグラフィックタイプのアクセスカウンタ”gacf (ver.1.0)”</A></H3>
　ホームページ(最初のWebページ)で使用できるグラフィックタイプのアクセス
カウンタ”gacf(graphic access counter for first Web page)”をここで
公開しております。<BR>
　ここから、ダウンロードして貴方のホームページに設置可能です。ここから
直接ダウンロードされた場合には、”無料”です。著作権は一応留保しますが、
貴方のサイトで自由に変更して頂いてかまいません。<BR>
<BR>
　このカウンタの特徴は、NECのC&C meshのようにSSI(Server Side Include)
は、使えないが、CGI(Common Gateway Interface)は、使えるプロバイダーの
ホームページで、使うことができる点です。<BR>
　２ページ目以降に取り付けるカウンタについては次節”gacs"を御覧下さい。<BR>

<H4>”gacf”の設置方法</H4>

    <OL>
    <LI>”index.html”のWebページの設定<BR>
        貴方の最初のWebページ(ファイル名を”index.html”とします)の
        カウンタの数字を入れたい部分に<BR><BR>

        &lt;!-- ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ --&gt;<BR><BR>

        という行を半角で挿入して下さい(説明文にこの文字列を半角で
        書いたらそこにもカウンタの数字が 挿入されてしまいました)。
        この行には、他の文字等は入れないで
        下さい。また、このWebページの他の部分には、
         ”ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ”(の半角の文字列)
        という文字列は、使用しないで下さい。<BR>
        　例えばページの最初に表示する場合の例を以下に示します。<BR>
        <BLOCKQUOTE>
           &lt;HTML&gt;<BR>
           &lt;HEAD&gt;<BR>
           &lt;TITLE&gt;Any Title&lt;/TITLE&gt;<BR>
           &lt;/HEAD&gt;<BR>
           &lt;BODY&gt;<BR>
           &lt;P ALIGN=RIGHT&gt;<BR>
           あなたは、<BR>
           &lt;!-- ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ --&gt;(ほんとは半角)<BR>
           人目です。<BR>
           &lt;/P&gt;<BR>

        </BLOCKQUOTE>
        ここで、”あなたは、”や”人目です。”の部分は、適宜変更してい
        ただいてかまいませんし、なくても問題ありません。その上の<BR><BR>

           &lt;P ALIGN=RIGHT&gt;<BR><BR>

        は、カウンタの表示を右側にすることを指示しています。しかし、
        ”ALIGN=RIGHT”の指定は、Netscape Navigator 2.0等でしか有効では
        ありません。TABLEタグを使って右寄せする方法はInternet Explorer 
        2.0等でも有効です。TABLEタグを使って右寄せする方法については、
        ”竹ソフト”のホームページの最初の部分のソースを御参照下さい。
       それでも、TABLEタグに対応していないブラウザでは、右寄せできませ
       ん。<BR><BR>

       　また、このファイルの一番最後の方にIMGタグから
       ”gacf.cgi”を呼び出す行を必ず挿入して下さい。以下に例を示します。
       <BR><BR>

       　　&lt;IMG SRC="gacf.cgi" BORDER=0 ALT=""&gt;<BR><BR>

       　　&lt;/BODY&gt;<BR>
       　　&lt;/HTML&gt;<BR><BR>


    <LI>”index_.html”の準備<BR>
        次に、”index.html”をコピーして、”index_.html”という名前の
        ファイルを作って下さい。”_”は、アンダースコア(アンダーバー)
        です。<BR><BR>

    <LI>”gacf”のCGIスクリプト<BR>
        次のファイルをここからダウンロードして下さい。Netscape Navigator
        の場合のダウンロードの仕方は、リンクをクリックして内容を表示
        させてから、メニューの”ファイル”から”名前を付けて保存”を選
        んで下さい。他のブラウザの場合は、マニュアルを御参照下さい。貴方
        のファイル名を指定するダイアログがでますから、同じ名前で保存し
        て下さい。このページへ戻るには、ブラウザの”戻るボタン”等を
        御使い下さい。<BR><BR>

        　　<A HREF="gacf.txt">gacf.txt</A><BR><BR>

        ダウンロードしたらファイル名を”gacf.cgi”と変更して下さい。
        　このカウンタをmesh以外で使用される場合には、一行目の<BR><BR>

         　　#!/usr/mesh/bin/perl<BR><BR>

        をそのサイトのperlのあるところに変更して下さい。<BR>
        　また、このカウンタに必要なファイル名をここで説明している
        ものと変える場合や、CGIではフルパスのファイル名を指定する必要
        がある場合には、このファイルの中の”(1)”の部分の５個のファイル
        (ディレクトリ)名を適宜変更して下さい。<BR><BR>

        [IE 2.0をお使いの方への注意事項]<BR>
        Windows 95上で作動するInternet Explorer 2.0を用いて、gacf.txtを
        ダウンロードした場合、ファイルの先頭に２行の空白行が勝手に挿入
        される場合があります。このような場合は、メモ帳や秀丸のような
        エディタで、先頭の空白行を必ず削除して下さい。先頭行で上に
        述べたperlのファイルを指定していないとperlのcgiは、うまく動き
        ません。<BR><BR>

        [Netscape Historyをお使いの方への注意事項]<BR>
        gacfのユーザーの方から「Netscape Historyというソフトを用いて
        キャッシュのデータからgacf.txtをsaveしたら、gacf.txtの一部が、
        ”__unavailable__.gif”に変わってしまった」という情報をいただき
        ました。このような変更が生じるとうまくカウンタが動かないので
        gacf.txtは、ここのWebページから直接ダウンロードしていただくよう
        お願いします。<BR><BR>


    <LI>”count.txt”ファイル<BR>
        カウンタの数値を入れるファイル<BR><BR>

        　　<A HREF="count.txt">count.txt</A><BR><BR>

        をここからダウンロードするか、エディターで半角の数字”0”のみ
        が入ったファイルを用意して下さい(リターンは入れないで下さい)。
        カウンタを途中の番号から始めたい場合は、始めたい番号より１小さ
        い数値を半角の数字で書いたファイルをエディターで作って下さい。
        ファイル名は、”count.txt”にして下さい。<BR><BR>

        [IE 2.0の場合の注意事項]<BR>
        Windows 95上で作動するInternet Explorer 2.0を用いて、count.txtを
        ダウンロードした場合、ファイルの先頭に２行の空白行が勝手に挿入
        される場合があります。このような場合は、メモ帳や秀丸のような
        エディタで、先頭の空白行を必ず削除して下さい。そして、count.txtは、
        ローカルファイル上でもftpで送ったWebサイト上でも最初は、必ず1バイ
        トです。<BR><BR>

    <LI>”trans.gif”ファイル<BR>
        ダミーとして送る小さい透明の四角のgifファイルです。このgifファ
        イルはここからダウンロードするか御自分で御用意下さい。ダウンロ
        ードする際に、この下の”tarns.gif”をクリックしてもこのgifは、
        透明なので、なにもないバックだけが表示されますが、かまわず、
        メニューの”ファイル”から”名前を付けて保存”を選ぶ等の
        操作で、ダウンロードして下さい。<BR><BR>

        　　<A HREF="trans.gif">trans.gif</A><BR><BR>

    <LI>数字のgifファイルの転送<BR>
        以下に示す数字を表示するためのgifファイルをどれか１組１０個
        ダウンロードして下さい。Netscape Navigatorの場合、数字の画像
        の上にマウスポインタを置き、右クリックして下さい(マックの場合
        数秒間押し続ける)。出てきたメニューから、”画像を名前を付けて
        保存”を選択して下さい。ファイル名は、”0.gif”、”1.gif”、
        ”2.gif”、...、”9.gif”のようにして下さい。
        自分で、数字のgifファイルを作る方や、他の数字のgifファイルを
        使う方は、ここからダウンロードする必要は、ありません。<BR><BR>

        ○白地に黒字(15 x 20 pixel)<BR><BR>
        <IMG SRC="../../image/0.gif" ALT="0">　
        <IMG SRC="../../image/1.gif" ALT="1">　
        <IMG SRC="../../image/2.gif" ALT="2">　
        <IMG SRC="../../image/3.gif" ALT="3">　
        <IMG SRC="../../image/4.gif" ALT="4">　
        <IMG SRC="../../image/5.gif" ALT="5">　
        <IMG SRC="../../image/6.gif" ALT="6">　
        <IMG SRC="../../image/7.gif" ALT="7">　
        <IMG SRC="../../image/8.gif" ALT="8">　
        <IMG SRC="../../image/9.gif" ALT="9"><BR><BR>

        ○白地に黒字(20 x 30 pixel)<BR><BR>
        <IMG SRC="../../image/b0.gif" ALT="0">　
        <IMG SRC="../../image/b1.gif" ALT="1">　
        <IMG SRC="../../image/b2.gif" ALT="2">　
        <IMG SRC="../../image/b3.gif" ALT="3">　
        <IMG SRC="../../image/b4.gif" ALT="4">　
        <IMG SRC="../../image/b5.gif" ALT="5">　
        <IMG SRC="../../image/b6.gif" ALT="6">　
        <IMG SRC="../../image/b7.gif" ALT="7">　
        <IMG SRC="../../image/b8.gif" ALT="8">　
        <IMG SRC="../../image/b9.gif" ALT="9"><BR><BR>

        ○黒字に白地(20 x 30 pixel)<BR><BR>
        <IMG SRC="../../image/w0.gif" ALT="0">　
        <IMG SRC="../../image/w1.gif" ALT="1">　
        <IMG SRC="../../image/w2.gif" ALT="2">　
        <IMG SRC="../../image/w3.gif" ALT="3">　
        <IMG SRC="../../image/w4.gif" ALT="4">　
        <IMG SRC="../../image/w5.gif" ALT="5">　
        <IMG SRC="../../image/w6.gif" ALT="6">　
        <IMG SRC="../../image/w7.gif" ALT="7">　
        <IMG SRC="../../image/w8.gif" ALT="8">　
        <IMG SRC="../../image/w9.gif" ALT="9"><BR><BR>

    <LI>ファイルのアップロードとアクセス権の変更<BR>
        ftpで次のファイルをホームページのディレクトリへ、テキストモード
        で転送(put)して下さい。<BR><BR>
        <UL>
        <LI>index.html
        <LI>index_.html
        <LI>count.txt
        <LI>gacf.cgi<BR><BR>
        </UL>
        次にホームページのディレクトリの下にimageというディレクトリを
        つくって(mkdir image)、下に示すgifファイルをバイナリーモードで
        転送して下さい。
        こうするのは、gifファイルは、一ヶ所に集めておいて各Webページ
        から共通にアクセスする方がわかりやすいからです。しかし、このよ
        うにしなくてもかまいません。その場合には、gacf.cgiの$gif_dir
        および$dummy_gif_fileを適宜変更して下さい。<BR><BR>
        <UL>
        <LI>trans.gif
        <LI>n.gif (nは、0 〜 9)<BR><BR>
        </UL>

        そして、”index.html”と”count.txt”のファイルのアクセス許可を
        ”666”に変更して下さい。”gacf.cgi”のファイルのアクセス許可を
        ”755”に変更して下さい。そのほかのファイルは、一般の人から読み
        出し可能であればよいので、通常変更不要です。<BR>
        　meshで、ファイルのアクセス許可を変更するには、ftpで目的のサイトに
        ログインして次のようにします。<BR><BR>
        　　ftp>cd public_html<BR>
        　　ftp>dir<BR>
        　　ftp>quote site chmod 666 index.html<BR>
        　　ftp>quote site chmod 666 count.txt<BR>
        　　ftp>quote site chmod 755 gacf.cgi<BR>
        　　ftp>dir<BR><BR>
        ここで、cdはディレクトリを移るコマンド、dirは、そのディレクトリのファ
        イル一覧を得るコマンドです(”ls -l”でもよい）。quoteのところでファイ
        ルのアクセスを変更しています。telnetでファイルのアクセス権を変更できる
        サイトでは、chmod以降の部分のみで変更できます。最後のdirは、アクセス権
        が変更されたかチェックするためのものです。<BR>
        　ftpのコマンドについて不案内の方は、技術資料のページの”計算機コマンド
        のRosetta Stone”を御覧下さい。表２に他のOSのコマンドとの対比を示してい         ます。<BR><BR>

        　CuteFTPをお使いの方は、次のようにしアクセス権を変更して下さい。<BR>
        <OL>
        <LI>アクセス権を変更するリモートのファイルをクリックして選択する
        <LI>メニューから Commands/Custom Commands/Change Files Access mask
            を順に選択する。
        <LI>出てきたダイアログに変更すべきアクセス権の３桁の数字(”755”等)
            を入力し”OK”ボタンをクリックする。<BR><BR>
        </OL>
        　Fetchをお使いの方は、ファイルを指定した後、次のようにして
        アクセス権を変更して下さい。<BR><BR>
        <PRE>
        アクセス許可を”755”にするのは Remote/Set Permissions..で
　　　　    　　　       Read     Write    Search/Execute
　　　　    Owner         x        x            x
　　　　    Group         x                     x
　　　　    Everyone      x                     x

        アクセス許可を”666”にするのは Remote/Set Permissions..で
　　　　    　　　       Read     Write    Search/Execute
　　　　    Owner         x         x            
　　　    　Group         x         x            
　　　　    Everyone      x         x            
        </PRE>


    <LI>ファイルのバックアップ等<BR>
        ftpでWebページのディレクトリへ送った１５個のファイルは、
        ”gacf”の不具合やサーバーの不調等の原因で破壊されるおそれが
        ありますので必ずローカルなディスクにバックアップを保存する
        とともに、フロッピーディスクやDAT等別媒体にもバックアップして
        おいて下さい。細心の注意を払って作っておりますが、”gacf”および
        その設置作業に伴う損害は、補償できませんので悪しからず御了承下
        さい。<BR>
        　また、カウンタの数値は、時々ホームページを見て、日付と時刻
        とともにメモしておいて下さい。”count.txt”ファイルが壊れた場合
        その数値を用いて再設定して下さい。<BR><BR>

    <LI>cgiの実行許可<BR>
    meshでは、ファイルの拡張子が”cgi”であれば、自動的
    にcgiとして実行可能なように設定済みなので、ユーザは、特別な設定は必要
    ありません。しかし、他のサイトでは、cgiファイルを置くディレクトリに
    ”.htaccess”という名前のファイルを作って、<BR><BR>
　　AddType application/x-httpd-cgi .cgi<BR><BR>
    という行を書く必要があったり、cgiはすべてユーザのcgi-binというディ
    レクトリに置く必要があったりする場合があります。詳しくは、プロバイ
    ダーまたはシステム管理者にお問い合わせ下さい。<BR><BR>
    
    <LI>最初のアクセス<BR>
    最初に”gacf”を設置した後、ホームページに最初にアクセスしたときに
    は、カウンタの数字は、表示されません。ブラウザの再読み込みのアイ
    コン(Netscapeの場合は、矢印がぐるっと一周しているマークです)を
    クリックするかメニューの中から再読み込みを選んで実行してみて下さい。
    再読み込みで”あなたは、1人目です。”というような表示がでたら”gacf”
    の設置は、成功です。<BR>
    　うまく行かない場合は、ftpで送った１５個のファイル名をブラウザのURL
    を指定するテキストボックスにフルパスで指定してみて、ファイルの存在
    と中身を確認して下さい。”trans.gif”ファイルは、透明なので、見えませんが
    ファイルがあるかどうかは、確認できます。すべてのファイルが正常に存在
    する場合は、ftp等でファイルのアクセス権が上述の設定通りになっているか
    確認して下さい。<BR><BR>

    <LI>修正の際の注意事項<BR>
    ”gacf.cgi”は、”index.html”の転送後に起動され、カウンタの数値
    を１増やしてから、”index_.html”を”index.html”に一行ずつコピー
    します。しかし、その行に ”ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ”(の半角)
　　という文字列があると
    カウンタの数値の個数だけ、カウンタの数値を示すgifファイルのIMGタグを
    ”index.html”に書き込みます。そうしてできた”index.html”は、次回の
     アクセスの際に使われます。<BR>
    　従って、Webの最初のページを修正する場合には、”index.html”では、
    なく、”index_.html”の方を修正して、Webの最初のページのディレクト
    リにお送り下さい。そして、”index.html”への修正は、一回遅れるので、
    再読み込みを実行してから、変更部分の確認を行って下さい。
      また、修正の際には、”index.html”をWebの最初のページのディレクトリ
    にftpで送らないで下さい。もし、送ってしまった場合には、アクセス許可
    を必ず666に変更して下さい。<BR><BR>

    <LI>このgacfに関する質問等<BR>
    NIFTY ServeのFINETAP "Webページ作成法"の電子会議室(現在＃３)で質問
   するか、当方まで、E-mailをお願いします。<BR><BR>

    <LI>謝辞<BR>
        ”gacf”の開発にあたり、鈴木 秀夫さんに貴重な助言を頂きました。
        ここに記して感謝の意を表します。<BR><BR>
    </OL>


<H3><A NAME="gacs">○２番目以降のページ用のグラフィックタイプのアクセスカウンタ”gacs(ver.1.0)”</A></H3>
　個人用Webページの２番目以降のページで使用できるグラフィックタイプの
アクセスカウンタ”gacs(graphic access counter for secondary Web page)”
をここで公開しております。ここから、ダウンロードして貴方のWebページに
設置可能です。ここから、直接ダウンロードしてくれた方は、”無料”です。
著作権は一応留保しますが、貴方のサイトで自由に変更していただいてかまい
ません。<BR>
　このカウンタの特徴は、meshのようにSSI(Server Side Include)は、使
えないが、CGI(Common Gateway Interface)は、使えるプロバイダーのWebページ
で、使用できることです。<BR>
　ファイルの転送方法、アクセス許可の変更方法、CGIファイルの実行許可
については、”gacf”の場合と同じですので、そちらを参照して下さい。<BR>

<H4>”gacs”の設置方法</H4>

<OL>
<LI>呼び出し側のWebページの設定<BR>
　呼び出し側(リンク元)のWebページが”index.html”で、呼ばれる側
(リンク先)のWebページが”second/second.html”であるとして説明します。
つまり、呼ばれる側のデータは、すべて”second”というディレクトリに入れて
いることにします。実際には”second”という名前でなくてもよく、
どんな名称でもかまいません(どんなといっても、英数字やピリオドやアンダースコア等
の半角で16文字以内にしておくのが安全です)。この呼び出し側で他のページにリンクを
張る場合、通常は、次のように指定します。<BR><BR>

　　&lt;A HREF="second/second.html"&gt;second ページ&lt;/A&gt;<BR><BR>

ここで、second.htmlにカウンタ”gacs”を付ける場合は、次のようにします。
<BR><BR>
　　&lt;A HREF="second/gacs.cgi"&gt;second ページ&lt;/A&gt;<BR><BR>

すなわち、htmlファイルを指定する代わりにcgiファイルを指定します。<BR><BR>

<LI>呼び出される側のWebページの設定<BR>
        カウンタの数字を入れたい部分に<BR><BR>

        &lt;!-- ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ --&gt;(半角にして下さい)<BR><BR>

        という行を挿入して下さい。この行には、他の文字等は入れないで
        下さい。また、このWebページの他の部分には、
　　　　”ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ”(の半角表示)
        という文字列は、使用しないで下さい。<BR>
        　例えばページの最初に表示する場合の例を以下に示します。<BR>
        <BLOCKQUOTE>
           &lt;HTML&gt;<BR>
           &lt;HEAD&gt;<BR>
           &lt;TITLE&gt;Second Page&lt;/TITLE&gt;<BR>
           &lt;/HEAD&gt;<BR>
           &lt;BODY&gt;<BR>
           &lt;P ALIGN=RIGHT&gt;<BR>
           あなたは、<BR>
           &lt;!-- ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ --&gt;(半角にして下さい)<BR>
           人目です。<BR>
           &lt;/P&gt;<BR>

        </BLOCKQUOTE>
        ここで、”あなたは、”や”人目です。”の部分は、適宜変更してい
        ただいてかまいませんし、なくても問題ありません。その上の
        ”ALIGN=RIGHT”に付いては、”gacf”のところの説明を御参照下さい。
        <BR><BR>

<LI>”gacs”のCGIスクリプト<BR>
        次のファイルをここからダウンロードして下さい。<BR><BR>

        　　<A HREF="gacs.txt">gacs.txt</A><BR><BR>

        ダウンロードしたらファイル名を”gacs.cgi”と変更してください。
        ダウンロードの仕方は、「”gacf”のCGIスクリプト」の項を参照して
        下さい。
        　このカウンタをmesh以外で使用される場合には、一行目の<BR><BR>

         　　#!/usr/mesh/bin/perl<BR><BR>

        をそのサイトのperlのあるところに変更して下さい。<BR>
        　また、CGIの中のhtmlファイル名<BR><BR>

        　　$html_file = &quot;second.html&quot;;<BR><BR>

        および、カウンタの数値が入っているファイル名<BR><BR>

        　　$count_file = &quot;count.txt&quot;;<BR><BR>

        は、適宜使用しているファイル名に変更して下さい。特にカウンタ
        の数値が入っているファイルは、他のページのカウンタのファイル名
        と重複しないようにして下さい。ページ毎にディレクトリを変えてい
        る場合には、すべて”count.txt”というように同じ名前でもかまいま
        せんがおなじディレクトリに入れる場合は、ページ毎に変えて下さい。
         ”gacs.cgi”ファイル自体も同じディレクトリに入れる場合に
        は、ページ毎にファイル名を変える必要がありますが、ページ毎に
        ディレクトリが異なる場合には、同じ名前でかまいません。<BR><BR>
        　また、$gif_dirを数字のgifファイルのあるディレクトリを示すよう
        適宜変更して下さい。例えば、”gacs.cgi”とこれで表示するhtml
        ファイルがWebの最初のページの”index.html”のあるディレクトリ
        より一段下と二段下の場合には次のようになります。<BR><BR>

        　　$gif_dir = &quot;../image/&quot; (index.htmlより一段下のディレクトリの場合)<BR>
        　　$gif_dir = &quot;../../image/&quot; (index.htmlより二段下のディレクトリの場合)<BR><BR>

        また、CGIではフルパスのファイル名を指定する必要のあるサイトでは
        、上述の３つのファイル(ディレクトリ)名をフルパスに変更して下さい。
<BR><BR>

    <LI>”count.txt”ファイル<BR>
        カウンタの数値を入れるファイル<BR><BR>

        　　<A HREF="count.txt">count.txt</A><BR><BR>

        をここからダウンロードするか、エディターで半角の数字”0”のみ
        が入ったファイルを用意して下さい(リターンは入れないで下さい)。
        カウンタを途中の番号から始めたい場合は、始めたい番号より１小さ
        い数値を半角の数字で書いたファイルをエディターで作って下さい。
        ファイル名は、”count.txt”にして下さい。<BR><BR>

    <LI>数字のgifファイルの転送<BR>
        数字を表示するためのgifファイルを１０個ダウンロード
        して下さい。自分で、数字のgifファイルを作る方や、他の数字のgif
        ファイルを使う方は、ここからダウンロードする必要は、ありません。
        また、Webの最初のページ用の”gacf”用にすでにこれらのファイルを
        ダウンロードしている場合には、新たにダウンロードする必要は、
        ありません。具体的なダウンロードの仕方は、”gacf”の
        ”数字のgifファイルの転送”の部分を御覧下さい。ファイル名は、
        ”0.gif”、”1.gif”、...、”9.gif”として下さい。<BR><BR>

    <LI>ファイルのアップロードとアクセス権の変更<BR>
        ftpで次のファイルをそれぞれのディレクトリへ転送(put)して下さい。
        gifファイルはバイナリーモードで、他はテキストモードで転送して
        下さい。<BR><BR>
        <UL>
        <LI>index.html　を”/.../user_id/public_html/”へ
        <LI>second.html を”/.../user_id/public_html/second/”へ
        <LI>count.txt 　を”/.../user_id/public_html/second/”へ
        <LI>gacs.cgi　　を”/.../user_id/public_html/second/”へ
        <LI>n.gif (nは、0〜9) を”/.../user_id/public_html/image/”へ
           <BR><BR>
        </UL>
        ただし、gifファイルはすでに”gacf”用に転送していればそれを
        共用できるので新たに転送する必要は、ありませんが、”gacs.cgi”
        の中の変数”$gif_dirがgifファイルのあるディレクトリを正しく
        指定するよう設定して下さい。<BR>
        　上の例は、”index.html”が呼び出し側(リンク元)のページ
        で”second.html”が呼び出される側(リンク先)の場合で、second.html
        関連のファイルは、secondというディレクトリにある場合です。<BR>
        　”index.html”に最初のWebページ用のカウンタ”gacf”または、
        ”tacf”を設置している場合には、”index.html”を”index_.html”
        にコピーして”index_.html”の方をftpでお送り下さい。<BR>
        　”/.../user_id/”は、ホームページのftpでloginした際のディレク
        トリを模式的に示したもので、実際はこの文字通りではありません。
         次に”count.txt”ファイルのアクセス許可を”666”に変更して下さ
        い。また、”gacs.cgi”のファイルのアクセス許可を”755”に変更
        して下さい。そのほかのファイルは、一般の人から読み出し可能であ
        ればよいので通常変更不要です。アクセス権の変更の仕方は、
        ”gacf”の”ファイルのアップロードとアクセス権の変更”の部分を
        御参照下さい。<BR><BR>

    <LI>ファイルのバックアップ等<BR>
        ftpでWebページのディレクトリへ送った４個または１４個のファイルは、
        ”gacs”の不具合やサーバーの不調等の原因で破壊されるおそれが
        ありますので必ずローカルなディスクにバックアップを保存する
        とともに、フロッピーディスクやDAT等別媒体にもバックアップして
        おいて下さい。細心の注意を払って作っておりますが、”gacs”および
        その設置作業に伴う損害は、補償できませんので悪しからず御了承下
        さい。<BR>
        　また、カウンタの数値は、時々Webページを見て、日付と時刻
        と共にメモしておいて下さい。”count.txt”ファイルが壊れた場合
        その数値を用いて再設定して下さい。<BR><BR>

<LI>FRAMEタグを使って”gacs”を最初のWebページに設置する場合(御参考)<BR>
    FRAMEタグを使う場合には、”gacs”を最初のページにも使うことができ
    ます。しかし、FRAMEタグは、1996年6月の時点では、Netscape Navigator 
    2.0以上のブラウザしか対応していません。FRAMEタグに対応していない
    ブラウザでは、一度リンクをクリックしてもらう必要があります。<BR><BR>

    <UL>
    <LI>Webページの名前変更<BR>
        最初のWebページ(ホームページ)にカウンタを付ける場合は、これまで
        のWebページのファイル名”index.html”を”main.html”に変更して
        下さい。<BR><BR>
    <LI>”main.html”での設定<BR>
        カウンタの数字を入れたい部分に<BR><BR>

        &lt;!-- ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ --&gt;(半角にしてください)<BR><BR>

        という行を挿入して下さい。この行には、他の文字等は入れないで
        下さい。<BR><BR>
    <LI>新しい”index.html”のWebページの設定<BR>
        次のような内容のファイルを作りファイル名を”index.html”にして下さい。
        <BLOCKQUOTE>
           &lt;HTML&gt;<BR>
           &lt;HEAD&gt;<BR>
           &lt;TITLE&gt;Any Title&lt;/TITLE&gt;<BR>
           &lt;/HEAD&gt;<BR>

           &lt;FRAMESET ROWS="80%, 20%"&gt;<BR>
           &lt;NOFRAME&gt;<BR>
            Please click this link.&lt;A HREF="gacs.cgi"&gt;[HERE]&lt;/A&gt;<BR>
           &lt;/NOFRAME&gt;<BR>

           &lt;FRAME NAME="MAIN_WINDOW" SRC="gacs.cgi"&gt;<BR>

           &lt;FRAME NAME="BOTTOM_WINDOW" SRC="bottom.html"&gt;<BR>

           &lt;/FRAMESET&gt;<BR>

        </BLOCKQUOTE>
        ここで、”bottom.html”は、ブラウザの下部２０％に表示される内容で
        貴方のメイルアドレス等を書いたWebページをご用意下さい。
        ”gacs.cgi”は、「”gacs”のCGIスクリプト」の項で説明したもの
        と同じです。同様にダウンロードして下さい。また、”count.txt”
        ファイルも上述の方法でダウンロードするかエディタで作って下さ
        い。<BR><BR>

    <LI>ファイルのアップロードとアクセス権の変更<BR>
        ftpで次のファイルを最初のWebページをおいておくディレクトリへ
        転送して下さい。<BR><BR>
        <UL>
        <LI>index.html
        <LI>main.html
        <LI>count.txt
        <LI>gacs.cgi<BR><BR>
        </UL>
        ファイルのアクセス権を”count.txt”は、666、”gacs.cgi”は、755
        に設定して下さい。<BR><BR>
    </UL>

<LI>METAタグを使う場合(参考用：おすすめは、しません)<BR>
”gacs”を最初のページに使うのにMETAタグを使う方法もあります。しかし、
METAタグは、Netscape Navigator 2.0やInternet Explorer 2.0等しか対応して
いません。その他のブラウザでは、リンクを一度クリックしてもらう必要
があります。また、この方法は、METAタグの一定時間後のページの切り替えの
機能を使っていますので、ダミーの”index.html”が一瞬表示されます。
　新しいWebページの設定以外は、FRAMEタグの場合と同じ(従来のWebページの
ファイルは”main.html”というファイル名に変更して下さい)ですので、この
部分のみ以下に例を示します。

    <BLOCKQUOTE>
    &lt;HTML&gt;<BR>
    &lt;HEAD&gt;<BR>
    &lt;TITLE&gt;TAKE Soft&lt;/TITLE&gt;<BR>

    &lt;META HTTP-EQUIV="Refresh" CONTENT="0;URL=http://www2a.meshnet.or.jp/~user_id/gacs.cgi"&gt;<BR>

    &lt;/HEAD&gt;<BR>
    &lt;BODY&gt;<BR>

    Please click this link.&lt;A HREF="gacs.cgi"&gt;[HERE]&lt;/A&gt;<BR>

    &lt;/BODY&gt;<BR>
    &lt;/HTML&gt;<BR>
    </BLOCKQUOTE>

    METAタグの意味は、”このWebページを表示して、０秒たったら、次にURLで
    示すページ(ここでは、CGIファイル)を表示しなさい”です。URLは、
    貴方のWebページのある場所のgacs.cgiを示すように変更して下さい。
    <BR><BR>

<LI>このgacsに関する質問等：NIFTY ServeのFINETAP 
    "Webページ作成法"の電子会議室(現在＃３)か、当方までE-mailお願い
    します。

</OL>

<H3><A NAME="gcounter">○meshで使える簡易グラフィックカウンタ”gcounter”</A></H3>
　この”gcounter”は、カウンタの各桁毎にCGIを実行する必要があるので、
通常は、”gacf”または、”gacs”を御使用下さい。<BR>
　NECのC&Cインターネットサービスmeshの個人用ホームページで使用できる
簡易グラフィックカウンタをここで公開しております。ここから、ダウン
ロードして貴方のホームページに設置可能です。ここから直接ダウンロード
下場合には、無料です。<BR>
　このカウンタの特徴は、meshのようにSSI(Server Side Include)は、使
えないが、CGI(Common Gateway Interface)は、使えるプロバイダーのホーム
ページで、IMGタグからCGIを起動して、グラフィックカウンタを表示するこ
とができる点です。ただし、このプログラム(スクリプト)は、Perl(ver.4.019)
で書きましたので、Perlが使えない場所のホームページでは使用できませ
ん。
<H4>gcounterの設置の方法</H4>
　gcounterの本体は、ここでは、すぐ
中身を見ることができるように"gcounter.txt"というファイル名にしてありますが、
ここから転送後は、"gcounter.cgi"という名前に必ず変更して下さい。その他
のファイルは、ファイル名を変えないで下さい。
<OL>
<LI>ファイルのダウンロード(get)：以下のファイルを貴方のコンピュータに
ダウンロード(転送)して下さい。Netscape Navigatorの場合のダウンロードの
しかたは、リンクをクリックして内容を表示させてから、メニューの
”ファイル”から”名前を付けて保存”を選んで下さい。貴方のファイル名を
指定するダイアログがでますから、同じ名前で保存して下さい。ただし、
”gcounter.txt”は、転送後に”gcounter.cgi”に変更しておいて下さい。
転送モードは、ブラウザが自動的に設定してくれます。
　　<UL>
    <LI>gcounterの転送：<A HREF="gcounter.txt">gcounter.txt</A>---gcounter本体
    <LI>count.txtの転送：<A HREF="count.txt">count.txt</A>---カウンタ
        の数値用(初期値の”0”のみのファイル)<BR><BR>

    <LI>数字のgifファイルの転送<BR>
        数字を表示するためのgifファイルを１０個ダウンロード
        して下さい。自分で、数字のgifファイルを作る方や、他の数字のgif
        ファイルを使う方は、ここからダウンロードする必要は、ありません。
        具体的なダウンロードの仕方は、”gacf”の
        ”数字のgifファイルの転送”の部分を御覧下さい。ファイル名は、
        ”0.gif”、”1.gif”、...、”9.gif”として下さい。<BR><BR>
    </UL>
<LI>ファイルの変更：必要に応じて以下の変更をして下さい。
    <UL>
    <LI>”gcounter.txt”のファイル名を必ず”gcounter.cgi”に変更して下さい。
    <LI>mesh以外で使用される場合は、gcounter.cgiのファイルの１行目を、
        そのサイトのperlを絶対パス名(full path)で指定するよう変更して下さい。
        (現状)”#!/usr/mesh/bin/perl"を、例えば、”#!/usr/local/bin/perl”
        のように変更して下さい。perlのある場所は、貴方のプロバイダーや
        システム管理者にお問い合わせ下さい。
　　<LI>meshでは、cgiを起動したときのworking directoryは、cgiのファイル
        のあるdirectoryになるようなので、gcounter.cgiの27行目の変数
        ”$home_dir”は、現在のdirectoryを示す”．”に設定していますが、
        絶対パスを指定する必要のあるサイトでは、カウンタを設置する
        index.htmlやgcounter.cgiのあるdirectoryを絶対パスで指定して下
        さい。ただし、この変数の場合は最後の”/”は、不要です。例えば<BR><BR>
        　　$home_dir = &quot;/home/usr01/user_id/public_html&quot;<BR><BR>
        です。パスの設定は、サイトによって異なりますので貴方のサイトの
        絶対パスが必要な場合は、プロバイダーまたはシステム管理者にお問
        い合わせ下さい。
    <LI>数字を示すgifファイルも貴方のグラフィック編集プログラムで変更
        したり、新しく作ってもかまいませんが、ファイル名は、元の通りの
        もの(十種類)を用意して下さい。<BR><BR>
    </UL>
<LI>ファイルのアップロード(put) ：ダウンロードして変更したファイル(計
１２個)をカウンタを設置するサイトのHTMLファイル(例えば”index.html”)
のあるディレクトリにftpで転送します。このときの転送のモードは、gif
ファイルはバイナリーモードで、その他は、テキストモードで転送して下さ
い。そしてファイルのアクセス許可を”gcounter.cgi”は７５５に、
”count.txt”は、６６６に変更して下さい。gifファイルは、他のユーザから
読み込み可能であればＯＫですので、通常は変更しなくてよいと思います。
meshで、ファイルのアクセス許可を変更するには、ftpで目的のサイトに
ログインして次のようにします。<BR><BR>
　　ftp>cd public_html<BR>
　　ftp>dir<BR>
　　ftp>quote site chmod 755 gcounter.cgi<BR>
　　ftp>quote site chmod 666 counter.txt<BR>
　　ftp>dir<BR><BR>
ここで、cdはディレクトリを移るコマンド、dirは、そのディレクトリのファ
イル一覧を得るコマンドです(”ls -l”でもよい）。quoteのところでファイ
ルのアクセスを変更しています。telnetでファイルのアクセス権を変更できる
サイトでは、chmod以降の部分のみで変更できます。最後のdirは、アクセス権
が変更されたかチェックするためのものです。<BR>
　ftpのコマンドについて不案内の方は、技術資料のページの”計算機コマンド
のRosetta Stone”を御覧下さい。表２に他のOSのコマンドとの対比を示しています。
<BR><BR>

<LI>Home Pageでの設定：例えば４桁のカウンタを設置する場合には、
カウンタを表示したい位置に次のように記述します。ここで、digitは、桁の
右からの位置を示します。例えば、４は、千の位です。incrは、カウンタの
数字の増分を示します。必ず、一番上の位のみ"1"にして、他の位は、"0"に
して下さい。下の例では、千の位を表示する前にcount.txtファイルのカウン
タの数値を１だけ増加させてから、表示を始めています。<BR>
   <PRE>
      &lt;IMG SRC=&quot;gcounter.cgi?digit=4&incr=1&quot; BORDER=0 ALT=&quot; &quot;&gt;
      &lt;IMG SRC=&quot;gcounter.cgi?digit=3&incr=0&quot; BORDER=0 ALT=&quot; &quot;&gt;
      &lt;IMG SRC=&quot;gcounter.cgi?digit=2&incr=0&quot; BORDER=0 ALT=&quot; &quot;&gt;
      &lt;IMG SRC=&quot;gcounter.cgi?digit=1&incr=0&quot; BORDER=0 ALT=&quot; &quot;&gt;
      人目(1996年xx月xx日から)
   </PRE>
IMGタグとIMGタグの間に改行文字があると表示した数字の間に隙間が空きバック
の色が少し見えます。これがいやな場合は、IMGタグ間で改行をしないように
してみて下さい。<BR>
　最大１０桁まで表示できますが、最初は、３桁にしておいて４桁になる前、
または４桁になった後に、４桁に変更するということもできます。３桁にして
おいて、実際のカウントが４桁になっていないかどうかは、ブラウザで確認で
きます。URLを指定するテキストボックスにホームページの指定を書きそのあと
に”count.txt”ファイルの指定してリターンキーを押します。例えば、
”竹ソフト”の場合は、次のように指定します。<BR>
<BR>
　　http://www2a.meshnet.or.jp/~takesoft/count.txt<BR>
<BR>
　カウンタ用のファイルの拡張子をわざわざ”txt”にしているのは、この
ようにすると中身をブラウザから直接見ることができるからです。ただし、
変更はできません。数値を変更する場合は、エディターで半角の数字のみの
ファイルを作り(リターンを入れないようにして下さい）、ftpで送る必要が
あります。最初の場合と同様にファイル名を”count.txt”とする事と、ftpで
送った後、ファイルのアクセス許可を666にする事が必要です。<BR><BR>

<LI>cgiの実行許可：meshでは、ファイルの拡張子が”cgi”であれば、自動的
にcgiとして実行可能なように設定済みなので、ユーザは、特別な設定は必要
ありません。しかし、他のサイトでは、cgiファイルを置くディレクトリに
”.htaccess”という名前のファイルを作って、<BR><BR>
　　AddType application/x-httpd-cgi .cgi<BR><BR>
という行を書く必要があったり、cgiはすべてユーザのcgi-binというディレクトリに置く必要があったりする場合があります。詳しくは、プロバイダーまたはシステム管理者にお問い合わせ下さい。<BR><BR>
<LI>このgcounterに関する質問等：NIFTY ServeのFINETAP 
    "Webページ作成法"の電子会議室(現在＃３)で質問するか、当方までE-mail下さい。
</OL>

<P ALIGN="RIGHT">
<A HREF="../../index.html">竹ソフトのホームページへ戻る<IMG SRC="../../image/home_ico.gif" ALIGN=MIDDLE HSPACE=5 BORDER=0 ALT=" "></A>
</P>

<HR>
<!------------------------------------------------------------------->
<P>
著作・制作(c)1996 竹ソフト: 竹ソフトのWebページに掲載の文書,図,表,アイコン,写真等の無断転載はしないで下さい(上のgcounterとtcounterのように本文中でよい旨表示している部分は除く)。竹ソフトのサイトから転送したファイルにより生じた損害等
あるいは転送作業による損害等は補償できませんので御了承下さい。<BR>
Copyright (c)1996 Takesoft: All rights reserved.<BR>
連絡先：<A HREF="mailto:takesoft@mxs.meshnet.or.jp">takesoft@mxs.meshnet.or.jp</A>
／初期設置日：1996年6月15日／最終変更日：1996年7月19日
</P>

</BODY>
</HTML>
