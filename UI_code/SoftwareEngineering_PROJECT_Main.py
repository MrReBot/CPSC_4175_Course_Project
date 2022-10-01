from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QTableWidgetItem
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

# Import Eriq's Finalized EXCEL document so it can be displayed in UI
#sys.path.insert(1, '..') # Makes it so we can access Eriq's Excel File
excelOutputFilePath = "" # Path to the output file
excelTemplateFilePath = "../Sandbox/Path To Graduation Template.xlsx" # Template file to base outputs on
sys.path.insert(1, '../Sandbox') # Makes it so we can access Database.py
import excelwriter
#   This allows this program to access Excel files
import pandas as pd
import openpyxl
from openpyxl.formula.translate import Translator


#---------------------------------------------------------------------------------
#   This creates a CLASS that utlizes the Input_GUI python file to contruct the UI
class InputWindow(qtw.QWidget):

    def __init__(self, *args, ** kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Input_window_frm()
        self.ui.setupUi(self)
        self.show()

        #
        #----------- Input UI Widget ACTION Definitions ---------------
        #

        #    When the Continue button is clicked, the program will store the
        #--- text field input as a String called 'inputFilePath'
        self.ui.Continue_btn.clicked.connect(self.storeInputForm)

        #    Then the Clear button is clicked, the program will clear
        #--- the lineEdit field for the InputFilePath_lineEdit
        self.ui.Clear_btn.clicked.connect(self.clearInputForm)


    #
    #----------- Input UI Widget Methods/Functions Definitions ---------------
    #

    #   This will store the 'String' for Input File Location
    #---This defines the functionality of the 'Continue_btn'
    def storeInputForm(self):

        global excelOutputFilePath
        # Making these global so this function can modify them

        # Stores Input for Student ID and Excel Output File Path
        inputStudentID = self.ui.InputStudentID_lineEdit.text()
        inputFilePath = self.ui.InputFilePath_lineEdit.text()
        outputWindow.show()
        inputWindow.hide()
        ew=excelwriter.ExcelWriter()
        st =  Student.Student(db)
        schedule_template = {
        "Fall": 15,
        "Spring": 15,
        "Summer": 3
        }
        schedule, classlist = st.generate_schedule(inputFilePath, schedule_template)
        excelOutputFilePath = f"Path to Graduation {inputStudentID}.xlsx"
        errorcheck = ew.savetofile(schedule,classlist,excelOutputFilePath,excelTemplateFilePath ) # Not sure about what the output filename should be
        print(inputFilePath)
        print(inputStudentID)

    #   This defines the functionality for the "Clear_btn"
    def clearInputForm(self):
        self.ui.InputStudentID_lineEdit.clear()
        self.ui.InputFilePath_lineEdit.clear()





#----------------------------------------------------------------------------------
#   This creates a CLASS that utlizes the Output_GUI python file to contruct the UI
class OutputWindow(qtw.QWidget):

    def __init__(self, *args, ** kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Output_window_frm()
        self.ui.setupUi(self)

        #
        #----------- Output UI Widget ACTION Definitions ---------------
        #

        # When the Generate Button is clicked, the program will pull the Excel
        # --- file and display the data in the QTable in the UI
        self.ui.GenerateSchedule_btn.clicked.connect(self.generateSchedule)
        #self.ui.GenerateSchedule_btn.clicked.connect(lambda _, xL_Path=excelOutputFilePath, sheet_Name='Sheet1': self.generateSchedule(xL_Path, sheet_Name))

        # When Return Button is clicked, the user will return to Main Menu Window
        self.ui.Return_btn.clicked.connect(self.returnToMainMenu)


    #
    #----------- Output UI Widget Methods/Functions Definitions ---------------
    #

    #    This loads the Finalized Excel File into the Outout GUI QTable
    def generateSchedule(self):
    #def generateSchedule(self, excel_file_path , excel_file_name):
        excelWorkbook = openpyxl.load_workbook(excelOutputFilePath)
        excelWorkSheet = excelWorkbook.active


        # Sets Yearly Credit Totals for Spreadsheet in Output UI Table
        # --- Note: This is a workaround because python will not calculate
        # --- Excel formulas

        totalCreditHours = 0
        # --- Year A
        fallYearA_columnTotal = 0
        for i in range(4,11):
            if excelWorkSheet.cell(row=i, column=2).value:
                fallYearA_columnTotal += excelWorkSheet.cell(row=i, column=2).value
            excelWorkSheet.cell(row=11, column=2).value = fallYearA_columnTotal
        totalCreditHours += fallYearA_columnTotal

        springYearA_columnTotal = 0
        for i in range(4,11):
            if excelWorkSheet.cell(row=i, column=4).value:
                springYearA_columnTotal += excelWorkSheet.cell(row=i, column=4).value
            excelWorkSheet.cell(row=11, column=4).value = springYearA_columnTotal
        totalCreditHours += springYearA_columnTotal

        summerYearA_columnTotal = 0
        for i in range(4,6):
            if excelWorkSheet.cell(row=i, column=6).value:
                summerYearA_columnTotal += excelWorkSheet.cell(row=i, column=6).value
            excelWorkSheet.cell(row=6, column=6).value = summerYearA_columnTotal
        totalCreditHours += summerYearA_columnTotal

        #--- Year B
        fallYearB_columnTotal= 0
        for i in range(13,20):
            if excelWorkSheet.cell(row=i, column=2).value:
                fallYearB_columnTotal += excelWorkSheet.cell(row=i, column=2).value
            excelWorkSheet.cell(row=20, column=2).value = fallYearB_columnTotal
        totalCreditHours += fallYearB_columnTotal

        springYearB_columnTotal= 0
        for i in range(13,20):
            if excelWorkSheet.cell(row=i, column=4).value:
                springYearB_columnTotal += excelWorkSheet.cell(row=i, column=4).value
            excelWorkSheet.cell(row=20, column=4).value = springYearB_columnTotal
        totalCreditHours += springYearB_columnTotal

        summerYearB_columnTotal = 0
        for i in range(13,15):
            if excelWorkSheet.cell(row=i, column=6).value:
                summerYearB_columnTotal += excelWorkSheet.cell(row=i, column=6).value
            excelWorkSheet.cell(row=15, column=6).value = summerYearB_columnTotal
        totalCreditHours += summerYearB_columnTotal

        #--- Year C
        fallYearC_columnTotal= 0
        for i in range(22,29):
            if excelWorkSheet.cell(row=i, column=2).value:
                fallYearC_columnTotal += excelWorkSheet.cell(row=i, column=2).value
            excelWorkSheet.cell(row=29, column=2).value = fallYearC_columnTotal
        totalCreditHours += fallYearC_columnTotal

        springYearC_columnTotal= 0
        for i in range(22,29):
            if excelWorkSheet.cell(row=i, column=4).value:
                springYearC_columnTotal += excelWorkSheet.cell(row=i, column=4).value
            excelWorkSheet.cell(row=29, column=4).value = springYearC_columnTotal
        totalCreditHours += springYearC_columnTotal

        summerYearC_columnTotal = 0
        for i in range(22,24):
            if excelWorkSheet.cell(row=i, column=6).value:
                summerYearC_columnTotal += excelWorkSheet.cell(row=i, column=6).value
            excelWorkSheet.cell(row=24, column=6).value = summerYearC_columnTotal
        totalCreditHours += summerYearC_columnTotal

        #--- Year D
        fallYearD_columnTotal= 0
        for i in range(31,38):
            if excelWorkSheet.cell(row=i, column=2).value:
                fallYearD_columnTotal += excelWorkSheet.cell(row=i, column=2).value
            excelWorkSheet.cell(row=38, column=2).value = fallYearD_columnTotal
        totalCreditHours += fallYearD_columnTotal

        springYearD_columnTotal= 0
        for i in range(31,38):
            if excelWorkSheet.cell(row=i, column=4).value:
                springYearD_columnTotal += excelWorkSheet.cell(row=i, column=4).value
            excelWorkSheet.cell(row=38, column=4).value = springYearD_columnTotal
        totalCreditHours += springYearD_columnTotal

        summerYearD_columnTotal = 0
        for i in range(31,33):
            if excelWorkSheet.cell(row=i, column=6).value:
                summerYearD_columnTotal += excelWorkSheet.cell(row=i, column=6).value
            excelWorkSheet.cell(row=33, column=6).value = summerYearD_columnTotal
        totalCreditHours += summerYearD_columnTotal

        # Years A through D Total Credit hours
        excelWorkSheet.cell(row=38, column=6).value = totalCreditHours





        # This portion of code sets the Rows and Columns, also removes NULL cells
        self.ui.SchedulerOutput_tbl.setRowCount(excelWorkSheet .max_row)
        self.ui.SchedulerOutput_tbl.setColumnCount(excelWorkSheet .max_column)

        excelWorkSheet_values_list = list(excelWorkSheet.values)
        self.ui.SchedulerOutput_tbl.setHorizontalHeaderLabels(excelWorkSheet_values_list[0])


        # This portion of code goes through the Excel File and Pulls the Data and Sets Data
        row_Index = 0
        for excelWorkSheet_row in excelWorkSheet_values_list:
            column_Index = 0
            for cell_value in excelWorkSheet_row :
                if cell_value == None:
                    cell_value = ''
                self.ui.SchedulerOutput_tbl.setItem(row_Index, column_Index, QTableWidgetItem(str(cell_value)))
                column_Index += 1
            row_Index += 1


        #finalScheduleOutputGUI = pd.read_excel(excel_file_path , excel_file_name)
        #if finalScheduleOutputGUI.size == 0:
        #    return

        #finalScheduleOutputGUI.fillna('', inplace=True)
        #self.ui.SchedulerOutput_tbl.setRowCount(finalScheduleOutputGUI.shape[0])
        #self.ui.SchedulerOutput_tbl.setColumnCount(finalScheduleOutputGUI.shape[1])
        #self.ui.SchedulerOutput_tbl.setHorizontalHeaderLabels(finalScheduleOutputGUI.columns)

        #for tableRow in finalScheduleOutputGUI.iterrows():
        #    tableRowValues = tableRow[1]
        #    for column_Table_Index, table_row_value in enumerate(tableRowValues):
        #        newTableItem = QTableWidgetItem(str(table_row_value))
        #        self.ui.SchedulerOutput_tbl.setItem(tableRow[0], column_Table_Index, newTableItem)



    #  This handles the 'Return' button functionality
    def returnToMainMenu(self):
        outputWindow.hide()
        inputWindow.show()



# This is the MAIN Application
# --- This creates the Input and Output GUI CLASS objects
# --- This allows the program to run correctly
if __name__ == '__main__':
    app = qtw.QApplication([])

    inputWindow = InputWindow()
    #inputWindow.show()
    outputWindow = OutputWindow()
    #outputWindow.show()

    app.exec_()
