<HTML>
<HEAD>
<TITLE>TAKE Soft/Text-type Access Counter</TITLE>
</HEAD>
<BODY BGCOLOR=#CCFFCC>

<P ALIGN=RIGHT>
371人目
</P>

<CENTER>
<TABLE WIDTH=500 BORDER=0>
<TR ALIGN=CENTER VALIGN=MIDDLE>

<TD WIDTH=100><IMG SRC="../../image/cntr_ico.gif" ALT=" "></TD>

<TD WIDTH=300>
<H2>テキストタイプの<BR>
    アクセスカウンタ</H2>
</TD>

<TD WIDTH=100><IMG SRC="../../image/cntr_ico.gif" ALT=" "></TD>

</TABLE>
</CENTER>

<HR>
<!------------------------------------------------------>
<H4>目次</H4>
<UL>
<LI><A HREF=#tacf>
    最初のページ用のテキストタイプのアクセスカウンタ</A>
<LI><A HREF=#tacs>
    ２番目以降のページ用のテキストタイプのアクセスカウンタ</A>
</UL>

<H3><A NAME="tacf">○最初のページ用のテキストタイプのアクセスカウンタ”tacf (ver.1.1)”</A></H3>
　ホームページ(最初のWebページ)で使用できるテキストタイプのアクセス
カウンタ”tacf(text-type access counter for first Web page)”をここで
公開しております。<BR>
　ここから、ダウンロードして貴方のホームページに設置可能です。ここから
直接ダウンロードしてくれた方は、”無料”です。著作権は一応留保しますが、
貴方のサイトで自由に変更して頂いてかまいません。<BR>
<BR>
　このカウンタの特徴は、NECのC&C meshのようにSSI(Server Side Include)
は、使えないが、CGI(Common Gateway Interface)は、使えるプロバイダーの
ホームページで、使うことができる点です。<BR>
　２ページ目以降に取り付けるカウンタについては次節”tacs"を御覧下さい。<BR>

<H4>”tacf”の設置方法</H4>

    <OL>
    <LI>”index.html”のWebページの設定<BR>
        貴方の最初のWebページ(ファイル名を”index.html”とします)の
        カウンタの数字を入れたい部分に<BR><BR>

        &lt;!-- ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ --&gt;(実際は半角で書いて下さい)<BR><BR>

        という行を挿入して下さい。この行には、他の文字等は入れないで
        下さい。また、このWebページの他の部分には、
