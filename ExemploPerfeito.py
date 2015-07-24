# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lolparser.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
class Ui_Form(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(803, 672)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.logsPathInput = QtWidgets.QLineEdit(Form)
        self.logsPathInput.setAutoFillBackground(False)
        self.logsPathInput.setObjectName("logsPathInput")
        self.horizontalLayout.addWidget(self.logsPathInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.summonerNameInput = QtWidgets.QLineEdit(Form)
        self.summonerNameInput.setObjectName("summonerNameInput")
        self.horizontalLayout_2.addWidget(self.summonerNameInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.mapButton = QtWidgets.QPushButton(Form)
        self.mapButton.setObjectName("mapButton")
        self.verticalLayout.addWidget(self.mapButton)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.resultDisplay = QtWidgets.QTextBrowser(Form)
        self.resultDisplay.setObjectName("resultDisplay")
        self.verticalLayout_5.addWidget(self.resultDisplay)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LolParser"))
        self.label.setText(_translate("Form", "Path of your Logs:"))
        self.logsPathInput.setPlaceholderText(_translate("Form", "C:\\\\Riot Games\\\\League of Legends\\\\Logs\\\\Game - R3d Logs\\\\"))
        self.label_2.setText(_translate("Form", "Your Summoner Name:"))
        self.summonerNameInput.setPlaceholderText(_translate("Form", "Dyrus"))
        self.mapButton.setText(_translate("Form", "Get Map!"))
        self.mapButton.clicked.connect(self.displayResults)

    def displayResults(self):
        self.resultDisplay.setText("Rola")

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Ui_Form()
    screen.show()

    sys.exit(app.exec_())
