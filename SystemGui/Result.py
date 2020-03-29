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
import Ranked
import getpass

class Ui_ResultsWindow(object):

    def __init__(self,window,rawData,data=[],title='',exp=0):
        self.wind = window
        self.data = data
        self.title = title
        self.expDash = exp
        self.rawData = rawData
    def openResultsWindow(self,data,title=""):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ranked.Ui_Ranked(self.window,self.rawData,data,title)
        self.ui.setupUi(self.window)
        self.wind.close()
        self.window.show()

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
        self.tableWidget.setGeometry(QtCore.QRect(165, 140, 471, 192))
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

    def setupUi(self, ResultsWindow):
        ResultsWindow.setObjectName("ResultsWindow")
        ResultsWindow.setFixedSize(800, 600)
        ResultsWindow.setStyleSheet('background-image: url("images/back2.png")')
        self.centralwidget = QtWidgets.QWidget(ResultsWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(670, 35, 450, 400))
        pixmap = QPixmap('images/logo.png')
        self.label_4.setPixmap(pixmap)
        self.label_4.resize(pixmap.width(), pixmap.height())

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 480, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(680, 0, 89, 25))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 480, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 400, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 440, 91, 20))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 90, 511, 20))
        self.label.setStyleSheet('background:none')
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 390, 151, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 430, 151, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.initTable(self.data)

        ResultsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ResultsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuResults = QtWidgets.QMenu(self.menubar)
        self.menuResults.setObjectName("menuResults")
        ResultsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ResultsWindow)
        self.statusbar.setObjectName("statusbar")
        ResultsWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuResults.menuAction())

        self.retranslateUi(ResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultsWindow)

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
    
    def rank(self):
        qual =str(self.lineEdit.text())
        exp = self.lineEdit_2.text()
        if qual and exp:
            if len(qual)<3:
                error = QtWidgets.QMessageBox()
                error.setText("Invalid Input For Qualification")
                error.setStandardButtons(QtWidgets.QMessageBox.Ok)
                error.exec_()
            if int(exp)<int(self.expDash)+1:
                error = QtWidgets.QMessageBox()
                error.setText("Experience Must be Grater Then Previous Entry")
                error.setStandardButtons(QtWidgets.QMessageBox.Ok)
                error.exec_()
            else:
                l2Array = []
                for user in self.data:
                    educ = user.get('experiences','').get('education','')
                    experience = 0
                    if int(exp) != 0:
                        experience = self.getExperience(user.get('experiences').get('jobs'))
                    if len([e for e in educ if qual.lower() in str(e.get('field_of_study')).lower() ])>0:
                        if int(experience)==int(exp):
                            l2Array.append(user)
                if len(l2Array)>0:
                    self.openResultsWindow(l2Array,title=self.title)
                else:
                    error = QtWidgets.QMessageBox()
                    error.setText("No Match Found")
                    error.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    error.exec_()  
        else:
            error = QtWidgets.QMessageBox()
            error.setText("Please Fill FIelds")
            error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error.exec_()
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

    def retranslateUi(self, ResultsWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultsWindow.setWindowTitle(_translate("ResultsWindow", "MainWindow"))
        self.pushButton.setText(_translate("ResultsWindow", "Search"))
        self.pushButton_1.setText(_translate("ResultsWindow", "Logout"))
        self.pushButton_2.setText(_translate("ResultsWindow", "<Back"))
        self.label_2.setText(_translate("ResultsWindow", "Qualification"))
        self.label_3.setText(_translate("ResultsWindow", "Experience"))
        self.label.setText(_translate("ResultsWindow", f"Resume for {self.title} Position"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("ResultsWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ResultsWindow", "Name"))
        self.menuResults.setTitle(_translate("ResultsWindow", "Results"))
        self.pushButton.clicked.connect(self.rank)
        self.pushButton_1.clicked.connect(self.logout)
        self.pushButton_2.clicked.connect(self.back)


