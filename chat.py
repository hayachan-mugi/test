import openai
import os

#chatgptへのアクセス情報を入力
openai.api_key = os.getenv("OPENAI_TOKEN")


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-4o-mini-2024-07-18",  # gpt-4モデルを使用
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens = 300
    )
    return response['choices'][0]['message']['content']





    # ユーザーの入力を会話履歴に追加
    # conversation_history.append({"content": user_input})
    # # conversation_history.append({"role": "user", "content": user_input})
    # # APIリクエストを送信
    # response = openai.ChatCompletion.create(
    #     model="gpt-4o-mini-2024-07-18",  # 使用するモデル
    #     max_tokens=100,
    #     messages=conversation_history
    # )

    # # GPT-4からの返答を取得
    # gpt_reply = response['choices'][0]['message']['content']

    # # GPT-4の返答を会話履歴に追加
    # conversation_history.append({"content": gpt_reply})
    # # conversation_history.append({"role": "assistant", "content": gpt_reply})

    # # GPT-4の返答を返す
    # return gpt_reply
