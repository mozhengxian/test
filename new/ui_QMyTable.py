# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\qmytable.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QMyTable(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1291, 746)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitterMain = QtWidgets.QSplitter(self.centralWidget)
        self.splitterMain.setOrientation(QtCore.Qt.Horizontal)
        self.splitterMain.setObjectName("splitterMain")
        self.groupBox = QtWidgets.QGroupBox(self.splitterMain)
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btnClearContents = QtWidgets.QPushButton(self.groupBox)
        self.btnClearContents.setObjectName("btnClearContents")
        self.gridLayout.addWidget(self.btnClearContents, 3, 1, 1, 1)
        self.btnSetRows = QtWidgets.QPushButton(self.groupBox)
        self.btnSetRows.setMinimumSize(QtCore.QSize(0, 25))
        self.btnSetRows.setObjectName("btnSetRows")
        self.gridLayout.addWidget(self.btnSetRows, 1, 0, 1, 1)
        self.btnInsertRow = QtWidgets.QPushButton(self.groupBox)
        self.btnInsertRow.setObjectName("btnInsertRow")
        self.gridLayout.addWidget(self.btnInsertRow, 2, 0, 1, 1)
        self.btnAppendRow = QtWidgets.QPushButton(self.groupBox)
        self.btnAppendRow.setObjectName("btnAppendRow")
        self.gridLayout.addWidget(self.btnAppendRow, 2, 1, 1, 1)
        self.btnSetHeader = QtWidgets.QPushButton(self.groupBox)
        self.btnSetHeader.setMinimumSize(QtCore.QSize(0, 25))
        self.btnSetHeader.setObjectName("btnSetHeader")
        self.gridLayout.addWidget(self.btnSetHeader, 0, 0, 1, 2)
        self.btnDelCurRow = QtWidgets.QPushButton(self.groupBox)
        self.btnDelCurRow.setObjectName("btnDelCurRow")
        self.gridLayout.addWidget(self.btnDelCurRow, 3, 0, 1, 1)
        self.spinRowCount = QtWidgets.QSpinBox(self.groupBox)
        self.spinRowCount.setMinimum(2)
        self.spinRowCount.setProperty("value", 53)
        self.spinRowCount.setObjectName("spinRowCount")
        self.gridLayout.addWidget(self.spinRowCount, 1, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.splitterMain)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.splitter.setLineWidth(2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableInfo = QtWidgets.QTableWidget(self.splitter)
        self.tableInfo.setAlternatingRowColors(True)
        self.tableInfo.setRowCount(0)
        self.tableInfo.setColumnCount(0)
        self.tableInfo.setObjectName("tableInfo")
        self.tableInfo.horizontalHeader().setDefaultSectionSize(100)
        self.tableInfo.verticalHeader().setDefaultSectionSize(30)
        self.verticalLayout.addWidget(self.splitterMain)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo3_10, QTableWidget的使用"))
        self.btnClearContents.setText(_translate("MainWindow", "清空表格内容"))
        self.btnSetRows.setText(_translate("MainWindow", "设置行数"))
        self.btnInsertRow.setText(_translate("MainWindow", "插入行"))
        self.btnAppendRow.setText(_translate("MainWindow", "添加行"))
        self.btnSetHeader.setText(_translate("MainWindow", "设置表头"))
        self.btnDelCurRow.setText(_translate("MainWindow", "删除当前行"))
# import res_rc
