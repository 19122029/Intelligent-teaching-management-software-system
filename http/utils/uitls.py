import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextBrowser
from PyQt5.QtCore import Qt, QObject, pyqtSignal, pyqtSlot, QThread
import os
import threading
import pickle
import pandas as pd


class Homework():
    def __init__(self):
        self.content = b""
        self.comment = ''
        self.goal = int

    # 教师端给作业进行批阅
    def edit(self, goal, comment):
        self.goal = goal
        self.comment = comment

    def change_data(self, data):
        self.content = data


class TeacherListening(QThread):
    """
    教师端监听线程
    """
    def __init__(self, socket):
        self.socket = socket

    def run(self):
        data = self.socket.recv(1024)

def listening(socket):
    pass

def client_handle(client_socket,client_address):

    """
        这里是服务器为单个客户端开辟的线程

    """
    
    while True:
        # 接收客户端请求
        request = client_socket.recv(1024).decode()
        # print(f"收到数据{request}")
        if request.startswith("STUDENT_GET_VIDEO"):
            # 处理客户端下载视频的请求
            video_filename = "datas/videos/uploaded_video.mp4"  # 视频文件名
            with open(video_filename, "rb") as video_file:
                video_data = video_file.read()
                video_data = video_data + b"EOF"
            client_socket.send(video_data)
            print(f"已向 {client_address} 发送视频文件")
        elif request.startswith("TEACHER_POST_VIDEO"):
            # 处理客户端上传视频的请求
            video_data = b""
            print('指令TEACHER_POST_VIDEO正在接收文件...')
            while True:
                data_chunk = client_socket.recv(1024)
                video_data += data_chunk
                if   b"EOF" in data_chunk:
                    break
            video_data = video_data[:-3]

            with open("datas/videos/uploaded_video.mp4", "wb") as uploaded_video:
                uploaded_video.write(video_data)
            print(f"已从 {client_address} 接收上传的视频文件")
        elif request.startswith("STUDENT_POST_HOMEWORK"):
            # 处理客户端上传视频的请求
            homework_data = b""
            print('指令STUDENT_POST_HOMEWORK正在接收文件...')
            while True:
                data_chunk = client_socket.recv(1024)
                homework_data += data_chunk
                if   b"EOF" in data_chunk:
                    break
            # homework_data = homework_data[:-3]
            # homework = pickle.loads(homework_data)
            with open("datas/homeworks/uploaded_homework.bin", "wb") as upload_homework:
                upload_homework.write(homework_data)
            print(f"已从 {client_address} 接收上传的作业文件")
        elif request.startswith("TEACHER_GET_HOMEWORK"):
            # 处理教师客户端请求下载作业的请求
            print("TEACHER_GET_HOMEWORK,给教师发送作业文件")
            homework_file_dir = "datas/homeworks/uploaded_homework.bin"
            with open(homework_file_dir,"rb") as file:
                homework_data = file.read()
                client_socket.send(homework_data)
            print("发送数据完成")
        elif request.startswith("TEACHER_POST_HOMEWORK_READ"):
            # 处理教师端批阅后上传的作业数据
            homework_file_dir = "datas/homeworks_read/homework_read.bin"
            print("指令TEACHER_POST_HOMEWORK_READ，接收教师端上传的批阅后作业")
            homework_data = b""
            while True:
                data_chunk = client_socket.recv(1024)
                homework_data += data_chunk
                if b"EOF" in data_chunk:
                    break
            with open(homework_file_dir,"wb") as file:
                file.write(homework_data)
            print("批阅后的作业保存成功")
        elif request.startswith("STUDENT_GET_HOMEWORK_READ"):
            # 处理学生端请求下载批阅后的作业
            homework_file_dir = "datas/homeworks_read/homework_read.bin"
            print("指令STUDENT_GET_HOMEWORK_READ")
            with open(homework_file_dir,'rb') as file:
                homework_data = file.read()
            client_socket.send(homework_data)
            print("发送数据完成")
        elif request.startswith("LOGIN_REQUEST_PERSONAL_INFO"):
            # 处理登陆界面请求人员信息的请求
            personal_info_dir = "datas/personal_infor/edit.xlsx"
            with open(personal_info_dir,"rb") as file:
                file_data = file.read()
            file_data += b"EOF"
            client_socket.send(file_data)
            print("persaonal_info已发送")
        
        elif request.startswith("AIMI_POST_EDITED_PERSONAL_INFO"):
            # 处理客户端上传的修改后的人员信息
            personal_info_file_dir = "datas/personal_infor/edit1.xlsx"
            print("指令AIMI_POST_EDITED_PERSONAL_INFO，接收管理员端上传的修改后的人员信息")
            info_data = b""
            while True:
                data_chunk = client_socket.recv(1024)
                info_data += data_chunk
                if b"EOF" in data_chunk:
                    break
            info_data = info_data[:-3]
            info_df = pickle.loads(info_data)
            info_df.to_excel(personal_info_file_dir)
    # client_socket.close()


def change_peraonal_info():
    pass

