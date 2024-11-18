# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: Table_3.py
# Bytecode version: 3.9.0beta5 (3425)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Table_3(object):

    def setupUi(self, Table_3):
        Table_3.setObjectName('Table_3')
        Table_3.resize(606, 401)
        self.tableView3 = QtWidgets.QTableView(parent=Table_3)
        self.tableView3.setGeometry(QtCore.QRect(10, 10, 590, 200))
        self.tableView3.setMidLineWidth(2)
        self.tableView3.setObjectName('tableView3')
        self.tableView3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView3.horizontalHeader().setDefaultSectionSize(40)
        self.tableView3.horizontalHeader().setSortIndicatorShown(False)
        self.tableView3.verticalHeader().setDefaultSectionSize(40)
        self.saveButton = QtWidgets.QPushButton(parent=Table_3)
        self.saveButton.setGeometry(QtCore.QRect(500, 340, 100, 50))
        self.saveButton.setObjectName('saveButton')
        self.addRowButton = QtWidgets.QPushButton(parent=Table_3)
        self.addRowButton.setGeometry(QtCore.QRect(10, 340, 101, 51))
        self.addRowButton.setObjectName('addRowButton')
        self.delRowButton = QtWidgets.QPushButton(parent=Table_3)
        self.delRowButton.setGeometry(QtCore.QRect(120, 340, 161, 51))
        self.delRowButton.setObjectName('delRowButton')
        self.retranslateUi(Table_3)
        QtCore.QMetaObject.connectSlotsByName(Table_3)

    def retranslateUi(self, Table_3):
        _translate = QtCore.QCoreApplication.translate
        Table_3.setWindowTitle(_translate('Table_3', 'Таблица 3'))
        self.saveButton.setText(_translate('Table_3', 'Сохранить'))
        self.addRowButton.setText(_translate('Table_3', 'Добавить строку'))
        self.delRowButton.setText(_translate('Table_3', 'Удалить выбранную строку'))