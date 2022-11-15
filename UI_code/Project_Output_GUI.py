# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project_Output_GUI_QT.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Output_window_frm(object):
    def setupUi(self, Output_window_frm):
        Output_window_frm.setObjectName("Output_window_frm")
        Output_window_frm.setEnabled(True)
        Output_window_frm.resize(665, 492)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Output_window_frm.setPalette(palette)
        self.ViewScheduler_lbl = QtWidgets.QLabel(Output_window_frm)
        self.ViewScheduler_lbl.setGeometry(QtCore.QRect(30, 20, 242, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.ViewScheduler_lbl.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ViewScheduler_lbl.setFont(font)
        self.ViewScheduler_lbl.setObjectName("ViewScheduler_lbl")
        self.Return_btn = QtWidgets.QPushButton(Output_window_frm)
        self.Return_btn.setGeometry(QtCore.QRect(10, 430, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Return_btn.setFont(font)
        self.Return_btn.setObjectName("Return_btn")
        self.Browse_output_filename_btn = QtWidgets.QPushButton(Output_window_frm)
        self.Browse_output_filename_btn.setEnabled(False)
        self.Browse_output_filename_btn.setGeometry(QtCore.QRect(500, 410, 121, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        self.Browse_output_filename_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Browse_output_filename_btn.setFont(font)
        self.Browse_output_filename_btn.setObjectName("Browse_output_filename_btn")
        self.CheckSchedule_btn = QtWidgets.QPushButton(Output_window_frm)
        self.CheckSchedule_btn.setEnabled(False)
        self.CheckSchedule_btn.setGeometry(QtCore.QRect(400, 450, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.CheckSchedule_btn.setFont(font)
        self.CheckSchedule_btn.setObjectName("CheckSchedule_btn")
        self.SchedulerOutput_tbl = QtWidgets.QTableWidget(Output_window_frm)
        self.SchedulerOutput_tbl.setGeometry(QtCore.QRect(30, 50, 601, 281))
        self.SchedulerOutput_tbl.setObjectName("SchedulerOutput_tbl")
        self.SchedulerOutput_tbl.setColumnCount(0)
        self.SchedulerOutput_tbl.setRowCount(0)
        self.GenerateSchedule_btn = QtWidgets.QPushButton(Output_window_frm)
        self.GenerateSchedule_btn.setGeometry(QtCore.QRect(470, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.GenerateSchedule_btn.setFont(font)
        self.GenerateSchedule_btn.setObjectName("GenerateSchedule_btn")
        self.Output_filename_lbl = QtWidgets.QLabel(Output_window_frm)
        self.Output_filename_lbl.setGeometry(QtCore.QRect(500, 350, 120, 18))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.Output_filename_lbl.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Output_filename_lbl.setFont(font)
        self.Output_filename_lbl.setObjectName("Output_filename_lbl")
        self.OutputFilePath_lineEdit = QtWidgets.QLineEdit(Output_window_frm)
        self.OutputFilePath_lineEdit.setGeometry(QtCore.QRect(110, 370, 511, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.OutputFilePath_lineEdit.setFont(font)
        self.OutputFilePath_lineEdit.setObjectName("OutputFilePath_lineEdit")
        self.CheckForPreReiqErrors_lbl = QtWidgets.QLabel(Output_window_frm)
        self.CheckForPreReiqErrors_lbl.setGeometry(QtCore.QRect(110, 340, 291, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.CheckForPreReiqErrors_lbl.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.CheckForPreReiqErrors_lbl.setFont(font)
        self.CheckForPreReiqErrors_lbl.setObjectName("CheckForPreReiqErrors_lbl")
        self.OpenExcelFile_btn = QtWidgets.QPushButton(Output_window_frm)
        self.OpenExcelFile_btn.setEnabled(False)
        self.OpenExcelFile_btn.setGeometry(QtCore.QRect(200, 450, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.OpenExcelFile_btn.setFont(font)
        self.OpenExcelFile_btn.setObjectName("OpenExcelFile_btn")

        self.retranslateUi(Output_window_frm)
        QtCore.QMetaObject.connectSlotsByName(Output_window_frm)

    def retranslateUi(self, Output_window_frm):
        _translate = QtCore.QCoreApplication.translate
        Output_window_frm.setWindowTitle(_translate("Output_window_frm", "Class Scheduler Application"))
        self.ViewScheduler_lbl.setText(_translate("Output_window_frm", "Schedule for Student"))
        self.Return_btn.setText(_translate("Output_window_frm", "Return to \n"
"Main Menu"))
        self.Browse_output_filename_btn.setText(_translate("Output_window_frm", "Browse"))
        self.CheckSchedule_btn.setText(_translate("Output_window_frm", "Check for Prerequiste Errors"))
        self.GenerateSchedule_btn.setText(_translate("Output_window_frm", "Generate Schedule"))
        self.Output_filename_lbl.setText(_translate("Output_window_frm", "File Destination"))
        self.CheckForPreReiqErrors_lbl.setText(_translate("Output_window_frm", "Choose File to check for errors"))
        self.OpenExcelFile_btn.setText(_translate("Output_window_frm", "Open Schedule in Excel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Output_window_frm = QtWidgets.QWidget()
    ui = Ui_Output_window_frm()
    ui.setupUi(Output_window_frm)
    Output_window_frm.show()
    sys.exit(app.exec_())
