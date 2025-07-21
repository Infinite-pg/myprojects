# Basic login UI with PyQt5
from PyQt5.QtWidgets import QApplication, QWidget

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')