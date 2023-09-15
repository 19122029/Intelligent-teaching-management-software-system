import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class TableViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('表格信息查看器')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        self.populateTable()

    def populateTable(self):
        # 在表格中添加数据
        data = [
            ("John", "Doe", "johndoe@email.com"),
            ("Jane", "Smith", "janesmith@email.com"),
            ("John", "Doe", "johndoe@email.com")
            
            # 添加更多的数据行
        ]

        self.table_widget.setColumnCount(3)
        self.table_widget.setRowCount(len(data))
        self.table_widget.setHorizontalHeaderLabels(["First Name", "Last Name", "Email"])

        for row, rowData in enumerate(data):
            for col, val in enumerate(rowData):
                item = QTableWidgetItem(val)
                self.table_widget.setItem(row, col, item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableViewer()
    window.show()
    sys.exit(app.exec_())
