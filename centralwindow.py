# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'centralwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 218)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.decorButton = QtWidgets.QPushButton(self.centralwidget)
        self.decorButton.setGeometry(QtCore.QRect(50, 80, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.decorButton.setFont(font)
        self.decorButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.decorButton.setStyleSheet("QPushButton{\n"
"    border-radius: 6px;\n"
"    background-color: rgb(85, 85, 255);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    border-radius: 6px;\n"
"    background-color: rgb(85, 0, 255);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border-radius: 6px;\n"
"    background-color: #BEB775;\n"
"    color: white;\n"
"}\n"
"")
        self.decorButton.setObjectName("decorButton")
        self.infoButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoButton.setGeometry(QtCore.QRect(260, 80, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.infoButton.setFont(font)
        self.infoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.infoButton.setStyleSheet("QPushButton{\n"
"    border-radius: 6px;\n"
"    background-color: rgb(85, 85, 255);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    border-radius: 6px;\n"
"    background-color: rgb(85, 0, 255);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border-radius: 6px;\n"
"    background-color: #BEB775;\n"
"    color: white;\n"
"}\n"
"")
        self.infoButton.setObjectName("infoButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BusinessAssistant"))
        self.decorButton.setText(_translate("MainWindow", "Оформление тура"))
        self.infoButton.setText(_translate("MainWindow", "Просмотр информации"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
