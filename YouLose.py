# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\JasmineJones\Documents\GuessingGame\YouLose.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(267, 170)
        Form.setMinimumSize(QtCore.QSize(267, 170))
        Form.setMaximumSize(QtCore.QSize(267, 170))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.Title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(14)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setAutoFillBackground(False)
        self.Title.setTextFormat(QtCore.Qt.AutoText)
        self.Title.setScaledContents(False)
        self.Title.setObjectName("Title")
        self.gridLayout.addWidget(self.Title, 1, 3, 1, 1)
        self.yes = QtWidgets.QPushButton(Form)
        self.yes.setObjectName("yes")
        self.gridLayout.addWidget(self.yes, 14, 3, 1, 1)
        self.no = QtWidgets.QPushButton(Form)
        self.no.setObjectName("no")
        self.gridLayout.addWidget(self.no, 15, 3, 1, 1)
        self.roundLabel = QtWidgets.QLabel(Form)
        self.roundLabel.setObjectName("roundLabel")
        self.gridLayout.addWidget(self.roundLabel, 3, 3, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setMaximumSize(QtCore.QSize(50, 25))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 4, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Title.setText(_translate("Form", "You Lose! Retry?"))
        self.yes.setText(_translate("Form", "Yes"))
        self.no.setText(_translate("Form", "No"))
        self.roundLabel.setText(_translate("Form", "Rounds:"))