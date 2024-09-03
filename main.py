from authorization import *
if __name__ == '__main__':
    App = QtWidgets.QApplication([])
    window = SingIn()
    window.show()
    App.exec()