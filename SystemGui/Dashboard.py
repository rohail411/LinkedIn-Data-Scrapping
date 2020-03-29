# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from Result import Ui_ResultsWindow
import Login
import Login
import time
import os
import shutil

class Ui_DashboardWindow(object):

    def __init__(self,window,data):
        self.wind = window
        self.data = data

    def openResultsWindow(self,data,exp=0,title=""):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ResultsWindow(self.window,self.data,data,title,exp)
        self.ui.setupUi(self.window)
        self.wind.close()
        self.window.show()
        

    def setupUi(self, DashboardWindow):
        DashboardWindow.setObjectName("DashboardWindow")
        DashboardWindow.setFixedSize(830, 500)
        DashboardWindow.setStyleSheet('background-image: url("images/back2.png")')
        self.centralwidget = QtWidgets.QWidget(DashboardWindow)
        self.centralwidget.setObjectName("centralwidget")

        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(650, 30, 461, 300))
        pixmap = QPixmap('images/logo.png')
        self.label_9.setPixmap(pixmap)
        self.label_9.resize(pixmap.width(), pixmap.height())

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 0, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(20)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 130, 367, 27))
        self.label.setStyleSheet('background:none')
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 130, 295, 27))
        self.label_2.setStyleSheet('background:none')
        
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 260, 81, 17))
        self.label_3.setObjectName("label_3")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 218, 81, 17))
        self.label_10.setObjectName("label_10")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 300, 91, 17))
        
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 340, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 300, 91, 17))
        
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 340, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 260, 131, 20))
        
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 220, 81, 17))
        
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 180, 67, 17))
        
        self.label_8.setObjectName("label_8")
        # self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit.setGeometry(QtCore.QRect(150, 90, 151, 31))
        # self.lineEdit.setStyleSheet("background-color: rgb(238, 238, 236);")
        # self.lineEdit.setText("")
        # self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 210, 151, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 250, 151, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 290, 151, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(580, 170, 151, 31))
        self.lineEdit_5.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(580, 210, 151, 31))
        self.lineEdit_6.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(580, 250, 151, 31))
        self.lineEdit_7.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(580, 290, 151, 31))
        self.lineEdit_8.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        DashboardWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DashboardWindow)
        self.statusbar.setObjectName("statusbar")
        DashboardWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(DashboardWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuDashboard = QtWidgets.QMenu(self.menubar)
        self.menuDashboard.setObjectName("menuDashboard")
        DashboardWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuDashboard.menuAction())

        self.retranslateUi(DashboardWindow)
        QtCore.QMetaObject.connectSlotsByName(DashboardWindow)
    
    def adminestrativeSearch(self):
        title = self.lineEdit_2.text()
        exp = self.lineEdit_3.text()
        qual = self.lineEdit_4.text()
        l1Array = []
        l2Array = []
        if exp and qual and title:
            path = 'C:/LinkedinMatchedDocxForAdministrative'
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                shutil.rmtree(path)
                os.mkdir(path)
            for user in self.data:
                educ = user.get('experiences','').get('education','')
                us = user.get('personal_info','').get('headline','')
                us1 = user.get('experiences').get('jobs')
                experience = 0
                if int(exp) != 0:
                    experience = self.getExperience(user.get('experiences').get('jobs'))
                if (title.strip().lower() in str(us).lower() or len([u for u in us1 if title.strip().lower() in str(u.get('title')).lower()])>0 ):
                    if len([e for e in educ if qual.strip().lower() in str(e.get('field_of_study')).lower() ])>0 and int(experience)>=int(exp):
                        l1Array.append(user)
                        shutil.copy('C:/LinkedinDocs/'+str(user.get('personal_info',"Error 1").get('name',"Error 2"))+'.docx',path)
                    # elif len([e for e in educ if qual.strip().lower() in str(e.get('field_of_study')).lower() ])>0 and int(experience)<=int(exp):
                    #     l2Array.append(user)
                    #     shutil.copy('C:/LinkedinDocs/'+str(user.get('personal_info',"Error 1").get('name',"Error 2"))+'.docx',path)
                
            resultArr = l1Array+l2Array
            if resultArr:
                self.openResultsWindow(resultArr,exp,title="Administrative")
            else:
                error = QtWidgets.QMessageBox()
                error.setText("Not Found")
                error.setStandardButtons(QtWidgets.QMessageBox.Ok)
                error.exec_()    
        else:
            error = QtWidgets.QMessageBox()
            error.setText("Please Fill FIelds")
            error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error.exec_()

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
    
    def fucalitySearch(self):
        title = self.lineEdit_5.text()
        exp = self.lineEdit_6.text()
        pub =self.lineEdit_7.text()
        qual =self.lineEdit_8.text()
        match = []
        #unMatch = []
        if title and exp and qual:
            path = 'C:/LinkedinMatchedDocxForFucalty'
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                shutil.rmtree(path)
                os.mkdir(path)
            if not str(pub).strip():
                pub = 0
            for user in self.data:
                us = user.get('personal_info','').get('headline','')
                us1 = user.get('experiences').get('jobs')
                publication = user.get('accomplishments','').get('publications','')
                educ = user.get('experiences','').get('education','')
                experience = 0
                if int(exp) != 0:
                    experience = self.getExperience(user.get('experiences').get('jobs'))
                if (title.strip().lower() in str(us).lower() or len([u for u in us1 if title.strip().lower() in str(u.get('title')).lower()])>0 ) and len(publication)>=int(pub) and len([e for e in educ if qual.strip().lower() in str(e.get('field_of_study')).lower() ])>0 and int(experience)>=int(exp):
                    match.append(user)
                    shutil.copy('C:/LinkedinDocs/'+str(user.get('personal_info',"Error 1").get('name',"Error 2"))+'.docx',path)    
            if match:
                self.openResultsWindow(match,exp,title="Faculty")
            else:
                error = QtWidgets.QMessageBox()
                error.setText("Not Found")
                error.setStandardButtons(QtWidgets.QMessageBox.Ok)
                error.exec_()    
        else:
            error = QtWidgets.QMessageBox()
            error.setText("Please Fill FIelds")
            error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error.exec_()
    
    def logout(self,):
        self.window = QtWidgets.QMainWindow()
        self.ui = Login.Ui_MainWindow(self.window)
        self.ui.setupUi(self.window)
        self.wind.close()
        self.window.show()
        

    def retranslateUi(self, DashboardWindow):
        _translate = QtCore.QCoreApplication.translate
        DashboardWindow.setWindowTitle(_translate("DashboardWindow", "DashboardWindow"))
        self.label.setText(_translate("DashboardWindow", "Search Resume for Administrative"))
        self.label_2.setText(_translate("DashboardWindow", "Search Resume for Faculty"))
        self.label_3.setText(_translate("DashboardWindow", "Experience"))
        self.label_4.setText(_translate("DashboardWindow", "Qualification"))
        self.pushButton.setText(_translate("DashboardWindow", "Search"))
        self.label_5.setText(_translate("DashboardWindow", "Qualification"))
        self.pushButton_2.setText(_translate("DashboardWindow", "Search"))
        self.pushButton_3.setText(_translate("DashboardWindow", "Logout"))
        self.label_6.setText(_translate("DashboardWindow", "No. of Publications"))
        self.label_7.setText(_translate("DashboardWindow", "Experience"))
        self.label_8.setText(_translate("DashboardWindow", "Job Title"))
        self.label_10.setText(_translate("DashboardWindow", "Job Title"))
        self.menuDashboard.setTitle(_translate("DashboardWindow", "Dashboard"))
        self.pushButton_2.clicked.connect(self.fucalitySearch)
        self.pushButton.clicked.connect(self.adminestrativeSearch)
        self.pushButton_3.clicked.connect(self.logout)


