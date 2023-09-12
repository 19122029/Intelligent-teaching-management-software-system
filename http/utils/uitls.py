import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextBrowser
from PyQt5.QtCore import Qt, QObject, pyqtSignal, pyqtSlot, QThread


class Homework():
    def __init__(self):
        self.contetn = None
        self.conment = ''
        self.goal = int

    # 教师端给作业进行批阅
    def edit(self, goal, conment):
        self.goal = goal
        self.conment = conment

    def change_data(self, data):
        self.contetn = data


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
