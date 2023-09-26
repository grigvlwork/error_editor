import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from data import datasource
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from images import files_rc



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainwindow.ui', self)  # Загружаем дизайн
        self.open_btn.clicked.connect(self.open_f)
        self.df = None
        self.tabWidget.currentChanged.connect(self.full_table)
        self.model = None
        # open_btn.clicked.connect(self.open_file())
        # Обратите внимание: имя элемента такое же как в QTDesigner

    # def run(self):
    # self.label.setText("OK")
    # Имя элемента совпадает с objectName в QTDesigner
    def open_f(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', "Excel файлы (*.xls *.xlsx)")
        if len(fname[0]) > 0:
            self.df = datasource.Dataframe()
            self.df.set_filename(fname[0])
            self.df.open()
            # self.comments_cb.clear()
            # self.comments_cb.addItems(self.df.get_comments())

    def full_table(self):
        if self.df is not None:
            self.model = QStandardItemModel()
            header = QStandardItem(self.df.headers['RowID'])
            self.model.setColumnCount(6)
            self.model.setHorizontalHeaderItem(0, header)
            header = QStandardItem(self.df.headers['comment'])
            self.model.setHorizontalHeaderItem(1, header)
            header = QStandardItem(self.df.headers['teach_ans'])
            self.model.setHorizontalHeaderItem(2, header)
            header = QStandardItem(self.df.headers['super_ans'])
            self.model.setHorizontalHeaderItem(3, header)
            header = QStandardItem(self.df.headers['task'])
            self.model.setHorizontalHeaderItem(4, header)
            header = QStandardItem(self.df.headers['new_ans'])
            self.model.setHorizontalHeaderItem(5, header)
            # self.model.setHorizontalHeaderItem()
            records = self.df.get_all_records(True)
            # self.model.setRowCount(len(records) + 1)
            row = 0
            for rec in records:
                items = []
                for it in rec.get_row():
                    item = QStandardItem(it)
                    items.append(item)
                self.model.appendRow(items)
            self.full_table_tv.setModel(self.model)
            self.full_table_tv.setColumnWidth(0, 55)
            self.full_table_tv.setColumnWidth(1, 120)
            self.full_table_tv.setColumnWidth(2, 220)
            self.full_table_tv.setColumnWidth(3, 220)
            self.full_table_tv.setColumnWidth(4, 220)
            self.full_table_tv.setColumnWidth(5, 220)

            # print(self.df.main_df.shape)
            # app = QApplication(sys.argv)
            # model =


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
