import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow
from for_fav import Ui_MainWindow_1
from PyQt5.QtCore import Qt

class SecondForm(QMainWindow, Ui_MainWindow_1):
    def __init__(self, *args):
        try:
            super().__init__()
            self.setupUi(self)
            self.num = 0
            self.NAME_OF_DB = 'arguments.db'
            self.next_fav.clicked.connect(self.go_next_fav)
            self.dont_show_fav.clicked.connect(self.remove_from_db_fav)
            con = sqlite3.connect(self.NAME_OF_DB)
            cur = con.cursor()
            self.all = cur.execute("""SELECT * FROM favs""").fetchall()
            self.result = self.all[self.num][2]
            self.title = self.all[self.num][1]
            self.author = self.all[self.num][0]
            self.textBrowser_fav.setText(
                self.result)
            self.title_array = []
            self.title_array.append(self.author)
            self.title_array.append(self.title)
            out = ' - '.join(self.title_array)
            self.name_of_book_fav.setText(out)
            self.name_of_book_fav.adjustSize()
            con.close()
        except Exception as e:
            pass

    def keyPressEvent(self, event):
        if int(event.key()) == int(Qt.Key_Enter) or int(event.key()) + 1 == int(Qt.Key_Enter):
            self.go_next_fav()
        if event.key() == int(Qt.Key_Delete):
            self.remove_from_db_fav()

    def go_next_fav(self):
        try:
            self.num += 1
            self.result = self.all[self.num % len(self.all)][2]
            self.title = self.all[self.num % len(self.all)][1]
            self.author = self.all[self.num % len(self.all)][0]
            self.textBrowser_fav.setText(
                self.result)
            self.title_array = []
            self.title_array.append(self.author)
            self.title_array.append(self.title)
            out = ' - '.join(self.title_array)
            self.name_of_book_fav.setText(out)
            self.name_of_book_fav.adjustSize()
        except Exception as e:
            pass

    def remove_from_db_fav(self):
        try:
            con = sqlite3.connect(self.NAME_OF_DB)
            cur = con.cursor()
            cur.execute("""DELETE from favs where Arg = ?""", (self.result,))
            con.commit()
            self.all.remove(self.all[self.num % len(self.all)])
            if len(self.all) == 0:
                self.name_of_book_fav.setText('')
                self.name_of_book_fav.adjustSize()
                self.textBrowser_fav.setText('Аргументы кончились')
            else:
                self.go_next_fav()
            con.close()
        except Exception as e:
            pass
