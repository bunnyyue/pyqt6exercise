from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from calculte import Ui_Form

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()
        self.result = ''

    def bind(self):
        self.pushButton_0.clicked.connect(lambda: self.addNumber('0'))
        self.pushButton_1.clicked.connect(lambda: self.addNumber('1'))
        self.pushButton_2.clicked.connect(lambda: self.addNumber('2'))
        self.pushButton_3.clicked.connect(lambda: self.addNumber('3'))
        self.pushButton_4.clicked.connect(lambda: self.addNumber('4'))
        self.pushButton_5.clicked.connect(lambda: self.addNumber('5'))
        self.pushButton_6.clicked.connect(lambda: self.addNumber('6'))
        self.pushButton_7.clicked.connect(lambda: self.addNumber('7'))
        self.pushButton_8.clicked.connect(lambda: self.addNumber('8'))
        self.pushButton_9.clicked.connect(lambda: self.addNumber('9'))
        self.pushButton_add.clicked.connect(lambda: self.addNumber('+'))
        self.pushButton_sub.clicked.connect(lambda: self.addNumber('-'))
        self.pushButton_mul.clicked.connect(lambda: self.addNumber('*'))
        self.pushButton_div.clicked.connect(lambda: self.addNumber('/'))
        self.pushButton_dot.clicked.connect(lambda: self.addNumber('.'))
        self.pushButton_equal.clicked.connect(self.equal)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_back.clicked.connect(self.clear)

    def addNumber(self, number):
        self.lineEdit.clear()
        self.result += number
        self.lineEdit.setText(self.result)

    def equal(self):
        #感觉这个地方eval的计算方式也是有问题的
        # 并没有按照eval真正的计算方法进行结果输出
        self.numberResult = eval(self.result)
        self.lineEdit.setText(str(self.numberResult))

    def clear(self):
        self.result = ''
        self.lineEdit.clear()
    
    def back(self):
        self.result = self.result[:-1]
        self.lineEdit.setText(self.result)
        #为什么back函数和clear是一个效果啊？



if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()