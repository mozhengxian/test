# -*- encoding=utf-8 -*-

import sys
from ui_QMyPlot import Ui_QMYWPLOT
from PyQt5.QtWidgets import QMainWindow, QApplication, QSplitter
from PyQt5.QtCore import Qt
from matplotlib import pyplot as plt
import matplotlib as mpl
import matplotlib.style as mplStyple
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,
                                                NavigationToolbar2QT as NavigationToolbar)


class QmyPBase(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_QMYWPLOT()
        self.ui.setupUi(self)

        mpl.rcParams['font.sans-serif'] = ['SimHei', 'KaiTi']  # 显示汉字为 楷体,黑体
        mpl.rcParams['font.size'] = 8
        mpl.rcParams['axes.unicode_minus'] = False  # 减号unicode编码
        mplStyple.use('seaborn-notebook')

        self.__createFigure()
        
    def __createFigure(self):

        # 设置窗口画布，并添加分割线
        self._fig = plt.Figure()
        figCanvas = FigureCanvas(self._fig)
        naviToolbar = NavigationToolbar(figCanvas, self)
        self.addToolBar(naviToolbar)
        splitter = QSplitter(self)
        splitter.setOrientation(Qt.Horizontal)
        splitter.addWidget(figCanvas)
        self.setCentralWidget(splitter)


class QmyPlotS(QmyPBase):

    # items[0] columns ['平均桨叶角度1a', '平均电网有功功率', '平均风速(m/s)', '平均叶轮转速1', '线速度', 'λ', 'Cp']
    # items[1] columns ['风机', '平均桨叶角度1a', '平均电网有功功率', '平均风速(m/s)', '平均叶轮转速1', '线速度', 'λ', 'Cp']
    # 散点图
    def __init__(self, parent=None, data_frame_list=None, df_theory=None, use_columns=None):
        super().__init__(parent)
        self.setWindowTitle("散点图")
        self._data_frame_list = data_frame_list
        self._df_theory = df_theory
        self.use_columns = use_columns
        self.__createFigure()

    def __createFigure(self):

        ax1 = self._fig.add_subplot(111)
        for items in self._data_frame_list:
            ax1.scatter(items[1][self.use_columns[3]], items[1][self.use_columns[2]],
                        label=f'{items[1].iloc[0, 0]}实际功率曲线', marker='.', linewidths=0)
        ax1.plot(self._df_theory['风速'], self._df_theory['理论功率'], color='red', label='理论功率曲线', linewidth=2,
                 linestyle='--')
        ax1.grid(True)
        ax1.legend(loc=0)
        self._fig.tight_layout()


class QmyPlotP(QmyPBase):

    # 功率曲线图
    def __init__(self, parent=None, data_frame_list=None, df_theory=None, use_columns=None):
        super().__init__(parent)
        self._data_frame_list = data_frame_list
        self._df_theory = df_theory
        self.use_columns = use_columns
        self.setWindowTitle("功率曲线")
        self.__createFigure()

    def __createFigure(self):
        ax1 = self._fig.add_subplot(111)

        ax1.plot(self._df_theory['风速'], self._df_theory['理论功率'], color='red', label='理论功率曲线', linewidth=2,
                 linestyle='--')

        for items in self._data_frame_list:
            ax1.plot(items[0][self.use_columns[3]], items[0][self.use_columns[2]],
                     label=f'{items[1].iloc[0, 0]}实际功率曲线', linewidth=1)
        ax1.grid(True)
        ax1.legend(loc=0)
        self._fig.tight_layout()


# 风速-λ
class QmyPlotL(QmyPBase):

    def __init__(self, parent=None, data_frame_list=None, use_columns=None):
        super().__init__(parent)
        self.setWindowTitle("风速 - λ")
        self._data_frame_list = data_frame_list
        self.use_columns = use_columns
        self.__createFigure()

    def __createFigure(self):
        ax1 = self._fig.add_subplot(111)
        for items in self._data_frame_list:
            ax1.plot(items[0][self.use_columns[3]], items[0][self.use_columns[6]],
                     label=f'{items[1].iloc[0, 0]} 风速-λ', linewidth=1)
        ax1.grid(True)
        ax1.set_xlabel('风速')
        ax1.set_ylabel('λ', rotation=0)
        ax1.legend(loc=0)
        self._fig.tight_layout()


# 风速-转速
class QmyPlotWQ(QmyPBase):

    def __init__(self, parent=None, data_frame_list=None, use_columns=None):
        super().__init__(parent)

        self.setWindowTitle("风速-转速")
        self._data_frame_list = data_frame_list
        self.use_columns = use_columns
        self.__createFigure()

    def __createFigure(self):
        ax1 = self._fig.add_subplot(111)
        for items in self._data_frame_list:
            ax1.plot(items[0][self.use_columns[3]], items[0][self.use_columns[4]],
                     label=f'{items[1].iloc[0, 0]} 风速-转速', linewidth=1)
        ax1.grid(True)
        ax1.set_xlabel('风速')
        ax1.set_ylabel('转速', rotation=0)
        ax1.legend(loc=0)
        self._fig.tight_layout()


# 转速-功率
class QmyPlotQG(QmyPBase):

    def __init__(self, parent=None, data_frame_list=None, use_columns=None):

        super().__init__(parent)
        self.setWindowTitle("转速-功率")
        self._data_frame_list = data_frame_list
        self.use_columns = use_columns
        self.__createFigure()

    def __createFigure(self):
        ax1 = self._fig.add_subplot(111)
        for items in self._data_frame_list:
            ax1.plot(items[0][self.use_columns[4]], items[0][self.use_columns[2]],
                     label=f'{items[1].iloc[0, 0]} 转速-功率', linewidth=1)
        ax1.grid(True)
        ax1.set_xlabel('转速')
        ax1.set_ylabel('功率', rotation=0)
        ax1.legend(loc=0)
        self._fig.tight_layout()


# 转速-转矩
class QmyPlotQJ(QmyPBase):

    def __init__(self, parent=None, data_frame_list=None, use_columns=None):
        super().__init__(parent)

        self.setWindowTitle("转速-转矩")
        self._data_frame_list = data_frame_list
        self.use_columns = use_columns
        self.__createFigure()

    def __createFigure(self):
        ax1 = self._fig.add_subplot(111)
        for items in self._data_frame_list:
            ax1.plot(items[0][self.use_columns[4]], items[0][self.use_columns[5]],
                     label=f'{items[1].iloc[0, 0]} 转速-转矩', linewidth=1)
        ax1.grid(True)
        ax1.set_xlabel('转速')
        ax1.set_ylabel('转矩', rotation=0)
        ax1.legend(loc=0)
        self._fig.tight_layout()


# 转矩-功率
class QmyPlotQP(QmyPBase):

    def __init__(self, parent=None, data_frame_list=None, use_columns=None):
        super().__init__(parent)

        self.setWindowTitle("转矩-功率")
        self._data_frame_list = data_frame_list
        self.use_columns = use_columns
        self.__createFigure()

    def __createFigure(self):
        ax1 = self._fig.add_subplot(111)
        for items in self._data_frame_list:
            ax1.plot(items[0][self.use_columns[5]], items[0][self.use_columns[2]],
                     label=f'{items[1].iloc[0, 0]} 转矩-功率', lienwidth=1)
        ax1.grid(True)
        ax1.set_xlabel('转矩')
        ax1.set_ylabel('功率', rotation=0)
        ax1.legend(loc=0)
        self._fig.tight_layout()


class QmyPlotPC(QmyPBase):

    # 功率-Cp图
    def __init__(self, parent=None, data_frame_list=None, df_theory=None, use_columns=None):
        super().__init__(parent)

        self.setWindowTitle("功率-Cp")
        self._df_theory = df_theory
        self._data_frame_list = data_frame_list
        self.use_columns = use_columns
        self.__createFigure()

    def __createFigure(self):
        ax1 = self._fig.add_subplot(111)
        ax1.plot(self._df_theory['风速'], self._df_theory['理论功率'], label='理论功率曲线',
                 color='red',linewidth=2, linestyle='--')

        for items in self._data_frame_list:
            ax1.plot(items[0][self.use_columns[3]], items[0][self.use_columns[2]],
                     label=f'{items[1].iloc[0, 0]} 实际功率曲线', linewidth=1)
        ax1.set_xlabel('风速')
        ax1.set_ylabel('功率', rotation=0)
        ax1.grid(True)
        ax2 = ax1.twinx()
        for items in self._data_frame_list:
            ax2.plot(items[0][self.use_columns[3]], items[0]['Cp'],
                     label=f'{items[1].iloc[0, 0]} 风速-Cp', linewidth=1)
        ax2.set_ylabel('Cp', rotation=0)
        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc=0)
        self._fig.tight_layout()


