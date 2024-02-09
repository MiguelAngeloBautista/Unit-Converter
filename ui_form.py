# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 430)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 431, 361))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(330, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.initialValue = QtWidgets.QDoubleSpinBox(parent=self.groupBox_2)
        self.initialValue.setGeometry(QtCore.QRect(10, 50, 101, 41))
        self.initialValue.setDecimals(10)
        self.initialValue.setMinimum(0.0)
        self.initialValue.setMaximum(9999999999999.0)
        self.initialValue.setObjectName("initialValue")
        self.label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 30, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(50, 150, 171, 16))
        self.label_5.setObjectName("label_5")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.groupBox_2)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(70, 170, 281, 91))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.cb_initial = QtWidgets.QComboBox(parent=self.tab)
        self.cb_initial.setEnabled(True)
        self.cb_initial.setGeometry(QtCore.QRect(10, 20, 91, 24))
        self.cb_initial.setFrame(True)
        self.cb_initial.setObjectName("cb_initial")
        self.cb_initial.addItem("")
        self.cb_initial.addItem("")
        self.cb_initial.addItem("")
        self.cb_initial.addItem("")
        self.cb_initial.addItem("")
        self.cb_initial.addItem("")
        self.cb_initial.addItem("")
        self.cb_initial.addItem("")
        self.cb_convert = QtWidgets.QComboBox(parent=self.tab)
        self.cb_convert.setEnabled(True)
        self.cb_convert.setGeometry(QtCore.QRect(181, 20, 91, 24))
        self.cb_convert.setFrame(True)
        self.cb_convert.setObjectName("cb_convert")
        self.cb_convert.addItem("")
        self.cb_convert.addItem("")
        self.cb_convert.addItem("")
        self.cb_convert.addItem("")
        self.cb_convert.addItem("")
        self.cb_convert.addItem("")
        self.cb_convert.addItem("")
        self.cb_convert.addItem("")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(130, 300, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.convertedValue = QtWidgets.QDoubleSpinBox(parent=self.groupBox_2)
        self.convertedValue.setGeometry(QtCore.QRect(310, 50, 111, 41))
        self.convertedValue.setDecimals(10)
        self.convertedValue.setMinimum(0.0)
        self.convertedValue.setMaximum(9999999999999.0)
        self.convertedValue.setObjectName("convertedValue")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 455, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_2.setText(_translate("MainWindow", "Converted"))
        self.label.setText(_translate("MainWindow", "Initial"))
        self.label_5.setText(_translate("MainWindow", "Choose unit types"))
        self.cb_initial.setItemText(0, _translate("MainWindow", "Kilometer"))
        self.cb_initial.setItemText(1, _translate("MainWindow", "Meter"))
        self.cb_initial.setItemText(2, _translate("MainWindow", "Centimeter"))
        self.cb_initial.setItemText(3, _translate("MainWindow", "Millimeter"))
        self.cb_initial.setItemText(4, _translate("MainWindow", "Mile"))
        self.cb_initial.setItemText(5, _translate("MainWindow", "Yard"))
        self.cb_initial.setItemText(6, _translate("MainWindow", "Foot"))
        self.cb_initial.setItemText(7, _translate("MainWindow", "Inch"))
        self.cb_convert.setItemText(0, _translate("MainWindow", "Kilometer"))
        self.cb_convert.setItemText(1, _translate("MainWindow", "Meter"))
        self.cb_convert.setItemText(2, _translate("MainWindow", "Centimeter"))
        self.cb_convert.setItemText(3, _translate("MainWindow", "Millimeter"))
        self.cb_convert.setItemText(4, _translate("MainWindow", "Mile"))
        self.cb_convert.setItemText(5, _translate("MainWindow", "Yard"))
        self.cb_convert.setItemText(6, _translate("MainWindow", "Foot"))
        self.cb_convert.setItemText(7, _translate("MainWindow", "Inch"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "DIstance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Temperature"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Speed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Weight"))
        self.pushButton.setText(_translate("MainWindow", "Convert"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())