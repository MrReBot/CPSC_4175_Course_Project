from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

#This imports the UI Layout code from the Input and Output Python files
from Project_Input_GUI import Ui_Input_window_frm
from Project_Output_GUI import Ui_Output_window_frm

import sys
# Import Brandon's Student Class to be able to call his Python program
sys.path.insert(1, '..') # Makes it so we can access Database.py
import Database
db = Database.Database("../database.txt")
import Student

#   This allows this program to access Excel files
import openpyxl as xl


#---------------------------------------------------------------------------------
#   This creates a class that utlizes the Input_GUI python file to contruct the UI
class InputWindow(qtw.QWidget):

    def __init__(self, *args, ** kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Input_window_frm()
        self.ui.setupUi(self)

        #
        #----------- Input UI Widget ACTION Definitions ---------------
        #

        #    When the Continue button is clicked, the program will store the
        #--- text field input as a String called 'inputFilePath'
        self.ui.Continue_btn.clicked.connect(self.storeInputFilePath)

        #    Then the Clear button is clicked, the program will clear
        #--- the lineEdit field for the InputFilePath_lineEdit
        self.ui.Clear_btn.clicked.connect(self.clearInputForm)


    #
    #----------- Input UI Widget Methods/Functions Definitions ---------------
    #

    #   This will store the 'String' for Input File Location
    #---This defines the functionality of the 'Continue_btn'
    def storeInputFilePath(self):
        inputFilePath = self.ui.InputFilePath_lineEdit.text()
        outputWindow.show()
        inputWindow.hide()
        st =  Student.Student(db, filename = inputFilePath)

        print(inputFilePath)

    #   This defines the functionality for the "Clear_btn"
    def clearInputForm(self):
        self.ui.InputFilePath_lineEdit.clear()





#----------------------------------------------------------------------------------
#   This creates a class that utlizes the Output_GUI python file to contruct the UI
class OutputWindow(qtw.QWidget):

    def __init__(self, *args, ** kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Output_window_frm()
        self.ui.setupUi(self)


        #
        #----------- Output UI Widget ACTION Definitions ---------------
        #

        # When Return button is clicked, the user will return to Main Menu Window
        self.ui.Return_btn.clicked.connect(self.returnToMainMenu)


    #
    #----------- Output UI Widget Methods/Functions Definitions ---------------
    #

    def returnToMainMenu(self):
        outputWindow.hide()
        inputWindow.show()

    #    This loads the Finalized Excel File into the Outout GUI Screen's Table
    def displaySchedule(self):
        print('It works')
    #    self.ui.SchedulerOutput_tbl




# This is the MAIN Application
# --- This creates the Input and Output GUI CLASS objects
# --- This allows the program to run correctly
if __name__ == '__main__':
    app = qtw.QApplication([])

    inputWindow = InputWindow()
    inputWindow.show()
    outputWindow = OutputWindow()
    #outputWindow.show()

    app.exec_()
