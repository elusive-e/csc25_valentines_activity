from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys
#end screen ui
from val_end_layout import Ui_Dialog
#main quiz ui
from val_layout import Ui_Dialog1

class EndDialog(QDialog):
    #ending dialog intiatied 
    def __init__(self):
        # here we make a endialog and apply the ui over it
        super().__init__()
        self.ui2 = Ui_Dialog() 
        self.ui2.setupUi(self)  

class MainMainWindow(QMainWindow):
    #main window!!
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog1() 
        self.ui.setupUi(self)
        #set up score and ending ui
        self.score = 0 
        self.end_dialog = EndDialog()

        #CHANGE YOUR BUTTONS HEREEEEEEEEEEEEEE
        self.ui.answer_12.clicked.connect(self.submit)
        self.ui.answer_1.clicked.connect(self.subtract_score)
        self.ui.answer_2.clicked.connect(self.subtract_score)
        self.ui.answer_3.clicked.connect(self.add_score)
        self.ui.answer_4.clicked.connect(self.add_score)
        self.ui.answer_5.clicked.connect(self.add_score)
        self.ui.answer_6.clicked.connect(self.add_score)
        self.ui.answer_7.clicked.connect(self.subtract_score)
        self.ui.answer_8.clicked.connect(self.subtract_score)
        self.ui.answer_9.clicked.connect(self.add_score)
        self.ui.answer_10.clicked.connect(self.subtract_score)
        self.ui.answer_11.clicked.connect(self.subtract_score)
        self.ui.answer_13.clicked.connect(self.subtract_score)
        self.ui.answer_14.clicked.connect(self.add_score)
        self.ui.answer_15.clicked.connect(self.subtract_score)
        self.ui.answer_16.clicked.connect(self.add_score)

    def submit(self):
        #show end dialog lol
        self.match() 
        self.end_dialog.show()
        self.hide() 
    def add_score(self):
        #adding score
        self.score = self.score+1
    def subtract_score(self):
        #suvrtracting score
        self.score = self.score -1
    def show_answers():
        #"I was the first, i have seen EVERYTHING"
        main_window.show()
    def match(self):
        score = self.score
        if score < 2:
            #call the translate funciton and set the ui
            #ADDD TEXT HEREEEEEEEEEEE
            _translate = QtCore.QCoreApplication.translate
            self.end_dialog.ui2.label.setText(_translate("Dialog", "We\'re not a match!"))
            self.end_dialog.ui2.label_2.setText(_translate("Dialog", "ADDD TEXT HEREEEEEEEEEEE"))
        else:
            # Caesar Cipher logic inspired by oOperaho, likegeeks, and thepythoncode
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            keyword = []
            #gets the name
            name = self.ui.lineEdit.text().strip() 
            key = len(name) 
            message_text = "INSERT YOUR MESSAGE HEREEEEEEEEEEE" 

            if 0 < key <= 26:
                for letter in message_text:
                    #encrypts only the laphabet
                    if letter.isalpha(): 
                        get_letter = (alphabet.index(letter.lower()) + key) % 26  
                        keyword.append(alphabet[get_letter])
                    else: #other stuff added in
                        keyword.append(letter)  

                encrypted_text = "".join(keyword)

            _translate = QtCore.QCoreApplication.translate    
            self.end_dialog.ui2.label.setText(_translate("Dialog", "We\'re a match!"))
            self.end_dialog.ui2.label_2.setText(_translate("Dialog", f"Here is your message from your match: {encrypted_text}"))
            self.end_dialog.ui2.label_3.setText(_translate("Dialog", "Hint: Your encryption key is the length of one of the answers from the quiz!"))
   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainMainWindow()
    main_window.show() 
    end_dialog=EndDialog()
    end_dialog.hide()
    sys.exit(app.exec_())
