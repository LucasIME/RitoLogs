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

        #self.progress = QProgressBar(self)
        #self.progress.setGeometry(200,80,250,20)
        #self.btn =  QPushButton("Download", self)
        #self.btn.move(200,120)
        #self.btn.clicked.connect(self.download)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def download(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LolParser"))
        self.label.setText(_translate("Form", "Path of your Logs Folder:"))
        self.logsPathInput.setPlaceholderText(_translate("Form", "C:\\\\Riot Games\\\\League of Legends\\\\Logs\\\\Game - R3d Logs\\\\"))
        self.label_2.setText(_translate("Form", "Summoner Name:"))
        self.summonerNameInput.setPlaceholderText(_translate("Form", "Dyrus"))
        self.mapButton.setText(_translate("Form", "Parse Logs!"))
        self.mapButton.clicked.connect(self.displayResults)

    def displayResults(self):
        from LogParser import logParser
        import sys
        import codecs
        sys.stdout =  codecs.getwriter("cp852")(sys.stdout.detach())
        logsPath  = self.logsPathInput.text()
        summonerName = self.summonerNameInput.text()
        Parser = logParser(logsPath)
        mapa = Parser.getSortedPlayerChampPairVector(summonerName)
        resultString = ""
        resultString = resultString.join( [ x[0] + ": " +  str(x[1]) + "\n" for x in mapa ] )
        self.resultDisplay.setText(resultString)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    screen = Ui_Form()
    screen.show()
    sys.exit(app.exec_())
