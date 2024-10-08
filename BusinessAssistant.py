# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BusinessAssistant.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(485, 246)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.newClientButton = QtWidgets.QPushButton(self.centralwidget)
        self.newClientButton.setGeometry(QtCore.QRect(60, 50, 181, 50))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.newClientButton.setFont(font)
        self.newClientButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newClientButton.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    border-radius: 6px;\n"
"    background-color: rgbrgb(240, 255, 255);\n"
"    color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border-radius: 6px;\n"
"    background-color: #BEB775;\n"
"    color: black;\n"
"}\n"
"")
        self.newClientButton.setObjectName("newClientButton")
        self.viewClientButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewClientButton.setGeometry(QtCore.QRect(260, 50, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.viewClientButton.setFont(font)
        self.viewClientButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.viewClientButton.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    border-radius: 6px;\n"
"    background-color: rgbrgb(240, 255, 255);\n"
"    color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border-radius: 6px;\n"
"    background-color: #BEB775;\n"
"    color: black;\n"
"}\n"
"")
        self.viewClientButton.setObjectName("viewClientButton")
        self.dealButton = QtWidgets.QPushButton(self.centralwidget)
        self.dealButton.setGeometry(QtCore.QRect(60, 110, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dealButton.setFont(font)
        self.dealButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dealButton.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    border-radius: 6px;\n"
"    background-color: rgbrgb(240, 255, 255);\n"
"    color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border-radius: 6px;\n"
"    background-color: #BEB775;\n"
"    color: black;\n"
"}\n"
"")
        self.dealButton.setObjectName("dealButton")
        self.returnButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnButton.setGeometry(QtCore.QRect(260, 110, 181, 50))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.returnButton.setFont(font)
        self.returnButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.returnButton.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    border-radius: 6px;\n"
"    background-color: rgbrgb(240, 255, 255);\n"
"    color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border-radius: 6px;\n"
"    background-color: #BEB775;\n"
"    color: black;\n"
"}\n"
"")
        self.returnButton.setObjectName("returnButton")
        self.salesButton = QtWidgets.QPushButton(self.centralwidget)
        self.salesButton.setGeometry(QtCore.QRect(160, 170, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.salesButton.setFont(font)
        self.salesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.salesButton.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    border-radius: 6px;\n"
"    background-color: rgbrgb(240, 255, 255);\n"
"    color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border-radius: 6px;\n"
"    background-color: #BEB775;\n"
"    color: black;\n"
"}\n"
"")
        self.salesButton.setObjectName("salesButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BusinessAssistant"))
        self.newClientButton.setText(_translate("MainWindow", "Новый клиент"))
        self.viewClientButton.setText(_translate("MainWindow", "Просмотр клиентов"))
        self.dealButton.setText(_translate("MainWindow", "Оформление сделки"))
        self.returnButton.setText(_translate("MainWindow", "Возврат тура"))
        self.salesButton.setText(_translate("MainWindow", "Список продаж"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
