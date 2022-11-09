# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project_Settings_GUI_QT.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings_window_frm(object):
    def setupUi(self, Settings_window_frm):
        Settings_window_frm.setObjectName("Settings_window_frm")
        Settings_window_frm.resize(332, 246)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 102, 235))
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
        Settings_window_frm.setPalette(palette)
        self.Manual_selection_checkBox = QtWidgets.QCheckBox(Settings_window_frm)
        self.Manual_selection_checkBox.setGeometry(QtCore.QRect(20, 20, 217, 22))
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
        self.Manual_selection_checkBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Manual_selection_checkBox.setFont(font)
        self.Manual_selection_checkBox.setChecked(True)
        self.Manual_selection_checkBox.setObjectName("Manual_selection_checkBox")
        self.Set_credit_limits_checkBox = QtWidgets.QCheckBox(Settings_window_frm)
        self.Set_credit_limits_checkBox.setGeometry(QtCore.QRect(20, 60, 151, 22))
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
        self.Set_credit_limits_checkBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Set_credit_limits_checkBox.setFont(font)
        self.Set_credit_limits_checkBox.setChecked(False)
        self.Set_credit_limits_checkBox.setObjectName("Set_credit_limits_checkBox")
        self.Fall_credits_lbl = QtWidgets.QLabel(Settings_window_frm)
        self.Fall_credits_lbl.setGeometry(QtCore.QRect(20, 100, 88, 18))
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
        self.Fall_credits_lbl.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Fall_credits_lbl.setFont(font)
        self.Fall_credits_lbl.setObjectName("Fall_credits_lbl")
        self.Spring_credits_lbl = QtWidgets.QLabel(Settings_window_frm)
        self.Spring_credits_lbl.setGeometry(QtCore.QRect(20, 130, 111, 18))
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
        self.Spring_credits_lbl.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Spring_credits_lbl.setFont(font)
        self.Spring_credits_lbl.setObjectName("Spring_credits_lbl")
        self.Summer_credits_lbl = QtWidgets.QLabel(Settings_window_frm)
        self.Summer_credits_lbl.setGeometry(QtCore.QRect(20, 160, 124, 18))
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
        self.Summer_credits_lbl.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Summer_credits_lbl.setFont(font)
        self.Summer_credits_lbl.setObjectName("Summer_credits_lbl")
        self.lineEdit = QtWidgets.QLineEdit(Settings_window_frm)
        self.lineEdit.setGeometry(QtCore.QRect(170, 100, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Settings_window_frm)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 130, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Settings_window_frm)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 160, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.Exit_btn = QtWidgets.QPushButton(Settings_window_frm)
        self.Exit_btn.setGeometry(QtCore.QRect(10, 210, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Exit_btn.setFont(font)
        self.Exit_btn.setObjectName("Exit_btn")
        self.Help_btn = QtWidgets.QPushButton(Settings_window_frm)
        self.Help_btn.setGeometry(QtCore.QRect(240, 210, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Help_btn.setFont(font)
        self.Help_btn.setObjectName("Help_btn")

        self.retranslateUi(Settings_window_frm)
        QtCore.QMetaObject.connectSlotsByName(Settings_window_frm)

    def retranslateUi(self, Settings_window_frm):
        _translate = QtCore.QCoreApplication.translate
        Settings_window_frm.setWindowTitle(_translate("Settings_window_frm", "Settings"))
        self.Manual_selection_checkBox.setText(_translate("Settings_window_frm", "Manually Select Electives"))
        self.Set_credit_limits_checkBox.setText(_translate("Settings_window_frm", "Set Credit Limits"))
        self.Fall_credits_lbl.setText(_translate("Settings_window_frm", "Fall Credits"))
        self.Spring_credits_lbl.setText(_translate("Settings_window_frm", "Spring Credits"))
        self.Summer_credits_lbl.setText(_translate("Settings_window_frm", "Summer Credits"))
        self.Exit_btn.setText(_translate("Settings_window_frm", "Exit"))
        self.Help_btn.setText(_translate("Settings_window_frm", "Help"))
        
    def get_values(self):
        """Return the Settings as a dictionary"""
        try:
            return {
            "Set_Credits" : self.Set_credit_limits_checkBox.isChecked(),
            "Manual Elective": self.Manual_selection_checkBox.isChecked(),
            "Credits" : {
                "Fall" : int(self.lineEdit.text()),
                "Spring": int(self.lineEdit_2.text()),
                "Summer": int(self.lineEdit_3.text())
            }
            }
        except ValueError:
            return {
                "Set_Credits" : self.Set_credit_limits_checkBox.isChecked(),
                "Manual Elective": self.Manual_selection_checkBox.isChecked(),
                "Credits" : {
                    "Fall" : 0,
                    "Spring": 0,
                    "Summer": 0
                }
                }
    
    def validate_values(self):
        """Check if the settings menu has valid values"""
        credit_hours = [self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text()]
        for hour in credit_hours:
            if not hour.isnumeric():
                return False
        return True
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings_window_frm = QtWidgets.QWidget()
    ui = Ui_Settings_window_frm()
    ui.setupUi(Settings_window_frm)
    Settings_window_frm.show()
    sys.exit(app.exec_())
