<HTML>
<HEAD>
<TITLE>TAKE Soft/Text-type Access Counter</TITLE>
</HEAD>
<BODY BGCOLOR=#CCFFCC>

<P ALIGN=RIGHT>
371����
</P>

<CENTER>
<TABLE WIDTH=500 BORDER=0>
<TR ALIGN=CENTER VALIGN=MIDDLE>

<TD WIDTH=100><IMG SRC="../../image/cntr_ico.gif" ALT=" "></TD>

<TD WIDTH=300>
<H2>�ƥ����ȥ����פ�<BR>
    ��������������</H2>
</TD>

<TD WIDTH=100><IMG SRC="../../image/cntr_ico.gif" ALT=" "></TD>

</TABLE>
</CENTER>

<HR>
<!------------------------------------------------------>
<H4>�ܼ�</H4>
<UL>
<LI><A HREF=#tacf>
    �ǽ�Υڡ����ѤΥƥ����ȥ����פΥ�������������</A>
<LI><A HREF=#tacs>
    �����ܰʹߤΥڡ����ѤΥƥ����ȥ����פΥ�������������</A>
</UL>

<H3><A NAME="tacf">���ǽ�Υڡ����ѤΥƥ����ȥ����פΥ������������󥿡�tacf (ver.1.1)��</A></H3>
���ۡ���ڡ���(�ǽ��Web�ڡ���)�ǻ��ѤǤ���ƥ����ȥ����פΥ�������
�����󥿡�tacf(text-type access counter for first Web page)�ɤ򤳤���
�������Ƥ���ޤ���<BR>
���������顢����������ɤ��Ƶ����Υۡ���ڡ��������ֲ�ǽ�Ǥ�����������
ľ�ܥ���������ɤ��Ƥ��줿���ϡ���̵���ɤǤ�������ϰ��α�ݤ��ޤ�����
�����Υ����ȤǼ�ͳ���ѹ�����ĺ���Ƥ��ޤ��ޤ���<BR>
<BR>
�����Υ����󥿤���ħ�ϡ�NEC��C&C mesh�Τ褦��SSI(Server Side Include)
�ϡ��Ȥ��ʤ�����CGI(Common Gateway Interface)�ϡ��Ȥ���ץ��Х�������
�ۡ���ڡ����ǡ��Ȥ����Ȥ��Ǥ������Ǥ���<BR>
�����ڡ����ܰʹߤ˼���դ��륫���󥿤ˤĤ��Ƥϼ����tacs"�������������<BR>

<H4>��tacf�ɤ�������ˡ</H4>

    <OL>
    <LI>��index.html�ɤ�Web�ڡ���������<BR>
        �����κǽ��Web�ڡ���(�ե�����̾���index.html�ɤȤ��ޤ�)��
        �����󥿤ο��������줿����ʬ��<BR><BR>

        &lt;!-- �ɣΣӣţңԡ��ãϣգΣԣţ� --&gt;(�ºݤ�Ⱦ�Ѥǽ񤤤Ʋ�����)<BR><BR>

        �Ȥ����Ԥ��������Ʋ����������ιԤˤϡ�¾��ʸ����������ʤ���
        ���������ޤ�������Web�ڡ�����¾����ʬ�ˤϡ�
