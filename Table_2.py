from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Table_2(object):

    def setupUi(self, Table_2):
        Table_2.setObjectName('Table_2')
        Table_2.resize(606, 401)
        self.tableView2 = QtWidgets.QTableView(parent=Table_2)
        self.tableView2.setGeometry(QtCore.QRect(10, 10, 590, 200))
        self.tableView2.setMidLineWidth(2)
        self.tableView2.setObjectName('tableView2')
        self.tableView2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView2.horizontalHeader().setDefaultSectionSize(40)
        self.tableView2.horizontalHeader().setSortIndicatorShown(False)
        self.tableView2.verticalHeader().setDefaultSectionSize(20)
        self.saveButton = QtWidgets.QPushButton(parent=Table_2)
        self.saveButton.setGeometry(QtCore.QRect(500, 340, 100, 50))
        self.saveButton.setObjectName('saveButton')
        self.addRowButton = QtWidgets.QPushButton(parent=Table_2)
        self.addRowButton.setGeometry(QtCore.QRect(10, 340, 101, 51))
        self.addRowButton.setObjectName('addRowButton')
        self.delRowButton = QtWidgets.QPushButton(parent=Table_2)
        self.delRowButton.setGeometry(QtCore.QRect(120, 340, 161, 51))
        self.delRowButton.setObjectName('delRowButton')
        self.retranslateUi(Table_2)
        QtCore.QMetaObject.connectSlotsByName(Table_2)

    def retranslateUi(self, Table_2):
        _translate = QtCore.QCoreApplication.translate
        Table_2.setWindowTitle(_translate('Table_2', 'Таблица 2'))
        self.saveButton.setText(_translate('Table_2', 'Сохранить'))
        self.addRowButton.setText(_translate('Table_2', 'Добавить строку'))
        self.delRowButton.setText(_translate('Table_2', 'Удалить выбранную строку'))