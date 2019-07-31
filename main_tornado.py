import json
#Tornado
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from linebot import LineBotApi, WebhookHandler
from linebot.models import *
from tornado.options import define, options
#Flask
from flask import Flask, request, abort
from linebot.exceptions import (InvalidSignatureError)
# 自訂義函數
from func.level1 import defs
from func.level1 import debug
from func.level1 import query
from func.level1 import update

define("port", default=5000, help="run on the given port", type=int)

# =============================== line =================================
class callback(tornado.web.RequestHandler):
    def post(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        channel_access_token = 'ogsnJ0eYvmaB7SjfVoMdIwFfSmSEPpyIHxY7/jQMYkOjZgo1vYarlbRj1yUvWT6y2PoR5l3apcUCvuAg5huI8ggGh/KxfOa+PgcSE3XvUWoKmJ4AyeRg0I8BMG9Ne1Gz4QuyxTv+PAkfgpWO6S92MgdB04t89/1O/w1cDnyilFU='
        line_bot_api = LineBotApi(channel_access_token)
        body = self.request.body.decode('utf-8')    
        body = json.loads(body)   
        querytext = body['queryResult']['queryText']     
        replytoken = body['originalDetectIntentRequest']['payload']['data']['replyToken']
        uid = body['originalDetectIntentRequest']['payload']['data']['source']['userId']       
        timestamp = int(body['originalDetectIntentRequest']['payload']['data']['timestamp'])
        action = body['queryResult']['action'] 
        debug.show(self)

        # 側錄所有訊息(缺少回復的對話資料)
        sql = "insert into log(uid,time,event) values('%s','%s','%s')" % (uid,timestamp,querytext)
        defs.run_mysql(sql)   

        # 查詢匯率值 from Sql (根據 action)
        # query.query(self,action)
        # update.update(self,action)

        # # 旋轉木馬選單(columns最多10個,actions數目要一樣,且不超過3個)
        if action == 'menu':
            Carousel_template = TemplateSendMessage(
            alt_text='旋轉木馬選單',
            template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    # thumbnail_image_url='https://images2.imgbox.com/4b/e4/QROIGrSo_o.jpg',
                    title='當天匯率查詢(測試用)',
                    text='免費版',
                    actions=[
                        PostbackTemplateAction(
                            label='當天匯率查詢',
                            text='query',
                            # data='action=buy&itemid=1'
                            data='ping'
                        ),
                        MessageTemplateAction(
                            label='當天匯率輸入',
                            text='update'
                        ),                                     
                        URITemplateAction(
                            label='教學說明',
                            uri='http://103.29.68.198/menu'
                        )
                        ]
                        ),  
                CarouselColumn(
                    # thumbnail_image_url='https://images2.imgbox.com/09/de/fP5G10Dz_o.jpg',
                    title='當天匯率查詢',
                    text='免費版',
                    actions=[
                        PostbackTemplateAction(
                            label='當天匯率查詢',
                            text='query',
                            # data='action=buy&itemid=1'
                            data='ping'
                        ),
                        MessageTemplateAction(
                            label='當天匯率輸入',
                            text='update'
                        ),                             
                        # PostbackTemplateAction(
                        #     label='當天匯率查詢',
                        #     text='query',
                        #     # data='action=buy&itemid=1'
                        #     data='ping'
                        # ),                                     
                        URITemplateAction(
                            label='教學說明',
                            uri='http://103.29.68.198/'
                        )
                        ]
                        )                          
            ]
            )
            )
            line_bot_api.reply_message(replytoken,TextSendMessage(text=event.message.text))

        # # 傳送位置
        # if action == 'map':
        #     line_bot_api.reply_message(replytoken,LocationSendMessage(title='地下銀行 (測試用)', 
        #     address='越南某處\n Mobile:0907195866', 
        #     latitude=10.720173, longitude=106.620025))                

# =============================== web =================================
# for input form use
class getdata(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "http://103.29.68.198")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS") 
        username = self.get_argument("username")
        password = self.get_argument("password")
        # self.write(username+password)
        self.write({username:username,password:password})

# for echart use
class getarr(tornado.web.RequestHandler):
    def post(self):
        tmp = []
        self.set_header("Access-Control-Allow-Origin", "http://103.29.68.198")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS") 
        sql = self.get_argument("sql")
        for row in defs.run_mysql(sql): #重新組裝
            tmp.extend(row)
        self.write(str(tmp))

if __name__ == '__main__':
    tornado.options.parse_command_line()
    print('\nTornado Server Running ......')
    app = tornado.web.Application(
        handlers=[
            (r'/callback',callback),
            (r'/input',getdata),
            (r'/getarr',getarr)
        ],
        debug=True,
        autoreload=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()