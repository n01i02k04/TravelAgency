import sqlite3

from PyQt5 import QtWidgets, QtSql
import BusinessAssistant, clientcontacts, newclient, decoration, info, centralwindow, deal, deleteTour, salesView

db = sqlite3.connect('BusinessAssistant.db')
cursor = db.cursor()

class Mainmenu(QtWidgets.QMainWindow, BusinessAssistant.Ui_MainWindow):
    def __init__(self):
        super(Mainmenu, self).__init__()
        self.setupUi(self)
        self.newClientButton.clicked.connect(self.newCustomerWindow)
        self.viewClientButton.clicked.connect(self.newCustomerContactsWindow)
        self.dealButton.clicked.connect(self.CreateDeal)
        self.returnButton.clicked.connect(self.ReturnTour)
        self.salesButton.clicked.connect(self.salesView)

    def newCustomerWindow(self):
        self.newCustomerWindow = Newcustomer()
        self.newCustomerWindow.show()
        self.hide()

    def newCustomerContactsWindow(self):
        self.newCustomerContactsWindow = NewCustomerContacts()
        self.newCustomerContactsWindow.show()
        self.hide()

    def CreateDeal(self):
        self.CreateDeal = Deal()
        self.CreateDeal.show()
        self.hide()

    def ReturnTour(self):
        self.ReturnTour = Refund()
        self.ReturnTour.show()
        self.hide()

    def salesView(self):
        self.salesView = Sales()
        self.salesView.show()
        self.hide()

class Newcustomer(QtWidgets.QMainWindow, newclient.Ui_MainWindow):
    def __init__(self):
        super(Newcustomer, self).__init__()
        self.setupUi(self)
        self.createCustomerButton.clicked.connect(self.createCustomer)
        self.exitCreateCustomerButton.clicked.connect(self.exitreateCustomer)

    def createCustomer(self):
        customer_initials = self.lineName.text()
        customer_passport = self.lineSurname.text()
        customer_phone = self.lineNumber.text()

        if len(customer_initials) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите инициалы!')
            return

        if len(customer_passport) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите паспорт!')
            return

        if len(customer_phone) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите телефон!')
            return

        cursor.execute(f'SELECT initials FROM clients WHERE initials="{customer_initials}"')

        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO clients (initials, passport, phone) VALUES ("{customer_initials}"'
                           f', "{customer_passport}", "{customer_phone}")')
            db.commit()
            QtWidgets.QMessageBox.information(self, 'Информация', f'Покупатель {customer_initials} был успешно создан')
        else:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Такой покупатель уже был создан!')

    def exitreateCustomer(self):
        self.exitreateCustomer = Mainmenu()
        self.exitreateCustomer.show()
        self.hide()

class NewCustomerContacts(QtWidgets.QMainWindow, clientcontacts.Ui_NewCustomerContacts):
    def __init__(self):
        super(NewCustomerContacts, self).__init__()
        self.setupUi(self)
        self.SearchCustomerButton.clicked.connect(self.searchCustomer)
        self.exitButton.clicked.connect(self.exitCustomerContacts)
        self.execute = ''

    def fillingTable(self, count, list, query, table):
        table.setColumnCount(count)
        table.setRowCount(len(query))
        for i in range(count):
            table.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(list[i]))

    def searchCustomer(self):
        self.customerTable.setColumnCount(0)
        self.customerTable.setRowCount(0)

        customer_initials = self.lineName.text()
        customer_passport = self.lineSurname.text()
        customer_phone = self.lineNumber.text()

        if len(customer_initials) == 0 and len(customer_passport) == 0 and len(customer_phone) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите инициалы, паспорт или телефон!')
            return

        if len(customer_initials) != 0:
            self.execute = f'SELECT * FROM clients WHERE initials LIKE "{customer_initials}%"'

        elif len(customer_passport) != 0:
            self.execute = f'SELECT * FROM clients WHERE passport LIKE "{customer_passport}%"'

        elif len(customer_phone) != 0:
            self.execute = f'SELECT * FROM clients WHERE phone LIKE "{customer_phone}%"'

        else:
            self.execute = f'SELECT * FROM clients WHERE initials = "{customer_initials}" ' \
                           f'and passport = "{customer_passport}" and phone = "{customer_phone}"'

        cursor.execute(self.execute)
        query = cursor.fetchall()

        self.fillingTable(4, ('Номер клиента', 'Инициалы', 'Паспорт', 'Телефон'), query, self.customerTable)

        i = 0
        for output in query:
            self.customerTable.setItem(i, 0, QtWidgets.QTableWidgetItem(str(output[0])))
            self.customerTable.setItem(i, 1, QtWidgets.QTableWidgetItem(str(output[1])))
            self.customerTable.setItem(i, 2, QtWidgets.QTableWidgetItem(str(output[2])))
            self.customerTable.setItem(i, 3, QtWidgets.QTableWidgetItem(str(output[3])))
            i += 1

    def exitCustomerContacts(self):
        self.exitCustomerContacts = Mainmenu()
        self.exitCustomerContacts.show()
        self.hide()

