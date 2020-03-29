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
import Login

class Ui_SignUp(object):

    def __init__(self,window=None):
        self.wind = window
    
    def naviagateToLogin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =Login.Ui_MainWindow(self.window)
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

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 190, 151, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 200, 91, 20))
        self.label_4.setObjectName("label_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 250, 89, 25))
        self.pushButton.setObjectName("pushButton")
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
    def signupListener(self):
        password = self.lineEdit.text()
        username = self.lineEdit_2.text()
        confirmPassword = self.lineEdit_3.text()
        credentials = []
        if username and password and confirmPassword:
            if len(confirmPassword)<6:
                error = QtWidgets.QMessageBox()
                error.setText("Password Length Must be equal or Grater then 6 characters!")
                error.setStandardButtons(QtWidgets.QMessageBox.Ok)
                error.exec_()
            else:
                if password==confirmPassword:
                    users = []
                    with open('credentials.csv','r') as csvFile:
                        reader = csv.reader(csvFile,delimiter=',')
                        for row in reader:
                            if row:
                                users.append(row)
                    matchUser = False
                    for user in users:
                        if username == user[0]:
                            matchUser = True
                            break                
                    if not matchUser:
                        with open('credentials.csv','a+') as csvFile:
                            csvFile.write(f'\n{username},{confirmPassword}\n')
                            csvFile.close()
                        self.naviagateToLogin()
                    else:
                        error = QtWidgets.QMessageBox()
                        error.setText("Username Already Exist!")
                        error.setStandardButtons(QtWidgets.QMessageBox.Ok)
                        error.exec_()
                
                else:
                    error = QtWidgets.QMessageBox()
                    error.setText("Password Not Match with Previous Entry!")
                    error.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    error.exec_()
        else:
            error = QtWidgets.QMessageBox()
            error.setText("Please Fill FIelds")
            error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Resume Sorter System"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "Confirm Password"))
        self.pushButton.setText(_translate("MainWindow", "Sign Up"))
        self.menuLogin.setTitle(_translate("MainWindow", "Admin Sign Up"))
        self.pushButton.clicked.connect(self.signupListener)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SignUp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

