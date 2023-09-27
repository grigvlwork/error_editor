import sys

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from data import datasource
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import QModelIndex
from images import files_rc



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainwindow.ui', self)  # Загружаем дизайн
        self.open_btn.clicked.connect(self.open_f)
        self.df = None
        self.tabWidget.currentChanged.connect(self.full_table)
        self.full_table_tv.clicked.connect(self.change_current_rec)
        # self.new_answer.textChanged.connect(self.check_edit_answer)
        self.next.clicked.connect(self.next_record)
        self.previous.clicked.connect(self.previous_record)
        self.tabWidget.setTabVisible(1, False)
        self.model = None
        self.code_model = None
        self.current_rec = None
        self.current_index = None
        self.records = None
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
            self.records = self.df.get_all_records()
            if len(self.records) > 0:
                self.current_index = 0
                self.current_rec = self.records[0]
                self.load_record()
            self.tabWidget.setTabVisible(1, True)
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
            self.records = self.df.get_all_records(True)
            # self.model.setRowCount(len(records) + 1)
            row = 0
            for rec in self.records:
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

    @QtCore.pyqtSlot("QModelIndex")
    def change_current_rec(self, modelIndex):
        if self.records is not None:
            if self.current_rec is not None:
                if self.current_rec.changed:
                    self.df.save_record(self.current_rec)
                    self.current_rec = False
            self.current_rec = self.records[modelIndex.row()]
            self.load_record()

    def clear_controls(self):
        self.couch_answer.clear()
        self.instruct.clear()
        self.my_answer.clear()
        self.new_answer.clear()

    def load_record(self):
        self.clear_controls()
        if self.current_rec is not None:
            row = self.current_rec.get_row()
            self.comment_lb.setText(row[1])
            self.couch_answer.appendPlainText(row[2])
            self.instruct.appendPlainText(row[4])
            self.my_answer.appendPlainText(row[3])
            self.new_answer.appendPlainText(row[5])
            if len(self.current_rec.code) > 0:
                self.code_model = QStandardItemModel()
                for row in self.current_rec.code:
                    it = QStandardItem(row)
                    self.code_model.appendRow(it)
                self.code_table.setModel(self.code_model)
                self.code_table.horizontalHeader().setVisible(False)
                self.code_table.resizeColumnToContents(0)
                if self.current_index == 0:
                    self.previous.setEnabled(False)
                else:
                    self.previous.setEnabled(True)
                if self.current_index >= len(self.records) - 1:
                    self.next.setEnabled(False)
                else:
                    self.next.setEnabled(True)
                # print(self.current_rec.code)
            # print(self.current_rec)

    # def check_edit_answer(self):
    #     if self.current_rec is not None:
    #         if self.current_rec.new_answer != self.new_answer.toPlainText():
    #             self.current_rec.new_answer = self.new_answer.toPlainText()
    #             self.current_rec.changed = True

    def next_record(self):
        print(self.new_answer.toPlainText())
        print(self.current_rec.new_answer)
        if self.new_answer.toPlainText() != str(self.current_rec.new_answer):
            self.current_rec.new_answer = self.new_answer.toPlainText()
            self.df.save_record(self.current_rec)
            self.model.setItem(self.current_index, self.current_reс.get_row())
            self.records[self.current_index] = self.current_rec
            self.save.setEnabled(True)
        if self.current_index < len(self.records) - 1:
            self.current_index += 1
            self.current_rec = self.records[self.current_index]
            self.load_record()

    def previous_record(self):
        if self.new_answer.toPlainText() != self.current_rec.new_answer:
            self.current_rec.new_answer = self.new_answer.toPlainText()
            self.df.save_record(self.current_rec)
            self.model.setItem(self.current_index, self.current_reс.get_row())
            self.records[self.current_index] = self.current_rec
            self.save.setEnabled(True)
        if self.current_index > 0:
            self.current_index -= 1
            self.current_rec = self.records[self.current_index]
            self.load_record()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
