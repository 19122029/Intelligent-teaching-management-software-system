import socket

# 服务器主机和端口
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12345

def download_video():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    client_socket.send(b"GET / HTTP/1.1")

    video_data = b""  # 创建一个空的字节串来存储接收的数据

    while True:
        data_chunk = client_socket.recv(1024)
        if not data_chunk:
            break
        video_data += data_chunk

    with open("downloaded_video.mp4", "wb") as video_file:
        video_file.write(video_data)
    print("已下载视频文件")

def upload_video():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    client_socket.send(b"POST / HTTP/1.1")

    with open("../videos/client_video.mp4", "rb") as video_file:
        video_data = video_file.read()
        client_socket.send(video_data)
    print("已上传视频文件")

if __name__ == "__main__":
    # download_video()  # 下载视频示例
    upload_video()    # 上传视频示例
