import json
import re
import time
import pymysql
from datetime import datetime
import datetime
from linebot import LineBotApi
from linebot.models import *
# 自訂義函數
from func.level1 import defs

# channel_access_token = 'GeK0zFV3RqaICQHejZuLpMxI9+jO/KH01WyJIR96mg0fL+DgjwLOnc/jHNzd2T+Awcqip3sHEDPn1LUVMg2wU8R1xMBEW9hUPV06bnX6/8FT3C8E9k73TRlIev3mkUXu0kBjfIt0k/fNNsZQfCwYpQdB04t89/1O/w1cDnyilFU='
# line_bot_api = LineBotApi(channel_access_token)

def update(self,action):
    body = self.request.body.decode('utf-8')
    body = json.loads(body)  
    replytoken = body['originalDetectIntentRequest']['payload']['data']['replyToken']
    queryText = body['queryResult']['queryText']
    userId = body['originalDetectIntentRequest']['payload']['data']['source']['userId']
    number = body['originalDetectIntentRequest']['payload']['data']['message']['text']
    timestamp =body['originalDetectIntentRequest']['payload']['data']['timestamp']

    try:
        ratetype = body['queryResult']['parameters']['ratetype']
    except:
        pass

    # 獲取日期時間
    now = time.localtime(int(time.time()))
    yymmdd = str(time.strftime('%Y-%m-%d',now))
    print(yymmdd)
    # hhmmss = str(time.strftime('%H:%M:%S',now))
    # print(hhmmss)
    # print(time.gmtime())
    
    # today = datetime.date.today()
    # td = today
    # print(td)

    # td = datetime.datetime.now().strftime("%Y-%m-%d")
    # print(td)

    # sql="select timestamp from rate"
    # conn = pymysql.connect('127.0.0.1','root','ooxx748@@','rate',charset='utf8')
    # cur = conn.cursor()
    # cur.execute(sql)
    # rows = cur.fetchall()
    # for row in rows:
    #     ts = list(row)[0]
    #     ts = re.sub("\D", "", ts)
    #     ts = int(int(ts)*0.001)
    #     tt = time.localtime(ts)
    #     yymmdd = time.strftime("%Y-%m-%d", tt)
    #     print(yymmdd)
    # conn.close()


    # 匯兌更新
    if action == 'rateupdate' and  ratetype == 'vndusd': 
        sql = 'insert into rate(timestamp,date,vndusd,who) values(%s,"%s",%s,"%s")' % (str(int(timestamp)),yymmdd,number,userId) #注意 "%s" 的部分          
        # # text = '越盾換美金'
        defs.run_mysql(sql)

    if action == 'rateupdate' and  ratetype == 'vndntd':
        sql = 'insert into rate(timestamp,vndntd,who) values(%s,%s,"%s")' % (str(int(timestamp)),number,userId)     
        # text = '越盾換台幣'
        defs.run_mysql(sql)

    if action == 'rateupdate' and  ratetype == 'ntdvnd':
        sql = 'insert into rate(timestamp,ntdvnd,who) values(%s,%s,"%s")' % (str(int(timestamp)),number,userId)     
        # text = '台幣換越盾'
        defs.run_mysql(sql)   

    if action == 'rateupdate' and  ratetype == 'usdvnd':
        sql = 'insert into rate(timestamp,usdvnd,who) values(%s,%s,"%s")' % (str(int(timestamp)),number,userId)      
        # text = '美金換越盾'
        defs.run_mysql(sql)
 