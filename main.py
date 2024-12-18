import sys
import os
import json
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPdfWriter, QPainter, QPageSize
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtCore import Qt, QModelIndex
from PyQt6.QtPdf import QPdfDocument
from PyQt6.QtPdfWidgets import QPdfView
import PyPDF2
from PIL import Image
from os import listdir, path
import MainWindow
import Titul
import Table_1


def raschotFunction(index, data, customID, old_value, rowC):
    if index.row() in (3, 4):
        data[index.row()][index.column()] = old_value
        return False

    elif index.row() != 0 and index.column() in (7, 8):
        data[index.row()][index.column()] = old_value
        return False

    elif index.row() == 0 and index.column() in (7, 8):
        try:
            for i in range(1, 7):
                data[4][i] = data[0][7] + (i-1) * data[0][8]
        except TypeError:
            return False
    else:
        try:
            data[3][index.column()] = (data[0][index.column()]**2 + data[1][index.column()]**2 + data[2][index.column()]**2)/3
        except TypeError:
            return False

    return True
        

class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data=None, header=None, customID=None, vheader=None):
        super(TableModel, self).__init__()
        self._data = data
        self._header = header
        self._customID = customID
        if vheader == None:
            self._vheader = [str(i + 1) for i in range(0, len(data))]
        else:
            self._vheader = vheader

    def data(self, index, role):
        if role == Qt.ItemDataRole.BackgroundRole:
            return QtGui.QColor('#d3d3d3')
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index=QtCore.QModelIndex):
        return len(self._data)

    def columnCount(self, index=QtCore.QModelIndex):
        return len(self._data[0])

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            old_value = self._data[index.row()][index.column()]
            try:
                self._data[index.row()][index.column()] = float(value)
                raschotFunction(index, self._data, self._customID, old_value, self.rowCount())
                return True
            except ValueError:
                return False
        return False

    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return str(self._header[section])
        if orientation == Qt.Orientation.Vertical and role == Qt.ItemDataRole.DisplayRole:
            return str(self._vheader[section])

    def insertRow(self, row=0, parent=QModelIndex()):
        return self.insertRows(row, count=1, parent=parent)

    def insertRows(self, row=0, count=1, parent=QModelIndex()):
        custom_row = ['' for i in range(len(self._header))]
        self.beginInsertRows(parent, len(self._vheader) + 1, count + len(self._vheader) + 1)
        for row in range(count):
            self._data.insert(len(self._vheader) + 1, custom_row)
            self._vheader.append(str(len(self._vheader) + 1))
        self.endInsertRows()
        return True

    def removeRow(self, row=0, parent=QModelIndex()):
        return self.removeRows(row, count=1, parent=parent)

    def removeRows(self, row=0, count=1, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row + count)
        if count >= len(self._data):
            self._data = None
        else:
            del self._data[row:row + count]
        self.endRemoveRows()
        return True

def initTable1():
    if os.path.exists('./data/table1.json'):
        with open('./data/table1.json', 'r', encoding='utf-8') as read_file:
            data = json.load(read_file)
            _data = []
            for row in data:
                _col = []
                for col in row:
                    _col.append(row[col])
                _data.append(_col)
            return _data
    else:
        return [['', '', '', ''], ['', '', '', ''], ['', '', '', '']]

def saveTable1(data, file='./data/table1.json'):
    with open(file, 'w', encoding='utf-8') as write_file:
        json.dump(data, write_file, ensure_ascii=False)

class Table1(QtWidgets.QMainWindow, Table_1.Ui_Table_1):

    def __init__(self):
        super().__init__()
        self._initModel()
        self.setupUi(self)
        self._initGui()

    def _initGui(self):
        self.tableView1.setModel(self.model)
        header = self.tableView1.horizontalHeader()
        vheader = self.tableView1.verticalHeader()
        header.ResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableView1.setHorizontalHeader(header)
        self.tableView1.setVerticalHeader(vheader)
        self.saveButton.clicked.connect(self.screen)
        #self.addRowButton.clicked.connect(self.addRow)
        #self.delRowButton.clicked.connect(self.delRow)

    def _initModel(self):
        data = initTable1()
        header = ['T₀', 'T₁', 'T₂', 'T₃', 'T₄', 'T₅', 'T₆', 'l₁', 'Δl']
        vheader = [i+1 for i in range(len(data))]
        customID = 1
        if len(vheader) >= 2:  # Добавляем кастомные названия для последних строк
            vheader[-2] = '〈T²〉'
            vheader[-1] = 'l²'
        self.rowC = int(len(data))
        self.model = TableModel(data, header, customID, vheader)

    def addRow(self):
        if int(self.rowC) < 8:
            self.rowC = int(self.rowC) + 1
            self.model.layoutAboutToBeChanged.emit()
            self.model.insertRows(self.model.rowCount(), count=1)
            self.model.layoutChanged.emit()
        return None

    def delRow(self):
        self.model.layoutAboutToBeChanged.emit()
        _index = self.tableView1.selectedIndexes()
        if not _index:
            return True
        rows = sorted(set((index.row() for index in _index)))
        self.model.removeRow(row=rows[0])
        self.model.layoutChanged.emit()
        self.rowC = int(self.rowC) - 1

    def saveModel(self):
        if not self.model._data:
            return
        _data = []
        for _row in self.model._data:
            _dict_task = {}
            for i in range(len(self.model._header)):
                _dict_task[self.model._header[i]] = _row[i]
            _data.append(_dict_task)
        saveTable1(_data, file='./data/table1.json')

    def screen(self):
        self.saveModel()
        imageTabel = self.tableView1.grab(self.tableView1.rect())
        imageTabel.save('./images/imageTabel1.png')

    def closeEvent(self, event):
        self.screen()
        self.close()

