import socket

Host = ''
port = 50007


def run_serve():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((Host, port))
        s.listen(5)
        conn, addr = s.accept()
        with conn:
            conn_msg = (f"Connected by: {addr}"
                        f"{s.getsockname()}"
                        f"{s.gettimeout()}")
            print(conn_msg)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                else:
                    push_msg = (f"{conn_msg}"
                                f"接收到{data.decode('utf-8')}了")
                    conn.sendall(push_msg.encode('utf-8'))


if __name__ == '__main__':
    run_serve()