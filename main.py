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
import Table_2
import pyqtgraph as pg
from pyqtgraph.exporters import ImageExporter
import math


def save_graph_to_png(x_data, y_data, file_path):
    """Сохраняет график в PNG без отображения его в приложении."""
    try:
        # Создаем виджет макета для графиков
        layout = pg.GraphicsLayoutWidget()
        plot_item = layout.addPlot()  # Добавляем график в макет

        # Построение графика
        plot_item.plot(x_data, y_data, pen=pg.mkPen(color='b', width=2), symbol='o', symbolSize=10)
        plot_item.setTitle("График данных")
        plot_item.setLabel('left', 'Y')
        plot_item.setLabel('bottom', 'X')
        plot_item.titleLabel.setPos(0, 20)

        # Увеличиваем отступы вокруг графика
        #plot_item.setContentsMargins(20, 20, 20, 20)  # left, top, right, bottom

        # Настраиваем видимую область
        view_box = plot_item.getViewBox()
        view_box.setAspectLocked(False)  # Разрешаем изменение масштаба
        view_box.enableAutoRange()  # Автоматическое масштабирование

        # Экспорт графика
        exporter = ImageExporter(plot_item)
        exporter.parameters()['width'] = 800  # Задаем ширину изображения (по желанию)
        exporter.export(file_path)

        print(f"График успешно сохранен в файл: {file_path}")
    except Exception as e:
        print(f"Ошибка при сохранении графика: {e}")

def get_xy_data(data, xCol, header):
    """Извлекает данные для x и y из таблицы."""

    # Инициализация списков для x и y
    x = []
    y = []

    # Получаем индексы столбцов
    index_h = header.index(xCol)
    index_t_avg = header.index('〈t〉, с')

    # Обработка данных
    for row in data:
        try:
            h = float(row[index_h])  # Получаем h
            t_avg = float(row[index_t_avg])  # Получаем среднее время 〈t〉

            y.append(t_avg)
            x.append(math.sqrt(h))
        except (ValueError, TypeError):
            # Игнорируем некорректные строки
            continue
    x.append(0)
    y.append(0)
    return x, y

