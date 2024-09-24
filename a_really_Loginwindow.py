from PySide6.QtWidgets import QApplication, QWidget, QLineEdit
from login import Ui_Form

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.loginFunc)
        
    def loginFunc(self):
        #拿到账号
        username = self.lineEdit.text()
        #拿到密码
        password = self.lineEdit_2.text()
        #判断账号密码是否正确
        if username == '123' and password == '123456':
            #登录成功
            print('登录成功')
        else:
            #登录失败
            print('登录失败')

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()