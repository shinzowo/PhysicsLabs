# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: Titul.py
# Bytecode version: 3.9.0beta5 (3425)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Titul(object):

    def setupUi(self, Titul):
        Titul.setObjectName('Titul')
        Titul.setEnabled(True)
        Titul.resize(760, 856)
        font = QtGui.QFont()
        font.setFamily('Arial')
        font.setPointSize(12)
        Titul.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=Titul)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName('centralwidget')
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 10, 595, 842))
        self.textEdit.setObjectName('textEdit')
        self.saveTitulButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.saveTitulButton.setGeometry(QtCore.QRect(640, 10, 100, 70))
        self.saveTitulButton.setObjectName('saveTitulButton')
        Titul.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Titul)
        self.statusbar.setObjectName('statusbar')
        Titul.setStatusBar(self.statusbar)
        self.retranslateUi(Titul)
        QtCore.QMetaObject.connectSlotsByName(Titul)

    def retranslateUi(self, Titul):
        _translate = QtCore.QCoreApplication.translate
        Titul.setWindowTitle(_translate('Titul', 'Титульный лист'))
        self.textEdit.setHtml(_translate('Titul', '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: "\\2610"; }\nli.checked::marker { content: "\\2612"; }\n</style></head><body style=" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;">\n<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Times New Roman\',\'serif\';">Федеральное государственное бюджетное образовательное учреждение высшего профессионального образования</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span></p>\n<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Times New Roman\',\'serif\'; font-size:13pt; font-weight:700;">Национальный исследовательский Томский политехнический университет</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span><span style=" font-family:\'Times New Roman\',\'serif\'; font-size:13pt;">\xa0</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span></p>\n<p align="center" style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Times New Roman\',\'serif\'; font-size:13pt;">\xa0</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;"><span style=" font-family:\'Times New Roman\',\'serif\';">Школа – ИЯТШ</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;"><span style=" font-family:\'Times New Roman\',\'serif\';">Направление – Прикладная математика и информатика</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span></p>\n<h2 align="center" style=" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;"><span style=" font-family:\'Segoe UI\'; font-size:9pt; font-weight:700;">ОПРЕДЕЛЕНИЕ ГЛАВНОГО ФОКУСНОГО РАССТОЯНИЯ  ТОНКИХ ЛИНЗ</span></h2>\n<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;"><span style=" font-family:\'Times New Roman\',\'serif\';">Лабораторная работа № 3-01</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span></p>\n<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;"><span style=" font-family:\'Times New Roman\',\'serif\';">По дисциплине «Физика»</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span></p>\n<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Times New Roman\',\'serif\';">\xa0</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Times New Roman\',\'serif\';">Исполнитель</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;"><br /></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Times New Roman\',\'serif\';">Студент, гр. (</span><span style=" font-family:\'Times New Roman\',\'serif\'; text-decoration: underline;">укажите свою группу</span><span style=" font-family:\'Times New Roman\',\'serif\';">)</span></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;"><br /></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Times New Roman\',\'serif\';">(</span><span style=" font-family:\'Times New Roman\',\'serif\'; text-decoration: underline;">укажите свои инициалы</span><span style=" font-family:\'Times New Roman\',\'serif\';">) ____________\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 ____________</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Times New Roman\',\'serif\';">                (подпись)\xa0\xa0\xa0\xa0\xa0\xa0 \xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 \xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 \xa0(дата)</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;"><br /></p>\n<p style=" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Times New Roman\',\'serif\';">Руководитель</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Times New Roman\',\'serif\';">Филимонова В. С.\xa0\xa0\xa0\xa0\xa0\xa0\xa0 \xa0\xa0\xa0\xa0 ____________\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 ____________</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Times New Roman\',\'serif\';">                                                (подпись)\xa0\xa0\xa0\xa0\xa0\xa0 \xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 \xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 \xa0(дата)</span><span style=" font-family:\'Segoe UI\'; font-size:9pt;"> </span></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;"><br /></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;"><br /></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;"><br /></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;"><br /></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;"><br /></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;"><br /></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;"><br /></p>\n<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Times New Roman\',\'serif\';">Томск 2024</span></p></body></html>'))
        self.saveTitulButton.setText(_translate('Titul', 'Сохранить'))