# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import csv
import os
import Signup
import Search

class Ui_MainWindow(object):

    def __init__(self,window=None):
        self.wind = window
    
    def naviagateToSearch(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =Search.Ui_SearchWindow(self.window)
        self.ui.setupUi(self.window)
        if self.wind:
            self.wind.close()
        else:    
            MainWindow.close()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(850, 400)
        MainWindow.setStyleSheet('background-image: url("images/back2.png")')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(730, 0, 461, 400))
        pixmap = QPixmap('images/logo.png')
        self.label_4.setPixmap(pixmap)
        self.label_4.resize(pixmap.width(), pixmap.height())

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 50, 269, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 110, 151, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 120, 91, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 150, 151, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 160, 91, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 200, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(460, 200, 89, 25))
        self.pushButton_1.setObjectName("pushButton_1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuLogin = QtWidgets.QMenu(self.menubar)
        self.menuLogin.setObjectName("menuLogin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuLogin.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def loginListener(self):
        password = self.lineEdit.text()
        username = self.lineEdit_2.text()
        credentials = []
        users = []
        #os.startfile('D:\LinkedinDocs\Faiz Ali.docx')
        if username and password:
            with open('credentials.csv','r') as csvFile:
                reader = csv.reader(csvFile,delimiter=',')
                for row in reader:
                    if row:
                        users.append(row)
            matchUser = False
            for user in users:
                if username == user[0] and password == user[1]:
                    matchUser = True
                    break                
            if matchUser:
                self.naviagateToSearch()
            else:
                error = QtWidgets.QMessageBox()
                error.setText("Wrong Credentials")
                error.setStandardButtons(QtWidgets.QMessageBox.Ok)
                error.exec_()
        else:
            error = QtWidgets.QMessageBox()
            error.setText("Please Fill FIelds")
            error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error.exec_()
    def signupListener(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =Signup.Ui_SignUp(self.window)
        self.ui.setupUi(self.window)
        if self.wind:
            self.wind.close()
        else:    
            MainWindow.close()
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Resume Sorter System"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_1.setText(_translate("MainWindow", "Sign Up"))
        self.menuLogin.setTitle(_translate("MainWindow", "Admin Login"))
        self.pushButton.clicked.connect(self.loginListener)
        self.pushButton_1.clicked.connect(self.signupListener)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

