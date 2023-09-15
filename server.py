import socket
import os
import threading
import pickle
from utils.uitls import *
# 读取人员信息


# 服务器主机和端口
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12345

# 创建一个套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

# 监听客户端连接
server_socket.listen(5)
print(f"服务器正在监听端口 {SERVER_PORT}...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"接受来自 {client_address} 的连接")

    # 为每个连接创建一个线程,线程内的操作在client_handle中
    client_thread = threading.Thread(target=client_handle, args=(client_socket,client_address))
    client_thread.start()

   