def raschotFunction(index, data, customID, old_value, rowC):
    if customID == 1:
        # Non-input columns
        if index.column() in (5, 6):
            return False 
        
        # Values that common for all columns
        if index.row() != 0 and index.column() in (8, 9):
            return False 
        
        try:
            h = data[index.row()][0]
            t = tuple(data[index.row()][i] for i in (1,2,3,4))
            if '' not in t:
                t_av = sum(t)/4
                data[index.row()][5] = t_av
                delta_t_i_2 = ((t_av - x)**2 for x in t)
                sigma_t = (sum(delta_t_i_2) / 12)**0.5
                dov_int = 3.182 * sigma_t
                err_1 = 0.95 * 0.005
                delta_t = (dov_int**2 + err_1**2)**0.5
                data[index.row()][6] = (delta_t // 0.00001) * 0.00001

        except ValueError:
            # data[index.row()][2] = ''
            return False

    elif customID == 2:
        # Non-input columns
        if index.column() in (2, 7, 8):
            return False 
        
        # Values that common for all columns
        if index.row() != 0 and index.column() in (1, ):
            return False 
        
        try:
            m = data[index.row()][0]
            M = data[0][1]
            if m == 0:
                return False
            
            if '' not in (m, M):
                data[index.row()][2] = M/m
            t = tuple(data[index.row()][i] for i in (3,4,5,6))
            if '' not in t:
                t_av = sum(t)/4
                data[index.row()][7] = t_av
                delta_t_i_2 = ((t_av - x)**2 for x in t)
                sigma_t = (sum(delta_t_i_2) / 12)**0.5
                dov_int = 3.182 * sigma_t
                err_1 = 0.95 * 0.005
                delta_t = (dov_int**2 + err_1**2)**0.5
                data[index.row()][8] = (delta_t // 0.00001) * 0.00001

        except ValueError:
            # data[index.row()][2] = ''
            return False
    
    else:
        data[index.row()][index.column()] = old_value
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
                if not raschotFunction(index, self._data, self._customID, old_value, self.rowCount()):
                    self._data[index.row()][index.column()] = old_value
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
        self.addRowButton.clicked.connect(self.addRow)
        self.delRowButton.clicked.connect(self.delRow)

    def _initModel(self):
        data = initTable1()
        header = ['h, м', 't₁, с', 't₂, с', 't₃, c',  't₄, c', '〈t〉, с', 'Δt, с', 'Δh, м', 'm, кг', 'm₀, кг']
        vheader = None
        customID = 1
        self.rowC = int(len(data))
        self.model = TableModel(data, header, customID, vheader)

    def addRow(self):
        if int(self.rowC) < 6:
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
    def get_data(self):
        """Возвращает текущие данные таблицы."""
        return self.model._data
    def get_header(self):
        return self.model._header

def initTable2():
    if os.path.exists('./data/table2.json'):
        with open('./data/table2.json', 'r', encoding='utf-8') as read_file:
            data = json.load(read_file)
            _data = []
            for row in data:
                _col = []
                for col in row:
                    _col.append(row[col])
                _data.append(_col)
            return _data
    else:
        return [['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', '']]

def saveTable2(data, file='./data/table2.json'):
    with open(file, 'w', encoding='utf-8') as write_file:
        json.dump(data, write_file, ensure_ascii=False)

class Table2(QtWidgets.QMainWindow, Table_2.Ui_Table_2):

    def __init__(self):
        super().__init__()
        self._initModel()
        self.setupUi(self)
        self._initGui()

    def _initGui(self):
        self.tableView2.setModel(self.model)
        header = self.tableView2.horizontalHeader()
        vheader = self.tableView2.verticalHeader()
        header.ResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableView2.setHorizontalHeader(header)
        self.tableView2.setVerticalHeader(vheader)
        self.saveButton.clicked.connect(self.screen)
        self.addRowButton.clicked.connect(self.addRow)
        self.delRowButton.clicked.connect(self.delRow)

    def _initModel(self):
        data = initTable2()
        header = ['m, кг', 'M, кг', 'M/m', 't₁, с', 't₂, с', 't₃, c',  't₄, c', '〈t〉, с', 'Δt, с']
        vheader = None
        customID = 2
        self.rowC = int(len(data))
        self.model = TableModel(data, header, customID, vheader)

    def addRow(self):
        if int(self.rowC) < 6:
            self.rowC = int(self.rowC) + 1
            self.model.layoutAboutToBeChanged.emit()
            self.model.insertRows(self.model.rowCount(), count=1)
            self.model.layoutChanged.emit()
        return None

    def delRow(self):
        self.model.layoutAboutToBeChanged.emit()
        _index = self.tableView2.selectedIndexes()
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
        saveTable2(_data, file='./data/table2.json')

    def screen(self):
        self.saveModel()
        imageTabel = self.tableView2.grab(self.tableView2.rect())
        imageTabel.save('./images/imageTabel2.png')

    def closeEvent(self, event):
        self.screen()
        self.close()
    def get_data(self):
        """Возвращает текущие данные таблицы."""
        return self.model._data
    def get_header(self):
        return self.model._header

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
        self.table2Button.clicked.connect(self.openTable2)
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
    def openTable2(self):
        if self.table2 and self.table2.isVisible():
            self.table2.saveModel()
        self.table2 = Table2()
        self.table2.show()

    def openTable3(self):
        if self.table3 and self.table3.isVisible():
            self.table3.saveModel()
        #self.table3 = Table3()
        self.table3.show()
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

            im2 = Image.open('./images/imageTabel2.png')

            Table2Header = Image.open('./images/Table2Header.png')

            self.mergePng(Table2Header, im2, resize_big_image=True).save('./images/newIm.png')

            newIm = Image.open('./images/newIm.png')
            a4im = Image.new('RGB', (595, 842), (255, 255, 255))
            a4im.paste(newIm, newIm.getbbox())
            a4im.save('images/pdfFiles/32_tables.pdf', 'PDF', quality=100)
            Table1Header = Image.open('./images/Table1Header.png')
            im1 = Image.open('./images/imageTabel1.png')
            self.mergePng(Table1Header, im1, resize_big_image=True).save('./images/t1.png')
            t1 = Image.open('./images/t1.png')
            a4im = Image.new('RGB', (595, 842), (255, 255, 255))
            a4im.paste(t1, t1.getbbox())
            a4im.save('images/pdfFiles/31_tables.pdf', 'PDF', quality=100)
            # Создаем графики из двух таблиц в формат png
            if (self.table1 == None):
                self.table1 = Table1()
            data = self.table1.get_data()
            x, y = get_xy_data(data, 'h, м', self.table1.get_header())
            save_graph_to_png(x, y, './images/graph1.png')
            if(self.table2 == None):
                self.table2=Table2()
            data = self.table2.get_data()
            x, y = get_xy_data(data, 'M/m', self.table2.get_header())
            save_graph_to_png(x, y, './images/graph2.png')

            graph=Image.open('./images/graph1.png')
            graph.thumbnail((400, 400))
            a4im = Image.new('RGB', (595, 842), (255, 255, 255))
            # Получаем размеры изображения и листа
            graph_width, graph_height = graph.size
            a4_width, a4_height = a4im.size

            # Рассчитываем координаты для центрирования изображения
            x = (a4_width - graph_width) // 2  # Центр по горизонтали
            y = 20  # Центр по вертикали

            # Вставляем изображение в центр листа A4
            a4im.paste(graph, (x, y))
            a4im.save('images/pdfFiles/41_graph.pdf', 'PDF', quality=100)

            graph = Image.open('./images/graph2.png')
            graph.thumbnail((400, 400))
            a4im = Image.new('RGB', (595, 842), (255, 255, 255))
            # Получаем размеры изображения и листа
            graph_width, graph_height = graph.size
            a4_width, a4_height = a4im.size

            # Рассчитываем координаты для центрирования изображения
            x = (a4_width - graph_width) // 2  # Центр по горизонтали
            y = 20  # Центр по вертикали

            # Вставляем изображение в центр листа A4
            a4im.paste(graph, (x, y))
            a4im.save('images/pdfFiles/42_graph.pdf', 'PDF', quality=100)
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