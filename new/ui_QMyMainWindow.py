# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 732)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plainText_logs = QtWidgets.QPlainTextEdit(self.tab)
        self.plainText_logs.setMinimumSize(QtCore.QSize(0, 0))
        self.plainText_logs.setLineWidth(1)
        self.plainText_logs.setObjectName("plainText_logs")
        self.verticalLayout_2.addWidget(self.plainText_logs)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(0, 100, 281, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(0, 260, 271, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setGeometry(QtCore.QRect(0, 410, 271, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.puB_logs = QtWidgets.QPushButton(self.groupBox)
        self.puB_logs.setGeometry(QtCore.QRect(30, 460, 91, 31))
        self.puB_logs.setObjectName("puB_logs")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(20, 290, 221, 81))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.puB_GenPower = QtWidgets.QPushButton(self.widget)
        self.puB_GenPower.setObjectName("puB_GenPower")
        self.gridLayout.addWidget(self.puB_GenPower, 0, 0, 1, 1)
        self.puB_Scatter = QtWidgets.QPushButton(self.widget)
        self.puB_Scatter.setObjectName("puB_Scatter")
        self.gridLayout.addWidget(self.puB_Scatter, 0, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(20, 20, 221, 61))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.puB_method = QtWidgets.QPushButton(self.widget1)
        self.puB_method.setObjectName("puB_method")
        self.gridLayout_2.addWidget(self.puB_method, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radB_filter = QtWidgets.QRadioButton(self.widget1)
        self.radB_filter.setObjectName("radB_filter")
        self.gridLayout_3.addWidget(self.radB_filter, 0, 0, 1, 1)
        self.puB_method_filter = QtWidgets.QPushButton(self.widget1)
        self.puB_method_filter.setObjectName("puB_method_filter")
        self.gridLayout_3.addWidget(self.puB_method_filter, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.widget2 = QtWidgets.QWidget(self.groupBox)
        self.widget2.setGeometry(QtCore.QRect(20, 150, 221, 71))
        self.widget2.setObjectName("widget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.airBlower_diameter = QtWidgets.QDoubleSpinBox(self.widget2)
        self.airBlower_diameter.setDecimals(3)
        self.airBlower_diameter.setSingleStep(0.001)
        self.airBlower_diameter.setProperty("value", 1.225)
        self.airBlower_diameter.setObjectName("airBlower_diameter")
        self.horizontalLayout_2.addWidget(self.airBlower_diameter)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.air_density = QtWidgets.QDoubleSpinBox(self.widget2)
        self.air_density.setMaximum(500.0)
        self.air_density.setProperty("value", 133.0)
        self.air_density.setObjectName("air_density")
        self.horizontalLayout_3.addWidget(self.air_density)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.Act_Open = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../images/openfile.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Act_Open.setIcon(icon)
        self.Act_Open.setObjectName("Act_Open")
        self.Act_About = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../images/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Act_About.setIcon(icon1)
        self.Act_About.setObjectName("Act_About")
        self.Act_Help = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../images/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Act_Help.setIcon(icon2)
        self.Act_Help.setObjectName("Act_Help")
        self.Act_Update = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../images/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Act_Update.setIcon(icon3)
        self.Act_Update.setObjectName("Act_Update")
        self.toolBar.addAction(self.Act_Open)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.Act_About)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.Act_Help)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.Act_Update)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "首  页"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.puB_logs.setText(_translate("MainWindow", "导出日记"))
        self.puB_GenPower.setText(_translate("MainWindow", "功率曲线"))
        self.puB_Scatter.setText(_translate("MainWindow", "散点图"))
        self.label.setText(_translate("MainWindow", "经验法(默认)"))
        self.puB_method.setText(_translate("MainWindow", "设置参数"))
        self.radB_filter.setText(_translate("MainWindow", "系数法"))
        self.puB_method_filter.setText(_translate("MainWindow", "设置参数"))
        self.label_2.setText(_translate("MainWindow", "空气密度:"))
        self.label_3.setText(_translate("MainWindow", "风机直径:"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.Act_Open.setText(_translate("MainWindow", "打开"))
        self.Act_Open.setToolTip(_translate("MainWindow", "导入数据"))
        self.Act_About.setText(_translate("MainWindow", "关于"))
        self.Act_About.setToolTip(_translate("MainWindow", "关于"))
        self.Act_Help.setText(_translate("MainWindow", "帮助"))
        self.Act_Help.setToolTip(_translate("MainWindow", "使用说明"))
        self.Act_Update.setText(_translate("MainWindow", "更新"))
        self.Act_Update.setToolTip(_translate("MainWindow", "更新"))