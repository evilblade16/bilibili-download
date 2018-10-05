# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(915, 580)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(915, 580))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main_ico/bilibili.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("border-image: url(:/main_ico/background.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(915, 580))
        self.centralwidget.setObjectName("centralwidget")
        self.display_table = QtWidgets.QTableWidget(self.centralwidget)
        self.display_table.setEnabled(True)
        self.display_table.setGeometry(QtCore.QRect(20, 130, 881, 431))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.display_table.setFont(font)
        self.display_table.setAutoFillBackground(False)
        self.display_table.setStyleSheet("border-image: None;\n"
"background-color:rgba(0, 0, 0,0.3);\n"
"font: 10pt \"幼圆\";\n"
"\n"
"selection-background-color: rgba(0, 0, 0,0.5);\n"
"selection-color: rgb(255, 255, 255);\n"
"gridline-color: white;\n"
"color:white;\n"
"border-radius:10px;")
        self.display_table.setAutoScroll(True)
        self.display_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.display_table.setAlternatingRowColors(False)
        self.display_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.display_table.setShowGrid(False)
        self.display_table.setGridStyle(QtCore.Qt.SolidLine)
        self.display_table.setObjectName("display_table")
        self.display_table.setColumnCount(6)
        self.display_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(5, item)
        self.display_table.horizontalHeader().setVisible(True)
        self.display_table.horizontalHeader().setCascadingSectionResizes(False)
        self.display_table.horizontalHeader().setHighlightSections(False)
        self.display_table.horizontalHeader().setSortIndicatorShown(False)
        self.display_table.verticalHeader().setVisible(False)
        self.display_table.verticalHeader().setDefaultSectionSize(37)
        self.display_table.verticalHeader().setHighlightSections(True)
        self.display_table.verticalHeader().setSortIndicatorShown(False)
        self.display_table.verticalHeader().setStretchLastSection(False)
        self.url_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.url_edit.setGeometry(QtCore.QRect(90, 50, 511, 41))
        self.url_edit.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border-image:none;\n"
"background-color:rgba(0, 0, 0,0.2);\n"
"border:1px solid rgb(255, 255, 255);\n"
"font: 10pt \"幼圆\";\n"
"color:white;\n"
"selection-background-color: rgba(0, 0, 0,0.5);\n"
"border-radius:10px;")
        self.url_edit.setObjectName("url_edit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 50, 93, 41))
        self.pushButton.setStyleSheet("border-image:none;\n"
"border:1px solid rgb(255, 255, 255);\n"
"background-color:rgba(100, 100, 100,0.5);\n"
"color:white;\n"
"border-radius:10px;\n"
"font: 17pt \"幼圆\";")
        self.pushButton.setObjectName("pushButton")
        self.all_select_check_button = QtWidgets.QCheckBox(self.centralwidget)
        self.all_select_check_button.setGeometry(QtCore.QRect(-150, 100, 121, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.all_select_check_button.setFont(font)
        self.all_select_check_button.setMouseTracking(True)
        self.all_select_check_button.setToolTip("")
        self.all_select_check_button.setStyleSheet("border-image:none;\n"
"font: 12pt \"幼圆\";\n"
"color:white;\n"
"background-color:rgba(0, 0, 0,0.2);")
        self.all_select_check_button.setObjectName("all_select_check_button")
        self.download_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_button.setGeometry(QtCore.QRect(922, 50, 93, 41))
        self.download_button.setStyleSheet("border-image:none;\n"
"background-color:rgba(100, 100, 100,0.5);\n"
"border:1px solid rgb(255, 255, 255);\n"
"color:white;\n"
"font: 17pt \"幼圆\";\n"
"border-radius:10px;")
        self.download_button.setObjectName("download_button")
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(870, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.close_button.setFont(font)
        self.close_button.setStyleSheet("border-image:none;\n"
"border:1px solid rgb(255, 255, 255);\n"
"background-color:rgba(255, 0, 0,0.5);\n"
"color:white;\n"
"border-radius:10px;\n"
"font: 17pt \"幼圆\";")
        self.close_button.setObjectName("close_button")
        self.min_button = QtWidgets.QPushButton(self.centralwidget)
        self.min_button.setGeometry(QtCore.QRect(830, 10, 31, 31))
        self.min_button.setStyleSheet("border-image:none;\n"
"border:1px solid rgb(255, 255, 255);\n"
"background-color:rgba(0, 0, 255,0.5);\n"
"color:white;\n"
"border-radius:10px;\n"
"font: 17pt \"幼圆\";")
        self.min_button.setObjectName("min_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.jiexi)
        self.all_select_check_button.stateChanged['int'].connect(MainWindow.all_select)
        self.download_button.clicked.connect(MainWindow.download)
        self.min_button.clicked.connect(MainWindow.min_click)
        self.close_button.clicked.connect(MainWindow.close_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "bilibili-download"))
        self.display_table.setSortingEnabled(False)
        item = self.display_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "选择"))
        item = self.display_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "标题"))
        item = self.display_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "时长"))
        item = self.display_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "大小"))
        item = self.display_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "进度"))
        item = self.display_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "段落"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.all_select_check_button.setText(_translate("MainWindow", "我全都要！"))
        self.download_button.setText(_translate("MainWindow", "下载"))
        self.close_button.setText(_translate("MainWindow", "×"))
        self.min_button.setText(_translate("MainWindow", "-"))

import bilibili_rc
