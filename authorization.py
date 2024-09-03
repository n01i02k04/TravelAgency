import sing_in, registration_ui
from Mainmenu import *
from PyQt5 import QtWidgets

class SingIn(QtWidgets.QMainWindow, sing_in.Ui_MainWindow):
    def __init__(self):
        super(SingIn, self).__init__()
        self.setupUi(self)
        self.AuthorizationButton.clicked.connect(self.login)
        self.RegistrationWindowButton.clicked.connect(self.registration)

    def login(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()

        if len(user_login) == 0:
            return

        if len(user_password) == 0:
            return

        cursor.execute(f'SELECT user_password FROM users WHERE user_login="{user_login}"')
        check_pass = cursor.fetchall()

        cursor.execute(f'SELECT user_login FROM users WHERE user_login="{user_login}"')
        check_login = cursor.fetchall()

        if check_pass[0][0] == user_password and check_login[0][0] == user_login:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Успешная авторизация!')

            cursor.execute(f'SELECT id_spec FROM users WHERE user_login="{user_login}"')
            check_spec = cursor.fetchall()

            if check_spec[0][0] == 2:
                self.mainmenu = Mainmenu()
                self.mainmenu.show()
                self.hide()
            else:
                self.createTour = ClientView()
                self.createTour.show()
                self.hide()
        else:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Ошибка авторизации!')


    def registration(self):
        self.login = Registration()
        self.login.show()
        self.hide()

class Registration(QtWidgets.QMainWindow, registration_ui.Ui_MainWindow):
    def __init__(self):
        super(Registration, self).__init__()
        self.setupUi(self)
        self.RegistrButton.clicked.connect(self.registration)
        self.SingInWindowButton.clicked.connect(self.sing_in_window)

    def registration(self):
        user_login = self.login.text()
        user_password = self.password.text()

        if len(user_login) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите логин!')
            return

        if len(user_password) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите пароль!')
            return

        if self.radioManagerButton.isChecked():
            user_spec_id = 1
        elif self.radioWorkerButton.isChecked():
            user_spec_id = 2
        else:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Выберите должность!')
            return

        cursor.execute(f'SELECT user_login FROM users WHERE user_login="{user_login}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO users (user_login, user_password, id_spec) VALUES ("{user_login}", '
                           f'"{user_password}", "{user_spec_id}")')
            QtWidgets.QMessageBox.information(self, 'Информация', f'Аккаунт {user_login} успешно зарегистрирован!')
            db.commit()
        else:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Такая запись уже имеется!')

    def sing_in_window(self):
        self.sing_in_window = SingIn()
        self.sing_in_window.show()
        self.hide()