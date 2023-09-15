import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt StackedWidget Example')
        self.setGeometry(100, 100, 800, 600)

        # 创建主页面
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.stacked_widget = QStackedWidget(self.central_widget)

        # 创建按钮，点击按钮切换到新页面
        self.button = QPushButton('Show Table Page', self.central_widget)
        self.button.clicked.connect(self.showTablePage)
        self.layout.addWidget(self.button)

        # 创建表格页面
        self.table_page = QWidget(self)
        table_layout = QVBoxLayout(self.table_page)
        self.table_widget = QTableWidget(self.table_page)
        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])

        for row in range(5):
            for col in range(3):
                item = QTableWidgetItem(f'Row {row}, Col {col}')
                self.table_widget.setItem(row, col, item)

        table_layout.addWidget(self.table_widget)
        self.stacked_widget.addWidget(self.central_widget)  # 主页面
        self.stacked_widget.addWidget(self.table_page)  # 表格页面

        self.layout.addWidget(self.stacked_widget)

    def showTablePage(self):
        # 切换到表格页面
        self.stacked_widget.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
