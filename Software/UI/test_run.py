# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RootPendantUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RootPendant_Main(object):
    def setupUi(self, RootPendant_Main):
        RootPendant_Main.setObjectName("RootPendant_Main")
        RootPendant_Main.setEnabled(True)
        RootPendant_Main.resize(240, 320)
        RootPendant_Main.setMinimumSize(QtCore.QSize(240, 320))
        RootPendant_Main.setMaximumSize(QtCore.QSize(240, 320))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(102, 153, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 179, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 153, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 153, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 153, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 29, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 153, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 179, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 153, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 153, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 153, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 29, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 179, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 153, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 29, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 29, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 179, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        RootPendant_Main.setPalette(palette)
        self.RootPendant_Widget = QtWidgets.QWidget(RootPendant_Main)
        self.RootPendant_Widget.setObjectName("RootPendant_Widget")
        self.DRO_X_WCO = QtWidgets.QLCDNumber(self.RootPendant_Widget)
        self.DRO_X_WCO.setGeometry(QtCore.QRect(20, 40, 91, 31))
        self.DRO_X_WCO.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DRO_X_WCO.setDigitCount(7)
        self.DRO_X_WCO.setProperty("value", 10000.0)
        self.DRO_X_WCO.setProperty("intValue", 10000)
        self.DRO_X_WCO.setObjectName("DRO_X_WCO")
        self.pushButton = QtWidgets.QPushButton(self.RootPendant_Widget)
        self.pushButton.setGeometry(QtCore.QRect(70, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.DRO_X_M = QtWidgets.QLCDNumber(self.RootPendant_Widget)
        self.DRO_X_M.setGeometry(QtCore.QRect(40, 70, 71, 21))
        self.DRO_X_M.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DRO_X_M.setDigitCount(7)
        self.DRO_X_M.setProperty("value", 10000.0)
        self.DRO_X_M.setProperty("intValue", 10000)
        self.DRO_X_M.setObjectName("DRO_X_M")
        self.X_AXIS = QtWidgets.QLabel(self.RootPendant_Widget)
        self.X_AXIS.setGeometry(QtCore.QRect(0, 50, 16, 16))
        self.X_AXIS.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.X_AXIS.setObjectName("X_AXIS")
        self.X_AXIS_2 = QtWidgets.QLabel(self.RootPendant_Widget)
        self.X_AXIS_2.setGeometry(QtCore.QRect(0, 100, 16, 16))
        self.X_AXIS_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.X_AXIS_2.setObjectName("X_AXIS_2")
        self.DRO_Y_M = QtWidgets.QLCDNumber(self.RootPendant_Widget)
        self.DRO_Y_M.setGeometry(QtCore.QRect(40, 120, 71, 21))
        self.DRO_Y_M.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DRO_Y_M.setDigitCount(7)
        self.DRO_Y_M.setProperty("value", 10000.0)
        self.DRO_Y_M.setProperty("intValue", 10000)
        self.DRO_Y_M.setObjectName("DRO_Y_M")
        self.DRO_Y_WCO = QtWidgets.QLCDNumber(self.RootPendant_Widget)
        self.DRO_Y_WCO.setGeometry(QtCore.QRect(20, 90, 91, 31))
        self.DRO_Y_WCO.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DRO_Y_WCO.setDigitCount(7)
        self.DRO_Y_WCO.setProperty("value", 10000.0)
        self.DRO_Y_WCO.setProperty("intValue", 10000)
        self.DRO_Y_WCO.setObjectName("DRO_Y_WCO")
        self.X_AXIS_3 = QtWidgets.QLabel(self.RootPendant_Widget)
        self.X_AXIS_3.setGeometry(QtCore.QRect(0, 150, 16, 16))
        self.X_AXIS_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.X_AXIS_3.setObjectName("X_AXIS_3")
        self.DRO_Z_M = QtWidgets.QLCDNumber(self.RootPendant_Widget)
        self.DRO_Z_M.setGeometry(QtCore.QRect(40, 170, 71, 21))
        self.DRO_Z_M.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DRO_Z_M.setDigitCount(7)
        self.DRO_Z_M.setProperty("value", 10000.0)
        self.DRO_Z_M.setProperty("intValue", 10000)
        self.DRO_Z_M.setObjectName("DRO_Z_M")
        self.DRO_Z_WCO = QtWidgets.QLCDNumber(self.RootPendant_Widget)
        self.DRO_Z_WCO.setGeometry(QtCore.QRect(20, 140, 91, 31))
        self.DRO_Z_WCO.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DRO_Z_WCO.setDigitCount(7)
        self.DRO_Z_WCO.setProperty("value", 10000.0)
        self.DRO_Z_WCO.setProperty("intValue", 10000)
        self.DRO_Z_WCO.setObjectName("DRO_Z_WCO")
        self.X_AXIS_4 = QtWidgets.QLabel(self.RootPendant_Widget)
        self.X_AXIS_4.setGeometry(QtCore.QRect(110, 50, 16, 16))
        self.X_AXIS_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.X_AXIS_4.setObjectName("X_AXIS_4")
        self.DRO_A_M = QtWidgets.QLCDNumber(self.RootPendant_Widget)
        self.DRO_A_M.setGeometry(QtCore.QRect(150, 70, 71, 21))
        self.DRO_A_M.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DRO_A_M.setDigitCount(7)
        self.DRO_A_M.setProperty("value", 10000.0)
        self.DRO_A_M.setProperty("intValue", 10000)
        self.DRO_A_M.setObjectName("DRO_A_M")
        self.DRO_A_WCO = QtWidgets.QLCDNumber(self.RootPendant_Widget)
        self.DRO_A_WCO.setGeometry(QtCore.QRect(130, 40, 91, 31))
        self.DRO_A_WCO.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DRO_A_WCO.setDigitCount(7)
        self.DRO_A_WCO.setProperty("value", 10000.0)
        self.DRO_A_WCO.setProperty("intValue", 10000)
        self.DRO_A_WCO.setObjectName("DRO_A_WCO")
        self.X_AXIS_5 = QtWidgets.QLabel(self.RootPendant_Widget)
        self.X_AXIS_5.setGeometry(QtCore.QRect(110, 100, 16, 16))
        self.X_AXIS_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.X_AXIS_5.setObjectName("X_AXIS_5")
        self.DRO_B_M = QtWidgets.QLCDNumber(self.RootPendant_Widget)
        self.DRO_B_M.setGeometry(QtCore.QRect(150, 120, 71, 21))
        self.DRO_B_M.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DRO_B_M.setDigitCount(7)
        self.DRO_B_M.setProperty("value", 10000.0)
        self.DRO_B_M.setProperty("intValue", 10000)
        self.DRO_B_M.setObjectName("DRO_B_M")
        self.DRO_B_WCO = QtWidgets.QLCDNumber(self.RootPendant_Widget)
        self.DRO_B_WCO.setGeometry(QtCore.QRect(130, 90, 91, 31))
        self.DRO_B_WCO.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DRO_B_WCO.setDigitCount(7)
        self.DRO_B_WCO.setProperty("value", 10000.0)
        self.DRO_B_WCO.setProperty("intValue", 10000)
        self.DRO_B_WCO.setObjectName("DRO_B_WCO")
        self.X_AXIS_6 = QtWidgets.QLabel(self.RootPendant_Widget)
        self.X_AXIS_6.setGeometry(QtCore.QRect(110, 150, 16, 16))
        self.X_AXIS_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.X_AXIS_6.setObjectName("X_AXIS_6")
        self.DRO_C_M = QtWidgets.QLCDNumber(self.RootPendant_Widget)
        self.DRO_C_M.setGeometry(QtCore.QRect(150, 170, 71, 21))
        self.DRO_C_M.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DRO_C_M.setDigitCount(7)
        self.DRO_C_M.setProperty("value", 10000.0)
        self.DRO_C_M.setProperty("intValue", 10000)
        self.DRO_C_M.setObjectName("DRO_C_M")
        self.DRO_C_WCO = QtWidgets.QLCDNumber(self.RootPendant_Widget)
        self.DRO_C_WCO.setGeometry(QtCore.QRect(130, 140, 91, 31))
        self.DRO_C_WCO.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DRO_C_WCO.setDigitCount(7)
        self.DRO_C_WCO.setProperty("value", 10000.0)
        self.DRO_C_WCO.setProperty("intValue", 10000)
        self.DRO_C_WCO.setObjectName("DRO_C_WCO")
        self.STATUS = QtWidgets.QLabel(self.RootPendant_Widget)
        self.STATUS.setGeometry(QtCore.QRect(20, 20, 201, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.STATUS.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.STATUS.setFont(font)
        self.STATUS.setAutoFillBackground(True)
        self.STATUS.setAlignment(QtCore.Qt.AlignCenter)
        self.STATUS.setObjectName("STATUS")
        self.Close = QtWidgets.QPushButton(self.RootPendant_Widget)
        self.Close.setGeometry(QtCore.QRect(80, 260, 75, 23))
        self.Close.setObjectName("Close")
        self.SETTINGS_BUT = QtWidgets.QToolButton(self.RootPendant_Widget)
        self.SETTINGS_BUT.setGeometry(QtCore.QRect(0, 0, 25, 19))
        self.SETTINGS_BUT.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.SETTINGS_BUT.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.SETTINGS_BUT.setAutoRaise(True)
        self.SETTINGS_BUT.setObjectName("SETTINGS_BUT")
        RootPendant_Main.setCentralWidget(self.RootPendant_Widget)
        self.statusbar = QtWidgets.QStatusBar(RootPendant_Main)
        self.statusbar.setObjectName("statusbar")
        RootPendant_Main.setStatusBar(self.statusbar)

        self.retranslateUi(RootPendant_Main)
        QtCore.QMetaObject.connectSlotsByName(RootPendant_Main)

    def retranslateUi(self, RootPendant_Main):
        _translate = QtCore.QCoreApplication.translate
        RootPendant_Main.setWindowTitle(_translate("RootPendant_Main", "MainWindow"))
        self.pushButton.setText(_translate("RootPendant_Main", "PushButton"))
        self.X_AXIS.setText(_translate("RootPendant_Main", "X"))
        self.X_AXIS_2.setText(_translate("RootPendant_Main", "Y"))
        self.X_AXIS_3.setText(_translate("RootPendant_Main", "Z"))
        self.X_AXIS_4.setText(_translate("RootPendant_Main", "A"))
        self.X_AXIS_5.setText(_translate("RootPendant_Main", "B"))
        self.X_AXIS_6.setText(_translate("RootPendant_Main", "C"))
        self.STATUS.setText(_translate("RootPendant_Main", "OFFLINE"))
        self.Close.setText(_translate("RootPendant_Main", "close"))
        self.SETTINGS_BUT.setText(_translate("RootPendant_Main", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RootPendant_Main = QtWidgets.QMainWindow()
    ui = Ui_RootPendant_Main()
    ui.setupUi(RootPendant_Main)
    RootPendant_Main.show()
    sys.exit(app.exec_())
