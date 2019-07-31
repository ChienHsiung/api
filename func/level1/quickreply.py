from linebot.models import *

def q_reply(qr_id):
    if qr_id == 1:
        qr = TextSendMessage(
        text='Quick reply',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(action=PostbackAction(label="POST DATA 0", data="data1")),
                QuickReplyButton(action=MessageAction(label="TEXT DATA", text="text2")),
                QuickReplyButton(action=DatetimePickerAction(label="DATE",data="data3",mode="date")),
                QuickReplyButton(action=CameraAction(label="label4")),
                QuickReplyButton(action=CameraRollAction(label="label5")),
                QuickReplyButton(action=LocationAction(label="Location")),
            ]))
    elif qr_id == 2:
        qr = TextSendMessage(
        text='Quick reply',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(action=MessageAction(label="TXT1", text="text1")),
                QuickReplyButton(action=MessageAction(label="TXT2", text="text2")),
                QuickReplyButton(action=MessageAction(label="TXT3", text="text3")),                
            ]))

    return qr  