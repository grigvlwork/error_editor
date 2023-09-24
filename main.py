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
            self.comments_cb.clear()
            self.comments_cb.addItems(self.df.get_comments())

    def full_table(self):
        if self.df is not None:
            self.model = QStandardItemModel()
            print(self.df.main_df.shape)
            # app = QApplication(sys.argv)
            # model =


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
