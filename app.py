# from flask import Flask, request, abort
# # from linebot import LineBotApi, WebhookHandler
# from linebot.exceptions import InvalidSignatureError
# from linebot.models import MessageEvent, TextMessage, TextSendMessage
# import os
# from dotenv import load_dotenv
# import json
# # from linebot.v3.messaging import MessagingApiClient
# # from linebot.v3.webhook import WebhookHandler
# from linebot.v3.messaging.messaging_api_client import MessagingApiClient
# from linebot.v3.webhook import WebhookHandler

import os
from flask import Flask, request, abort
# from linebot.v3.messaging import MessagingApiClient, Configuration, ApiClient
from linebot.v3.webhook import WebhookHandler
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from linebot.v3.messaging.models import TextMessage

from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
)

# load_dotenv()

app = Flask(__name__)

# ABS_PATH = os.path.dirname(os.path.abspath(__file__))
# with open(ABS_PATH+'/conf.json', 'r') as f:
#     CONF_DATA = json.load(f)

# 環境変数からトークンとシークレットを取得
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

# line_bot_api = MessagingApiClient(channel_access_token=LINE_CHANNEL_ACCESS_TOKEN)
configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
with ApiClient(configuration) as api_client:
    line_bot_api = MessagingApi(api_client)
handler = WebhookHandler(LINE_CHANNEL_SECRET)
# line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
# handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/")
def hello():
    return "Hello, this is a LINE Echo Bot!"

@app.route("/webhook", methods=["POST"])
def webhook():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 入力テキストをそのまま返す
    reply_text = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # RenderでPORTが環境変数で渡される
    app.run(host="0.0.0.0", port=port)

# if __name__ == "__main__":
#     app.run()
    



# import os
# import json
# import chat
# from flask import Flask, request, abort

# from linebot import (
#     LineBotApi, WebhookHandler
# )
# from linebot.exceptions import (
#     InvalidSignatureError
# )
# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage, MessageAction, TemplateSendMessage, CarouselTemplate, CarouselColumn, QuickReplyButton, QuickReply)
# from linebot.models import (
#     RichMenu, RichMenuArea,
#     RichMenuBounds, RichMenuSize, TemplateSendMessage,ButtonsTemplate, PostbackEvent
# )
# from linebot.models.actions import PostbackAction


# app = Flask(__name__)

# # endpoint
# @app.route("/")
# def test():
#     return "<h1>It Works!</h1>"


# ABS_PATH = os.path.dirname(os.path.abspath(__file__))
# with open(ABS_PATH+'/conf.json', 'r') as f:
#     CONF_DATA = json.load(f)

# #LINEへのアクセス情報を入力
# LINE_CHANNEL_ACCESS_TOKEN = CONF_DATA["CHANNEL_ACCESS_TOKEN"]
# LINE_CHANNEL_SECRET = CONF_DATA["CHANNEL_SECRET"]
# # YOUR_USER_ID = "U016a51ebf4f73cbc69cad12a6312fd2d"

# line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
# handler = WebhookHandler(LINE_CHANNEL_SECRET)






# #ルーティングの設定、POSTリクエストが来たらcallback関数を返す
# @app.route("/callback", methods=['POST'])
# def callback():
#     # リクエストヘッダーからアクセス情報の検証のための値を取得
#     signature = request.headers['X-Line-Signature']

#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)
#     # アクセス情報を検証し、成功であればhandleの関数を呼び出す
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)

#     return 'OK'










# #メッセージを受け取った後にどんな処理を行うかを記述
# @handler.add(MessageEvent, message=TextMessage)
# def response_message(event):
#     global mame_text, message
#     if event.message.text == '豆知識🫛':
        
#         language_list = ["bees","うどん","かんぱち","香川県","そば","はまち","愛知県","野洲","韓国","k-pop","そうめん","チャットGPT","バッタ"]

#         items = [QuickReplyButton(action=MessageAction(label=f"{language}", text=f"Please tell me one trivia about {language}!")) for language in language_list]
#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text="↓知りたい豆知識を一つ選択してください", quick_reply=QuickReply(items=items)))

#     elif event.message.text == 'シチュエーション🛫':
        
#         language_list = ["旅行","道案内","お会計","空港","スーパーマーケット","貿易","魚市場","カフェ"]

#         items = [QuickReplyButton(action=MessageAction(label=f"{language}", text=f"Let's have a conversation in English about {language} situation!")) for language in language_list]
#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text="↓どのシチュエーションにしますか？", quick_reply=QuickReply(items=items)))


#     elif event.message.text == '英作文👦':
        
#         language_list = ["旅行","道案内","お会計","空港","スーパーマーケット","貿易","魚市場","カフェ"]

#         items = [QuickReplyButton(action=MessageAction(label=f"{language}", text=f"Please create one writing prompt in English about {language} situation!")) for language in language_list]
#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text="↓どのシチュエーションにしますか？", quick_reply=QuickReply(items=items)))


#     elif event.message.text == '相談🤫':
        
