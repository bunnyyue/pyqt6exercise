import sys
import pandas as pd
import serial
import time
from PyQt6 import QtWidgets, QtCore

class DataMonitor(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # 初始化用户界面
        self.timer = QtCore.QTimer()  # 创建定时器
        self.timer.timeout.connect(self.read_data)  # 连接定时器超时信号到读取数据的方法
        self.timer.start(1000)  # 每秒读取数据

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle("数据监控")
        self.setGeometry(100, 100, 800, 600)

        # 创建表格用于显示数据
        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(3)  # 设置列数
        self.table.setHorizontalHeaderLabels(["通道", "电压", "功率"])  # 设置表头

        # 创建布局
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.table)  # 添加表格到布局

        # 创建导出数据按钮
        self.export_button = QtWidgets.QPushButton("导出数据", self)
        self.export_button.clicked.connect(self.export_data)  # 连接按钮点击事件到导出方法
        self.layout.addWidget(self.export_button)

        self.setLayout(self.layout)  # 设置主布局

        # 初始化串口连接（根据实际情况修改端口和波特率）
        self.serial_port = serial.Serial('COM3', 9600, timeout=1)

    def read_data(self):
        # 发送指令AAA给下位机
        self.serial_port.write(b'AAA')
        response = self.serial_port.readline().decode('utf-8').strip()  # 读取下位机返回的数据并解码
        if response:
            self.update_table(response)  # 更新表格

    def update_table(self, data):
        # 假设返回数据格式为"通道,电压,功率"
        channel, voltage, power = map(float, data.split(','))  # 解析返回的数据
        row_position = self.table.rowCount()  # 获取当前行数
        self.table.insertRow(row_position)  # 插入新行
        # 将数据填入表格
        self.table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(channel)))
        self.table.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(voltage)))
        self.table.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(power)))

    def export_data(self):
        # 打开文件对话框以选择保存位置和文件名
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "导出数据", "", "Excel Files (*.xlsx);;CSV Files (*.csv);;DAT Files (*.dat)", options=options)
        if file_name:
            self.save_to_file(file_name)  # 调用保存文件的方法

    def save_to_file(self, file_name):
        data = []
        # 遍历表格数据并将其保存到列表中
        for row in range(self.table.rowCount()):
            row_data = []
            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)  # 获取单元格内容
                row_data.append(item.text() if item else "")  # 添加到行数据
            data.append(row_data)  # 添加行数据到总数据
        
        # 创建DataFrame以便于导出
        df = pd.DataFrame(data, columns=["通道", "电压", "功率"])
        # 根据文件扩展名选择导出格式
        if file_name.endswith('.xlsx'):
            df.to_excel(file_name, index=False)  # 导出为Excel
        elif file_name.endswith('.csv'):
            df.to_csv(file_name, index=False)  # 导出为CSV
        elif file_name.endswith('.dat'):
            df.to_csv(file_name, index=False, sep='\t')  # 导出为DAT，使用制表符分隔

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建应用程序实例
    monitor = DataMonitor()  # 创建数据监控实例
    monitor.show()  # 显示窗口
    sys.exit(app.exec())  # 启动事件循环
