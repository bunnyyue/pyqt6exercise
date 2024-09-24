import sys
import time
import usb.core
import usb.util
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton

class VoltageMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voltage Monitor")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel("Voltage: ", self)
        self.label.setStyleSheet("font-size: 20px;")
        
        self.start_button = QPushButton("Start Monitoring", self)
        self.start_button.clicked.connect(self.start_monitoring)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.monitoring = False

    def start_monitoring(self):
        if not self.monitoring:
            self.monitoring = True
            self.start_button.setEnabled(False)
            self.monitor_voltage()

    def monitor_voltage(self):
        # 在这里添加读取电压的代码
        while self.monitoring:
            voltage = self.read_voltage_from_device()
            self.label.setText(f"Voltage: {voltage:.2f} V")
            QApplication.processEvents()  # 更新界面
            time.sleep(1)  # 每秒读取一次

    def read_voltage_from_device(self):
        # USB 读取电压的实现
        # 需要根据下位机的具体协议来实现
        dev = usb.core.find(idVendor=0xXXXX, idProduct=0xYYYY)  # 替换为你的设备ID
        if dev is None:
            return 0  # 没有找到设备
        dev.set_configuration()
        
        # 读取数据的具体实现，根据你的下位机协议
        # 这里假设返回的是一个电压值
        # data = dev.read(endpoint, size)
        # voltage = process_data(data)  # 处理数据以获取电压

        return 5.0  # 示例值，替换为实际读取的电压值

    def closeEvent(self, event):
        self.monitoring = False  # 停止监控
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VoltageMonitor()
    window.show()
    sys.exit(app.exec())
