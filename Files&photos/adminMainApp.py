import os

from PyQt5.QtWidgets import QDialog, QFileDialog, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem
from PyQt5 import uic

import FisrtPage
import db
import finger
import DeleteUser

Form = uic.loadUiType(os.path.join(os.getcwd(), 'adminMainApp.ui'))[0]


class MainApp(Form, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.findUser.clicked.connect(self.find)
        self.deleteUser.clicked.connect(self.delete)
        self.Quit.clicked.connect(self.quit)
        self.username = None

    def getusername(self, user):
        self.username = user

    def find(self):
        path = QFileDialog.getOpenFileName(self, 'Open file',
                                           'c:\\', 'Image files (*.jpg *.png)')
        db1 = db.DBHandler()
        paths = db1.compare()
        count = 0
        for i in paths:
            compatible = False
            compatible = finger.comp(path[0], i[0])
            if compatible:
                count = count + 1
                ID = db1.findfingerId(i[0])
                userId = ID[0][0]
                data = db1.readUser(userId)
                print(f'Username : {data[0][2]}, Phone : {data[0][1]}')
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                numcols = 2
                numrows = self.tableWidget.rowCount()
                self.tableWidget.setRowCount(numrows)
                self.tableWidget.setColumnCount(numcols)
                self.tableWidget.setItem(numrows - 1, 0, QTableWidgetItem(data[0][2]))
                self.tableWidget.setItem(numrows - 1, 1, QTableWidgetItem(str(data[0][1])))
                print("guest added")

    def delete(self):
        self.close()
        self.window = QDialog()
        self.ui = DeleteUser.delete()
        self.ui.setModal(True)
        self.ui.exec()

    def quit(self):
        self.close()
        self.window = QDialog()
        self.ui = FisrtPage.fisrtpage()
        self.ui.setModal(True)
        self.ui.exec()
