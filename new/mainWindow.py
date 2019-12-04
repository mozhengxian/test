# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QDir, pyqtSlot, Qt, QUrl
from PyQt5.QtGui import QIcon, QFont, QDesktopServices
from ui_QMyMainWindow import Ui_MainWindow
import myPlot
import myData
from myTable import QMyTable
from pandas import Series, read_csv
from requests import get


class QmyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.my_data = myData.QMyData()
        self.filter_data_method = True

#         self.power_theory = None
#         self.df_columns_list = None
#         self.filter_data = False
#         self.P = 1.225
#         self.__messages = {}
        self.CurVersion = 'V3.0'
#         self.judge = '兴化湾'
#         self.__font = QFont()
#         self.__font.setPointSize(14)
#
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
#
#         # TabWidget
#         self.ui.tabWidget.setTabsClosable(True)
#         self.setCentralWidget(self.ui.tabWidget)
#         self.setWindowState(Qt.WindowMinimized)
#
#         # icon
#         self.setWindowTitle("功率曲线分析 V2.0")
#         self.setWindowIcon(QIcon('../images/icon.png'))
#
#         # Show Messages
#         self.show_messages()
#         # self.MySE_number()
#         self.ui.lineEdit.setFont(self.__font)
#         self.ui.lineEdit.setStyleSheet("color: red")
#         self.ui.lineEdit.setText("  MySE5.5_155")
#         self.ui.lineEdit.setReadOnly(True)
#
#         # 空气密度
#         self.ui.lineEdit_2.setFont(self.__font)
#         self.ui.lineEdit_2.setStyleSheet("color: red")
#         self.ui.lineEdit_2.setText("1.225")
#
#         # qcombox
#         # self.ui.comboBox.currentIndexChanged[str].connect(self.__project)
        self.ui.radB_filter.toggled.connect(self.on_radB_filter)
#
    #  ==============自定义功能函数========================

    def handleData(self, columns, files, file_type):
        try:
            queue = self.my_data.dealData(self.filter_data_method, files, columns,
                                          file_type, data_frame=self.filter_params)
            while not queue.empty():
                values = queue.get()
                if isinstance(values, tuple):
                    self.myData.append(values)
                if isinstance(values, dict):
                    self.__messages = dict(self.__messages, **values)
                if isinstance(values, list):
                    self.df_columns_list = values

            self.power_theory = self.my_data.theory_fill()
            return True
        except Exception as e:
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText("\n***** Error *****")
            self.ui.plainTextEdit.appendPlainText(repr(e))
            return False

    def show_messages(self):
        self.ui.plainTextEdit.setReadOnly(True)
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.setFont(self.__font)
        self.ui.plainTextEdit.appendPlainText("""\n\t=== 功率曲线拟合度 === 理论发电量 \
=== 实际发电量 ===\n""")

    # 判断csv 标签点
    def judge_label(self, file_path):
        file = file_path.rsplit('.')[-1]
        if file == 'csv':
            df = read_csv(file_path, engine='python', encoding='gbk', nrows=3)
            re = "^风机|桨叶角度1[a,A]$|^平均电网有功功率|^电网有功功率|^平均风速|^风速|" \
                 "^平均叶轮转速1|^叶轮转速1"
            df = df.filter(regex=re)
            return df.columns.tolist(), 'csv'
        if file == 'xlsx':
            pass

    # 读取空气密度p
    def lou_p(self):
        p = self.ui.lineEdit_2.text()
        try:
            self.P = float(p)
        except Exception as e:
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.appendPlainText(repr(e))
            self.ui.plainTextEdit.appendPlainText("\n*****请输入正确的空气密度*****")

    #  ==============event处理函数==========================

    #  ==========由connectSlotsByName()自动连接的槽函数============

    @pyqtSlot()
    def on_Act_Open_triggered(self):
        # start = time.time()
        # self.myData = []
        # self.__messages = {}
        # self.lou_p()
        path = QDir.homePath()
        dlgTitle = "选择一个或者多个"
        file = "csv files (*.csv *.xlsx)"
        openfile_names, _ = QFileDialog.getOpenFileNames(self, dlgTitle, path, file)
        if openfile_names:
            # ['D:/滨海/分钟数据/CX09F.csv', 'D:/滨海/分钟数据/CX10F.csv', 'D:/滨海/分钟数据/CX11F.csv']
            df_columns_list, file_type = self.judge_label(openfile_names[0])
            print(df_columns_list, file_type)
            # result = self.handleData(df_columns_list, openfile_names)
