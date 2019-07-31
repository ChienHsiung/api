import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage
from tornado.options import define, options
define("port",default=5000,type=int)

class callback(tornado.web.RequestHandler):
    def post(self):
        channel_access_token = 'bnGwSEddmvOfmAjIF8lzuqirUEUN4PaTBSjgbnyqK7GqIVl0E+7IlVvFtRpdzr8tCUGR4BuIV1yTJoVRKXIzmYZ6AcfMGE4C6jpB+6FK3lcOgDC66lF03UAlFV4j84RVSF91CNCPo6vklWLfce3FMAdB04t89/1O/w1cDnyilFU='
        line_bot_api = LineBotApi(channel_access_token)

        body = self.request.body.decode('utf-8')    
        print(body,"~~~")
        body = json.loads(body)   
        # print(body,"~~~")
        querytext = body['queryResult']['queryText']     
        replytoken = body['originalDetectIntentRequest']['payload']['data']['replyToken']
        # uid = body['originalDetectIntentRequest']['payload']['data']['source']['userId']       
        # timestamp = int(body['originalDetectIntentRequest']['payload']['data']['timestamp'])
        # action = body['queryResult']['action']

        line_bot_api.reply_message(replytoken,TextSendMessage(querytext))

class test(tornado.web.RequestHandler):
    def post(self):
        print('!! test !!')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    print('\nTornado Server Running ......')
    app = tornado.web.Application(
        handlers=[
            (r'/callback',callback),
            (r'/test',test)
        ],
        debug=True,
        autoreload=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()