from PySide6.QtWidgets import QApplication, QWidget, QLineEdit
from calculte import Ui_Form

class MyWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()

        # self.ui = Ui_Form()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()