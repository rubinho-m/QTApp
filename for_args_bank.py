# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'args_bank.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1001, 659)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(280, 0, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.change_problem = QtWidgets.QPushButton(self.centralwidget)
        self.change_problem.setGeometry(QtCore.QRect(770, 0, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(18)
        self.change_problem.setFont(font)
        self.change_problem.setObjectName("change_problem")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(180, 150, 651, 391))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(22)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.dont_show = QtWidgets.QPushButton(self.centralwidget)
        self.dont_show.setGeometry(QtCore.QRect(10, 550, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(19)
        self.dont_show.setFont(font)
        self.dont_show.setObjectName("dont_show")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(730, 550, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.next.setFont(font)
        self.next.setAutoDefault(False)
        self.next.setDefault(False)
        self.next.setFlat(False)
        self.next.setObjectName("next")
        self.favourite = QtWidgets.QPushButton(self.centralwidget)
        self.favourite.setGeometry(QtCore.QRect(0, 100, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.favourite.setFont(font)
        self.favourite.setObjectName("favourite")
        self.how_to_use = QtWidgets.QPushButton(self.centralwidget)
        self.how_to_use.setGeometry(QtCore.QRect(0, 0, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.how_to_use.setFont(font)
        self.how_to_use.setObjectName("how_to_use")
        self.name_of_book = QtWidgets.QLabel(self.centralwidget)
        self.name_of_book.setGeometry(QtCore.QRect(200, 110, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.name_of_book.setFont(font)
        self.name_of_book.setText("")
        self.name_of_book.setObjectName("name_of_book")
        self.sort_button = QtWidgets.QPushButton(self.centralwidget)
        self.sort_button.setGeometry(QtCore.QRect(0, 170, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sort_button.setFont(font)
        self.sort_button.setObjectName("sort_button")
        self.like = QtWidgets.QCheckBox(self.centralwidget)
        self.like.setGeometry(QtCore.QRect(770, 70, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.like.setFont(font)
        self.like.setObjectName("like")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "Аргументы ЕГЭ"))
        self.change_problem.setText(_translate("MainWindow", "Выбрать проблему"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Yu Gothic UI Light\'; font-size:22pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.dont_show.setText(_translate("MainWindow", "Не показывать больше"))
        self.next.setText(_translate("MainWindow", "Следующий аргумент"))
        self.favourite.setText(_translate("MainWindow", "Избранное"))
        self.how_to_use.setText(_translate("MainWindow", "?"))
        self.sort_button.setText(_translate("MainWindow", "Поиск по произведению"))
        self.like.setText(_translate("MainWindow", "Мне нравится"))