���������ɣɣΣӣţңԡ��ãϣգΣԣţҡ�(��Ⱦ��)
        �Ȥ���ʸ����ϡ����Ѥ��ʤ��ǲ����������Ѥ���Ȥ����ˤ⥫����
        ��ɽ������Ƥ��ޤ��ޤ��������顢����������ʸ�Ǥϡ����Ѥ�ɽ��
        ���Ƥ��ޤ���<BR>
        ���㤨�Хڡ����κǽ��ɽ������������ʲ��˼����ޤ���<BR>
        <BLOCKQUOTE>
           &lt;HTML&gt;<BR>
           &lt;HEAD&gt;<BR>
           &lt;TITLE&gt;Any Title&lt;/TITLE&gt;<BR>
           &lt;/HEAD&gt;<BR>
           &lt;BODY&gt;<BR>
           &lt;P ALIGN=RIGHT&gt;<BR>
           ���ʤ��ϡ�<BR>
           &lt;!-- �ɣΣӣţңԡ��ãϣգΣԣţ� --&gt;(�ºݤ�Ⱦ�Ѥǽ񤤤Ʋ�����)<BR>
           ���ܤǤ���<BR>
           &lt;/P&gt;<BR>

        </BLOCKQUOTE>
        �����ǡ��ɤ��ʤ��ϡ��ɤ�ɿ��ܤǤ����ɤ���ʬ�ϡ�Ŭ���ѹ����Ƥ�
        �������Ƥ��ޤ��ޤ��󤷡��ʤ��Ƥ����ꤢ��ޤ��󡣤��ξ��<BR><BR>

           &lt;P ALIGN=RIGHT&gt;<BR><BR>

        �ϡ������󥿤�ɽ����¦�ˤ��뤳�Ȥ�ؼ����Ƥ��ޤ�����������
        ��ALIGN=RIGHT�ɤλ���ϡ�Netscape Navigator 2.0���Ǥ���ͭ���Ǥ�
        ����ޤ���TABLE������ȤäƱ��󤻤�����ˡ��Internet Explorer 
        2.0���Ǥ�ͭ���Ǥ���TABLE������ȤäƱ��󤻤�����ˡ�ˤĤ��Ƥϡ�
        ���ݥ��եȡɤΥۡ���ڡ����κǽ����ʬ�Υ�������滲�Ȳ�������
       ����Ǥ⡢TABLE�������б����Ƥ��ʤ��֥饦���Ǥϡ����󤻤Ǥ��ޤ�
       ��<BR><BR>

       ���ޤ������Υե�����ΰ��ֺǸ������IMG��������
       ��tacf.cgi�ɤ�ƤӽФ��Ԥ�ɬ���������Ʋ��������ʲ�����򼨤��ޤ���
       <BR><BR>

       ����&lt;IMG SRC="tacf.cgi" BORDER=0 ALT=""&gt;<BR><BR>

       ����&lt;/BODY&gt;<BR>
       ����&lt;/HTML&gt;<BR><BR>


    <LI>��index_.html�ɤν���<BR>
        ���ˡ���index.html�ɤ򥳥ԡ����ơ���index_.html�ɤȤ���̾����
        �ե�������äƲ���������_�ɤϡ��������������(��������С�)
        �Ǥ���<BR><BR>

    <LI>��tacf�ɤ�CGI������ץ�<BR>
        ���Υե�����򤳤��������������ɤ��Ʋ�������Netscape Navigator
        �ξ��Υ���������ɤλ����ϡ���󥯤򥯥�å��������Ƥ�ɽ��
        �����Ƥ��顢��˥塼�Ρɥե�����ɤ����̾�����դ�����¸�ɤ���
        ��ǲ�������¾�Υ֥饦���ξ��ϡ��ޥ˥奢���滲�Ȳ�����������
        �Υե�����̾����ꤹ��������������Ǥޤ����顢Ʊ��̾������¸��
        �Ʋ����������Υڡ��������ˤϡ��֥饦���Ρ����ܥ��������
        ��Ȥ���������<BR><BR>

        ����<A HREF="tacf.txt">tacf.txt</A><BR><BR>

        ����������ɤ�����ե�����̾���tacf.cgi�ɤ��ѹ����Ʋ�������
        �����Υ����󥿤�mesh�ʳ��ǻ��Ѥ������ˤϡ�����ܤ�<BR><BR>

         ����#!/usr/mesh/bin/perl<BR><BR>

        �򤽤Υ����Ȥ�perl�Τ���Ȥ������ѹ����Ʋ�������<BR>
        ���ޤ������Υ����󥿤�ɬ�פʥե�����̾�򤳤����������Ƥ���
        ��Τ��Ѥ�����䡢CGI�Ǥϥե�ѥ��Υե�����̾����ꤹ��ɬ��
        ��������ˤϡ���(1)�ɤ���ʬ�Σ��ĤΥե�����̾��Ŭ���ѹ�����
        ��������<BR><BR>

        [IE 2.0�ξ������ջ���]<BR>
        Windows 95��Ǻ�ư����Internet Explorer 2.0���Ѥ��ơ�tacf.txt��
        ����������ɤ�����硢�ե��������Ƭ�ˣ��Ԥζ���Ԥ����������
        ������礬����ޤ������Τ褦�ʾ��ϡ����Ģ�佨�ݤΤ褦��
        ���ǥ����ǡ���Ƭ�ζ���Ԥ�ɬ��������Ʋ���������Ƭ�ԤǾ��
        �Ҥ٤�perl�Υե��������ꤷ�Ƥ��ʤ���perl��cgi�ϡ����ޤ�ư��
        �ޤ���<BR><BR>


    <LI>��count.txt�ɥե�����<BR>
        �����󥿤ο��ͤ������ե�����<BR><BR>

        ����<A HREF="count.txt">count.txt</A><BR><BR>

        �򤳤��������������ɤ��뤫�����ǥ�������Ⱦ�Ѥο�����0�ɤΤ�
        �����ä��ե�������Ѱդ��Ʋ�����(�꥿���������ʤ��ǲ�����)��
        �����󥿤�������ֹ椫��Ϥ᤿�����ϡ��Ϥ᤿���ֹ��꣱����
        �����ͤ�Ⱦ�Ѥο����ǽ񤤤��ե�����򥨥ǥ������Ǻ�äƲ�������
        �ե�����̾�ϡ���count.txt�ɤˤ��Ʋ�������<BR><BR>

        [IE 2.0�ξ������ջ���]<BR>
        Windows 95��Ǻ�ư����Internet Explorer 2.0���Ѥ��ơ�count.txt��
        ����������ɤ�����硢�ե��������Ƭ�ˣ��Ԥζ���Ԥ����������
        ������礬����ޤ������Τ褦�ʾ��ϡ����Ģ�佨�ݤΤ褦��
        ���ǥ����ǡ���Ƭ�ζ���Ԥ�ɬ��������Ʋ������������ơ�count.txt�ϡ�
        ��������ե������Ǥ�ftp�����ä�Web�����Ⱦ�Ǥ�ǽ�ϡ�ɬ��1�Х�
        �ȤǤ���<BR><BR>


    <LI>��trans.gif�ɥե�����<BR>
        ���ߡ��Ȥ������뾮����Ʃ���λͳѤ�gif�ե�����Ǥ�������gif�ե�
        ����Ϥ����������������ɤ��뤫�漫ʬ�Ǹ��Ѱղ��������������
        ���ɤ���ݤˡ����β��Ρ�tarns.gif�ɤ򥯥�å����Ƥ⤳��gif�ϡ�
        Ʃ���ʤΤǡ��ʤˤ�ʤ��Хå�������ɽ������ޤ��������ޤ鷺��
        ��˥塼�Ρɥե�����ɤ����̾�����դ�����¸�ɤ���������
        ���ǡ�����������ɤ��Ʋ�������<BR><BR>

        ����<A HREF="trans.gif">trans.gif</A><BR><BR>

    <LI>�ե�����Υ��åץ����ɤȥ������������ѹ�<BR>
        ftp�Ǽ��Υե������ۡ���ڡ����Υǥ��쥯�ȥ��ž��(put)���Ʋ�������
        gif�ե�����ϡ��Х��ʥ꡼�⡼�ɤǡ�¾�ϡ��ƥ����ȥ⡼�ɤ�ž��
        ���Ʋ�������<BR><BR>
        <UL>
        <LI>index.html
        <LI>index_.html
        <LI>count.txt
        <LI>trans.gif
        <LI>tacf.cgi<BR><BR>
        </UL>
        �����ơ���index.html�ɤȡ�count.txt�ɤΥե�����Υ����������Ĥ�
        ��666�ɤ��ѹ����Ʋ���������tacf.cgi�ɤΥե�����Υ����������Ĥ�
        ��755�ɤ��ѹ����Ʋ����������Τۤ��Υե�����ϡ����̤οͤ����ɤ�
        �Ф���ǽ�Ǥ���Ф褤�Τǡ��̾��ѹ����פǤ���<BR>
        ��mesh�ǡ��ե�����Υ����������Ĥ��ѹ�����ˤϡ�ftp����Ū�Υ����Ȥ�
        �������󤷤Ƽ��Τ褦�ˤ��ޤ���<BR><BR>
        ����ftp>cd public_html<BR>
        ����ftp>dir<BR>
        ����ftp>quote site chmod 666 index.html<BR>
        ����ftp>quote site chmod 666 count.txt<BR>
        ����ftp>quote site chmod 755 tacf.cgi<BR>
        ����ftp>dir<BR><BR>
        �����ǡ�cd�ϥǥ��쥯�ȥ��ܤ륳�ޥ�ɡ�dir�ϡ����Υǥ��쥯�ȥ�Υե�
        ������������륳�ޥ�ɤǤ�(��ls -l�ɤǤ�褤�ˡ�quote�ΤȤ����ǥե���
        ��Υ����������ѹ����Ƥ��ޤ���telnet�ǥե�����Υ������������ѹ��Ǥ���
        �����ȤǤϡ�chmod�ʹߤ���ʬ�Τߤ��ѹ��Ǥ��ޤ����Ǹ��dir�ϡ�����������
        ���ѹ����줿�������å����뤿��Τ�ΤǤ���<BR>
        ��ftp�Υ��ޥ�ɤˤĤ����԰�������ϡ����ѻ����Υڡ����Ρɷ׻������ޥ��
        ��Rosetta Stone�ɤ������������ɽ����¾��OS�Υ��ޥ�ɤȤ�����򼨤��Ƥ�         �ޤ���<BR><BR>

        ��CuteFTP�򤪻Ȥ������ϡ����Τ褦�ˤ��������������ѹ����Ʋ�������<BR>
        <OL>
        <LI>�������������ѹ������⡼�ȤΥե�����򥯥�å��������򤹤�
        <LI>��˥塼���� Commands/Custom Commands/Change Files Access mask
            �������򤹤롣
        <LI>�ФƤ����������������ѹ����٤������������Σ���ο���(��755����)
            �����Ϥ���OK�ɥܥ���򥯥�å����롣<BR><BR>
        </OL>
        ��Fetch�򤪻Ȥ������ϡ��ե��������ꤷ���塢���Τ褦�ˤ���
        �������������ѹ����Ʋ�������<BR><BR>
        <PRE>
        �����������Ĥ��755�ɤˤ���Τ� Remote/Set Permissions..��
��������    ������       Read     Write    Search/Execute
��������    Owner         x        x            x
��������    Group         x                     x
��������    Everyone      x                     x

        �����������Ĥ��666�ɤˤ���Τ� Remote/Set Permissions..��
��������    ������       Read     Write    Search/Execute
��������    Owner         x         x            
������    ��Group         x         x            
��������    Everyone      x         x            
        </PRE>

    <LI>�ե�����ΥХå����å���<BR>
        ftp��Web�ڡ����Υǥ��쥯�ȥ�����ä����ĤΥե�����ϡ�
        ��tacf�ɤ��Զ��䥵���С�����Ĵ���θ������˲�����뤪���줬
        ����ޤ��Τ�ɬ����������ʥǥ������˥Хå����åפ���¸����
        �ȤȤ�ˡ��ե��åԡ��ǥ�������DAT�������Τˤ�Хå����åפ���
        �����Ʋ��������ٿ������դ�ʧ�äƺ�äƤ���ޤ�������tacf�ɤ����
        �������ֺ�Ȥ�ȼ��»���ϡ�����Ǥ��ޤ���Τǰ������餺��λ����
        ������<BR>
        ���ޤ��������󥿤ο��ͤϡ������ۡ���ڡ����򸫤ơ����դȻ���
        �ȤȤ�˥�⤷�Ƥ����Ʋ���������count.txt�ɥե����뤬���줿���
        ���ο��ͤ��Ѥ��ƺ����ꤷ�Ʋ�������<BR><BR>

    <LI>cgi�μ¹Ե���<BR>
    mesh�Ǥϡ��ե�����γ�ĥ�Ҥ���cgi�ɤǤ���С���ưŪ
    ��cgi�Ȥ��Ƽ¹Բ�ǽ�ʤ褦������ѤߤʤΤǡ��桼���ϡ����̤������ɬ��
    ����ޤ��󡣤�������¾�Υ����ȤǤϡ�cgi�ե�������֤��ǥ��쥯�ȥ��
    ��.htaccess�ɤȤ���̾���Υե�������äơ�<BR><BR>
����AddType application/x-httpd-cgi .cgi<BR><BR>
    �Ȥ����Ԥ��ɬ�פ����ä��ꡢcgi�Ϥ��٤ƥ桼����cgi-bin�Ȥ����ǥ�
    �쥯�ȥ���֤�ɬ�פ����ä��ꤹ���礬����ޤ����ܤ����ϡ��ץ��Х�
    �����ޤ��ϥ����ƥ�����Ԥˤ��䤤��碌��������<BR><BR>
    
    <LI>�ǽ�Υ�������<BR>
    �ǽ�ˡ�tacf�ɤ����֤����塢�ۡ���ڡ����˺ǽ�˥������������Ȥ���
    �ϡ������󥿤ο����ϡ�ɽ������ޤ��󡣥֥饦���κ��ɤ߹��ߤΥ���
    ����(Netscape�ξ��ϡ����������äȰ�����Ƥ���ޡ����Ǥ�)��
    ����å����뤫��˥塼���椫����ɤ߹��ߤ�����Ǽ¹Ԥ��ƤߤƲ�������
    ���ɤ߹��ߤǡɤ��ʤ��ϡ�1���ܤǤ����ɤȤ����褦��ɽ�����Ǥ����tacf��
    �����֤ϡ������Ǥ���<BR>
    �����ޤ��Ԥ��ʤ����ϡ�ftp�����ä����ĤΥե�����̾��֥饦����URL
    ����ꤹ��ƥ����ȥܥå����˥ե�ѥ��ǻ��ꤷ�Ƥߤơ��ե������¸��
    ����Ȥ��ǧ���Ʋ�������gif�ե�����ϡ�Ʃ���ʤΤǡ������ޤ���
    �ե����뤬���뤫�ɤ����ϡ���ǧ�Ǥ��ޤ������٤ƤΥե����뤬�����¸��
    ������ϡ�ftp���ǥե�����Υ�������������Ҥ������̤�ˤʤäƤ��뤫
    ��ǧ���Ʋ�������<BR><BR>

    <LI>�����κݤ����ջ���<BR>
    ��tacf.cgi�ɤϡ���index.html�ɤ�ž����˵�ư���졢����Ū�ˤ�
    ��index_.html�ɤ��index.html�ɤ˰�Ԥ��ĥ��ԡ����ޤ��������������ιԤ�
    �ɣɣΣӣţңԡ��ãϣգΣԣţҡ�(��Ⱦ��)�Ȥ���ʸ���󤬤���Ȥ��ι�
    �����ϡ����ԡ����������
    �����󥿤ο��ͤ򣱤������ä������������index.html�ɤ˽񤭹��ߤޤ���
    �����ơ��Ǥ�����index.html�ɤϡ�����Υ��������κݤ˻Ȥ��ޤ���<BR>
    �����äơ�Web�κǽ�Υڡ�������������ˤϡ���index.html�ɤǤϡ�
    �ʤ�����index_.html�ɤ����������ơ�Web�κǽ�Υڡ����Υǥ��쥯��
    ��ˤ����겼�����������ơ���index.html�ɤؤν����ϡ�����٤��Τǡ�
    ���ɤ߹��ߤ�¹Ԥ��Ƥ��顢�ѹ���ʬ�γ�ǧ��ԤäƲ�������
      �ޤ��������κݤˤϡ���index.html�ɤ�Web�κǽ�Υڡ����Υǥ��쥯�ȥ�
    ��ftp������ʤ��ǲ��������⤷�����äƤ��ޤä����ˤϡ�������������
    ��ɬ��666���ѹ����Ʋ�������<BR><BR>

    <LI>����tacf�˴ؤ��������<BR>
    NIFTY Serve��FINETAP "Web�ڡ�������ˡ"���ŻҲ�ļ�(���ߡ���)�Ǽ���
   ���뤫�������ޤǡ�E-mail�򤪴ꤤ���ޤ���<BR><BR>

    <LI>���ͤ�<BR><BR>
        <UL>
        <LI>�Х���1996ǯ6��22�� 11:11 ����<BR>
        ��tacf.txt�ɤ˼��Τ褦�ʥХ�������ޤ�
        ���Τǡ���������˥���������ɤ��줿���ϡ��������Ƥ���������
        �⤦���١�tacf.txt�ɤ����������ɤ��Ƥ���������<BR><BR>

        ��(��) if ( $_ =~ /GUEST_NUMBER/ )<BR><BR>

        ��(��) if ( $_ =~ /�ɣΣӣţңԡ��ãϣգΣԣţ�/ )<BR><BR>

        ���Ѥ���ʬ�ϼºݤ�Ⱦ�Ѥǽ񤤤Ʋ����������˿���������ޤ���Ǥ�����
        <BR><BR>

        <LI>����ʸ�Υߥ���1996ǯ6��29��21:10����<BR>
            �ɥե�����Υ��åץ����ɤȥ������������ѹ��ɤι�ǡ������󥿤�
            ���ͤ������ե�����̾����count.html�ɤȤʤäƤ���ޤ�������
            ����ϡ���count.txt�ɤθ���Ǥ������˿���������ޤ���Ǥ�����
            <BR><BR>
        </UL>

    <LI>�ռ�<BR>
        ��tacf�ɤγ�ȯ�ˤ����ꡢ���� ���פ���˵��Ťʽ�����ĺ���ޤ�����
        �����˵����ƴ��դΰդ�ɽ���ޤ���<BR><BR>
    </OL>


<H3><A NAME="tacs">�������ܰʹߤΥڡ����ѤΥƥ����ȥ����פΥ������������󥿡�tacs(ver.1.2)�ɸ�����</A></H3>
���Ŀ���Web�ڡ����Σ����ܰʹߤΥڡ����ǻ��ѤǤ���ƥ����ȥ����פ�
�������������󥿡�tacs(Text-type access counter for secondary Web page)��
�򤳤��Ǹ������Ƥ���ޤ����������顢����������ɤ��Ƶ�����Web�ڡ�����
���ֲ�ǽ�Ǥ����������顢ľ�ܥ���������ɤ��Ƥ��줿���ϡ���̵���ɤǤ���
����ϰ��α�ݤ��ޤ����������Υ����ȤǼ�ͳ���ѹ����Ƥ��������Ƥ��ޤ�
�ޤ���<BR>
�����Υ����󥿤���ħ�ϡ�mesh�Τ褦��SSI(Server Side Include)�ϡ���
���ʤ�����CGI(Common Gateway Interface)�ϡ��Ȥ���ץ��Х�������Web�ڡ���
�ǡ����ѤǤ��뤳�ȤǤ���<BR>
���ե������ž����ˡ�������������Ĥ��ѹ���ˡ��CGI�ե�����μ¹Ե���
�ˤĤ��Ƥϡ���tacf�ɤξ���Ʊ���Ǥ��Τǡ�������򻲾Ȥ��Ʋ�������<BR>

<H4>��tacs�ɤ�������ˡ</H4>

<OL>
<LI>�ƤӽФ�¦��Web�ڡ���������<BR>
���ƤӽФ�¦(��󥯸�)��Web�ڡ�������index.html�ɤǡ��ƤФ��¦
(�����)��Web�ڡ�������second/second.html�ɤǤ���Ȥ����������ޤ���
�Ĥޤꡢ�ƤФ��¦�Υǡ����ϡ����٤ơ�second�ɤȤ����ǥ��쥯�ȥ�������
���뤳�Ȥˤ��ޤ����ºݤˤϡ�second�ɤȤ���̾���Ǥʤ��Ƥ�褯��
�ɤ��̾�ΤǤ⤫�ޤ��ޤ���(�ɤ�ʤȤ��äƤ⡢�ѿ�����ԥꥪ�ɤ䥢�������������
��Ⱦ�Ѥ�16ʸ������ˤ��Ƥ����Τ������Ǥ�)�����θƤӽФ�¦��¾�Υڡ����˥�󥯤�
ĥ���硢�̾�ϡ����Τ褦�˻��ꤷ�ޤ���<BR><BR>

����&lt;A HREF="second/second.html"&gt;second �ڡ���&lt;/A&gt;<BR><BR>

�����ǡ�second.html�˥����󥿡�tacs�ɤ��դ�����ϡ����Τ褦�ˤ��ޤ���
<BR><BR>
����&lt;A HREF="second/tacs.cgi"&gt;second �ڡ���&lt;/A&gt;<BR><BR>

���ʤ����html�ե��������ꤹ�������cgi�ե��������ꤷ�ޤ���<BR><BR>

<LI>�ƤӽФ����¦��Web�ڡ���������<BR>
        �����󥿤ο��������줿����ʬ��<BR><BR>

        &lt;!-- �ɣΣӣţңԡ��ãϣգΣԣţ� --&gt;(�ºݤ�Ⱦ�Ѥ�)<BR><BR>

        �Ȥ����Ԥ��������Ʋ����������ιԤˤϡ�¾��ʸ����������ʤ���
        ���������ޤ�������Web�ڡ�����¾����ʬ�ˤϡ�
        �ɣɣΣӣţңԡ��ãϣգΣԣţҡ�(��Ⱦ��)
        �Ȥ���ʸ����ϡ����Ѥ��ʤ��ǲ�������<BR>
        ���㤨�Хڡ����κǽ��ɽ������������ʲ��˼����ޤ���<BR>
        <BLOCKQUOTE>
           &lt;HTML&gt;<BR>
           &lt;HEAD&gt;<BR>
           &lt;TITLE&gt;Second Page&lt;/TITLE&gt;<BR>
           &lt;/HEAD&gt;<BR>
           &lt;BODY&gt;<BR>
           &lt;P ALIGN=RIGHT&gt;<BR>
           ���ʤ��ϡ�<BR>
           &lt;!-- �ɣΣӣţңԡ��ãϣգΣԣţ� --&gt;(�ºݤ�Ⱦ��)<BR>
           ���ܤǤ���<BR>
           &lt;/P&gt;<BR>

        </BLOCKQUOTE>
        �����ǡ��ɤ��ʤ��ϡ��ɤ�ɿ��ܤǤ����ɤ���ʬ�ϡ�Ŭ���ѹ����Ƥ�
        �������Ƥ��ޤ��ޤ��󤷡��ʤ��Ƥ����ꤢ��ޤ��󡣤��ξ��
        ��ALIGN=RIGHT�ɤ��դ��Ƥϡ���tacf�ɤΤȤ�����������滲�Ȳ�������
        <BR><BR>

<LI>��tacs�ɤ�CGI������ץ�<BR>
        ���Υե�����򤳤��������������ɤ��Ʋ�������<BR><BR>

        ����<A HREF="tacs.txt">tacs.txt</A><BR><BR>

        ����������ɤ�����ե�����̾���tacs.cgi�ɤ��ѹ����Ƥ���������
        ����������ɤλ����ϡ��֡�tacf�ɤ�CGI������ץȡפι�򻲾Ȥ���
        ��������
        �����Υ����󥿤�mesh�ʳ��ǻ��Ѥ������ˤϡ�����ܤ�<BR><BR>

         ����#!/usr/mesh/bin/perl<BR><BR>

        �򤽤Υ����Ȥ�perl�Τ���Ȥ������ѹ����Ʋ�������<BR>
        ���ޤ���CGI�����html�ե�����̾<BR><BR>

        ����$html_file = &quot;second.html&quot;;<BR><BR>

        ����ӡ������󥿤ο��ͤ����äƤ���ե�����̾<BR><BR>

        ����$count_file = &quot;count.txt&quot;;<BR><BR>

        �ϡ�Ŭ�����Ѥ��Ƥ���ե�����̾���ѹ����Ʋ��������ä˥�����
        �ο��ͤ����äƤ���ե�����ϡ�¾�Υڡ����Υ����󥿤Υե�����̾
        �Ƚ�ʣ���ʤ��褦�ˤ��Ʋ��������ڡ�����˥ǥ��쥯�ȥ���Ѥ��Ƥ�
        ����ˤϡ����٤ơ�count.txt�ɤȤ����褦��Ʊ��̾���Ǥ⤫�ޤ���
        ���󤬤��ʤ��ǥ��쥯�ȥ���������ϡ��ڡ�������Ѥ��Ʋ�������
         ��tacs.cgi�ɥե����뼫�Τ�Ʊ���ǥ��쥯�ȥ����������
        �ϡ��ڡ�����˥ե�����̾���Ѥ���ɬ�פ�����ޤ������ڡ������
        �ǥ��쥯�ȥ꤬�ۤʤ���ˤϡ�Ʊ��̾���Ǥ��ޤ��ޤ���<BR>

        �ޤ���CGI�Ǥϥե�ѥ��Υե�����̾����ꤹ��ɬ�פΤ��륵���ȤǤ�
        ����ҤΣ��ĤΥե�����̾��ե�ѥ����ѹ����Ʋ�������<BR><BR>

    <LI>��count.txt�ɥե�����<BR>
        �����󥿤ο��ͤ������ե�����<BR><BR>

        ����<A HREF="count.txt">count.txt</A><BR><BR>

        �򤳤��������������ɤ��뤫�����ǥ�������Ⱦ�Ѥο�����0�ɤΤ�
        �����ä��ե�������Ѱդ��Ʋ�����(�꥿���������ʤ��ǲ�����)��
        �����󥿤�������ֹ椫��Ϥ᤿�����ϡ��Ϥ᤿���ֹ��꣱����
        �����ͤ�Ⱦ�Ѥο����ǽ񤤤��ե�����򥨥ǥ������Ǻ�äƲ�������
        �ե�����̾�ϡ���count.txt�ɤˤ��Ʋ�������<BR><BR>

    <LI>�ե�����Υ��åץ����ɤȥ������������ѹ�<BR>
        ftp�Ǽ��Υե�����򤽤줾��Υǥ��쥯�ȥ��ž�����Ʋ�������
        ���٤ƥƥ����ȥ⡼�ɤ�ž�����Ʋ�������<BR><BR>
        <UL>
        <LI>index.html�����/.../user_id/public_html/�ɤ�
        <LI>second.html ���/.../user_id/public_html/second/�ɤ�
        <LI>count.txt �����/.../user_id/public_html/second/�ɤ�
        <LI>tacs.cgi�������/.../user_id/public_html/second/�ɤ�<BR><BR>
        </UL>

        �����ϡ���index.html�ɤ��ƤӽФ�¦(��󥯸�)�Υڡ���
        �ǡ�second.html�ɤ��ƤӽФ����¦(�����)�ξ��ǡ�second.html
        ��Ϣ�Υե�����ϡ�second�Ȥ����ǥ��쥯�ȥ�ˤ�����Ǥ���<BR>
        ����index.html�ɤ˺ǽ��Web�ڡ����ѤΥ����󥿡�tacf�ɤޤ��ϡ�
        ��gacf�ɤ����֤��Ƥ�����ˤϡ���index.html�ɤ��index_.html��
        �˥��ԡ����ơ�index_.html�ɤ�����ftp�Ǥ����겼������<BR>
        ����/.../user_id/�ɤϡ��ۡ���ڡ�����ftp��login�����ݤΥǥ��쥯
        �ȥ���ϼ�Ū�˼�������Τǡ��ºݤϤ���ʸ���̤�ǤϤ���ޤ���
         ���ˡ�count.txt�ɥե�����Υ����������Ĥ��666�ɤ��ѹ����Ʋ���
        �����ޤ�����tacs.cgi�ɤΥե�����Υ����������Ĥ��755�ɤ��ѹ�
        ���Ʋ����������Τۤ��Υե�����ϡ����̤οͤ����ɤ߽Ф���ǽ�Ǥ�
        ��Ф褤�Τ��̾��ѹ����פǤ����ե�����Υ������������ѹ���ˡ
        �ˤĤ��Ƥϡ���tacf�ɤΡɥե�����Υ��åץ����ɤȥ������������ѹ���
        ����ʬ��滲�Ȳ�������<BR><BR>

    <LI>�ե�����ΥХå����å���<BR>
        ftp��Web�ڡ����Υǥ��쥯�ȥ�����ä����ĤΥե�����ϡ�
        ��tacs�ɤ��Զ��䥵���С�����Ĵ���θ������˲�����뤪���줬
        ����ޤ��Τ�ɬ����������ʥǥ������˥Хå����åפ���¸����
        �ȤȤ�ˡ��ե��åԡ��ǥ�������DAT�������Τˤ�Хå����åפ���
        �����Ʋ��������ٿ������դ�ʧ�äƺ�äƤ���ޤ�������tacs�ɤ����
        �������ֺ�Ȥ�ȼ��»���ϡ�����Ǥ��ޤ���Τǰ������餺��λ����
        ������<BR>
        ���ޤ��������󥿤ο��ͤϡ�����Web�ڡ����򸫤ơ����դȻ���
        �ȶ��˥�⤷�Ƥ����Ʋ���������count.txt�ɥե����뤬���줿���
        ���ο��ͤ��Ѥ��ƺ����ꤷ�Ʋ�������<BR><BR>

<LI>FRAME������Ȥäơ�tacs�ɤ�ǽ��Web�ڡ��������֤�����(�滲��)<BR>
    FRAME������Ȥ����ˤϡ���tacs�ɤ�ǽ�Υڡ����ˤ�Ȥ����Ȥ��Ǥ�
    �ޤ�����������FRAME�����ϡ�1996ǯ6��λ����Ǥϡ�Netscape Navigator 
    2.0�ʾ�Υ֥饦�������б����Ƥ��ޤ���FRAME�������б����Ƥ��ʤ�
    �֥饦���Ǥϡ����٥�󥯤򥯥�å����Ƥ�餦ɬ�פ�����ޤ���<BR><BR>

    <UL>
    <LI>Web�ڡ�����̾���ѹ�<BR>
        �ǽ��Web�ڡ���(�ۡ���ڡ���)�˥����󥿤��դ�����ϡ�����ޤ�
        ��Web�ڡ����Υե�����̾��index.html�ɤ��main.html�ɤ��ѹ�����
        ��������<BR><BR>
    <LI>��main.html�ɤǤ�����<BR>
        �����󥿤ο��������줿����ʬ��<BR><BR>

        &lt;!-- �ɣΣӣţңԡ��ãϣգΣԣţ� --&gt;(�ºݤ�Ⱦ��)<BR><BR>

        �Ȥ����Ԥ��������Ʋ����������ιԤˤϡ�¾��ʸ����������ʤ���
        ��������<BR><BR>
    <LI>��������index.html�ɤ�Web�ڡ���������<BR>
        ���Τ褦�����ƤΥե��������ե�����̾���index.html�ɤˤ��Ʋ�������
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
        �����ǡ���bottom.html�ɤϡ��֥饦���β����������ɽ����������Ƥ�
        �����Υᥤ�륢�ɥ쥹����񤤤�Web�ڡ������Ѱղ�������
        ��tacs.cgi�ɤϡ��֡�tacs�ɤ�CGI������ץȡפι�������������
        ��Ʊ���Ǥ���Ʊ�ͤ˥���������ɤ��Ʋ��������ޤ�����count.txt��
        �ե�������Ҥ���ˡ�ǥ���������ɤ��뤫���ǥ����Ǻ�äƲ���
        ����<BR><BR>

    <LI>�ե�����Υ��åץ����ɤȥ������������ѹ�<BR>
        ftp�Ǽ��Υե������ǽ��Web�ڡ����򤪤��Ƥ����ǥ��쥯�ȥ��
        ž�����Ʋ�������<BR><BR>
        <UL>
        <LI>index.html
        <LI>main.html
        <LI>count.txt
        <LI>tacs.cgi<BR><BR>
        </UL>
        �ե�����Υ������������count.txt�ɤϡ�666����tacs.cgi�ɤϡ�755
        �����ꤷ�Ʋ�������<BR><BR>
    </UL>

<LI>META������Ȥ����(�����ѡ���������ϡ����ޤ���)<BR>
��tacs�ɤ�ǽ�Υڡ����˻Ȥ��Τ�META������Ȥ���ˡ�⤢��ޤ�����������
META�����ϡ�Netscape Navigator 2.0��Internet Explorer 2.0�������б�����
���ޤ��󡣤���¾�Υ֥饦���Ǥϡ���󥯤���٥���å����Ƥ�餦ɬ��
������ޤ����ޤ���������ˡ�ϡ�META�����ΰ�����ָ�Υڡ������ڤ��ؤ���
��ǽ��ȤäƤ��ޤ��Τǡ����ߡ��Ρ�index.html�ɤ����ɽ������ޤ���
��������Web�ڡ���������ʳ��ϡ�FRAME�����ξ���Ʊ��(�����Web�ڡ�����
�ե�����ϡ�main.html�ɤȤ����ե�����̾���ѹ����Ʋ�����)�Ǥ��Τǡ�����
��ʬ�Τ߰ʲ�����򼨤��ޤ���

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

    META�����ΰ�̣�ϡ��ɤ���Web�ڡ�����ɽ�����ơ����ä��ä��顢����URL��
    �����ڡ���(�����Ǥϡ�CGI�ե�����)��ɽ�����ʤ����ɤǤ���URL�ϡ�
    ������Web�ڡ����Τ������tacs.cgi�򼨤��褦���ѹ����Ʋ�������
    <BR><BR>

<LI>����tacs�˴ؤ����������NIFTY Serve��FINETAP 
    "Web�ڡ�������ˡ"���ŻҲ�ļ�(���ߡ���)���������ޤ�E-mail���ꤤ
    ���ޤ���

</OL>


<P ALIGN="RIGHT">
<A HREF="../../index.html">�ݥ��եȤΥۡ���ڡ��������<IMG SRC="../../image/home_ico.gif" ALIGN=MIDDLE HSPACE=5 BORDER=0 ALT=""></A>
</P>

<HR>
<!------------------------------------------------------------------->
<P>
�������(c)1996 �ݥ��ե�: �ݥ��եȤ�Web�ڡ����˷Ǻܤ�ʸ��,��,ɽ,��������,�̿�����̵��ž�ܤϤ��ʤ��ǲ�����(���gcounter��tcounter�Τ褦����ʸ��Ǥ褤��ɽ�����Ƥ�����ʬ�Ͻ���)���ݥ��եȤΥ����Ȥ���ž�������ե�����ˤ��������»����
���뤤��ž����Ȥˤ��»����������Ǥ��ޤ���ΤǸ�λ����������<BR>
Copyright (c)1996 Takesoft: All rights reserved.<BR>
Ϣ���衧<A HREF="mailto:takesoft@mxs.meshnet.or.jp">takesoft@mxs.meshnet.or.jp</A>
�������������1996ǯ6��15�����ǽ��ѹ�����1996ǯ7��17��
</P>

</BODY>
</HTML>