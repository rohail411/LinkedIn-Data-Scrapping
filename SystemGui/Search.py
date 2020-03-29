# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Search.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import Dashboard
import linkedin_scraping
import csv
import ast
import pprint
import re

class Ui_SearchWindow(object):
    def __init__(self,window):
        self.wind = window
    def openResultsWindow(self,data):
        self.window = QtWidgets.QMainWindow()
        self.ui = Dashboard.Ui_DashboardWindow(self.window,data)
        self.ui.setupUi(self.window)
        self.wind.close()
        self.window.show()
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.setFixedSize(850, 450)
        SearchWindow.setStyleSheet('background-image: url("images/back2.png")')
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(730, 0, 461, 400))
        pixmap = QPixmap('images/logo.png')
        self.label_5.setPixmap(pixmap)
        self.label_5.resize(pixmap.width(), pixmap.height())

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 70, 151, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 150, 151, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 80, 91, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(350, 110, 151, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 120, 91, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 160, 91, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 200, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 200, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        
        SearchWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SearchWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 22))
        self.menubar.setObjectName("menubar")
        self.menuSearch = QtWidgets.QMenu(self.menubar)
        self.menuSearch.setObjectName("menuSearch")
        SearchWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SearchWindow)
        self.statusbar.setObjectName("statusbar")
        SearchWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSearch.menuAction())

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def search(self):
        location = self.lineEdit.text()
        jobTitle = self.lineEdit_2.text()
        cookie = self.lineEdit_3.text()
        if cookie:
            with open('cookie.csv','w') as csvfile2:
                csvfile2.write(cookie)
            csvfile2.close()
        else:
            with open('cookie.csv','r') as csvFile:
                reader = csv.reader(csvFile,delimiter=' ')
                for read in reader:
                    if not cookie:
                        cookie = read[0]
            csvFile.close()
                
        if location and jobTitle and cookie:
            data =linkedin_scraping.test(jobTitle,str(location).capitalize(),cookie)
            try:
                with open('data.txt', 'w') as f:
                    for item in data:
                        del item['personal_info']['image']
                        result = re.sub(r'[^a-zA-Z]', " ", item['personal_info']['name'])
                        result = re.sub(' +', ' ', result)
                        item['personal_info']['name'] = result
                        f.write("%s\n" % item)
                f.close()
            except Exception as e:
                print(e)
            finally:
                self.openResultsWindow(data)
        else:
            error = QtWidgets.QMessageBox()
            error.setText("Please Fill FIelds")
            error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error.exec_()
    def existSearch(self):
        lis = []
        with open('data.txt','r') as f1:
            for line in f1.readlines():
                lis.append(ast.literal_eval(line))
        f1.close()
        if lis:
            self.openResultsWindow(lis)
        else:
            error = QtWidgets.QMessageBox()
            error.setText("Data Not Found")
            error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error.exec_()

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "MainWindow"))
        self.label_2.setText(_translate("SearchWindow", "Job Title"))
        self.label_3.setText(_translate("SearchWindow", "Location"))
        self.label_4.setText(_translate("SearchWindow","Cookie (LI_AT)"))
        self.pushButton.setText(_translate("SearchWindow", "New Search"))
        self.menuSearch.setTitle(_translate("SearchWindow", "Search"))
        self.pushButton_2.setText(_translate("SearchWindow", "Existing Search"))
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.existSearch)


