# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Results.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import Login
import Dashboard
import os
import time
import shutil
import getpass

class Ui_Ranked(object):

    def __init__(self,window,rawData,data=[],title=''):
        self.data = data
        self.title = title
        self.wind = window
        self.rawData = rawData

    def openFile(self,i):
        if i.column() == 0:
            a = self.tableWidget.item(i.row(),i.column()).text()
            if self.title == 'Faculty':
                os.startfile("C:/LinkedinMatchedDocxForFucalty/"+str(a))
            elif self.title == 'Administrative':
                os.startfile("C:/LinkedinMatchedDocxForAdministrative/"+str(a))
        elif i.column() == 1:
            a = self.tableWidget.item(i.row(),0).text()
            filePath = ""
            if self.title == 'Faculty':
                filePath = "C:/LinkedinMatchedDocxForFucalty/"+str(a)
            elif self.title == 'Administrative':
                filePath = "C:/LinkedinMatchedDocxForAdministrative/"+str(a)
            shutil.copy(filePath,f'C:/Users/{getpass.getuser()}/Downloads')
            msg = QtWidgets.QMessageBox()
            msg.setText("File Download Successfully See Downloads Folder to get File!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_() 
        

    def initTable(self,data=[]):
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(165, 140, 481, 300))
        self.tableWidget.setStyleSheet('background:#88AAFF;')
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        length = 0
        if len(data):
            length = len(data)
        
        self.tableWidget.setRowCount(length)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item1 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item1)
        for i in range(len(data)):
            for d in range(1):
                self.tableWidget.setItem(i,d, QtWidgets.QTableWidgetItem(str(data[i].get('personal_info',"Error 1").get('name',"Error 2"))+'.docx'))
                self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem('Download'))
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setColumnWidth(0, 360)
        self.tableWidget.doubleClicked.connect(self.openFile)
        
        #self.tableWidget.clicked.connect(self.openFile)

    def setupUi(self, Ranked):
        Ranked.setObjectName("Ranked")
        Ranked.setFixedSize(800, 500)
        Ranked.setStyleSheet('background-image: url("images/back2.png")')
        self.centralwidget = QtWidgets.QWidget(Ranked)
        self.centralwidget.setObjectName("centralwidget")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(670, 30, 461, 400))
        pixmap = QPixmap('images/logo.png')
        self.label_4.setPixmap(pixmap)
        self.label_4.resize(pixmap.width(), pixmap.height())

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 0, 89, 25))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 420, 89, 25))
        self.pushButton_1.setObjectName("pushButton_1")
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(230, 380, 91, 20))
        # self.label_2.setObjectName("label_2")
        # self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(230, 420, 91, 20))
        # self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 70, 525, 25))
        self.label.setStyleSheet('background:none')
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit.setGeometry(QtCore.QRect(340, 370, 151, 31))
        # self.lineEdit.setStyleSheet("background-color: rgb(238, 238, 236);")
        # self.lineEdit.setText("")
        # self.lineEdit.setObjectName("lineEdit")
        # self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit_2.setGeometry(QtCore.QRect(340, 410, 151, 31))
        # self.lineEdit_2.setStyleSheet("background-color: rgb(238, 238, 236);")
        # self.lineEdit_2.setText("")
        # self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.initTable(self.data)

        Ranked.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ranked)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuResults = QtWidgets.QMenu(self.menubar)
        self.menuResults.setObjectName("menuResults")
        Ranked.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ranked)
        self.statusbar.setObjectName("statusbar")
        Ranked.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuResults.menuAction())

        self.retranslateUi(Ranked)
        QtCore.QMetaObject.connectSlotsByName(Ranked)

    def getExperience(self,user=[]):
        char = ('J','F','M','A','M','J','S','O','N','D')
        exp = 0
        for u in user:
            if u.get('date_range','') is not None:
                arr = u.get('date_range','').split(" ")
                if arr[0].startswith(char):
                    arr.pop(0)
                    if arr[0].isdigit() and arr[-1].isdigit():
                        exp += int(arr[-1])-int(arr[0])
                    elif arr[0].isdigit() and arr[-1].startswith("P"):
                        curr = time.ctime().split(" ")[-1]
                        exp += int(curr)-int(arr[0])
        return exp

    def logout(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Login.Ui_MainWindow(self.window)
        self.ui.setupUi(self.window)
        self.wind.close()
        self.window.show()
    
    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =Dashboard.Ui_DashboardWindow(self.window,self.rawData)
        self.ui.setupUi(self.window)
        self.wind.close()
        self.window.show()

    def retranslateUi(self, Ranked):
        _translate = QtCore.QCoreApplication.translate
        Ranked.setWindowTitle(_translate("Ranked", "MainWindow"))
        self.pushButton.setText(_translate("Ranked", "Logout"))
        self.pushButton_1.setText(_translate("Ranked", "<Back"))
        # self.label_2.setText(_translate("Ranked", "Qualification"))
        # self.label_3.setText(_translate("Ranked", "Experience"))
        self.label.setText(_translate("Ranked", f'Filtered Resumse for {self.title} Position'))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Ranked", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Ranked", "Name"))
        self.menuResults.setTitle(_translate("Ranked", "Results"))
        self.pushButton.clicked.connect(self.logout)
        self.pushButton_1.clicked.connect(self.back)



