from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

#This imports the UI Layout code from the Input and Output Python files
from Project_Input_GUI import Ui_Input_window_frm
from Project_Output_GUI import Ui_Output_window_frm

import sys

# This allows this program to access Execel files
import openpyxl

class InputWindow(qtw.QWidget):

    def __init__(self, *args, ** kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Input_window_frm()
        self.ui.setupUi(self)

class OutputWindow(qtw.QWidget):

    def __init__(self, *args, ** kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Output_window_frm()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = qtw.QApplication([])

    inputWindow = InputWindow()
    inputWindow.show()
    outputWindow = OutputWindow()
    outputWindow.show()

    app.exec_()
