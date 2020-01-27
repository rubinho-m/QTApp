# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'for_fav.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_fav = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_fav.setGeometry(QtCore.QRect(80, 130, 651, 351))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(22)
        self.textBrowser_fav.setFont(font)
        self.textBrowser_fav.setObjectName("textBrowser_fav")
        self.dont_show_fav = QtWidgets.QPushButton(self.centralwidget)
        self.dont_show_fav.setGeometry(QtCore.QRect(0, 490, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(19)
        self.dont_show_fav.setFont(font)
        self.dont_show_fav.setObjectName("dont_show_fav")
        self.name_fav = QtWidgets.QLabel(self.centralwidget)
        self.name_fav.setGeometry(QtCore.QRect(300, 0, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.name_fav.setFont(font)
        self.name_fav.setObjectName("name_fav")
        self.next_fav = QtWidgets.QPushButton(self.centralwidget)
        self.next_fav.setGeometry(QtCore.QRect(510, 490, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(20)
        self.next_fav.setFont(font)
        self.next_fav.setAutoDefault(False)
        self.next_fav.setDefault(False)
        self.next_fav.setFlat(False)
        self.next_fav.setObjectName("next_fav")
        self.name_of_book_fav = QtWidgets.QLabel(self.centralwidget)
        self.name_of_book_fav.setGeometry(QtCore.QRect(90, 90, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.name_of_book_fav.setFont(font)
        self.name_of_book_fav.setText("")
        self.name_of_book_fav.setObjectName("name_of_book_fav")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.textBrowser_fav.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Yu Gothic UI Light\'; font-size:22pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.dont_show_fav.setText(_translate("MainWindow", "Удалить"))
        self.name_fav.setText(_translate("MainWindow", "Избранное"))
        self.next_fav.setText(_translate("MainWindow", "Следующий аргумент"))