#         language_list = ["仕事","友人関係","将来","お金"]

#         items = [QuickReplyButton(action=MessageAction(label=f"{language}", text=f"I would like to consult about {language} in English.")) for language in language_list]
#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text="↓相談内容を選択ください", quick_reply=QuickReply(items=items)))


#     elif event.message.text == '勉強📚':
        
#         language_list = ["be動詞","5w1h","文法"]

#         items = [QuickReplyButton(action=MessageAction(label=f"{language}", text=f"英語の{language}に関して教えてください！")) for language in language_list]
#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text="↓どれを学習しますか？", quick_reply=QuickReply(items=items)))


#     elif event.message.text == 'AIモード💻':
        
#         language_list = ["蜂","うどん","かんぱち","香川県","そば","はまち","愛知県","野洲","韓国","k-pop","そうめん","iphone16","バッタ"]

#         items = [QuickReplyButton(action=MessageAction(label=f"{language}", text=f"{language}の豆知識を一つ教えてください！")) for language in language_list]
#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text="↓から知りたい豆知識を一つ選択してください！", quick_reply=QuickReply(items=items)))
        


#     # elif "😃" in event.message.text:
#     #     line_bot_api.reply_message(
#     #         event.reply_token,
#     #         TextSendMessage(text=chat.chat_with_gpt_unlimited(event.message.text)))


#     else:
#         # message = event.message.text
#         # mame_text = chat.chat_with_gpt_unlimited(message)
#         # language_list = ["日本語訳","送信した文章を添削"]
#         # items = [
#         #     QuickReplyButton(
#         #     action=PostbackAction(label=language_list[0], data="action=buy&itemid=123", displayText=language_list[0])),
            
#         #     QuickReplyButton(
#         #     action=PostbackAction(label=language_list[1],
#         #                           data="action=sell&itemid=456", displayText=language_list[1]))]
        
#         # line_bot_api.reply_message(
#         #     event.reply_token,
#         #     TextSendMessage(text=mame_text, quick_reply=QuickReply(items=items)))

#         message = event.message.text
#         mame_text = chat.chat_with_gpt(message)
#         language_list = ["日本語訳","送信した文章を添削"]
#         buttons_template_message = TemplateSendMessage(
#             alt_text='Buttons template',
#             template=ButtonsTemplate(
#                 # title='Menu',
#                 text=mame_text,
#                 actions=[
#                     PostbackAction(
#                         label=language_list[0],
#                         display_text=language_list[0],
#                         # data='action=buy&itemid=1'
#                         data=mame_text
#                     ),
#                     PostbackAction(
#                         label=language_list[1],
#                         display_text=language_list[1],
#                         # data='action=buy&itemid=1'
#                         data=message
#                     )
#                 ]
#             )
#         ) 
#         # line_bot_api.reply_message(
#         #     event.reply_token,
#         #     TextSendMessage(text=mame_text))
#         line_bot_api.reply_message(
#             event.reply_token,
#             messages=buttons_template_message)

# # Postbackイベントを処理する関数
# @handler.add(PostbackEvent)
# def handle_postback(event):
#     # 選択に基づいてメッセージを返信
#     label = event.postback.label  # ユーザーが選んだオプションのデータを取得
#     data = event.postback.data
#     if "日本語訳" in label:
#         rep_mame_text = data + " を日本語訳してください"
#         response_text = chat.chat_with_gpt_unlimited(rep_mame_text)
#     else:
#         rep_mame_text = data + " この文章を日本語で添削してください"
#         response_text = chat.chat_with_gpt_unlimited(rep_mame_text)
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=response_text)
#     )



# # Postbackイベントを処理する関数
# # @handler.add(PostbackEvent)
# # def handle_postback(event):
# #     global mame_text, message
# #     # 選択に基づいてメッセージを返信
# #     data = event.postback.data  # ユーザーが選んだオプションのデータを取得
# #     if "action=buy" in data:
# #         rep_mame_text = mame_text + " を日本語訳してください"
# #         response_text = chat.chat_with_gpt_unlimited(rep_mame_text)
# #     else:
# #         rep_mame_text = message + " この文章を日本語で添削してください"
# #         response_text = chat.chat_with_gpt_unlimited(rep_mame_text)
# #     line_bot_api.reply_message(
# #         event.reply_token,
# #         TextSendMessage(text=response_text)
# #     )
# #     mame_text =""
# #     message =""




# # アプリケーションの起動
# if __name__ == "__main__":
#     app.run(debug=True)


# if __name__ == "__main__":
#     port = int(os.getenv("PORT", 5000))
#     app.run(host="0.0.0.0", port=port)













# # from linebot import LineBotApi, WebhookHandler
# # from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackAction, QuickReply, QuickReplyButton, PostbackEvent
# # from flask import Flask, request, abort

# # # Flaskアプリケーションの設定
# # app = Flask(__name__)

# # # LINE Messaging APIのアクセストークンとシークレット
# # line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
# # handler = WebhookHandler('YOUR_CHANNEL_SECRET')

