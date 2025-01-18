from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSvg import QSvgWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_end_Screen(object):
    def setupUi(self, end_Screen):
        end_Screen.setObjectName("end_Screen")
        end_Screen.resize(452, 284)
        self.gridLayout = QtWidgets.QGridLayout(end_Screen)
        self.gridLayout.setObjectName("gridLayout")
        self.hint = QtWidgets.QLabel(end_Screen)
        self.hint.setObjectName("hint")
        self.gridLayout.addWidget(self.hint, 2, 0, 1, 2)
        self.makeurown = QtWidgets.QPushButton(end_Screen)
        self.makeurown.setObjectName("makeurown")
        self.gridLayout.addWidget(self.makeurown, 4, 1, 1, 1)
        self.message = QtWidgets.QLabel(end_Screen)
        self.message.setObjectName("message")
        self.gridLayout.addWidget(self.message, 1, 0, 1, 2)
        self.match = QtWidgets.QLabel(end_Screen)
        self.match.setObjectName("match")
        self.gridLayout.addWidget(self.match, 0, 0, 1, 1)
        #ellie's svg is from goodfreephotos.com
        self.graphicsView = QSvgWidget("final658-heart-in-heart.svg",end_Dialog)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 5, 0, 1, 2)
        self.see_answers = QtWidgets.QPushButton(end_Screen)
        self.see_answers.setObjectName("see_answers")
        self.gridLayout.addWidget(self.see_answers, 4, 0, 1, 1)

        self.retranslateUi(end_Screen)
        QtCore.QMetaObject.connectSlotsByName(end_Screen)

    def retranslateUi(self, end_Screen):
        _translate = QtCore.QCoreApplication.translate
        end_Screen.setWindowTitle(_translate("end_Screen", "Dialog"))
        self.hint.setText(_translate("end_Screen", "Hint: Your encryption key is the length of one of the answers from the quiz!"))
        self.makeurown.setText(_translate("end_Screen", "Make your own"))
        self.message.setText(_translate("end_Screen", "Here is your message from your match: \"\""))
        self.match.setText(_translate("end_Screen", "We\'re a match!"))
        self.see_answers.setText(_translate("end_Screen", "See your answers"))