class Deal(QtWidgets.QMainWindow, deal.Ui_MainWindow):
    def __init__(self):
        super(Deal, self).__init__()
        self.setupUi(self)
        self.newSaleButton.clicked.connect(self.NewSale)
        self.toursButton.clicked.connect(self.showTours)
        self.clientsButton.clicked.connect(self.showClients)
        self.exitButton.clicked.connect(self.exit)

        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("BusinessAssistant.db")

        self.showTours()

    def NewSale(self):
        date_sale = self.date_sale.text()
        id_tour = self.id_tour.text()
        client_initials = self.client_initials.text()
        employee_initials = self.employee_initials.text()
        employee_phone = self.employee_phone.text()

        if len(date_sale) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите дату продажи!')
            return

        if len(id_tour) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите номер тура!')
            return

        if len(client_initials) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите инициалы клиента!')
            return

        if len(employee_initials) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите инициалы работника!')
            return

        if len(employee_phone) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите телефон работника!')
            return

        cursor.execute(f'INSERT INTO employees (employee_initials, employee_phone) VALUES ("{employee_initials}",'
                       f'"{employee_phone}")')
        db.commit()

        cursor.execute(f'SELECT id_client FROM clients WHERE initials = "{client_initials}"')
        id_client = cursor.fetchall()

        cursor.execute(f'SELECT id_employee FROM employees WHERE employee_initials = "{employee_initials}"')
        id_employee = cursor.fetchall()

        cursor.execute(f'INSERT INTO sales (date_sale, id_tour, id_client, id_employee) VALUES ("{date_sale}", '
                        f'"{id_tour}", "{id_client[0][0]}", "{id_employee[0][0]}")')
        db.commit()

        QtWidgets.QMessageBox.information(self, 'Информация', f'Продажа создана успешно!')

    def showTours(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable('tours')
        self.model.select()
        self.tableShow.setModel(self.model)
        self.tableShow.resizeColumnsToContents()

    def showClients(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable('clients')
        self.model.select()
        self.tableShow.setModel(self.model)
        self.tableShow.resizeColumnsToContents()

    def exit(self):
        self.exit = Mainmenu()
        self.exit.show()
        self.hide()

class Refund(QtWidgets.QMainWindow, deleteTour.Ui_MainWindow):
    def __init__(self):
        super(Refund, self).__init__()
        self.setupUi(self)

        self.deleteButton.clicked.connect(self.DeleteTour)
        self.toursButton.clicked.connect(self.showTours)
        self.exitButton.clicked.connect(self.exit)

        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("BusinessAssistant.db")

        self.showTours()

    def DeleteTour(self):
        id_tour = self.id_tour.text()

        if len(id_tour) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите номер тура!')
            return

        cursor.execute(f'DELETE FROM tours WHERE id_tour = "{id_tour}"')
        db.commit()

        QtWidgets.QMessageBox.information(self, 'Информация', f'Тур с номером {id_tour} успешно удалён!')


    def showTours(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable('tours')
        self.model.select()
        self.tableShow.setModel(self.model)
        self.tableShow.resizeColumnsToContents()

    def exit(self):
        self.exit = Mainmenu()
        self.exit.show()
        self.hide()

class Sales(QtWidgets.QMainWindow, salesView.Ui_MainWindow):
    def __init__(self):
        super(Sales, self).__init__()
        self.setupUi(self)

        self.exitButton.clicked.connect(self.exit)

        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("BusinessAssistant.db")

        self.showSales()

    def showSales(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable('sales')
        self.model.select()
        self.tableShow.setModel(self.model)
        self.tableShow.resizeColumnsToContents()

    def exit(self):
        self.exit = Mainmenu()
        self.exit.show()
        self.hide()

class ClientView(QtWidgets.QMainWindow, centralwindow.Ui_MainWindow):
    def __init__(self):
        super(ClientView, self).__init__()
        self.setupUi(self)
        self.decorButton.clicked.connect(self.DecorTour)
        self.infoButton.clicked.connect(self.Info)

        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("BusinessAssistant.db")

    def DecorTour(self):
        self.DecorTour = NewDecor()
        self.DecorTour.show()
        self.hide()

    def Info(self):
        self.Info = InfoView()
        self.Info.show()
        self.hide()

class NewDecor(QtWidgets.QMainWindow, decoration.Ui_MainWindow):
    def __init__(self):
        super(NewDecor, self).__init__()
        self.setupUi(self)
        self.newTourButton.clicked.connect(self.createTour)
        self.newIDButton.clicked.connect(self.showHotels)
        self.newNutritionButton.clicked.connect(self.showNutrition)
        self.newTypeButton.clicked.connect(self.showTypes)
        self.newCityButton.clicked.connect(self.showCities)
        self.newExitButton.clicked.connect(self.exit)

        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("BusinessAssistant.db")

        self.showNutrition()

    def fillingTable(self, count, list, query, table):
        table.setColumnCount(count)
        table.setRowCount(len(query))
        for i in range(count):
            table.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(list[i]))

    def createTour(self):
        client_initials = self.initials.text()
        client_passport = self.passport.text()
        client_phone = self.phone.text()
        client_date = self.date.text()
        client_city = self.city.text()
        client_adults = self.adults.text()
        client_children = self.adults_2.text()
        client_nights = self.nights.text()
        client_type = self.type_tour.text()
        client_nutrition = self.type_nutrition.text()
        name_hotel = self.name_hotel.text()


        if len(client_initials) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите инициалы!')
            return

        if len(client_passport) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите паспорт!')
            return

        if len(client_phone) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите телефон!')
            return

        if len(client_date) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите дату вылета!')
            return

        if len(client_city) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите город вылета!')
            return

        if len(client_adults) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите количество взрослых!')
            return

        if len(client_children) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите количество детей!')
            return

        if len(client_nights) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите количество ночей!')
            return

        if len(client_type) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите тип отеля!')
            return

        if len(client_nutrition) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите тип питания!')
            return

        if len(name_hotel) == 0:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Введите id отеля!')
            return

        cursor.execute(f'INSERT INTO clients (initials, passport, phone) VALUES ("{client_initials}"'
                       f', "{client_passport}", "{client_phone}")')

        db.commit()

        cursor.execute(f'SELECT id_type FROM types_tours WHERE name_type = "{client_type}"')
        id_type = cursor.fetchall()

        cursor.execute(f'SELECT id_nutrition FROM nutrition WHERE name_nutrition = "{client_nutrition}"')
        id_nutrition = cursor.fetchall()

        cursor.execute(f'SELECT id_hotel FROM hotels WHERE name_hotel = "{name_hotel}"')
        id_hotel = cursor.fetchall()


        cursor.execute(f'INSERT INTO tours (departure_date, departure_city, number_adults, number_children, cnt_nights,'
                       f'id_type, id_nutrition, id_hotel) VALUES ("{client_date}", "{client_city}", "{client_adults}", '
                       f'"{client_children}", "{client_nights}", "{id_type[0][0]}", "{id_nutrition[0][0]}", '
                       f'"{id_hotel[0][0]}")')
        db.commit()

        QtWidgets.QMessageBox.information(self, 'Информация', f'Тур на человека {client_initials} успешно создан!')

    def showNutrition(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable('nutrition')
        self.model.select()
        self.tableShow.setModel(self.model)
        self.tableShow.resizeColumnsToContents()

    def showCities(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable('cities')
        self.model.select()
        self.tableShow.setModel(self.model)
        self.tableShow.resizeColumnsToContents()

    def showTypes(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable('types_tours')
        self.model.select()
        self.tableShow.setModel(self.model)
        self.tableShow.resizeColumnsToContents()

    def showHotels(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable('hotels')
        self.model.select()
        self.tableShow.setModel(self.model)
        self.tableShow.resizeColumnsToContents()

    def exit(self):
        self.exit = ClientView()
        self.exit.show()
        self.hide()

class InfoView(QtWidgets.QMainWindow, info.Ui_MainWindow):
    def __init__(self):
        super(InfoView, self).__init__()
        self.setupUi(self)

        self.countryButton.clicked.connect(self.showCountries)
        self.nutritionButton.clicked.connect(self.showNutrition)
        self.typesButton.clicked.connect(self.showTypes)
        self.cityButton.clicked.connect(self.showCities)
        self.hotelsButton.clicked.connect(self.showHotels)
        self.exitButton.clicked.connect(self.exit)

        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("BusinessAssistant.db")

    def showNutrition(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable('nutrition')
        self.model.select()
        self.tableShow.setModel(self.model)
        self.tableShow.resizeColumnsToContents()

    def showCountries(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable('countries')
        self.model.select()
        self.tableShow.setModel(self.model)
        self.tableShow.resizeColumnsToContents()

    def showCities(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable('cities')
        self.model.select()
        self.tableShow.setModel(self.model)
        self.tableShow.resizeColumnsToContents()

    def showTypes(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable('types_tours')
        self.model.select()
        self.tableShow.setModel(self.model)
        self.tableShow.resizeColumnsToContents()

    def showHotels(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable('hotels')
        self.model.select()
        self.tableShow.setModel(self.model)
        self.tableShow.resizeColumnsToContents()

    def exit(self):
        self.exit = ClientView()
        self.exit.show()
        self.hide()