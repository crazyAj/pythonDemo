import socket
import time
import _thread
import traceback

dic = {}


# 建立客户端连接
def run():
    print('--- ServerSocket Start ---')
    # 创建 socket 对象
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定 ip、port
    serverSocket.bind(('192.168.11.164', 9999))
    # 设置最大连接数，超过后排队
    serverSocket.listen(5)
    while True:
        # 建立客户端连接
        conn, address = serverSocket.accept()
        # 缓存连接
        dic[address] = conn


def send():
    while True:
        print(dic)
        temp = dic.copy()
        for key in temp.keys():
            try:
                msg = "[%s] hello %s" % (time.ctime(time.time()), key)
                temp[key].send(msg.encode('utf-8'))
            except:
                dic.pop(key)
                print(traceback.format_exc())
        time.sleep(5)


# 服务端
if __name__ == '__main__':
    t1 = _thread.start_new_thread(run, ())
    t2 = _thread.start_new_thread(send, ())
    while True:
        time.sleep(10)
