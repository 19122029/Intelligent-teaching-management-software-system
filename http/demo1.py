import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextBrowser
from PyQt5.QtCore import Qt, QObject, pyqtSignal, pyqtSlot, QThread

class ClientApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('客户端')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.upload_button = QPushButton('上传文件')
        self.upload_button.clicked.connect(self.upload_file)

        self.message_box = QTextBrowser()
        self.message_box.setReadOnly(True)

        layout.addWidget(self.upload_button)
        layout.addWidget(self.message_box)

        self.setLayout(layout)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 8080))  # 连接到服务器

        # 创建一个线程来处理接收消息的任务
        self.message_thread = MessageThread(self.client_socket)
        self.message_thread.message_received.connect(self.handle_message)
        self.message_thread.start()

    def upload_file(self):
        # 在这里添加上传文件的代码
        pass

    def handle_message(self, message):
        # 处理接收到的消息，将其显示在消息框中
        self.message_box.append(message)

class MessageThread(QThread):
    message_received = pyqtSignal(str)

    def __init__(self, socket):
        super().__init__()
        self.socket = socket

    def run(self):
        while True:
            data = self.socket.recv(1024).decode('utf-8')
            if not data:
                break
            self.message_received.emit(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = ClientApp()
    client.show()
    sys.exit(app.exec_())
