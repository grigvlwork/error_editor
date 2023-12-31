import sys

from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QMenu
from data import datasource
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.Qt import QClipboard
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
        self.filter_comments_cb.stateChanged.connect(self.filter_comments)
        self.accept.clicked.connect(self.accepted)
        self.irrelevant.clicked.connect(self.irrelevanted)
        self.triple_tik_my.clicked.connect(self.triple_ticking_my)
        self.triple_tik_couch.clicked.connect(self.triple_ticking_couch)
        self.my_answer.textChanged.connect(self.my_text_changed)
        self.tabWidget.setTabVisible(1, False)
        self.filter_comments_cb.setVisible(False)
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
            self.filter_comments()
            if len(self.records) > 0:
                self.current_index = 0
                self.current_rec = self.records[0]
                self.load_record()
            self.tabWidget.setTabVisible(1, True)
            self.save_btn.setEnabled(True)

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
            header = QStandardItem(self.df.headers['score'])
            self.model.setHorizontalHeaderItem(6, header)
            header = QStandardItem(self.df.headers['verdict'])
            self.model.setHorizontalHeaderItem(7, header)
            header = QStandardItem(self.df.headers['id'])
            self.model.setHorizontalHeaderItem(8, header)
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
            self.full_table_tv.setColumnWidth(6, 70)
            self.full_table_tv.setColumnWidth(7, 120)
            self.full_table_tv.setColumnWidth(8, 55)

            # https://stackoverflow.com/questions/62407539/
        # self.full_table_tv.clearSelection()
        # start = self.model.index(0, 8)
        # text = self.current_rec.id
        # matches = self.model.match(
        #     start,
        #     QtCore.Qt.DisplayRole,
        #     text,
        #     hits=1,
        #     flags=QtCore.Qt.MatchExactly
        # )
        # if matches:
        #     index = matches[0]
            # index.row(), index.column()
        index = self.model.index(int(self.current_rec.id) - 2, 8)
        self.full_table_tv.selectionModel().select(
            index, QtCore.QItemSelectionModel.Select)
        self.full_table_tv.scrollTo(index)

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
            self.counter_lb.setText('id:' + row[0] + ' (' + str(self.current_index + 1) + '/' +
                                    str(len(self.records)) + ')')
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
            if self.current_rec.verdict:
                self.accept.toggle()
                self.score_lb.show()
                self.score.setCurrentIndex(2 - int(self.current_rec.score))
                self.score.show()
            else:
                self.irrelevant.toggle()
                self.score_lb.hide()
                self.score.hide()

    def next_record(self):
        flag = False
        if self.new_answer.toPlainText() != str(self.current_rec.new_answer):
            self.current_rec.new_answer = self.new_answer.toPlainText()
            flag = True
        if self.current_rec.verdict != self.accept.isChecked():
            self.current_rec.verdict = self.accept.isChecked()
            self.current_rec.score = self.score.currentText() if self.accept.isChecked() else ''
            flag = True
        if self.score.currentText() != self.current_rec.score:
            self.current_rec.score = self.score.currentText() if self.accept.isChecked() else ''
            flag = True
        if flag:
            self.df.save_record(self.current_rec)
            # if self.model is not None:
            #     # иногда пропадает self.current_rec
            #     self.model.setItem(self.current_index, self.current_reс.get_row())
            self.records[self.current_index] = self.current_rec
            self.save_btn.setEnabled(True)
        if self.current_index < len(self.records) - 1:
            self.current_index += 1
            self.current_rec = self.records[self.current_index]
            self.load_record()

    def previous_record(self):
        flag = False
        if self.new_answer.toPlainText() != str(self.current_rec.new_answer):
            self.current_rec.new_answer = self.new_answer.toPlainText()
            flag = True
        if self.current_rec.verdict != self.accept.isChecked():
            self.current_rec.verdict = self.accept.isChecked()
            self.current_rec.score = self.score.currentText() if self.accept.isChecked() else ''
            flag = True
        if self.score.currentText() != self.current_rec.score:
            self.current_rec.score = self.score.currentText() if self.accept.isChecked() else ''
            flag = True
        if flag:
            self.df.save_record(self.current_rec)
            # if self.model is not None:
            #     self.model.setItem(self.current_index, self.current_reс.get_row())
            self.records[self.current_index] = self.current_rec
            self.save_btn.setEnabled(True)
        if self.current_index > 0:
            self.current_index -= 1
            self.current_rec = self.records[self.current_index]
            self.load_record()

    def save_data(self):
        flag = False
        if self.new_answer.toPlainText() != str(self.current_rec.new_answer):
            self.current_rec.new_answer = self.new_answer.toPlainText()
            flag = True
        if self.accept.isDown() and not self.current_rec.verdict or \
                self.irrelevant.isChecked() and self.current_rec.verdict:
            self.current_rec.verdict = self.accept().isDown()
            flag = True
        if self.current_rec.verdict and self.current_rec.score != self.score.currentText():
            self.current_rec.score = self.score.currentText()
            flag = True
        if not self.current_rec.verdict and self.current_rec.score != '':
            self.current_rec.score = ''
        if flag:
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

    def filter_comments(self):
        if self.filter_comments_cb.isChecked():
            self.df.get_all_records(True, False)
        else:
            self.df.get_all_records(True, True)
        self.current_index = 0
        self.current_rec = self.records[0]
        self.load_record()
        self.model = None

    def accepted(self):
        # self.current_rec.verdict = True
        self.score_lb.show()
        self.score.show()

    def irrelevanted(self):
        # self.current_rec.verdict = False
        self.score_lb.hide()
        self.score.hide()

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        copyAction = contextMenu.addAction('Копировать')
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))

    def triple_ticking_my(self):
        t = self.my_answer.toPlainText()
        text = t.split('```')[1]
        self.my_answer.clear()
        t = t.replace('```' + text + '```', '\n```\n' + text + '\n```')
        if t[-1] == '.':
            t = t[:-1]
        self.my_answer.setPlainText(t)

    def triple_ticking_couch(self):
        t = self.couch_answer.toPlainText()
        text = t.split('```')[1]
        self.my_answer.clear()
        t = t.replace('```' + text + '```', '\n```\n' + text + '\n```')
        if t[-1] == '.':
            t = t[:-1]
        self.couch_answer.setPlainText(t)

    def my_text_changed(self):
        if len(self.my_answer.toPlainText()) > 0:
            self.copy_my_to_answer.setEnabled(True)


if __name__ == '__main__':
    import traceback

    app = QApplication(sys.argv)
    ex = MyWidget()


    def excepthook(exc_type, exc_value, exc_tb):
        tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
        # tb += '\n'.join(ex.current_rec.get_row())
        print(tb)

        msg = QMessageBox.critical(
            None,
            "Error catched!:",
            tb
        )
        QApplication.quit()


    sys.excepthook = excepthook
    ex.show()
    sys.exit(app.exec_())
