from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('bnGwSEddmvOfmAjIF8lzuqirUEUN4PaTBSjgbnyqK7GqIVl0E+7IlVvFtRpdzr8tCUGR4BuIV1yTJoVRKXIzmYZ6AcfMGE4C6jpB+6FK3lcOgDC66lF03UAlFV4j84RVSF91CNCPo6vklWLfce3FMAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f2c4294af930c7fdef3d140e86ef129c')

@app.route("/callback", methods=['POST'])
def callback():
    print("-"*100)
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
        
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 5000,debug = True )