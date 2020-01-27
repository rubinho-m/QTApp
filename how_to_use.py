from PyQt5.QtWidgets import QMainWindow
from for_how_to_use import Ui_MainWindow_2


class ThirdForm(QMainWindow, Ui_MainWindow_2):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
