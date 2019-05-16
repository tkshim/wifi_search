#!/usr/bin/env python
# coding: utf-8
import sqlite3
#DB_PATH='/Users/takeshi/googleDrive/dev/wifi_search/cgi-bin/base.db'
DB_NAME='base.db'

class air:
    def getAirportURL(self, code):
        # 1. DBに接続
        #conn = sqlite3.connect(DB_PATH)
	#DBはトップディレクトリ配下に保存
        #conn = sqlite3.connect(DB_PATH)
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()

        # 2. 一旦、空港コードをaircodeに代入
        aircode=(code,code,)
        URLValues = c.execute("SELECT url FROM main WHERE airport = ? OR code = ? ", aircode)

        # 3. リストを作成
        airportURLList = []

        # 4. リストに空港コードの答えを入れる
        for i in URLValues:
            airportURLList.append(i)

        #5.  答えを取り出す
        for x in airportURLList:
            presentAirport= x

        conn.commit()
        c.close()

        return presentAirport
