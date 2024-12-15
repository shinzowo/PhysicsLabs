from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(538, 600)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.titulButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.titulButton.setGeometry(QtCore.QRect(120, 260, 300, 60))
        font = QtGui.QFont()
        font.setFamily('Arial')
        font.setPointSize(12)
        font.setBold(True)
        self.titulButton.setFont(font)
        self.titulButton.setObjectName('titulButton')
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 481, 81))
        font = QtGui.QFont()
        font.setFamily('Arial')
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.label.setObjectName('label')
        self.metodButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.metodButton.setGeometry(QtCore.QRect(120, 120, 300, 60))
        font = QtGui.QFont()
        font.setFamily('Arial')
        font.setPointSize(12)
        font.setBold(True)
        self.metodButton.setFont(font)
        self.metodButton.setObjectName('metodButton')

        font = QtGui.QFont()
        font.setFamily('Arial')
        font.setPointSize(12)
        font.setBold(True)
        self.otchotButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.otchotButton.setGeometry(QtCore.QRect(120, 490, 300, 60))
        font = QtGui.QFont()
        font.setFamily('Arial')
        font.setPointSize(12)
        font.setBold(True)
        self.otchotButton.setFont(font)
        self.otchotButton.setObjectName('otchotButton')
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 400, 441, 81))
        font = QtGui.QFont()
        font.setFamily('Arial')
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName('label_2')
        self.table1Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.table1Button.setGeometry(QtCore.QRect(120, 190, 300, 60))
        font = QtGui.QFont()
        font.setFamily('Arial')
        font.setPointSize(12)
        font.setBold(True)
        self.table1Button.setFont(font)
        self.table1Button.setObjectName('table1Button')
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', 'Лабораторная работа № 1-06'))
        self.titulButton.setText(_translate('MainWindow', 'Редактирование титульного листа'))
        self.label.setText(_translate('MainWindow', 'Лабораторная работа № 1-06'))
        self.metodButton.setText(_translate('MainWindow', 'Методические указания'))

        self.otchotButton.setText(_translate('MainWindow', 'Сохранить отчёт'))
        self.label_2.setText(_translate('MainWindow', '<html><head/><body><p align="center"><span style=" font-size:10pt;">ВНИМАНИЕ!</span></p><p align="center"><span style=" font-size:10pt;">Не забудьте сохранить внесённые данные перед</span></p><p align="center"><span style=" font-size:10pt;"> сохранением отчёта!</span></p></body></html>'))
        self.table1Button.setText(_translate('MainWindow', 'Таблица 1'))
