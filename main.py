import os

from linebot import (
        LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError        
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage        
)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

def callback(event, context):
    signature = event['headers']['X-Line-Signature']
    body = event['body'] 
    print("Request body:" + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))