# 绘制散点图 ================================
# 转速-转矩，风速-桨叶角度，转速-桨叶角度


# 转速-转矩
class WinPScatter(QmyPBase):

    def __init__(self, parent=None, data_frame_list=None, use_columns=None):
        super().__init__(parent)

        self.setWindowTitle("转速-转矩 散点图")
        self._data_frame_list = data_frame_list
        self.use_columns = use_columns
        self.__createFigure()

    def __createFigure(self):
        ax = self._fig.add_subplot(111)
        for items in self._data_frame_list:
            ax.scatter(items[1][self.use_columns[4]], items[1][self.use_columns[5]],
                       label=f'{items[1].iloc[0, 0]} 转速-转矩', linewidths=0,
                       marker='.')
        ax.grid(True)
        ax.legend(loc=0)
        self._fig.tight_layout()


# 风速-桨叶角度
class WinTScatter(QmyPBase):

    def __init__(self, parent=None, data_frame_list=None, use_columns=None):
        super().__init__(parent)

        self.setWindowTitle("风速-桨叶角度 散点图")
        self._data_frame_list = data_frame_list
        self.use_columns = use_columns
        self.__createFigure()

    def __createFigure(self):
        ax = self._fig.add_subplot(111)
        for items in self._data_frame_list:
            ax.scatter(items[1][self.use_columns[3]], items[1][self.use_columns[1]],
                       label=f'{items[1].iloc[0, 0]} 风速-桨叶角度',
                       linewidths=0, marker='.')
        ax.grid(True)
        ax.legend(loc=0)
        self._fig.tight_layout()


# 转速-桨叶角度
class SpeedTScatter(QmyPBase):

    def __init__(self, parent=None, data_frame_list=None, use_columns=None):
        super().__init__(parent)

        self.setWindowTitle("转速-桨叶角度 散点图")
        self._data_frame_list = data_frame_list
        self.use_columns = use_columns
        self.__createFigure()

    def __createFigure(self):
        ax = self._fig.add_subplot(111)
        for items in self._data_frame_list:
            ax.scatter(items[1][self.use_columns[4]], items[1][self.use_columns[1]],
                       label=f'{items[1].iloc[0, 0]} 转速-桨叶角度',
                       linewidths=0, marker='.')
        ax.grid(True)
        ax.legend(loc=0)
        self._fig.tight_layout()


if __name__ == "__main__":         # 用于当前窗体测试
    app = QApplication(sys.argv)   # 创建GUI应用程序
    form = QmyPBase()              # 创建窗体
    form.show()
    sys.exit(app.exec_())