# # # LINEのWebhookエンドポイント
# # @app.route("/callback", methods=['POST'])
# # def callback():
# #     signature = request.headers['X-Line-Signature']
# #     body = request.get_data(as_text=True)
# #     try:
# #         handler.handle(body, signature)
# #     except InvalidSignatureError:
# #         abort(400)
# #     return 'OK'

# # # メッセージイベントを処理する関数
# # @handler.add(MessageEvent, message=TextMessage)
# # def handle_message(event):
# #     # クイックリプライボタンを作成
# #     quick_reply_buttons = QuickReply(
# #         items=[
# #             QuickReplyButton(
# #                 action=PostbackAction(label="Option 1", data="action=buy&itemid=123", displayText="You selected Option 1")
# #             ),
# #             QuickReplyButton(
# #                 action=PostbackAction(label="Option 2", data="action=sell&itemid=456", displayText="You selected Option 2")
# #             )
# #         ]
# #     )

# #     # クイックリプライを付けたメッセージを返信
# #     line_bot_api.reply_message(
# #         event.reply_token,
# #         TextSendMessage(
# #             text="Choose an option:",
# #             quick_reply=quick_reply_buttons
# #         )
# #     )

# # # Postbackイベントを処理する関数
# # @handler.add(PostbackEvent)
# # def handle_postback(event):
# #     data = event.postback.data  # ユーザーが選んだオプションのデータを取得
# #     if "action=buy" in data:
# #         response_text = "You have selected to buy item."
# #     elif "action=sell" in data:
# #         response_text = "You have selected to sell item."
# #     else:
# #         response_text = "Unknown action."

# #     # 選択に基づいてメッセージを返信
# #     line_bot_api.reply_message(
# #         event.reply_token,
# #         TextSendMessage(text=response_text)
# #     )

# # # アプリケーションの起動
# # if __name__ == "__main__":
# #     app.run(debug=True)







#         # buttons_template_message = TemplateSendMessage(
#         #     alt_text='Buttons template',
#         #     template=ButtonsTemplate(
#         #     # title='Menu',
#         #         text="上の文章",
#         #         actions=[

#         #             MessageAction(
#         #                 label='日本語訳',  # ボタンに表示されるテキスト
#         #                 text=rep_mame_text       # ユーザーが押したときに送信されるメッセージ
#         #             ),
#         #             MessageAction(
#         #                 label='一つ前の文章を添削',  # ボタンに表示されるテキスト
#         #                 text=rep2_text       # ユーザーが押したときに送信されるメッセージ
#         #             )
                    
#         #             # PostbackAction(
#         #             #     label='日本語訳',
#         #             #     display_text = rep_mame_text,
#         #             #     # data='action=buy&itemid=1'
#         #             #     data="英訳してください"
#         #             # )
#         #         ]
#         #     )
#         # )    
#         # line_bot_api.reply_message(
#         #     event.reply_token,
#         #     TextSendMessage(text=chat.chat_with_gpt_unlimited(event.message.text)))
        
#         # line_bot_api.reply_message(
#         #     event.reply_token,
#         #     messages=buttons_template_message)
        

#     # messages = TextSendMessage(text="どの言語が好きですか？",
#     #                            quick_reply=QuickReply(items=items))

#     # line_bot_api.reply_message(event.reply_token, messages=messages)

# # buttons_template_message = TemplateSendMessage(
# #     alt_text='Buttons template',
# #     template=ButtonsTemplate(
# #         # title='Menu',
# #         text='Please select',
# #         actions=[
# #             PostbackAction(
# #                 label='postback',
# #                 display_text='postback text',
# #                 # data='action=buy&itemid=1'
# #                 data='ああ'
# #             )
# #         ]
# #     )
# # )    






# # @handler.add(PostbackEvent)
# # def handle_postback(event):
# #     postback_data = event.postback.data
# #     # if postback_data == 'no':
# #     #     text_message = 'かしこまりました'
# #     # else:

# #         # user_id = event.source.user_id
# #         # register_mycity(user_id, postback_data)
# #         # text_message = '登録しました'
# #     line_bot_api.reply_message(
# #         event.reply_token,
# #         TextSendMessage(text=postback_data))



# # buttons_template_message = TemplateSendMessage(
# #     alt_text='Buttons template',
# #     template=ButtonsTemplate(
# #         # title='Menu',
# #         text='Please select',
# #         actions=[
# #             PostbackAction(
# #                 label='postback',
# #                 display_text='postback text',
# #                 # data='action=buy&itemid=1'
# #                 data='ああ'
# #             )
# #         ]
# #     )
# # )    
# # line_bot_api.push_message(YOUR_USER_ID, buttons_template_message)


# # @handler.add(MessageEvent, message=TextMessage)
# # def handle_message(event):
# #     line_bot_api.reply_message(
# #         event.reply_token,
# #         TextSendMessage(text=chat.chat_with_gpt(event.message.text)))


