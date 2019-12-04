import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QTableWidgetItem, QAbstractItemView)

from enum import Enum  # 枚举类型

from PyQt5.QtCore import pyqtSlot, Qt, QDate

from PyQt5.QtGui import QFont, QBrush, QIcon

from ui_QMyTable import Ui_QMyTable


# class CellType(Enum):  ##各单元格的类型
#     ctName = 1000
#     ctSex = 1001
#     ctBirth = 1002
#     ctNation = 1003
#     ctScore = 1004
#     ctPartyM = 1005
#
#
# class FieldColNum(Enum):  ##各字段在表格中的列号
#     colName = 0
#     colSex = 1
#     colBirth = 2
#     colNation = 3
#     colScore = 4
#     colPartyM = 5


class QMyTable(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_QMyTable()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        #      self.setWindowTitle("Demo3_10，QTableWidget的使用")

        # self.LabCellIndex = QLabel("当前单元格坐标：", self)
        # self.LabCellIndex.setMinimumWidth(250)
        # self.LabCellType = QLabel("当前单元格类型：", self)
        # self.LabCellType.setMinimumWidth(200)
        # self.LabStudID = QLabel("学生ID：", self)
        # self.LabStudID.setMinimumWidth(200)
        # self.ui.statusBar.addWidget(self.LabCellIndex)  # 加到状态栏
        # self.ui.statusBar.addWidget(self.LabCellType)
        # self.ui.statusBar.addWidget(self.LabStudID)

        self.ui.tableInfo.setAlternatingRowColors(True)  # 交替行颜色
        # self.__tableInitialized = False  # 表格数据未初始化

        # 自动行高
        self.ui.tableInfo.resizeRowsToContents()

        # 自动列宽
        self.ui.tableInfo.resizeColumnsToContents()

    #  ==============自定义功能函数============

    #  ==========由connectSlotsByName() 自动连接的槽函数==================

    @pyqtSlot()  # “设置表头”按钮
    def on_btnSetHeader_clicked(self):
        # headerText = ["功率1", "功率2", "桨叶1", "桨叶2", "风速1", "风速2", "转速1", "转速2", "风速",
        #               "理论功率", "过滤系数 * 理论功率", "风速下限", "风速上限"]
        headerText = ["功率1", "功率2", "桨叶1", "桨叶2", "风速1", "风速2", "转速1", "转速2"]
        self.ui.tableInfo.setColumnCount(len(headerText))  # 列数
        #       self.ui.tableInfo.setHorizontalHeaderLabels(headerText)   #简单的表头文字，无格式

        for i in range(len(headerText)):
            headerItem = QTableWidgetItem(headerText[i])
            font = headerItem.font()
            #  font.setBold(True)
            font.setPointSize(11)
            headerItem.setFont(font)
            headerItem.setForeground(QBrush(Qt.red))  # 前景色，即文字颜色
            self.ui.tableInfo.setHorizontalHeaderItem(i, headerItem)

    @pyqtSlot()  # 设置行数
    def on_btnSetRows_clicked(self):
        self.ui.tableInfo.setRowCount(self.ui.spinRowCount.value())  # 设置数据区行数

    # @pyqtSlot()  # 初始化表格数据
    # def on_btnIniData_clicked(self):
    #     self.ui.tableInfo.clearContents()  # 清除表格内容
    #
    #     birth = QDate(1998, 6, 23)
    #     isParty = True
    #     nation = "汉族"
    #     score = 70
    #
    #     rowCount = self.ui.tableInfo.rowCount()  # 表格行数
    #     for i in range(rowCount):
    #         strName = "学生%d" % i
    #         if ((i % 2) == 0):
    #             strSex = "男"
    #         else:
    #             strSex = "女"
    #         self.__createItemsARow(i, strName, strSex,
    #                                birth, nation, isParty, score)
    #         birth = birth.addDays(20)
    #         isParty = not isParty
    #
    #     self.__tableInitialized = True  # 表格数据已初始化

    # @pyqtSlot()  # 插入行
    # def on_btnInsertRow_clicked(self):
    #     curRow = self.ui.tableInfo.currentRow()  # 当前行号
    #     self.ui.tableInfo.insertRow(curRow)
    #     birth = QDate.fromString("1998-4-5", "yyyy-M-d")
    #     self.__createItemsARow(curRow, "新学生", "男", birth, "苗族", True, 65)
    #
    # @pyqtSlot()  # 添加行
    # def on_btnAppendRow_clicked(self):
    #     curRow = self.ui.tableInfo.rowCount()
    #     self.ui.tableInfo.insertRow(curRow)
    #     birth = QDate.fromString("1999-1-10", "yyyy-M-d")
    #     self.__createItemsARow(curRow, "新生", " 女", birth, "土家族", False, 86)

    @pyqtSlot()  # 删除当前行
    def on_btnDelCurRow_clicked(self):
        curRow = self.ui.tableInfo.currentRow()  # 当前行号
        self.ui.tableInfo.removeRow(curRow)

    @pyqtSlot()  # 清空表格内容
    def on_btnClearContents_clicked(self):
        self.ui.tableInfo.clearContents()

#  =============自定义槽函数===============================

#  ============窗体测试程序 ================================


if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QMyTable()
    form.show()
    sys.exit(app.exec_())