　　　　”ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ”(の半角)
        という文字列は、使用しないで下さい。使用するとそこにもカウンタ
        が表示されてしまいます。だから、ここの説明文では、全角で表示
        しています。<BR>
        　例えばページの最初に表示する場合の例を以下に示します。<BR>
        <BLOCKQUOTE>
           &lt;HTML&gt;<BR>
           &lt;HEAD&gt;<BR>
           &lt;TITLE&gt;Any Title&lt;/TITLE&gt;<BR>
           &lt;/HEAD&gt;<BR>
           &lt;BODY&gt;<BR>
           &lt;P ALIGN=RIGHT&gt;<BR>
           あなたは、<BR>
           &lt;!-- ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ --&gt;(実際は半角で書いて下さい)<BR>
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
       ”tacf.cgi”を呼び出す行を必ず挿入して下さい。以下に例を示します。
       <BR><BR>

       　　&lt;IMG SRC="tacf.cgi" BORDER=0 ALT=""&gt;<BR><BR>

       　　&lt;/BODY&gt;<BR>
       　　&lt;/HTML&gt;<BR><BR>


    <LI>”index_.html”の準備<BR>
        次に、”index.html”をコピーして、”index_.html”という名前の
        ファイルを作って下さい。”_”は、アンダースコア(アンダーバー)
        です。<BR><BR>

    <LI>”tacf”のCGIスクリプト<BR>
        次のファイルをここからダウンロードして下さい。Netscape Navigator
        の場合のダウンロードの仕方は、リンクをクリックして内容を表示
        させてから、メニューの”ファイル”から”名前を付けて保存”を選
        んで下さい。他のブラウザの場合は、マニュアルを御参照下さい。貴方
        のファイル名を指定するダイアログがでますから、同じ名前で保存し
        て下さい。このページへ戻るには、ブラウザの”戻るボタン”等を
        御使い下さい。<BR><BR>

        　　<A HREF="tacf.txt">tacf.txt</A><BR><BR>

        ダウンロードしたらファイル名を”tacf.cgi”と変更して下さい。
        　このカウンタをmesh以外で使用される場合には、一行目の<BR><BR>

         　　#!/usr/mesh/bin/perl<BR><BR>

        をそのサイトのperlのあるところに変更して下さい。<BR>
        　また、このカウンタに必要なファイル名をここで説明している
        ものと変える場合や、CGIではフルパスのファイル名を指定する必要
        がある場合には、”(1)”の部分の４個のファイル名を適宜変更して
        下さい。<BR><BR>

        [IE 2.0の場合の注意事項]<BR>
        Windows 95上で作動するInternet Explorer 2.0を用いて、tacf.txtを
        ダウンロードした場合、ファイルの先頭に２行の空白行が勝手に挿入
        される場合があります。このような場合は、メモ帳や秀丸のような
        エディタで、先頭の空白行を必ず削除して下さい。先頭行で上に
        述べたperlのファイルを指定していないとperlのcgiは、うまく動き
        ません。<BR><BR>


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

    <LI>ファイルのアップロードとアクセス権の変更<BR>
        ftpで次のファイルをホームページのディレクトリへ転送(put)して下さい。
        gifファイルは、バイナリーモードで、他は、テキストモードで転送
        して下さい。<BR><BR>
        <UL>
        <LI>index.html
        <LI>index_.html
        <LI>count.txt
        <LI>trans.gif
        <LI>tacf.cgi<BR><BR>
        </UL>
        そして、”index.html”と”count.txt”のファイルのアクセス許可を
        ”666”に変更して下さい。”tacf.cgi”のファイルのアクセス許可を
        ”755”に変更して下さい。そのほかのファイルは、一般の人から読み
        出し可能であればよいので、通常変更不要です。<BR>
        　meshで、ファイルのアクセス許可を変更するには、ftpで目的のサイトに
        ログインして次のようにします。<BR><BR>
        　　ftp>cd public_html<BR>
        　　ftp>dir<BR>
        　　ftp>quote site chmod 666 index.html<BR>
        　　ftp>quote site chmod 666 count.txt<BR>
        　　ftp>quote site chmod 755 tacf.cgi<BR>
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
        ftpでWebページのディレクトリへ送った５個のファイルは、
        ”tacf”の不具合やサーバーの不調等の原因で破壊されるおそれが
        ありますので必ずローカルなディスクにバックアップを保存する
        とともに、フロッピーディスクやDAT等別媒体にもバックアップして
        おいて下さい。細心の注意を払って作っておりますが、”tacf”および
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
    最初に”tacf”を設置した後、ホームページに最初にアクセスしたときに
    は、カウンタの数字は、表示されません。ブラウザの再読み込みのアイ
    コン(Netscapeの場合は、矢印がぐるっと一周しているマークです)を
    クリックするかメニューの中から再読み込みを選んで実行してみて下さい。
    再読み込みで”あなたは、1人目です。”というような表示がでたら”tacf”
    の設置は、成功です。<BR>
    　うまく行かない場合は、ftpで送った５個のファイル名をブラウザのURL
    を指定するテキストボックスにフルパスで指定してみて、ファイルの存在
    と中身を確認して下さい。gifファイルは、透明なので、見えませんが
    ファイルがあるかどうかは、確認できます。すべてのファイルが正常に存在
    する場合は、ftp等でファイルのアクセス権が上述の設定通りになっているか
    確認して下さい。<BR><BR>

    <LI>修正の際の注意事項<BR>
    ”tacf.cgi”は、”index.html”の転送後に起動され、基本的には
    ”index_.html”を”index.html”に一行ずつコピーします。しかし、その行に
    ”ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ”(の半角)という文字列があるとその行
    だけは、コピーする代わりに
    カウンタの数値を１だけ増加させた数字を”index.html”に書き込みます。
    そして、できた”index.html”は、次回のアクセスの際に使われます。<BR>
    　従って、Webの最初のページを修正する場合には、”index.html”では、
    なく、”index_.html”の方を修正して、Webの最初のページのディレクト
    リにお送り下さい。そして、”index.html”への修正は、一回遅れるので、
    再読み込みを実行してから、変更部分の確認を行って下さい。
      また、修正の際には、”index.html”をWebの最初のページのディレクトリ
    にftpで送らないで下さい。もし、送ってしまった場合には、アクセス許可
    を必ず666に変更して下さい。<BR><BR>

    <LI>このtacfに関する質問等<BR>
    NIFTY ServeのFINETAP "Webページ作成法"の電子会議室(現在＃３)で質問
   するか、当方まで、E-mailをお願いします。<BR><BR>

    <LI>お詫び<BR><BR>
        <UL>
        <LI>バグ：1996年6月22日 11:11 以前<BR>
        ”tacf.txt”に次のようなバグがありまし
        たので、これ以前にダウンロードされた方は、修正していただくか
        もう一度”tacf.txt”をダウンロードしてください。<BR><BR>

        　(誤) if ( $_ =~ /GUEST_NUMBER/ )<BR><BR>

        　(正) if ( $_ =~ /ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ/ )<BR><BR>

        全角の部分は実際は半角で書いて下さい。誠に申し訳ありませんでした。
        <BR><BR>

        <LI>説明文のミス：1996年6月29日21:10以前<BR>
            ”ファイルのアップロードとアクセス権の変更”の項で、カウンタの
            数値を入れるファイル名が”count.html”となっておりましたが、
            これは、”count.txt”の誤りです。誠に申し訳ありませんでした。
            <BR><BR>
        </UL>

    <LI>謝辞<BR>
        ”tacf”の開発にあたり、鈴木 秀夫さんに貴重な助言を頂きました。
        ここに記して感謝の意を表します。<BR><BR>
    </OL>


