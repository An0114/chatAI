import socket
Host = '127.0.0.1'
port = 50007


def run_client(send_msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((Host, port))
        msg = send_msg
        s.sendall(msg.encode('utf-8'))
        data = s.recv(1024)
        data = data.decode('utf-8')
        print(data)
    return data


if __name__ == '__main__':
    run_client("你好")