import socket
import time
import traceback

# 客户端
if __name__ == '__main__':
    while True:
        try:
            print('--- ClientSocket Start ---')
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect(('192.168.11.164', 9999))
            while True:
                time.sleep(1)
                # 接收小于 1024 字节的数据
                msg = clientSocket.recv(1024)
                if msg is None:
                    continue
                print('recive - %s' % msg.decode("utf-8"))
        except:
            print(traceback.format_exc())
        finally:
            clientSocket.close()
            time.sleep(5)