class TitulWindow(QtWidgets.QMainWindow, Titul.Ui_Titul):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._initGui()

    def _initGui(self):
        self.saveTitulButton.clicked.connect(self.saveTitulPdf)

    def saveTitulPdf(self):
        file_path = './images/pdfFiles/1_titul.pdf'
        widget = self.textEdit
        if file_path:
            printer = QPrinter(QPrinter.PrinterMode.ScreenResolution)
            printer.setPageSize(QPageSize(QPageSize.PageSizeId.A4))
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(file_path)
            writer = QPdfWriter(file_path)
            painter = QPainter(printer)
            painter.begin(printer)
            xscale = printer.pageRect(QPrinter.Unit.DevicePixel).width() * 1.0 / widget.width()
            yscale = printer.pageRect(QPrinter.Unit.DevicePixel).height() * 1.0 / widget.height()
            scale = min(xscale, yscale)
            painter.translate(printer.paperRect(QPrinter.Unit.DevicePixel).x() + printer.pageRect(QPrinter.Unit.DevicePixel).width() / 2, printer.paperRect(QPrinter.Unit.DevicePixel).y() + 0)
            painter.scale(scale, scale)
            painter.translate(-widget.width() / 2, 0)
            widget.render(painter)
            painter.end()

    def closeEvent(self, event):
        self.close()

class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._initGui()
        self.table1 = None
        self.table2 = None
        self.table3 = None
        self.titul = None
        self.view = None
    def _initGui(self):
        self.metodButton.clicked.connect(self.openMetod)
        self.table1Button.clicked.connect(self.openTable1)
        #self.table2Button.clicked.connect(self.openTable2)
        self.titulButton.clicked.connect(self.openTitul)
        self.otchotButton.clicked.connect(self.saveOtchot)
    def openMetod(self):
        file_path = './images/pdfFiles/2_teor.pdf'
        self.document = QPdfDocument(None)
        self.document.load(file_path)
        self.view = QPdfView(None)
        self.view.setWindowTitle('Методические указания')
        self.view.setPageMode(QPdfView.PageMode.MultiPage)
        self.view.setDocument(self.document)
        self.view.show()
    def openTable1(self):
        if self.table1 and self.table1.isVisible():
            self.table1.saveModel()
        self.table1 = Table1()
        self.table1.show()
    #def openTable2(self):
        #if self.table2 and self.table2.isVisible():
            #self.table2.saveModel()
        #self.table2 = Table2()
        #self.table2.show()

    #def openTable3(self):
        #if self.table3 and self.table3.isVisible():
            #self.table3.saveModel()
        #self.table3 = Table3()
        #self.table3.show()
    def openTitul(self):
        self.titul = TitulWindow()
        self.titul.show()
    def mergePng(self, im2, im3, resample=Image.BICUBIC, resize_big_image=True):
        _im2 = im2.resize((595, im2.height), resample=resample)
        _im3 = im3.resize((595, im3.height), resample=resample)
        dst = Image.new('RGB', (_im2.width, _im2.height + _im3.height))
        dst.paste(_im2, (0, 0))
        dst.paste(_im3, (0, _im2.height))
        return dst

    def saveOtchot(self):
        if path.isfile('./images/imageTabel1.png') and path.isfile('./images/imageTabel2.png'):
            #im2 = Image.open('./images/imageTabel2.png')

            #Table2Header = Image.open('./images/Table2Header.png')

            #self.mergePng(Table2Header, im2, resize_big_image=True).save('./images/newIm.png')
            #newIm = Image.open('./images/newIm.png')

            #newIm = Image.open('./images/newIm.png')

            #newIm = Image.open('./images/newIm.png')
            #a4im = Image.new('RGB', (595, 842), (255, 255, 255))
            #a4im.paste(newIm, newIm.getbbox())
            #a4im.save('images/pdfFiles/32_tables.pdf', 'PDF', quality=100)
            Table1Header = Image.open('./images/Table1Header.png')
            im1 = Image.open('./images/imageTabel1.png')
            self.mergePng(Table1Header, im1, resize_big_image=True).save('./images/t1.png')
            t1 = Image.open('./images/t1.png')
            a4im = Image.new('RGB', (595, 842), (255, 255, 255))
            a4im.paste(t1, t1.getbbox())
            a4im.save('images/pdfFiles/31_tables.pdf', 'PDF', quality=100)
        merger = PyPDF2.PdfMerger()
        files = [f for f in listdir('./images/pdfFiles/') if path.isfile('./images/pdfFiles/' + f) and f.endswith('.pdf')]
        for file in files:
            merger.append('./images/pdfFiles/' + file)
        with open(path.abspath('./otchot/otchot.pdf'), 'wb') as append_all_pdfs:
            merger.write(append_all_pdfs)
    def closeEvent(self, event):
        if self.table1 and self.table1.isVisible():
            self.table1.closeEvent(None)
        if self.table2 and self.table2.isVisible():
            self.table2.closeEvent(None)
        if self.table3 and self.table3.isVisible():
            self.table3.closeEvent(None)
        if self.titul and self.titul.isVisible():
            self.titul.closeEvent(None)
        if self.view and self.view.isVisible():
            self.view.close()
        self.close()
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec()