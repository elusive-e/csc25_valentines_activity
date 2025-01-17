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
from OpenGL import GLU
class MainMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainMainWindow, self).__init__()
        self.score = None
        self.setupUi(self)
        self.mmmm = self.molecule_maker_tab(self)
        self.mf = self.MenuFunctionsss(self)
        
        self.pushButton_14.clicked.connect(self.mmmm.start_bonds)
        self.pushButton_13.clicked.connect(self.mmmm.start_bonds)
        self.pushButton_12.clicked.connect(self.mmmm.start_atoms)
        self.pushButton_11.clicked.connect(self.mmmm.smiles_import)
        self.pushButton_9.clicked.connect(self.mmmm.load_pdbmmmm)
        self.pushButton_10.clicked.connect(self.mmmm.save_file)
        def start_score():
            self.score= 0
        def subtract_score():
            self.score -= 1
        def add_score():
            self.score += 1
        def match():
            if self.score < 2:
                #not a match

            if self.score >= 2:
                #match
                #encrypt a message


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainMainWindow()
    end_dialog.hide()
    window.show()


    sys.exit(app.exec())
