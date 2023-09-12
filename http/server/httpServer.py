import socket
import os
import threading
import pickle


# 服务器主机和端口
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12345

# 创建一个套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

# 监听客户端连接
server_socket.listen(1)
print(f"服务器正在监听端口 {SERVER_PORT}...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"接受来自 {client_address} 的连接")

    # 接收客户端请求
    request = client_socket.recv(1024).decode()

    if request.startswith("GET"):
        # 处理客户端下载视频的请求
        video_filename = "../videos/server_video.mp4"  # 视频文件名
        with open(video_filename, "rb") as video_file:
            video_data = video_file.read()
        client_socket.send(video_data)
        print(f"已向 {client_address} 发送视频文件")
    elif request.startswith("POST_video"):
        # 处理客户端上传视频的请求
        video_data = b""
        print('正在接收文件...')
        while True:
            data_chunk = client_socket.recv(1024)
            if not data_chunk:
                break
            video_data += data_chunk
        
        with open("uploaded_video.mp4", "wb") as uploaded_video:
            uploaded_video.write(video_data)
        print(f"已从 {client_address} 接收上传的视频文件")
    elif request.startswith("POST_homework"):
        # 处理客户端上传视频的请求
        homework_data = b""
        print('正在接收文件POST_homework...')
        while True:
            data_chunk = client_socket.recv(1024)
            if not data_chunk:
                break
            homework_data += data_chunk
        
        homework = pickle.loads(homework_data)
        print(f"已从 {client_address} 接收上传的作业文件")

    client_socket.close()
