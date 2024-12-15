from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Table_1(object):

    def setupUi(self, Table_1):
        Table_1.setObjectName('Table_1')
        Table_1.resize(606, 360)
        self.tableView1 = QtWidgets.QTableView(parent=Table_1)
        self.tableView1.setGeometry(QtCore.QRect(40, 40, 480, 230))
        self.tableView1.setMidLineWidth(2)
        self.tableView1.setObjectName('tableView1')
        self.tableView1.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView1.horizontalHeader().setDefaultSectionSize(20)
        self.tableView1.horizontalHeader().setSortIndicatorShown(False)
        self.tableView1.verticalHeader().setDefaultSectionSize(40)
        self.saveButton = QtWidgets.QPushButton(parent=Table_1)
        self.saveButton.setGeometry(QtCore.QRect(500, 280, 100, 50))
        self.saveButton.setObjectName('saveButton')
        """
        self.addRowButton = QtWidgets.QPushButton(parent=Table_1)
        self.addRowButton.setGeometry(QtCore.QRect(10, 440, 101, 51))
        self.addRowButton.setObjectName('addRowButton')
        self.delRowButton = QtWidgets.QPushButton(parent=Table_1)
        self.delRowButton.setGeometry(QtCore.QRect(120, 440, 161, 51))
        self.delRowButton.setObjectName('delRowButton')"""
        self.retranslateUi(Table_1)
        QtCore.QMetaObject.connectSlotsByName(Table_1)

    def retranslateUi(self, Table_1):
        _translate = QtCore.QCoreApplication.translate
        Table_1.setWindowTitle(_translate('Table_1', 'Таблица 1'))
        self.saveButton.setText(_translate('Table_1', 'Сохранить'))
        #self.addRowButton.setText(_translate('Table_1', 'Добавить строку'))
        #self.delRowButton.setText(_translate('Table_1', 'Удалить выбранную строку'))