<H3><A NAME="tacs">○２番目以降のページ用のテキストタイプのアクセスカウンタ”tacs(ver.1.2)”公開中</A></H3>
　個人用Webページの２番目以降のページで使用できるテキストタイプの
アクセスカウンタ”tacs(Text-type access counter for secondary Web page)”
をここで公開しております。ここから、ダウンロードして貴方のWebページに
設置可能です。ここから、直接ダウンロードしてくれた方は、”無料”です。
著作権は一応留保しますが、貴方のサイトで自由に変更していただいてかまい
ません。<BR>
　このカウンタの特徴は、meshのようにSSI(Server Side Include)は、使
えないが、CGI(Common Gateway Interface)は、使えるプロバイダーのWebページ
で、使用できることです。<BR>
　ファイルの転送方法、アクセス許可の変更方法、CGIファイルの実行許可
については、”tacf”の場合と同じですので、そちらを参照して下さい。<BR>

<H4>”tacs”の設置方法</H4>

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

ここで、second.htmlにカウンタ”tacs”を付ける場合は、次のようにします。
<BR><BR>
　　&lt;A HREF="second/tacs.cgi"&gt;second ページ&lt;/A&gt;<BR><BR>

すなわち、htmlファイルを指定する代わりにcgiファイルを指定します。<BR><BR>

