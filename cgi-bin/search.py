#!/usr/bin/env python
# coding: utf-8

# ------------------------------------------------------
# 1. CGIの設定
# ------------------------------------------------------

import cgi
form=cgi.FieldStorage()
inputcode=form.getvalue('input_value')
#小文字に統一
tmpcode=inputcode.lower()


# ------------------------------------------------------
# 2. DBのsearch用インスタンスを作成
# ------------------------------------------------------

import geturlClass
instance001 = geturlClass.air()
# tmpcodeをDB用のインスタンスに代入
presentURL = instance001.getAirportURL(tmpcode)


# ------------------------------------------------------
# 3. HTMLの本体を定義
# ------------------------------------------------------

body = u"""
<HTML>
<head>
<meta name="viewport" content="width=device-width,initial-scale=1">
</head>
  <BODY background="/image/airport.png"  link=white vlink=white alink=white>
  <center><font color=white>
  <BR>
  <center>
  <!-- 
　オプション：contentのデータ型を定義
  ここに直接も事例を入れても良い
  -->
  <!-- 
              HERE 
  -->

  %s

  <p>
  <input type="button" value="前のページへ戻る" onclick="history.back()">
  </BODY>
</HTML>"""


# ------------------------------------------------------
# 4. %sにはcontentのデータが入る。
# 命名規則としてcontentでなく任意の文字列で良い
# ------------------------------------------------------

content=""
content+=u"<br/>WIFI Information page is"
content+=u"<p> <iframe src=%s width='400' height='252' style='border:none;overflow:hidden' scrolling='no' frameborder='0' allowTransparency='true' allow='encrypted-media'></iframe>" % (presentURL)
content+=u"<br/><A HREF=%s target='_blank'>" % (presentURL)
content+=u" %s </A> " % (presentURL)

# ------------------------------------------------------
# 5. bodyとcontentを定義
# ------------------------------------------------------

print ("Content-type: text/html;charset=utf-8\n")
print (body % content).encode('utf-8')


