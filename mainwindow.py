# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableView, QVBoxLayout, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1358, 879)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 1341, 871))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1331, 841))
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.open_btn = QPushButton(self.widget)
        self.open_btn.setObjectName(u"open_btn")
        icon = QIcon()
        icon.addFile(u":/icons/open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_btn.setIcon(icon)
        self.open_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.open_btn)

        self.save_btn = QPushButton(self.widget)
        self.save_btn.setObjectName(u"save_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_btn.setIcon(icon1)
        self.save_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.save_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.instruct = QPlainTextEdit(self.widget)
        self.instruct.setObjectName(u"instruct")

        self.verticalLayout_5.addWidget(self.instruct)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.code_table = QTableView(self.widget)
        self.code_table.setObjectName(u"code_table")

        self.verticalLayout_2.addWidget(self.code_table)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.copy_couch_to_answer = QPushButton(self.widget)
        self.copy_couch_to_answer.setObjectName(u"copy_couch_to_answer")
        icon2 = QIcon()
        icon2.addFile(u":/icons/move.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.copy_couch_to_answer.setIcon(icon2)
        self.copy_couch_to_answer.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.copy_couch_to_answer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.couch_answer = QPlainTextEdit(self.widget)
        self.couch_answer.setObjectName(u"couch_answer")

        self.verticalLayout_3.addWidget(self.couch_answer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.copy_my_to_answer = QPushButton(self.widget)
        self.copy_my_to_answer.setObjectName(u"copy_my_to_answer")
        self.copy_my_to_answer.setIcon(icon2)
        self.copy_my_to_answer.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.copy_my_to_answer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.my_answer = QPlainTextEdit(self.widget)
        self.my_answer.setObjectName(u"my_answer")

        self.verticalLayout_4.addWidget(self.my_answer)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.plainTextEdit = QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_6.addWidget(self.plainTextEdit)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.total_edited = QLabel(self.widget)
        self.total_edited.setObjectName(u"total_edited")

        self.horizontalLayout_6.addWidget(self.total_edited)

        self.remain_to_edit = QLabel(self.widget)
        self.remain_to_edit.setObjectName(u"remain_to_edit")

        self.horizontalLayout_6.addWidget(self.remain_to_edit)

        self.show_all = QCheckBox(self.widget)
        self.show_all.setObjectName(u"show_all")

        self.horizontalLayout_6.addWidget(self.show_all)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.previous = QPushButton(self.widget)
        self.previous.setObjectName(u"previous")
        icon3 = QIcon()
        icon3.addFile(u":/icons/back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.previous.setIcon(icon3)
        self.previous.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.previous)

        self.next = QPushButton(self.widget)
        self.next.setObjectName(u"next")
        icon4 = QIcon()
        icon4.addFile(u":/icons/forward.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.next.setIcon(icon4)
        self.next.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.next)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.full_table = QTableView(self.tab_2)
        self.full_table.setObjectName(u"full_table")
        self.full_table.setGeometry(QRect(70, 70, 911, 631))
        self.full_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u043f\u043e \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044e", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0430\u043a\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442 \u0442\u0440\u0435\u043d\u0435\u0440\u0430", None))
        self.copy_couch_to_answer.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432 \u043d\u043e\u0432\u044b\u0439", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0439 \u043e\u0442\u0432\u0435\u0442", None))
        self.copy_my_to_answer.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432 \u043d\u043e\u0432\u044b\u0439", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u043e\u0442\u0432\u0435\u0442", None))
        self.total_edited.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e \u0438\u0441\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043e", None))
        self.remain_to_edit.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u0438\u0441\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.show_all.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.previous.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0439", None))
        self.next.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0439", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u043f\u043e \u043e\u0434\u043d\u043e\u043c\u0443", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0442\u0430\u0431\u043b\u0438\u0446\u0435\u0439", None))
    # retranslateUi