<LI>呼び出される側のWebページの設定<BR>
        カウンタの数字を入れたい部分に<BR><BR>

        &lt;!-- ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ --&gt;(実際は半角で)<BR><BR>

        という行を挿入して下さい。この行には、他の文字等は入れないで
        下さい。また、このWebページの他の部分には、
        ”ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ”(の半角)
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
           &lt;!-- ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ --&gt;(実際は半角)<BR>
           人目です。<BR>
           &lt;/P&gt;<BR>

        </BLOCKQUOTE>
        ここで、”あなたは、”や”人目です。”の部分は、適宜変更してい
        ただいてかまいませんし、なくても問題ありません。その上の
        ”ALIGN=RIGHT”に付いては、”tacf”のところの説明を御参照下さい。
        <BR><BR>

<LI>”tacs”のCGIスクリプト<BR>
        次のファイルをここからダウンロードして下さい。<BR><BR>

        　　<A HREF="tacs.txt">tacs.txt</A><BR><BR>

        ダウンロードしたらファイル名を”tacs.cgi”と変更してください。
        ダウンロードの仕方は、「”tacf”のCGIスクリプト」の項を参照して
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
         ”tacs.cgi”ファイル自体も同じディレクトリに入れる場合に
        は、ページ毎にファイル名を変える必要がありますが、ページ毎に
        ディレクトリが異なる場合には、同じ名前でかまいません。<BR>

        また、CGIではフルパスのファイル名を指定する必要のあるサイトでは
        、上述の２つのファイル名をフルパスに変更して下さい。<BR><BR>

    <LI>”count.txt”ファイル<BR>
        カウンタの数値を入れるファイル<BR><BR>

        　　<A HREF="count.txt">count.txt</A><BR><BR>

        をここからダウンロードするか、エディターで半角の数字”0”のみ
        が入ったファイルを用意して下さい(リターンは入れないで下さい)。
        カウンタを途中の番号から始めたい場合は、始めたい番号より１小さ
        い数値を半角の数字で書いたファイルをエディターで作って下さい。
        ファイル名は、”count.txt”にして下さい。<BR><BR>

    <LI>ファイルのアップロードとアクセス権の変更<BR>
        ftpで次のファイルをそれぞれのディレクトリへ転送して下さい。
        すべてテキストモードで転送して下さい。<BR><BR>
        <UL>
        <LI>index.html　を”/.../user_id/public_html/”へ
        <LI>second.html を”/.../user_id/public_html/second/”へ
        <LI>count.txt 　を”/.../user_id/public_html/second/”へ
        <LI>tacs.cgi　　を”/.../user_id/public_html/second/”へ<BR><BR>
        </UL>

        上の例は、”index.html”が呼び出し側(リンク元)のページ
        で”second.html”が呼び出される側(リンク先)の場合で、second.html
        関連のファイルは、secondというディレクトリにある場合です。<BR>
        　”index.html”に最初のWebページ用のカウンタ”tacf”または、
        ”gacf”を設置している場合には、”index.html”を”index_.html”
        にコピーして”index_.html”の方をftpでお送り下さい。<BR>
        　”/.../user_id/”は、ホームページのftpでloginした際のディレク
        トリを模式的に示したもので、実際はこの文字通りではありません。
         次に”count.txt”ファイルのアクセス許可を”666”に変更して下さ
        い。また、”tacs.cgi”のファイルのアクセス許可を”755”に変更
        して下さい。そのほかのファイルは、一般の人から読み出し可能であ
        ればよいので通常変更不要です。ファイルのアクセス権の変更方法
        については、”tacf”の”ファイルのアップロードとアクセス権の変更”
        の部分を御参照下さい。<BR><BR>

    <LI>ファイルのバックアップ等<BR>
        ftpでWebページのディレクトリへ送った４個のファイルは、
        ”tacs”の不具合やサーバーの不調等の原因で破壊されるおそれが
        ありますので必ずローカルなディスクにバックアップを保存する
        とともに、フロッピーディスクやDAT等別媒体にもバックアップして
        おいて下さい。細心の注意を払って作っておりますが、”tacs”および
        その設置作業に伴う損害は、補償できませんので悪しからず御了承下
        さい。<BR>
        　また、カウンタの数値は、時々Webページを見て、日付と時刻
        と共にメモしておいて下さい。”count.txt”ファイルが壊れた場合
        その数値を用いて再設定して下さい。<BR><BR>

