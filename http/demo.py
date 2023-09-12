import pickle
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QMessageBox,QFileDialog
from PyQt5.QtCore import QThread
import socket
from utils.uitls import *
import threading
# 服务器主机和端口
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12345

# 创建客户端套接字以连接服务器
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 客户端尝试连接服务器
        try:
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            print("连接成功")
        except ConnectionRefusedError:
            print("连接被拒绝")
        except socket.timeout:
            print("连接超时")
        except Exception as e:
            print(f"连接错误: {e}")


        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 400, 150)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.account_label = QLabel("Enter Account:")
        self.account_input = QLineEdit()
        self.login_button = QPushButton("Login")

        self.login_button.clicked.connect(self.login)

        self.layout.addWidget(self.account_label)
        self.layout.addWidget(self.account_input)
        self.layout.addWidget(self.login_button)

        self.central_widget.setLayout(self.layout)

    def login(self):
        account = self.account_input.text().strip()
        if account.startswith("t"):
            self.openSubpage1()
        elif account.startswith("s"):
            self.openSubpage2()
        else:
            QMessageBox.warning(self.central_widget, 'warning', 'Please input right id!')
            self.account_input.clear()

    def openSubpage1(self):
        subpage1 = Subpage1()
        self.setCentralWidget(subpage1)

    def openSubpage2(self):
        subpage2 = Subpage2()
        self.setCentralWidget(subpage2)

class Subpage1(QWidget):
    """
    教师客户端，需要实时监听服务器传来的消息
    """
    def __init__(self):
        super().__init__()
        # 页面布局
        self.setWindowTitle("Subpage 1")
        self.setGeometry(100, 100, 400, 150)
        label = QLabel("Welcome to Subpage 1!")
        self.btn_upload_Video = QPushButton("点击上传视频")
        self.layout = QVBoxLayout()
        self.layout.addWidget(label)
        self.layout.addWidget(self.btn_upload_Video)


        self.setLayout(self.layout)

        # 槽函数
        self.btn_upload_Video.clicked.connect(self.upload_video)
        # 其他属性
        # self.lisening_thread = QThread()

    def receive_homeworks(self):
        pass

    def eidt_and_upload_homework(self):
        pass

    def upload_video(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", "",
                                                   "All Files (*);;Text Files (*.txt);;Image Files (*.png *.jpg)",
                                                   options=options)
        if file_name:
            client_socket.send(b"POST_VIDEO / HTTP/1.1")
            with open(file_name, "rb") as video_file:
                video_data = video_file.read()
                video_data = video_data + b"EOF" # 给数据流加上结束标志，以与接收端协议何时结束
                client_socket.send(video_data)
            print("已上传视频文件")


class Subpage2(QWidget):
    def __init__(self):
        super().__init__()
        # 页面布局
        self.setWindowTitle("Subpage 2")
        self.setGeometry(100, 100, 400, 150)
        self.btn_upload = QPushButton('upload homework')
        label = QLabel("Welcome to Subpage 2!")
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.btn_upload)
        self.setLayout(layout)

        # 槽函数
        self.btn_upload.clicked.connect(self.upload_homework)

        # 其他属性
        self.homework = Homework() #------------------bug

    def upload_homework(self):
        # 选择作业文件
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", "",
                                                   "All Files (*);;Text Files (*.txt);;Image Files (*.png *.jpg)",
                                                   options=options)
        # 读取作业文件为数据流，便于封装为类
        with open(file_name, 'rb') as homework_file:
            homework_data = homework_file.read()
            self.homework.change_data(homework_data)
        # 将作业对象绑定作业数据流,并将作业对象化为字节流，便于传输

        homework_data = pickle.dumps(self.homework)

        if file_name:
            client_socket.send(b"POST_homework / HTTP/1.1")
            client_socket.send(homework_data)
            QMessageBox.information(self, "information", f"上传作业：{file_name}")


    def download_vedios(self):
        pass



def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
