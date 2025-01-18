# mark clearly where the questions and answers are
#add encryption logic
#add different encruption methods???
#add the logic for see your answers and make your own
#add a fully finished example
#reaplce textbox with svg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QDialog, QDialogButtonBox, QMessageBox
from PyQt5 import QtOpenGL
from PyQt5 import QtWidgets
from val_end_layout import Ui_end_Screen
import numpy as np
import random
import sys
import re
import subprocess
from val_layout import valwindow
class MainWindow(QtWidgets.QMainWindow, valwindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.score = None
        self.setupUi(self)
        self.sk = self.score_keeping(self)
        #self.mf = self.MenuFunctionsss(self)
        self.answer_1.clicked.connect(self.sk.subtract_score)
        self.answer_2.clicked.connect(self.sk.subtract_score)
        self.submit_button.clicked.connect(self.submit)
        self.answer_3.clicked.connect(self.sk.subtract_score)
        self.answer_4.clicked.connect(self.sk.subtract_score)
        self.answer_5.clicked.connect(self.sk.subtract_score)
        self.answer_6.clicked.connect(self.sk.subtract_score)
        self.answer_7.clicked.connect(self.sk.subtract_score)
        self.answer_8.clicked.connect(self.sk.subtract_score)
        self.answer_9.clicked.connect(self.sk.subtract_score)
        self.answer_10.clicked.connect(self.sk.subtract_score)
        self.answer_11.clicked.connect(self.sk.subtract_score)
        self.answer_12.clicked.connect(self.sk.subtract_score)
        self.answer_13.clicked.connect(self.sk.subtract_score)
        self.answer_14.clicked.connect(self.sk.subtract_score)
        self.answer_15.clicked.connect(self.sk.subtract_score)
        self.answer_16.clicked.connect(self.sk.subtract_score)
        class score_keeping:
            def __init__(self, MainWindow):
                self.MainWindow = MainWindow
                self.score = None
            def start_score(self):
                self.score= 0
                return score
            def subtract_score(self):
                self.score -= 1
                return score
            def add_score(self):
                self.score += 1
                return score
            def submit(self):
                end_dialog.show()
                intro_window.hide()
                self.match()
            def show_answers(self):
                intro_window.show()
                def match():
                    if self.score < 2:
                        pass
                    
                        #not a match
                #add actual use later
               # self.match_or_not.setText(_translate("Dialog", "We\'re a match!"))
                #self.message.setText(_translate("Dialog", "Here is your message from your match: \"\""))
                  #  self.hint.setText(_translate("Dialog", "Hint: Your encryption key is the length of one of the answers from the quiz!"))
                    
                    else:
                        #match
                        #Adapted from Ceaser Cipher code by oOperaho
                        alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
                        get_letter, keyword = 0, []
                        #change input code
                        text = str(input("Enter the text: ")).strip().lower()
                        #change the key code 
                        key = int(input("Enter the key: "))
# 
#             if 0 < key <= 26:
#                 for letter in text:
#                     get_letter = alphabet.index(letter) + key	
#                     keyword.append(alphabet[get_letter])
#                 print("".join(keyword))
#             else:
#                 print("Key must be between 1 and 26!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    intro_window = MainWindow()
    end_dialog = Ui_end_Screen()
    intro_window.show()


    sys.exit(app.exec())