<LI>FRAMEタグを使って”tacs”を最初のWebページに設置する場合(御参考)<BR>
    FRAMEタグを使う場合には、”tacs”を最初のページにも使うことができ
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

        &lt;!-- ＩＮＳＥＲＴ＿ＣＯＵＮＴＥＲ --&gt;(実際は半角)<BR><BR>

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
            Please click this link.&lt;A HREF="tacs.cgi"&gt;[HERE]&lt;/A&gt;<BR>
           &lt;/NOFRAME&gt;<BR>

           &lt;FRAME NAME="MAIN_WINDOW" SRC="tacs.cgi"&gt;<BR>

           &lt;FRAME NAME="BOTTOM_WINDOW" SRC="bottom.html"&gt;<BR>

           &lt;/FRAMESET&gt;<BR>

        </BLOCKQUOTE>
        ここで、”bottom.html”は、ブラウザの下部２０％に表示される内容で
        貴方のメイルアドレス等を書いたWebページをご用意下さい。
        ”tacs.cgi”は、「”tacs”のCGIスクリプト」の項で説明したもの
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
        <LI>tacs.cgi<BR><BR>
        </UL>
        ファイルのアクセス権を”count.txt”は、666、”tacs.cgi”は、755
        に設定して下さい。<BR><BR>
    </UL>

<LI>METAタグを使う場合(参考用：おすすめは、しません)<BR>
”tacs”を最初のページに使うのにMETAタグを使う方法もあります。しかし、
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

    &lt;META HTTP-EQUIV="Refresh" CONTENT="0;URL=http://www2a.meshnet.or.jp/~user_id/tacs.cgi"&gt;<BR>

    &lt;/HEAD&gt;<BR>
    &lt;BODY&gt;<BR>

    Please click this link.&lt;A HREF="tacs.cgi"&gt;[HERE]&lt;/A&gt;<BR>

    &lt;/BODY&gt;<BR>
    &lt;/HTML&gt;<BR>
    </BLOCKQUOTE>

    METAタグの意味は、”このWebページを表示して、０秒たったら、次にURLで
    示すページ(ここでは、CGIファイル)を表示しなさい”です。URLは、
    貴方のWebページのある場所のtacs.cgiを示すように変更して下さい。
    <BR><BR>

<LI>このtacsに関する質問等：NIFTY ServeのFINETAP 
    "Webページ作成法"の電子会議室(現在＃３)か、当方までE-mailお願い
    します。

</OL>


<P ALIGN="RIGHT">
<A HREF="../../index.html">竹ソフトのホームページへ戻る<IMG SRC="../../image/home_ico.gif" ALIGN=MIDDLE HSPACE=5 BORDER=0 ALT=""></A>
</P>

<HR>
<!------------------------------------------------------------------->
<P>
著作・制作(c)1996 竹ソフト: 竹ソフトのWebページに掲載の文書,図,表,アイコン,写真等の無断転載はしないで下さい(上のgcounterとtcounterのように本文中でよい旨表示している部分は除く)。竹ソフトのサイトから転送したファイルにより生じた損害等
あるいは転送作業による損害等は補償できませんので御了承下さい。<BR>
Copyright (c)1996 Takesoft: All rights reserved.<BR>
連絡先：<A HREF="mailto:takesoft@mxs.meshnet.or.jp">takesoft@mxs.meshnet.or.jp</A>
／初期設置日：1996年6月15日／最終変更日：1996年7月17日
</P>

</BODY>
</HTML>