#             if not result:
#                 QMessageBox.warning(self, '文件读取', '文件读取错误！请查看错误信息!',
#                                     QMessageBox.Yes,
#                                     QMessageBox.Yes)
#             # messages = self.my_data.show_messages()
#             self.ui.plainTextEdit.appendPlainText(f'\t\t\t\t\t{self.judge}\n')
#             for k, v in self.__messages.items():
#                 v = Series(v.values)
#                 R = 1 - ((self.power_theory['理论功率'] - v) ** 2).sum() / ((v - v.mean()) ** 2).sum()
#                 self.ui.plainTextEdit.appendPlainText(f"""机号:{k}\t{round(R * 100, 4)}%\t\
# {round(self.power_theory['理论功率'].sum(), 4)}\t    {round(v.sum(), 4)}\n""")
            # self.df_columns_list = self.my_data.scatter_after_columns()
        # end = time.time()
        # print(f'total times {round((end - start), 3)} s')

#     #  功率曲线窗口, 功率-Cp窗口, 转速/转矩窗口
#     @pyqtSlot()
#     def on_puB_GenP_clicked(self):
#         my_scatter = myPlot.QmyPlotS(self, self.myData, self.power_theory, use_columns=self.df_columns_list)
#         my_scatter.setAttribute(Qt.WA_DeleteOnClose)
#         curIndex = self.ui.tabWidget.addTab(my_scatter, f'{my_scatter.windowTitle()} ')
#         my_scatter.setVisible(True)
#
#         # 功率曲线窗口
#         mygen_power = myPlot.QmyPlotP(self, self.myData, self.power_theory, use_columns=self.df_columns_list)
#         mygen_power.setAttribute(Qt.WA_DeleteOnClose)
#         curIndex = self.ui.tabWidget.addTab(mygen_power,
#                                             f'{mygen_power.windowTitle()} ')
#         mygen_power.setVisible(True)
#
#         # 功率-Cp窗口
#         mygen_cp = myPlot.QmyPlotPC(self, self.myData, self.power_theory, use_columns=self.df_columns_list)
#         mygen_cp.setAttribute(Qt.WA_DeleteOnClose)
#         curIndex = self.ui.tabWidget.addTab(mygen_cp,
#                                             f'{mygen_cp.windowTitle()} ')
#         mygen_cp.setVisible(True)
#
#         # 风速-λ窗口
#         mygen_l = myPlot.QmyPlotL(self, self.myData, use_columns=self.df_columns_list)
#         mygen_l.setAttribute(Qt.WA_DeleteOnClose)
#         curIndex = self.ui.tabWidget.addTab(mygen_l,
#                                             f'{mygen_l.windowTitle()} ')
#         mygen_l.setVisible(True)
#
#         # 风速-转速
#         mygen_wq = myPlot.QmyPlotWQ(self, self.myData, use_columns=self.df_columns_list)
#         mygen_wq.setAttribute(Qt.WA_DeleteOnClose)
#         curIndex = self.ui.tabWidget.addTab(mygen_wq,
#                                             f'{mygen_wq.windowTitle()} ')
#         mygen_wq.setVisible(True)
#
#         # 转速-功率
#         mygen_qg = myPlot.QmyPlotQG(self, self.myData, use_columns=self.df_columns_list)
#         mygen_qg.setAttribute(Qt.WA_DeleteOnClose)
#         curIndex = self.ui.tabWidget.addTab(mygen_qg,
#                                             f'{mygen_qg.windowTitle()} ')
#         mygen_qg.setVisible(True)
#
#         # if '转矩' in self.df_columns_list:
#         #     # # 转速-转矩
#         #     mygen_qj = myPlot.QmyPlotQJ(self, self.myData, use_columns=self.df_columns_list)
#         #     mygen_qj.setAttribute(Qt.WA_DeleteOnClose)
#         #     curIndex = self.ui.tabWidget.addTab(mygen_qj,
#         #                                         f'{mygen_qj.windowTitle()} ')
#         #     mygen_qj.setVisible(True)
#
#         #     # 转矩-功率
#         #     mygen_qp = myPlot.QmyPlotQP(self, self.myData, use_columns=self.df_columns_list)
#         #     mygen_qp.setAttribute(Qt.WA_DeleteOnClose)
#         #     curIndex = self.ui.tabWidget.addTab(mygen_qp,
#         #                                         f'{mygen_qp.windowTitle()} ')
#         #     mygen_qp.setVisible(True)
#
#     # 散点图窗口
#     @pyqtSlot()
#     def on_puB_Scatter_clicked(self):
#
#         if '转矩' in self.df_columns_list:
#             # 转速-转矩
#             winPS = myPlot.WinPScatter(self, self.myData, use_columns=self.df_columns_list)
#             # winPS.show()
#             winPS.setAttribute(Qt.WA_DeleteOnClose)
#             curIndex = self.ui.tabWidget.addTab(winPS,
#                                                 f'{winPS.windowTitle()} ')
#             winPS.setVisible(True)
#
#         # 风速-桨叶角度
#         winTS = myPlot.WinTScatter(self, self.myData, use_columns=self.df_columns_list)
#         # winTS.show()
#         winTS.setAttribute(Qt.WA_DeleteOnClose)
#         curIndex = self.ui.tabWidget.addTab(winTS,
#                                             f'{winTS.windowTitle()} ')
#         winTS.setVisible(True)
#
#         # 转速-桨叶角度
#         speedTS = myPlot.SpeedTScatter(self, self.myData, use_columns=self.df_columns_list)
#         # speedTS.show()
#         speedTS.setAttribute(Qt.WA_DeleteOnClose)
#         curIndex = self.ui.tabWidget.addTab(speedTS,
#                                             f'{speedTS.windowTitle()} ')
#
#     # closed tab
#
#     def on_tabWidget_currentChanged(self, index):  # tabWidget当前页面变化
#         hasTabs = self.ui.tabWidget.count() > 0  # 再无页面时
#         self.ui.tabWidget.setVisible(hasTabs)
#
#     def on_tabWidget_tabCloseRequested(self, index):  # 分页关闭时关闭窗体
#         if index < 0:
#             return
#         aForm = self.ui.tabWidget.widget(index)
#         aForm.close()
#
# #  =============自定义槽函数==================================
# #     def __project(self, project):
# #         # message _ MySE
# #         project_list = ["兴化湾", "外罗", "滨海", "达坂城", "海丰", "如东", "克旗", "恭城",
# #         "四子王旗", "宝山", "黄骅", "新密", "金海", "牛朗山", "南兴", "秦山", "五连山",
# #         "井仔", "枣阳", "乌兰", "石沃"]
# #         project_dict = {"兴化湾": "MySE5.5_155", "外罗": "MySE5.5_155", "滨海": "MySE3.0_135",
# #         "达坂城": "MySE3.0_100", "海丰": "MySE3.0_110", "如东": "SCD2.75_110", "克旗": "MySE3.6_135",
# #         "恭城": "MySE3.0_121","四子王旗": "MySE3.0_121", "宝山": "MySE3.0_121", "黄骅": "MySE3.0_135",
# #         "新密": "MySE3.0_121", "金海": "MySE3.0_135", "牛朗山": "MySE3.0_135", "南兴": "MySE3.0_135",
# #         "秦山": "MySE2.75_145", "五连山": "MySE3.0_145","井仔": "MySE3.0_121", "枣阳": "MySE3.0_145",
# #         "乌兰": "MySE2.5_135", "石沃": "MySE2.75_158"}
# #         self.judge = project_list[project_list.index(project)]
# #         self.ui.lineEdit.clear()
# #         self.ui.lineEdit.setText(f"  {project_dict.get(project)}")

    # filter_param one
    @pyqtSlot()
    def on_puB_method_clicked(self):
        my_table = QMyTable(self)
        my_table.setAttribute(Qt.WA_DeleteOnClose)
        my_table.setWindowTitle('Paramers Setting')
        my_table.show()

    # filter_param two
    @pyqtSlot()
    def on_puB_method_filter_clicked(self):
        my_table_two = QMyTable(self)
        my_table_two.setAttribute(Qt.WA_DeleteOnClose)
        my_table_two.setWindowTitle('Paramers Setting')
        my_table_two.show()

    # Update software
    @pyqtSlot()
    def on_Act_Update_triggered(self):
        Url = "https://gitee.com/mozhengxian/power_app/raw/master/update.json"
        headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                   "Connection": "keep-alive",
                   "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7"}
        r = get(Url, headers=headers)
        if r.status_code == 200:
            strings = r.json()
            version = strings.get('PulseSensor')['LatestVersion']
            url = strings.get('PulseSensor')['Url']
            update_time = strings.get('PulseSensor')['UpdateTime']
            release_note = strings.get('PulseSensor')['ReleaseNote']

            if version > self.CurVersion:
                warning_str = f"检测到新版本!\n版本号: {version}\n更新时间: " \
                              f"{update_time}\n更新说明: {release_note}"
                msg = QMessageBox.warning(self, '检查更新', warning_str,
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                # Yes button
                if msg == 16384:
                    QDesktopServices.openUrl(QUrl(url))
                # No button
                # if msg == 65536:
                #     QDesktopServices.openUrl(QUrl('http://www.baidu.com/'))
            if not (version > self.CurVersion):
                QMessageBox.warning(self, "检查更新", "当前已经是最新版本!",
                                    QMessageBox.Yes, QMessageBox.Yes)

    # filter method
    @pyqtSlot()
    def on_radB_filter(self):
        if self.ui.radB_filter.isChecked() == True:
            self.filter_data_method = True
        if self.ui.radB_filter.isChecked() == False:
            self.filter_data_method = False


#  ============窗体测试程序 ================================
if __name__ == "__main__":  # 用于当前窗体测试
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyMainWindow()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
