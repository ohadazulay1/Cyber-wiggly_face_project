# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from clientHelperForOnline import ClientHelperForOnline
from threading import Thread
from _thread import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from computerCam import Camera
from commonUtils import commonUtils
from userNameClass import UserNameClass
from PyQt5.QtCore import pyqtSlot
from client import Client

import Emotion
from graphics import Graphics

class Ui_MainWindow(object):
    def __init__(self, firstWindow):
        self.MainWindow = firstWindow
        self.setupUi()

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(2890, 1502)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(700, 30, 691, 271))
        font = QtGui.QFont()
        font.setFamily("Vivaldi")
        font.setPointSize(72)
        font.setItalic(True)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.pressToSee_label = QtWidgets.QLabel(self.centralwidget)
        self.pressToSee_label.setGeometry(QtCore.QRect(80, 380, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pressToSee_label.setFont(font)
        self.pressToSee_label.setObjectName("pressToSee_label")
        self.records_button = QtWidgets.QPushButton(self.centralwidget)
        self.records_button.setGeometry(QtCore.QRect(90, 420, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.records_button.setFont(font)
        self.records_button.setObjectName("records_button")
        self.playOnline_button = QtWidgets.QPushButton(self.centralwidget)
        self.playOnline_button.setGeometry(QtCore.QRect(460, 730, 411, 181))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.playOnline_button.setFont(font)
        self.playOnline_button.setObjectName("playOnline_button")
        self.playOffline_button = QtWidgets.QPushButton(self.centralwidget)
        self.playOffline_button.setGeometry(QtCore.QRect(940, 730, 411, 181))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.playOffline_button.setFont(font)
        self.playOffline_button.setObjectName("playOffline_button")
        self.pic_label = QtWidgets.QLabel(self.centralwidget)
        self.pic_label.setGeometry(QtCore.QRect(660, 290, 491, 321))
        self.pic_label.setText("")
        self.pic_label.setPixmap(QtGui.QPixmap(
            "../../OneDrive/תמונות/forProject/patches-smiley-face-happy-sad-venn_grande.webp"))
        self.pic_label.setObjectName("pic_label")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2890, 26))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.playOffline_button.clicked.connect(Ui_MainWindow.playOfflinePressed)
        self.records_button.clicked.connect(Ui_MainWindow.recordsPressed)
        self.playOnline_button.clicked.connect(Ui_MainWindow.playOnlinePressed)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "wiggly face"))
        self.pressToSee_label.setText(_translate("MainWindow", "press to see world records:"))
        self.records_button.setText(_translate("MainWindow", "records"))
        self.playOnline_button.setText(_translate("MainWindow", "play online"))
        self.playOffline_button.setText(_translate("MainWindow", "play offline"))


    def playOfflinePressed(self):
        cp = Camera()
        camThread = Thread(target=cp.mainProcess)
        camThread.start()

        gr = Graphics("")
        gr.objectsManeger()

    def recordsPressed(self):
        client = Client.get_instance()
        topDict = client.topFive()

        result = ""
        for user, value in topDict.items():
            result += "{:<15} \t {} \n".format(user, commonUtils.get_time_str(value))

        msg = QMessageBox()
        msg.setWindowTitle("records")
        msg.setText("                         THE BEST SCORES IN THE WHOLE GAME:                        ")
        msg.setStandardButtons(QMessageBox.Close)
        msg.setInformativeText(result)
        x = msg.exec_()


    def playOnlinePressed(self):
        clientHelper = ClientHelperForOnline.get_instance()
        selfUserName = UserNameClass.get_instance().getUserName()
        clientHelper.connectToAnotherUser(selfUserName)