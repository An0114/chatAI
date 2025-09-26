import socket
import os
import time
from openai import OpenAI


api_key = os.getenv("DASHSCOPE_DEEPSEEK_API_KEY")
url = "https://api.deepseek.com"
client = OpenAI(api_key=api_key, base_url=url)
messages = [{"role": "user", "content": ''}]
Host = ''
port = 50007

def get_message(text):
    messages.append({"role": "user", "content": text})
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )
    messages.append(response.choices[0].message)
    return response.choices[0].message.content


def run_serve():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((Host, port))
        s.listen(5)
        conn, addr = s.accept()
        print("启动成功")
        with conn:
            conn_msg = (f"Connected by: {addr}"
                        f"{s.getsockname()}"
                        f"{s.gettimeout()}")
            print(conn_msg)
            while True:
                data = conn.recv(1024)
                if not data:
                    print("客户主动断开连接")
                    break
                else:
                    data = data.decode('utf-8', errors='ignore')
                    data = get_message(data)
                    push_msg = (f"An:{data}")
                    conn.sendall(push_msg.encode('utf-8'))


def start_server():
    while True:
        run_serve()


def stop_serve():
    pass


if __name__ == '__main__':
    start_server()
