import time
import pymysql
from linebot import LineBotApi
from linebot.models import TextSendMessage

line_bot_api = LineBotApi('GeK0zFV3RqaICQHejZuLpMxI9+jO/KH01WyJIR96mg0fL+DgjwLOnc/jHNzd2T+Awcqip3sHED \
    Pn1LUVMg2wU8R1xMBEW9hUPV06bnX6/8FT3C8E9k73TRlIev3mkUXu0kBjfIt0k/fNNsZQfCwYpQdB04t89/1O/w1cDnyilFU=')

def read_mysql():
    # 連接資料庫
    db = pymysql.connect('127.0.0.1','root','ooxx748@@','rate',charset='utf8')
    cur = db.cursor()
    cur.execute('select * from rate')
    rows = cur.fetchall()
    for row in rows:
        print(row)
        print(row[1],row[3])
    cur.close
    db.close    
    return 12345000

def get_datetime():
    now = int(time.time())
    timeArray = time.localtime(now)
    mydate = time.strftime("%Y-%m-%d", timeArray)
    mytime = time.strftime("%H:%M:%S", timeArray)
    print(time.gmtime())
    print("date %s \ntime %s" % (mydate,mytime))    

def trytry(event):
    text = "ddt from trytry ............ !! "
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text))             