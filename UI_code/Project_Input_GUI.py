# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project_Input_GUI_QT.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Input_window_frm(object):
    def setupUi(self, Input_window_frm):
        Input_window_frm.setObjectName("Input_window_frm")
        Input_window_frm.resize(665, 492)
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
        Input_window_frm.setPalette(palette)
        self.CSU_logo_pic = QtWidgets.QLabel(Input_window_frm)
        self.CSU_logo_pic.setGeometry(QtCore.QRect(170, 20, 311, 161))
        self.CSU_logo_pic.setText("")
        self.CSU_logo_pic.setPixmap(QtGui.QPixmap("csu-logo.jpg"))
        self.CSU_logo_pic.setScaledContents(True)
        self.CSU_logo_pic.setObjectName("CSU_logo_pic")
        self.Welcome_lbl = QtWidgets.QLabel(Input_window_frm)
        self.Welcome_lbl.setGeometry(QtCore.QRect(90, 190, 511, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.Welcome_lbl.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Welcome_lbl.setFont(font)
        self.Welcome_lbl.setObjectName("Welcome_lbl")
        self.InputFilePath_lbl = QtWidgets.QLabel(Input_window_frm)
        self.InputFilePath_lbl.setGeometry(QtCore.QRect(210, 260, 217, 24))
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
        self.InputFilePath_lbl.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.InputFilePath_lbl.setFont(font)
        self.InputFilePath_lbl.setObjectName("InputFilePath_lbl")
        self.lineEdit = QtWidgets.QLineEdit(Input_window_frm)
        self.lineEdit.setGeometry(QtCore.QRect(50, 300, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.Clear_btn = QtWidgets.QPushButton(Input_window_frm)
        self.Clear_btn.setGeometry(QtCore.QRect(80, 410, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Clear_btn.setFont(font)
        self.Clear_btn.setObjectName("Clear_btn")
        self.Continue_btn = QtWidgets.QPushButton(Input_window_frm)
        self.Continue_btn.setGeometry(QtCore.QRect(460, 410, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Continue_btn.setFont(font)
        self.Continue_btn.setObjectName("Continue_btn")

        self.retranslateUi(Input_window_frm)
        QtCore.QMetaObject.connectSlotsByName(Input_window_frm)

    def retranslateUi(self, Input_window_frm):
        _translate = QtCore.QCoreApplication.translate
        Input_window_frm.setWindowTitle(_translate("Input_window_frm", "Class Scheduler Application"))
        self.Welcome_lbl.setText(_translate("Input_window_frm", "Welcome to the Class Scheduler Application"))
        self.InputFilePath_lbl.setText(_translate("Input_window_frm", "Input File Path Below:"))
        self.Clear_btn.setText(_translate("Input_window_frm", "Clear Form"))
        self.Continue_btn.setText(_translate("Input_window_frm", "Continue to Scheduler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Input_window_frm = QtWidgets.QWidget()
    ui = Ui_Input_window_frm()
    ui.setupUi(Input_window_frm)
    Input_window_frm.show()
    sys.exit(app.exec_())
