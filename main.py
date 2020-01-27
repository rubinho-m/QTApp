import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog

from for_args_bank import Ui_MainWindow
from PyQt5.QtCore import Qt
from fav import SecondForm
from how_to_use import ThirdForm


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.change_problem.clicked.connect(self.select_problem)
        self.next.clicked.connect(self.go_next)
        self.sort_button.clicked.connect(self.select_sort)
        self.dont_show.clicked.connect(self.remove_from_db)
        self.favourite.clicked.connect(self.show_fav)
        self.how_to_use.clicked.connect(self.show_how_to_use)
        self.like.stateChanged.connect(self._on_radio_button_clicked)
        self.like.setVisible(False)
        self.all = []
        self.NAME_OF_DB = 'arguments.db'
        self.ALL_PROBLEMS = ["ПРОБЛЕМА СТОЙКОСТИ И МУЖЕСТВА РУССКОЙ АРМИИ ВО ВРЕМЯ ВОЕННЫХ ИСПЫТАНИЙ",
                             "ПРОБЛЕМА НЕЖНОСТИ",
                             "ПРОБЛЕМА СОХРАНЕНИЯ ЧЕСТИ",
                             "ПРОБЛЕМА ПРЕДАННОЙ ЛЮБВИ",
                             "ПРОБЛЕМА РАСКАЯНИЯ",
                             "ПРОБЛЕМА ПОИСКА СМЫСЛА ЖИЗНИ В СОВРЕМЕННОМ МИРЕ",
                             "ПРОБЛЕМА ЛИТЕРАТУРНОЙ БЕЗГРАМОТНОСТИ И НИЗКОГО УРОВНЯ ОБРАЗОВАННОСТИ СРЕДИ МОЛОДЁЖИ",
                             "ПРОБЛЕМА ВОСПИТАНИЯ ДЕТЕЙ",
                             "ПРОБЛЕМА РОЛИ ПРОФЕССИОНАЛИЗМА",
                             "ПРОБЛЕМА СОЛДАТСКОЙ СУДЬБЫ НА ВОЙНЕ",
                             "ПРОБЛЕМА ЭГОИЗМА ВЛЮБЛЕННОГО ЧЕЛОВЕКА",
                             "ПРОБЛЕМА ПРЕДАТЕЛЬСТВА",
                             "ПРОБЛЕМА ОБМАНЧИВОСТИ ВНЕШНЕГО ВИДА",
                             "ПРОБЛЕМА ПРЕДАТЕЛЬСТВА НА ВОЙНЕ",
                             "ПРОБЛЕМА ВЛИЯНИЯ ЛЮБВИ К РОДИНЕ НА ТВОРЧЕСТВО",
                             "ПРОБЛЕМА ВЛИЯНИЯ ДЕТСКИХ ВОСПОМИНАНИЙ НА ЖИЗНЬ ЧЕЛОВЕКА",
                             "ПРОБЛЕМА ВЫБОРА ЖИЗЕННОГО ПУТИ",
                             "ПРОБЛЕМА СОБАЧЬЕЙ ПРЕДАННОСТИ",
                             "ПРОБЛЕМА МАСТЕРСТВА В ИСКУССТВЕ",
                             "ПРОБЛЕМА ЗНАЧИМОСТИ ЖИЗНЕННОГО ОПЫТА ДЛЯ ПИСАТЕЛЕЙ",
                             "ПРОБЛЕМА ВЛИЯНИЯ МУЗЫКИ НА ДУШЕВНОЕ СОСТОЯНИЕ ЧЕЛОВЕКА",
                             "ПРОБЛЕМА МАТЕРИНСКОЙ ЛЮБВИ",
                             "ПРОБЛЕМА ВОЗДЕЙСТВИЯ ПРОИЗВЕДЕНИЙ ИСКУССТВА О ВОЙНЕ НА ЧЕЛОВЕКА",
                             "ПРОБЛЕМА ЛЖЕНАУКИ",
                             "ПРОБЛЕМА ПОЗДНЕГО РАСКАЯНИЯ",
                             "ПРОБЛЕМА ИСТОРИЧЕСКОЙ ПАМЯТИ",
                             "ПРОБЛЕМА ЖИЗНЕННОГО ПУТИ ОДАРЕННОГО ЧЕЛОВЕКА",
                             "ПРОБЛЕМА РАЗРУШИТЕЛЬНЫХ ПОСЛЕДСТВИЙ ВОЙНЫ",
                             "ПРОБЛЕМА ПРОТИВОРЕЧИВОСТИ ВНУТРЕННЕГО МИРА ЧЕЛОВЕКА",
                             "ПРОБЛЕМА СПРАВЕДЛИВОГО ОТНОШЕНИЯ К ЛЮДЯМ",
                             "ПРОБЛЕМА ВЗАИМОСВЯЗИ ЧЕЛОВЕКА И ПРИРОДЫ",
                             "ПРОБЛЕМА РОЛИ МУЗЫКИ В ЖИЗНИ ЧЕЛОВЕКА",
                             "ПРОБЛЕМА ВЫТЕСНЕНИЯ КНИГ ТЕЛЕВИДЕНИЕМ",
                             "ПРОБЛЕМА РУССКОЙ ДЕРЕВНИ",
                             "ПРОБЛЕМА ОТНОШЕНИЯ К ПОЭТАМ И ИХ ТВОРЧЕСТВУ",
                             "ПРОБЛЕМА ВЛИЯНИЯ УЧИТЕЛЯ НА УЧЕНИКОВ",
                             "ПРОБЛЕМА ОТНОШЕНИЯ К ДЕТЯМ-СИРОТАМ",
                             "ПРОБЛЕМА РОЛИ ЖЕНЩИНЫ В ВОВ",
                             "ПРОБЛЕМА ИЗМЕНЕНИЙ В РУССКОМ ЯЗЫКЕ",
                             "ПРОБЛЕМА ВЫБОРА ПРОФЕССИИ"]
        self.ALL_BOOKS = [
            "Война и Мир",
            "А зори здесь тихие",
            "Джен Эйр",
            "Капитанская дочка",
            "Тарас Бульба",
            "Мастер и Маргарита",
            "Преступление и наказание",
            "Господин из Сан-Франциско",
            "В письмах о добром и прекрасном",
            "451 градус по Фаренгейту",
            "Обломов",
            "Летят мои кони...",
            "Слепой музыкант",
            "Сотников",
            "Парфюмер. История одного убийцы",
            "Два капитана",
            "Живи и помни",
            "Собор Парижской Богоматери",
            "Разбуженный соловьями",
            "Мой путь",
            "Белый Бим Черное Ухо",
            "Лесси",
            "Тапёр",
            "Доктор Живаго"
            "Мартин Иден",
            "Гранатовый браслет",
            "Великое противостояние",
            "Белые одежды",
            "Кандидат наук",
            "Телеграмма",
            "Вечное поле",
            "Моцарт и Сальери",
            "Матренин двор",
            "Судьба человека",
            "Отцы и дети",
            "Хамелеон",
            "Царь-рыба",
            "Олеся",
            "Тихий Дон",
            "Прощание с Матерой",
            "Поэт и толпа",
            "Во весь голос",
            "Уроки французского",
            "Маленький принц",
            "О великий и могучий новый русский язык!",
            "Людочка",
            "Кем быть?",
            "Дарвин"]

    def connect_to_db(self):
        con = sqlite3.connect(self.NAME_OF_DB)
        cur = con.cursor()
        return cur, con

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.show_fav()
        if int(event.key()) == int(Qt.Key_Enter) or int(event.key()) + 1 == int(Qt.Key_Enter):
            self.go_next()
        if event.key() == Qt.Key_Delete:
            self.remove_from_db()
        if int(event.modifiers()) == Qt.ControlModifier:
            if event.key() == Qt.Key_F:
                self.select_sort()
        if int(event.modifiers()) == Qt.ControlModifier:
            if event.key() == Qt.Key_P:
                self.select_problem()

    def show_how_to_use(self):
        self.third_form = ThirdForm(self, "How to use")
        self.third_form.show()

    def _on_radio_button_clicked(self, state):
        try:
            if state == Qt.Checked:
                con = sqlite3.connect(self.NAME_OF_DB)
                cur = con.cursor()
                cur.execute("INSERT OR REPLACE INTO favs VALUES (?, ?, ?, ?)", (
                    self.title[self.num % len(self.result)][0],
                    self.title[self.num % len(self.result)][1],
                    self.result[self.num % len(self.result)][0],
                    self.problem))
                con.commit()
                con.close()
            else:
                con = sqlite3.connect(self.NAME_OF_DB)
                cur = con.cursor()
                cur.execute("""DELETE  FROM favs where Arg = ?""", (self.result[self.num % len(self.result)][0],))
                con.commit()
                con.close()

        except Exception as e:
            print(e)

    def select_problem(self):
        x, okBtnPressed = QInputDialog.getItem(self,
                                               "Выбор проблемы",
                                               "Выберите проблему для сочинения ЕГЭ",
                                               self.ALL_PROBLEMS,
                                               0, False)
        if okBtnPressed:
            try:
                con_1 = sqlite3.connect(self.NAME_OF_DB)
                cur_1 = con_1.cursor()
                self.all = []
                self.into_fav = cur_1.execute("""SELECT Arg FROM favs""").fetchall()
                for y in self.into_fav:
                    self.all.append(*y)
                self.like.setVisible(True)
                self.problem = x
                cur, con = self.connect_to_db()
                self.result = cur.execute("""SELECT Arg FROM books 
                              WHERE Problem = ?""", (self.problem,)).fetchall()
                self.title = cur.execute("""SELECT Author, Title FROM books 
                                          WHERE Problem = ?""", (self.problem,)).fetchall()
                self.num = 0
                self.textBrowser.setText(self.result[self.num][0])
                out = ' - '.join(self.title[self.num])
                self.name_of_book.setText(out)
                self.name_of_book.adjustSize()
                if self.result[self.num % len(self.result)][0] in self.all:
                    self.like.setChecked(True)
                else:
                    self.like.setChecked(False)
                con.close()
            except Exception as e:
                print(e)

    def go_next(self):
        try:
            con = sqlite3.connect(self.NAME_OF_DB)
            cur = con.cursor()
            self.num += 1
            self.all = []
            self.into_fav = cur.execute("""SELECT Arg FROM favs""").fetchall()
            for x in self.into_fav:
                self.all.append(*x)
            self.textBrowser.setText(
                self.result[self.num % len(self.result)][0])
            if len(self.result) == 0:
                self.textBrowser.setText('Аргументы кончились')
            out = ' - '.join(self.title[self.num % len(self.result)])
            self.name_of_book.setText(out)
            self.name_of_book.adjustSize()
            if self.result[self.num % len(self.result)][0] in self.all:
                self.like.setChecked(True)
            else:
                self.like.setChecked(False)

        except:
            pass

    def remove_from_db(self):
        try:
            cur, con = self.connect_to_db()
            cur.execute("""DELETE  FROM books 
                                    WHERE Arg = ?""",
                        (self.result[self.num % len(self.result)][0],))
            self.all = []
            self.into_fav = cur.execute("""SELECT Arg FROM favs""").fetchall()
            for x in self.into_fav:
                self.all.append(*x)
            if self.result[self.num % len(self.result)][0] in self.all:
                print(1)
                cur.execute("""DELETE  FROM favs where Arg = ?""", (self.result[self.num % len(self.result)][0],))
            con.commit()
            self.result = cur.execute("""SELECT Arg FROM books 
                                    WHERE Problem = ?""", (self.problem,)).fetchall()
            self.title = cur.execute("""SELECT Author, Title FROM books 
                                                WHERE Problem = ?""",
                                     (self.problem,)).fetchall()
            if len(self.result) == 0:
                self.name_of_book.setText('')
                self.name_of_book.adjustSize()
                self.textBrowser.setText('Аргументы кончились')
                self.like.setChecked(False)
            else:
                self.go_next()
            con.close()
        except:
            pass

    def show_fav(self):
        self.second_form = SecondForm(self, "Избранное")
        self.second_form.show()

    def select_sort(self):
        x, okBtnPressed = QInputDialog.getItem(self,
                                               "Выбор произведения",
                                               "Выберите произведение",
                                               (self.ALL_BOOKS
                                                ),
                                               0, False)
        if okBtnPressed:
            try:
                con_1 = sqlite3.connect(self.NAME_OF_DB)
                cur_1 = con_1.cursor()
                self.all = []
                self.into_fav = cur_1.execute("""SELECT Arg FROM favs""").fetchall()
                for y in self.into_fav:
                    self.all.append(*y)
                self.like.setVisible(True)
                self.name_sort = x
                cur, con = self.connect_to_db()
                self.result = cur.execute("""SELECT Arg FROM books 
                                        WHERE Title = ?""", (self.name_sort,)).fetchall()
                self.title = cur.execute("""SELECT Author, Title FROM books 
                                                    WHERE Title = ?""",
                                         (self.name_sort,)).fetchall()
                self.num = 0
                self.problem = cur.execute("""SELECT Problem from books where Arg = ?""",
                                           (self.result[0][0],)).fetchall()[0][0]
                self.textBrowser.setText(self.result[self.num][0])
                out = ' - '.join(self.title[self.num])
                self.name_of_book.setText(out)
                self.name_of_book.adjustSize()
                if self.result[self.num % len(self.result)][0] in self.all:
                    self.like.setChecked(True)
                else:
                    self.like.setChecked(False)
                con.close()
            except Exception as e:
                pass


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
