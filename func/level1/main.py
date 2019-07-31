import json,time
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,CarouselTemplate,CarouselColumn,LocationSendMessage,StickerSendMessage,TemplateSendMessage,ButtonsTemplate,MessageTemplateAction,URITemplateAction,PostbackTemplateAction)
from linebot import LineBotApi
line_bot_api = LineBotApi('GeK0zFV3RqaICQHejZuLpMxI9+jO/KH01WyJIR96mg0fL+DgjwLOnc/jHNzd2T+Awcqip3sHEDPn1LUVMg2wU8R1xMBEW9hUPV06bnX6/8FT3C8E9k73TRlIev3mkUXu0kBjfIt0k/fNNsZQfCwYpQdB04t89/1O/w1cDnyilFU=')

# 自訂義函數
from func.level1 import defs

def mysub(event):
    # 取出userId
    userId = json.loads(str(event.source))
    userId = userId['userId']    
    # 將timestamp轉成localtime
    now = time.localtime(event.timestamp)
    yymmdd = str(time.strftime('%Y/%m/%d',now))
    hhmmss = str(time.strftime('%H:%M:%S',now))
    
    # 側錄所有訊息
    sql = "insert into log(uid,time,event) values('%s','%s','%s')" % (userId,event.timestamp,event.message.text)
    defs.run_mysql(sql)    

    # ========== 判斷式 ==========
    if event.source.type == 'user' and event.message.text == 'show':
        # 呼叫自訂義函數
        # defs.get_datetime()
        # 呼叫自訂義函數        
        # 可傳送sql查詢
        # 有接收return值
        
        sql = '''insert into log(uid,time,event) values('%s','%s','%s')''' % (userId,event.timestamp,event.message.text)
        defs.run_mysql(sql)
        text = "SQL指令執行完成"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text))
    elif event.source.type == 'user'and event.message.text == 'ddt':
        # 呼叫import的函數
        defs.trytry(event)
        # text = "ddt"
        # line_bot_api.reply_message(event.reply_token,TextSendMessage(text))    
    elif event.message.text == "貼圖":
        # 使用StickerSendMessage
        line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=1, sticker_id=2))
        # 同時傳送兩個訊息      
        # line_bot_api.reply_message(event.reply_token,[StickerSendMessage(package_id=1, sticker_id=2),LocationSendMessage(title='地下銀行', address='地獄 -18F \n Cont Ty THNN XXXXX', latitude=10.718926, longitude=106.639811)])    
        # 顯示位置座標
    elif event.message.text == "位置":
        line_bot_api.reply_message(event.reply_token,
        LocationSendMessage(title='地下銀行', address='地獄 -18F \n Cont Ty THNN XXXXX', latitude=10.718926, longitude=106.639811))
        # 使用Buttons Template (單個)(之一)
    elif event.message.text == "menu":
        buttons_template = TemplateSendMessage(
            alt_text='次選單',
            template=ButtonsTemplate(
                title='選擇服務(最多四個)',
                text='請選擇',
                thumbnail_image_url='https://thumbs2.imgbox.com/ad/2e/NahWaebN_t.gif',
                actions=[
                    MessageTemplateAction(
                        label='越盾買美金',
                        text='越盾買美金'
                    ),
                    MessageTemplateAction(
                        label='美金買越盾',
                        text='美金買越盾'
                    ),
                    MessageTemplateAction(
                        label='越盾買台幣',
                        text='越盾買台幣'
                    ),
                    MessageTemplateAction(
                        label='台幣買越盾',
                        text='台幣買越盾'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)   
        # 使用Buttons Template (單個)(之二)
    elif event.message.text == "Buttons Template":       
        buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='這是ButtonsTemplate',
            text='ButtonsTemplate可以傳送text,uri',
            thumbnail_image_url='https://thumbs2.imgbox.com/ad/2e/NahWaebN_t.gif',
            actions=[
                MessageTemplateAction(
                    label='ButtonsTemplate',
                    text='ButtonsTemplate'
                ),
                URITemplateAction(
                    label='VIDEO1',
                    uri='http://sendvid.com/pkdn0s4w'
                ),
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='postback1'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        # 使用Carousel template (多個Buttons Template)
    elif event.message.text == "Carousel template":
        print("Carousel template")       
        Carousel_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://thumbs2.imgbox.com/ad/2e/NahWaebN_t.gif',
                title='this is menu1',
                text='description1',
                actions=[
                    PostbackTemplateAction(
                        label='postback1',
                        # text='postback text1',
                        # data='action=buy&itemid=1'
                        data='ping'
                    ),
                    MessageTemplateAction(
                        label='message1',
                        text='message text1'
                    ),
                    URITemplateAction(
                        label='uri1',
                        uri='http://103.29.68.198/'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://images2.imgbox.com/fe/11/6JobQjTm_o.jpg',
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackTemplateAction(
                        label='postback2',
                        text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageTemplateAction(
                        label='message2',
                        text='message text2'
                    ),
                    URITemplateAction(
                        label='連結2',
                        uri='http://sendvid.com/pkdn0s4w'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://thumbs2.imgbox.com/2e/1c/AP41ETSA_t.jpg',
                title='this is menu3',
                text='description3',
                actions=[
                    PostbackTemplateAction(
                        label='postback2',
                        text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageTemplateAction(
                        label='message2',
                        text='message text2'
                    ),
                    URITemplateAction(
                        label='連結2',
                        uri='http://sendvid.com/pkdn0s4w'
                    )
                ]
            )            
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)                  
    else:
        text="userId= \n %s \n message.text=%s \n source.type=%s \n event.timestamp= \n %s" %  (userId,event.message.text,event.source.type,event.timestamp)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text))
