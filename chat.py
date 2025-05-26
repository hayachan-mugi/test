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
