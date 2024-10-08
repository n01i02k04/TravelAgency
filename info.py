# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 407)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cityButton = QtWidgets.QPushButton(self.centralwidget)
        self.cityButton.setGeometry(QtCore.QRect(250, 90, 201, 50))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cityButton.setFont(font)
        self.cityButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cityButton.setStyleSheet("\n"
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
        self.cityButton.setObjectName("cityButton")
        self.typesButton = QtWidgets.QPushButton(self.centralwidget)
        self.typesButton.setGeometry(QtCore.QRect(250, 150, 201, 50))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.typesButton.setFont(font)
        self.typesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.typesButton.setStyleSheet("\n"
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
        self.typesButton.setObjectName("typesButton")
        self.nutritionButton = QtWidgets.QPushButton(self.centralwidget)
        self.nutritionButton.setGeometry(QtCore.QRect(150, 210, 201, 50))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.nutritionButton.setFont(font)
        self.nutritionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nutritionButton.setStyleSheet("\n"
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
        self.nutritionButton.setObjectName("nutritionButton")
        self.hotelsButton = QtWidgets.QPushButton(self.centralwidget)
        self.hotelsButton.setGeometry(QtCore.QRect(50, 150, 191, 50))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.hotelsButton.setFont(font)
        self.hotelsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hotelsButton.setStyleSheet("\n"
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
        self.hotelsButton.setObjectName("hotelsButton")
        self.tableShow = QtWidgets.QTableView(self.centralwidget)
        self.tableShow.setGeometry(QtCore.QRect(510, 10, 400, 371))
        self.tableShow.setObjectName("tableShow")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(150, 280, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet("QPushButton{\n"
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
        self.exitButton.setObjectName("exitButton")
        self.countryButton = QtWidgets.QPushButton(self.centralwidget)
        self.countryButton.setGeometry(QtCore.QRect(50, 90, 191, 50))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.countryButton.setFont(font)
        self.countryButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.countryButton.setStyleSheet("\n"
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
        self.countryButton.setObjectName("countryButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BusinessAssistant"))
        self.cityButton.setText(_translate("MainWindow", "Города"))
        self.typesButton.setText(_translate("MainWindow", "Типы туров"))
        self.nutritionButton.setText(_translate("MainWindow", "Типы питания"))
        self.hotelsButton.setText(_translate("MainWindow", "Отели"))
        self.exitButton.setText(_translate("MainWindow", "Выход"))
        self.countryButton.setText(_translate("MainWindow", "Страны"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
