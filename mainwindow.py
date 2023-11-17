# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 852)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.open_btn = QtWidgets.QPushButton(self.tab)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_btn.setIcon(icon)
        self.open_btn.setIconSize(QtCore.QSize(24, 24))
        self.open_btn.setObjectName("open_btn")
        self.horizontalLayout_6.addWidget(self.open_btn)
        self.save_btn = QtWidgets.QPushButton(self.tab)
        self.save_btn.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon1)
        self.save_btn.setIconSize(QtCore.QSize(24, 24))
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_6.addWidget(self.save_btn)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.accept = QtWidgets.QRadioButton(self.tab)
        self.accept.setObjectName("accept")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.accept)
        self.verticalLayout.addWidget(self.accept)
        self.irrelevant = QtWidgets.QRadioButton(self.tab)
        self.irrelevant.setObjectName("irrelevant")
        self.buttonGroup.addButton(self.irrelevant)
        self.verticalLayout.addWidget(self.irrelevant)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.score_lb = QtWidgets.QLabel(self.tab)
        self.score_lb.setObjectName("score_lb")
        self.horizontalLayout.addWidget(self.score_lb)
        self.score = QtWidgets.QComboBox(self.tab)
        self.score.setObjectName("score")
        self.score.addItem("")
        self.score.addItem("")
        self.score.addItem("")
        self.score.addItem("")
        self.score.addItem("")
        self.horizontalLayout.addWidget(self.score)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.filter_comments_cb = QtWidgets.QCheckBox(self.tab)
        self.filter_comments_cb.setChecked(True)
        self.filter_comments_cb.setObjectName("filter_comments_cb")
        self.verticalLayout_3.addWidget(self.filter_comments_cb)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.comment_lb = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.comment_lb.setFont(font)
        self.comment_lb.setWordWrap(True)
        self.comment_lb.setObjectName("comment_lb")
        self.horizontalLayout_6.addWidget(self.comment_lb)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.instruct = QtWidgets.QPlainTextEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.instruct.setFont(font)
        self.instruct.setObjectName("instruct")
        self.verticalLayout_5.addWidget(self.instruct)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.code_table = QtWidgets.QTableView(self.tab)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.code_table.setFont(font)
        self.code_table.setObjectName("code_table")
        self.verticalLayout_2.addWidget(self.code_table)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.triple_tik_couch = QtWidgets.QPushButton(self.tab)
        self.triple_tik_couch.setObjectName("triple_tik_couch")
        self.horizontalLayout_3.addWidget(self.triple_tik_couch)
        self.copy_couch_to_answer = QtWidgets.QPushButton(self.tab)
        self.copy_couch_to_answer.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/move.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_couch_to_answer.setIcon(icon2)
        self.copy_couch_to_answer.setIconSize(QtCore.QSize(24, 24))
        self.copy_couch_to_answer.setObjectName("copy_couch_to_answer")
        self.horizontalLayout_3.addWidget(self.copy_couch_to_answer)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.couch_answer = QtWidgets.QPlainTextEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.couch_answer.setFont(font)
        self.couch_answer.setObjectName("couch_answer")
        self.verticalLayout_6.addWidget(self.couch_answer)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.triple_tik_my = QtWidgets.QPushButton(self.tab)
        self.triple_tik_my.setObjectName("triple_tik_my")
        self.horizontalLayout_4.addWidget(self.triple_tik_my)
        self.copy_my_to_answer = QtWidgets.QPushButton(self.tab)
        self.copy_my_to_answer.setEnabled(False)
        self.copy_my_to_answer.setIcon(icon2)
        self.copy_my_to_answer.setIconSize(QtCore.QSize(24, 24))
        self.copy_my_to_answer.setObjectName("copy_my_to_answer")
        self.horizontalLayout_4.addWidget(self.copy_my_to_answer)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.my_answer = QtWidgets.QPlainTextEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.my_answer.setFont(font)
        self.my_answer.setObjectName("my_answer")
        self.verticalLayout_6.addWidget(self.my_answer)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.new_answer = QtWidgets.QPlainTextEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.new_answer.setFont(font)
        self.new_answer.setObjectName("new_answer")
        self.verticalLayout_6.addWidget(self.new_answer)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.counter_lb = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.counter_lb.setFont(font)
        self.counter_lb.setObjectName("counter_lb")
        self.horizontalLayout_5.addWidget(self.counter_lb)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.previous = QtWidgets.QPushButton(self.tab)
        self.previous.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous.setIcon(icon3)
        self.previous.setIconSize(QtCore.QSize(24, 24))
        self.previous.setObjectName("previous")
        self.horizontalLayout_5.addWidget(self.previous)
        self.next = QtWidgets.QPushButton(self.tab)
        self.next.setEnabled(False)
        self.next.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/forward.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon4)
        self.next.setIconSize(QtCore.QSize(24, 24))
        self.next.setObjectName("next")
        self.horizontalLayout_5.addWidget(self.next)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.full_table_tv = QtWidgets.QTableView(self.tab_2)
        self.full_table_tv.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.full_table_tv.setObjectName("full_table_tv")
        self.horizontalLayout_8.addWidget(self.full_table_tv)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_7.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Работа над ошибками"))
        self.open_btn.setText(_translate("MainWindow", "Открыть файл"))
        self.save_btn.setText(_translate("MainWindow", "Сохранить файл"))
        self.accept.setText(_translate("MainWindow", "Ответ принят"))
        self.irrelevant.setText(_translate("MainWindow", "Не актуальный"))
        self.score_lb.setText(_translate("MainWindow", "  Оценка"))
        self.score.setItemText(0, _translate("MainWindow", "2"))
        self.score.setItemText(1, _translate("MainWindow", "1"))
        self.score.setItemText(2, _translate("MainWindow", "0"))
        self.score.setItemText(3, _translate("MainWindow", "-1"))
        self.score.setItemText(4, _translate("MainWindow", "-2"))
        self.filter_comments_cb.setText(_translate("MainWindow", "Показать все"))
        self.comment_lb.setText(_translate("MainWindow", "Комментарий"))
        self.label_5.setText(_translate("MainWindow", "Инстракт"))
        self.label_2.setText(_translate("MainWindow", "Программа"))
        self.label_3.setText(_translate("MainWindow", "Ответ тренера"))
        self.triple_tik_couch.setText(_translate("MainWindow", "```"))
        self.copy_couch_to_answer.setText(_translate("MainWindow", "Копировать в новый"))
        self.label_4.setText(_translate("MainWindow", "Мой ответ"))
        self.triple_tik_my.setText(_translate("MainWindow", "```"))
        self.copy_my_to_answer.setText(_translate("MainWindow", "Копировать в новый"))
        self.label_6.setText(_translate("MainWindow", "Новый ответ"))
        self.counter_lb.setText(_translate("MainWindow", "_"))
        self.previous.setText(_translate("MainWindow", "Предыдущий"))
        self.next.setText(_translate("MainWindow", "Следующий"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Просмотр по одному"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Просмотр таблицей"))
import files_rc
