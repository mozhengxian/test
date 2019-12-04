# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qmywplot.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QMYWPLOT(object):
    def setupUi(self, QMYWPLOT):
        QMYWPLOT.setObjectName("QMYWPLOT")
        QMYWPLOT.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(QMYWPLOT)
        self.centralwidget.setObjectName("centralwidget")
        QMYWPLOT.setCentralWidget(self.centralwidget)

        self.retranslateUi(QMYWPLOT)
        QtCore.QMetaObject.connectSlotsByName(QMYWPLOT)

    def retranslateUi(self, QMYWPLOT):
        _translate = QtCore.QCoreApplication.translate
        QMYWPLOT.setWindowTitle(_translate("QMYWPLOT", "MainWindow"))
