import json
from linebot import LineBotApi
from linebot.models import *
# 自訂義函數
from func.level1 import defs
from func.level1 import quickreply

channel_access_token = 'ogsnJ0eYvmaB7SjfVoMdIwFfSmSEPpyIHxY7/jQMYkOjZgo1vYarlbRj1yUvWT6y2PoR5l3apcUCvuAg5huI8ggGh/KxfOa+PgcSE3XvUWoKmJ4AyeRg0I8BMG9Ne1Gz4QuyxTv+PAkfgpWO6S92MgdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(channel_access_token)

def query(self,action):
    body = self.request.body.decode('utf-8')
    body = json.loads(body)  
    replytoken = body['originalDetectIntentRequest']['payload']['data']['replyToken']
    queryText = body['queryResult']['queryText']
    
    # 匯兌查詢
    if action == 'vnd>usd' :
        sql = "select timestamp,vndusd from rate where vndusd !='' order by timestamp desc"        
        # text = '越盾換美金'
        text = str(defs.query_mysql(sql))+' Đ'+' : 1 USD'
        line_bot_api.reply_message(replytoken,[TextMessage(text=text),quickreply.q_reply(qr_id=1)])     

    if action == 'vnd>ntd' :
        sql = "select timestamp,vndntd from rate where vndntd !='' order by timestamp desc"
        # text = '越盾換台幣'
        text = str(defs.query_mysql(sql))+' Đ' + ' : 1 NTD' 
        line_bot_api.reply_message(replytoken,[TextMessage(text=text),quickreply.q_reply(qr_id=2)])

    if action == 'ntd>vnd' :
        sql = "select timestamp,ntdvnd from rate where ntdvnd !='' order by timestamp desc"
        # text = '台幣換越盾'
        text = '1 Đ : 1 / '+str(defs.query_mysql(sql))+' NTD'
        line_bot_api.reply_message(replytoken,[TextMessage(text=text),quickreply.q_reply(qr_id=2)])    

    if action == 'usd>vnd' :
        sql = "select timestamp,usdvnd from rate where usdvnd !='' order by timestamp desc"
        # text = '美金換越盾'
        # text = '%0.10f USD : 1 Đ' % defs.query_mysql(sql)
        text = '1 Đ : 1 / ' +str(defs.query_mysql(sql))+' USD'        
        line_bot_api.reply_message(replytoken,[TextMessage(text=text),quickreply.q_reply(qr_id=1)])    

