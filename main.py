import sys

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
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
        self.copy_couch_to_answer.clicked.connect(self.copy_couch)
        self.copy_my_to_answer.clicked.connect(self.copy_my)
        self.next.clicked.connect(self.next_record)
        self.previous.clicked.connect(self.previous_record)
        self.save_btn.clicked.connect(self.save_data)
        self.tabWidget.setTabVisible(1, False)
        self.model = None
        self.code_model = None
        self.current_rec = None
        self.current_index = None
        self.records = None

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
            self.save_btn.setEnabled(True)
            # self.comments_cb.addItems(self.df.get_comments())

    def full_table(self):
        if self.df is not None and self.model is None:
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
            self.records = self.df.get_all_records(True)
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
            # https: // stackoverflow.com / questions / 62407539 / qtableview - search - and -highlight - items
            # start = self.model.index(0, 0)
            # text = self.current_rec.row_id
            # matches = self.model.match(
            #     start,
            #     QtCore.Qt.DisplayRole,
            #     text,
            #     hits=1,
            #     flags=QtCore.Qt.MatchContains
            # )
            # if matches:
            #     index = matches[0]
            #     # index.row(), index.column()
            #     self.full_table_tv.selectionModel().select(
            #         index, QtCore.QItemSelectionModel.Select)

    @QtCore.pyqtSlot("QModelIndex")
    def change_current_rec(self, modelIndex):
        if self.records is not None:
            if self.current_rec is not None:
                if self.new_answer.toPlainText() != str(self.current_rec.new_answer):
                    self.current_rec.new_answer = self.new_answer.toPlainText()
                    self.df.save_record(self.current_rec)
                    if self.model is not None:
                        self.model.setItem(self.current_index, self.current_reс.get_row())
                    self.records[self.current_index] = self.current_rec
                    self.save_btn.setEnabled(True)
            self.current_rec = self.records[modelIndex.row()]
            self.current_index = modelIndex.row()
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
            if len(row[2]) > 0:
                self.copy_couch_to_answer.setEnabled(True)
            else:
                self.copy_couch_to_answer.setEnabled(False)
            self.instruct.appendPlainText(row[4])
            self.my_answer.appendPlainText(row[3])
            if len(row[3]) > 0:
                self.copy_my_to_answer.setEnabled(True)
            else:
                self.copy_my_to_answer.setEnabled(False)
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

    def next_record(self):
        if self.new_answer.toPlainText() != str(self.current_rec.new_answer):
            self.current_rec.new_answer = self.new_answer.toPlainText()
            self.df.save_record(self.current_rec)
            if self.model is not None:
                self.model.setItem(self.current_index, self.current_reс.get_row())
            self.records[self.current_index] = self.current_rec
            self.save_btn.setEnabled(True)
        if self.current_index < len(self.records) - 1:
            self.current_index += 1
            self.current_rec = self.records[self.current_index]
            self.load_record()

    def previous_record(self):
        if self.new_answer.toPlainText() != self.current_rec.new_answer:
            self.current_rec.new_answer = self.new_answer.toPlainText()
            self.df.save_record(self.current_rec)
            if self.model is not None:
                self.model.setItem(self.current_index, self.current_reс.get_row())
            self.records[self.current_index] = self.current_rec
            self.save_btn.setEnabled(True)
        if self.current_index > 0:
            self.current_index -= 1
            self.current_rec = self.records[self.current_index]
            self.load_record()

    def save_data(self):
        if self.new_answer.toPlainText() != str(self.current_rec.new_answer):
            self.current_rec.new_answer = self.new_answer.toPlainText()
            self.df.save_record(self.current_rec)
        if self.df is not None:
            self.df.save()
            buttonReply = QMessageBox.information(self, "Информация", 'Файл создан в том же каталоге', QMessageBox.Ok)
            # self.save_btn.setEnabled(False)

    def copy_couch(self):
        self.new_answer.clear()
        self.new_answer.appendPlainText(self.couch_answer.toPlainText())

    def copy_my(self):
        self.new_answer.clear()
        self.new_answer.appendPlainText(self.my_answer.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
