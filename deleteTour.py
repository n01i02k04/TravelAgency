# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteTour.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 399)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(100, 160, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.deleteButton.setFont(font)
        self.deleteButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteButton.setStyleSheet("\n"
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
        self.deleteButton.setObjectName("deleteButton")
        self.id_tour = QtWidgets.QLineEdit(self.centralwidget)
        self.id_tour.setGeometry(QtCore.QRect(80, 100, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.id_tour.setFont(font)
        self.id_tour.setStyleSheet("border: 1px solid rgb(186, 186, 186);\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"color: black;")
        self.id_tour.setText("")
        self.id_tour.setObjectName("id_tour")
        self.toursButton = QtWidgets.QPushButton(self.centralwidget)
        self.toursButton.setGeometry(QtCore.QRect(540, 330, 211, 50))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.toursButton.setFont(font)
        self.toursButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toursButton.setStyleSheet("\n"
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
        self.toursButton.setObjectName("toursButton")
        self.tableShow = QtWidgets.QTableView(self.centralwidget)
        self.tableShow.setGeometry(QtCore.QRect(329, 50, 641, 241))
        self.tableShow.setObjectName("tableShow")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(100, 220, 181, 41))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BusinessAssistant"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить тур"))
        self.id_tour.setPlaceholderText(_translate("MainWindow", "ID тура"))
        self.toursButton.setText(_translate("MainWindow", "Туры"))
        self.exitButton.setText(_translate("MainWindow", "Выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
