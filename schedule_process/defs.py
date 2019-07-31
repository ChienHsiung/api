import time
import re
import pymysql

def run_mysql(sql):
    # 連接資料庫
    arr = []
    conn = pymysql.connect('127.0.0.1','root','','rate',charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    try:
        conn.commit()
        rows = cur.fetchall()
        for row in rows: #重新組裝
            arr.extend(row) #要用extend才行
        conn.close()    
        return rows
    except:
        conn.rollback()

def query_mysql(sql):
    # 取得當天日期
    now = int(time.time())
    timeArray = time.localtime(now)
    mydate = time.strftime("%Y-%m-%d", timeArray)
    # 連接資料庫
    conn = pymysql.connect('127.0.0.1','root','ooxx748@@','rate',charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        ts = list(row)[0]
        ts = re.sub("\D", "", ts)
        ts = int(int(ts)*0.001)
        # 取得timestamp日期
        tt = time.localtime(ts)
        yymmdd = time.strftime("%Y-%m-%d", tt)
        if mydate == yymmdd: #檢查日期是否為當日日期,返回匯率值
            return row[1] 
    conn.close() 