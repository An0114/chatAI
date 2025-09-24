# Please install OpenAI SDK first: `pip3 install openai`
import os
import time
from openai import OpenAI

api_key = os.getenv("DASHSCOPE_DEEPSEEK_API_KEY")
url = "https://api.deepseek.com"
client = OpenAI(api_key=api_key, base_url=url)
message = [{"role": "user", "content": ''}]

def get_message(text):
    message.append({"role": "user", "content": text})
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=message,
        # stream=True
    )
    message.append(response.choices[0].message)
    for char in response.choices[0].message.content:
        if char == "\n":
            print()
        else:
            print(char, end='', flush=True)
            time.sleep(0.05)
    return response.choices[0].message.content

if __name__ == '__main__':
    while 1:
        text = input("请输入：")
        if text == "exit":
            break
        else:
            get_message(text)
            print()