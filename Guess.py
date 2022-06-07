from cmath import sqrt
from datetime import datetime
from random import random, uniform
from threading import Event
from xml.sax.handler import feature_external_ges
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractScrollArea
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
import openpyxl
import os
from reportlab.lib.pagesizes import letter
import textwrap
from reportlab.lib import colors
from datetime import datetime
import time

def rand(gues):
    x = int(uniform(1,4))
    if gues == x:
        return True
    return False

def lost(m, percent):
    money = m*100
    t = round(((money - (percent * money))/100),2)
    return t

def won(m, percent):
    money = m*100
    t = round(((money + (percent * money))/100),2)
    return t

def toIntp(p):
    speChars = "%"
    pp = p.replace(speChars, '')
    p = float(pp)/100
    return p

def toIntm(p):
    speChars = "$"
    pp = p.replace(speChars, '')
    p = float(pp)
    return p

class Window2(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window22222")

class Ui_MainWindow(object):

    def one_btn(self):
        self.winLose.clear()
        m = toIntm(self.money.toPlainText())
        p = toIntp(self.percentBox.currentText())

        if rand(1) == True:
            time.sleep(1)
            self.winLose.setText("You Won!!")
            self.money.setText("$"+str(won(m,p)))
            
        else:
            time.sleep(1)
            self.winLose.setText("You Lost :(") 
            self.money.setText("$"+str(lost(m,p)))

    def two_btn(self):
        self.winLose.clear()
        m = toIntm(self.money.toPlainText())
        p = toIntp(self.percentBox.currentText())

        if rand(2) == True:
            time.sleep(1)
            self.winLose.setText("You Won!!")
            self.money.setText("$"+str(won(m,p)))
            
        else:
            time.sleep(1)
            self.winLose.setText("You Lost :(") 
            self.money.setText("$"+str(lost(m,p)))

    def three_btn(self):
        self.winLose.clear()
        m = toIntm(self.money.toPlainText())
        p = toIntp(self.percentBox.currentText())

        if rand(3) == True:
            time.sleep(1)
            self.winLose.setText("You Won!!")
            self.money.setText("$"+str(won(m,p)))
            
        else:
            time.sleep(1)
            self.winLose.setText("You Lost :(")            
            self.money.setText("$"+str(lost(m,p)))


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(332, 250)
        MainWindow.setMinimumSize(QtCore.QSize(332, 250))
        MainWindow.setMaximumSize(QtCore.QSize(700, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.moneyLabel = QtWidgets.QLabel(self.centralwidget)
        self.moneyLabel.setObjectName("moneyLabel")
        self.gridLayout.addWidget(self.moneyLabel, 2, 1, 1, 1)
        self.percentLabel = QtWidgets.QLabel(self.centralwidget)
        self.percentLabel.setObjectName("percentLabel")
        self.gridLayout.addWidget(self.percentLabel, 4, 1, 1, 2)

        self.winLose = QtWidgets.QTextBrowser(self.centralwidget)
        self.winLose.setMaximumSize(QtCore.QSize(700, 20))
        self.winLose.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.winLose.setFrameShadow(QtWidgets.QFrame.Plain)
        self.winLose.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.winLose.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.winLose.setObjectName("winLose")
        self.gridLayout.addWidget(self.winLose, 10, 1, 1, 4)


        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setObjectName("two")
        self.gridLayout.addWidget(self.two, 8, 3, 1, 1)
        self.two.clicked.connect(self.two_btn)

        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setObjectName("one")
        self.gridLayout.addWidget(self.one, 8, 2, 1, 1)
        self.one.clicked.connect(self.one_btn)

        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setObjectName("three")
        self.gridLayout.addWidget(self.three, 8, 4, 1, 1)
        self.three.clicked.connect(self.three_btn)

        self.prompt = QtWidgets.QLabel(self.centralwidget)
        self.prompt.setObjectName("prompt")
        self.gridLayout.addWidget(self.prompt, 6, 1, 1, 1)
        
        self.percentBox = QtWidgets.QComboBox(self.centralwidget)
        self.percentBox.setMaximumSize(QtCore.QSize(120, 20))
        self.percentBox.setObjectName("percentBox")
        self.percentBox.addItem("")
        self.percentBox.addItem("")
        self.percentBox.addItem("")
        self.percentBox.addItem("")
        self.percentBox.addItem("")
        self.percentBox.addItem("")
        self.percentBox.addItem("")
        self.gridLayout.addWidget(self.percentBox, 4, 3, 1, 1)
        
        self.money = QtWidgets.QTextBrowser(self.centralwidget)
        self.money.setMaximumSize(QtCore.QSize(120, 25))
        self.money.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.money.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.money.setObjectName("money")
        self.gridLayout.addWidget(self.money, 2, 3, 1, 1)
        
        self.Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(14)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.gridLayout.addWidget(self.Title, 0, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 332, 22))
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
        self.moneyLabel.setText(_translate("MainWindow", "Your Money:"))
        self.percentLabel.setText(_translate("MainWindow", "Choose a percentage"))
        self.two.setText(_translate("MainWindow", "2"))
        self.one.setText(_translate("MainWindow", "1"))
        self.three.setText(_translate("MainWindow", "3"))
        self.prompt.setText(_translate("MainWindow", "Make a guess..."))
        self.percentBox.setItemText(0, _translate("MainWindow", "5%"))
        self.percentBox.setItemText(1, _translate("MainWindow", "15%"))
        self.percentBox.setItemText(2, _translate("MainWindow", "25%"))
        self.percentBox.setItemText(3, _translate("MainWindow", "50%"))
        self.percentBox.setItemText(4, _translate("MainWindow", "75%"))
        self.percentBox.setItemText(5, _translate("MainWindow", "85%"))
        self.percentBox.setItemText(6, _translate("MainWindow", "100%"))
        self.money.setText(_translate("MainWindow", "$200"))
        self.Title.setText(_translate("MainWindow", "Guessing Game"))

    def window2(self):                                             # <===
        self.w = Window2()
        self.w.show()
        self.hide()

    



if __name__ == "__main__": #### Creates Scene ####
    import sys
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    win = QMainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec())
