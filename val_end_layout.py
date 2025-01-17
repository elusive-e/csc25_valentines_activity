from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(452, 284)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 1, 1, 1)
        self.match_or_not = QtWidgets.QLabel(Dialog)
        self.match_or_not.setObjectName("match_or_not")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        #ADD SVG
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 5, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 1)
        self.message = QtWidgets.QLabel(Dialog)
        self.message.setObjectName("message")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.hint = QtWidgets.QLabel(Dialog)
        self.hint.setObjectName("hint")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "Make your own"))
        self.match_or_not.setText(_translate("Dialog", "We\'re a match!"))
        self.pushButton.setText(_translate("Dialog", "See your answers"))
        self.message.setText(_translate("Dialog", "Here is your message from your match: \"\""))
        self.hint.setText(_translate("Dialog", "Hint: Your encryption key is the length of one of the answers from the quiz!"))
