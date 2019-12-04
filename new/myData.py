# -*- encoding=utf-8 -*-

import pandas as pd
from math import pi
import sqlite3 as lite
from multiprocessing import Pool, Manager


class QMyData:

    def __init__(self):
        pass
        # self.use_columns = use_columns
        # self.data_path = data_path
        # self.P = P
        # self.theory_data = None
        # self.theory_data = None
        # self._u = None
        # self._mess = {}
        # self.judge = judge

    # def r_database(self, judge):
    #     # 读取理论功率曲线数据
    #     con = lite.connect('../database/myDatabase.db')
    #     self.theory_data = pd.read_sql(f'SELECT * FROM {judge}', con=con)
    #     con.close()

    def readFile(self, file, columns, file_type):
        # read csv file
        if file_type == 'csv':
            # use_columns ['风机', '平均桨叶角度1a', '平均电网有功功率', '平均风速(m/s)', '平均叶轮转速1'| 转矩]
            df = pd.read_csv(file, engine='python', encoding='gbk',
                             usecols=columns, converters={
                              columns[1]: self.strtofloat,
                              columns[2]: self.strtofloat,
                              columns[3]: self.strtofloat,
                              columns[4]: self.strtofloat
                                        })
            return df
        # read excel file
        if file_type == 'xlsx':
            df = pd.read_excel(file, usecols=columns)
            return df

    def dealData(self, filter_method, files_paths, df_columns, file_type, data_frame=None):
        # self.r_database(self.judge)
        pool = Pool(processes=4)
        queue = Manager().Queue()
        for file_path in files_paths:
            pool.apply_async(self.pools, (file_path, queue, filter_method, df_columns, file_type))
        pool.close()
        pool.join()
        return queue

    # 筛选条件 
    # 经验过滤法
    # def filt(self, df):
    #     # columns['风机', '平均桨叶角度1a', '平均电网有功功率', '平均风速(m/s)', '平均叶轮转速1', '线速度', 'λ', 'Cp']
    #     a = (
    #                 (self.theory_data.iloc[0, 0] < df.iloc[:, 2]
    #                  ) & (
    #                         df.iloc[:, 2] <= self.theory_data.iloc[0, 1]
    #                 ) & (
    #                         self.theory_data.iloc[0, 2] < df.iloc[:, 1]
    #                 ) & (
    #                         df.iloc[:, 1] <= self.theory_data.iloc[0, 3]
    #                 ) & (
    #                         self.theory_data.iloc[0, 4] < df.iloc[:, 3]
    #                 ) & (
    #                         df.iloc[:, 3] <= self.theory_data.iloc[0, 5]
    #                 ) & (
    #                         self.theory_data.iloc[0, 6] < df.iloc[:, 4]
    #                 ) & (
    #                         df.iloc[:, 4] <= self.theory_data.iloc[0, 7]
    #                 )) | (
    #                 (self.theory_data.iloc[1, 0] < df.iloc[:, 2]) & (
    #                 df.iloc[:, 2] <= self.theory_data.iloc[1, 1]) & (
    #                         self.theory_data.iloc[1, 2] < df.iloc[:, 1]
    #                 ) & (
    #                         df.iloc[:, 1] <= self.theory_data.iloc[1, 3]
    #                 ) & (
    #                         self.theory_data.iloc[1, 4] < df.iloc[:, 3]
    #                 ) & (
    #                         df.iloc[:, 3] <= self.theory_data.iloc[1, 5]
    #                 ) & (
    #                         self.theory_data.iloc[1, 6] < df.iloc[:, 4]
    #                 ) & (
    #                         df.iloc[:, 4] <= self.theory_data.iloc[1, 7]
    #                 )
    #         ) | (
    #                 (self.theory_data.iloc[2, 0] < df.iloc[:, 2]) & (
    #                 df.iloc[:, 2] <= self.theory_data.iloc[2, 1]) & (
    #                         self.theory_data.iloc[2, 2] < df.iloc[:, 1]
    #                 ) & (
    #                         df.iloc[:, 1] <= self.theory_data.iloc[2, 3]
    #                 ) & (
    #                         self.theory_data.iloc[2, 4] < df.iloc[:, 3]
    #                 ) & (
    #                         df.iloc[:, 3] <= self.theory_data.iloc[2, 5]
    #                 ) & (
    #                         self.theory_data.iloc[2, 6] < df.iloc[:, 4]
    #                 ) & (
    #                         df.iloc[:, 4] <= self.theory_data.iloc[2, 7]
    #                 )
    #         ) | (
    #                 (self.theory_data.iloc[3, 0] < df.iloc[:, 2]) & (
    #                 df.iloc[:, 2] <= self.theory_data.iloc[3, 1]) & (
    #                         self.theory_data.iloc[3, 2] < df.iloc[:, 1]
    #                 ) & (
    #                         df.iloc[:, 1] <= self.theory_data.iloc[3, 3]
    #                 ) & (
    #                         self.theory_data.iloc[3, 4] < df.iloc[:, 3]
    #                 ) & (
    #                         df.iloc[:, 3] <= self.theory_data.iloc[3, 5]
    #                 ) & (
    #                         self.theory_data.iloc[3, 6] < df.iloc[:, 4]
    #                 ) & (
    #                         df.iloc[:, 4] <= self.theory_data.iloc[3, 7]
    #                 )
    #         ) | (
    #                 (self.theory_data.iloc[4, 0] < df.iloc[:, 2]) & (
    #                 df.iloc[:, 2] <= self.theory_data.iloc[4, 1]) & (
    #                         self.theory_data.iloc[4, 2] < df.iloc[:, 1]
    #                 ) & (
    #                         df.iloc[:, 1] <= self.theory_data.iloc[4, 3]
    #                 ) & (
    #                         self.theory_data.iloc[4, 4] < df.iloc[:, 3]
    #                 ) & (
    #                         df.iloc[:, 3] <= self.theory_data.iloc[4, 5]
    #                 ) & (
    #                         self.theory_data.iloc[4, 6] < df.iloc[:, 4]
    #                 ) & (
    #                         df.iloc[:, 4] <= self.theory_data.iloc[4, 7]
    #                 )
    #         ) | (
    #                 (self.theory_data.iloc[5, 0] < df.iloc[:, 2]) & (
    #                 df.iloc[:, 2] <= self.theory_data.iloc[5, 1]) & (
    #                         self.theory_data.iloc[5, 2] < df.iloc[:, 1]
    #                 ) & (
    #                         df.iloc[:, 1] <= self.theory_data.iloc[5, 3]
    #                 ) & (
    #                         self.theory_data.iloc[5, 4] < df.iloc[:, 3]
    #                 ) & (
    #                         df.iloc[:, 3] <= self.theory_data.iloc[5, 5]
    #                 ) & (
    #                         self.theory_data.iloc[5, 6] < df.iloc[:, 4]
    #                 ) & (
    #                         df.iloc[:, 4] <= self.theory_data.iloc[5, 7]
    #                 )
    #         ) | (
    #                 (self.theory_data.iloc[6, 0] < df.iloc[:, 2]) & (
    #                 df.iloc[:, 2] <= self.theory_data.iloc[6, 1]) & (
    #                         self.theory_data.iloc[6, 2] < df.iloc[:, 1]
    #                 ) & (
    #                         df.iloc[:, 1] <= self.theory_data.iloc[6, 3]
    #                 ) & (
    #                         self.theory_data.iloc[6, 4] < df.iloc[:, 3]
    #                 ) & (
    #                         df.iloc[:, 3] <= self.theory_data.iloc[6, 5]
    #                 ) & (
    #                         self.theory_data.iloc[6, 6] < df.iloc[:, 4]
    #                 ) & (
    #                         df.iloc[:, 4] <= self.theory_data.iloc[6, 7]
    #                 )
    #         )
    #     data_frame = df[~a]
    #     del df
    #     return data_frame

    # Show Messages
    def show_messages(self):
        return self._mess

    def theory_fill(self):
        return self.theory_data

    def strtofloat(self, args):
        if isinstance(args, str):
            new_val = args.replace(',', '').strip()
            return float(new_val)

    def pools(self, file_path, q, filter_method, df_columns, file_type):
        data_frame = self.readFile(file_path, df_columns, file_type)
        if not filter_method:
            df = self.filt(data_frame)
            # print(f'method filt {filter_method}')
            R = self.theory_data.loc[0, 'R']
            df['线速度'] = df.apply(
                lambda x: x[self.use_columns[4]] * R / 2 * pi / 30, axis=1)
            df.mask(df.loc[:, self.use_columns[3]] == 0, inplace=True)
            df['λ'] = df.apply(lambda x: x['线速度'] / x[self.use_columns[3]], axis=1)
            df['PS'] = df.apply(
                lambda x: x[self.use_columns[3]] ** 3 * pi * (R / 2) ** 2 * self.P, axis=1)
            df['Cp'] = df.apply(
                lambda x: 2 * 1000 * x[self.use_columns[2]] / x['PS'], axis=1)
            df.drop(columns='PS', axis=1, inplace=True)
            df2 = df
            df = df.groupby(pd.cut(
                df[self.use_columns[3]], self.theory_data['风速下限'].tolist(), right=False)).mean()
            self._mess[file_path.split('/')[-1].split('.')[0]] = df[self.use_columns[2]]
            if self.data_path[0] == file_path:
                self._u = df2.columns.tolist()
                q.put(self._u)
            q.put((df, df2))
            q.put(self._mess)
            # print("put the {0}".format(file_path.rsplit('/', 1)[-1]))
        if filter_method:
            df = self.filt_method_wind_speed(data_frame)
            # print(f'method filt_method_wind_speed {filter_method}')
            R = self.theory_data.loc[0, 'R']
            df['线速度'] = df.apply(
                lambda x: x[self.use_columns[4]] * R / 2 * pi / 30, axis=1)
            df.mask(df.loc[:, self.use_columns[3]] == 0, inplace=True)
            df['λ'] = df.apply(lambda x: x['线速度'] / x[self.use_columns[3]], axis=1)
            df['PS'] = df.apply(
                lambda x: x[self.use_columns[3]] ** 3 * pi * (R / 2) ** 2 * self.P, axis=1)
            df['Cp'] = df.apply(
                lambda x: 2 * 1000 * x[self.use_columns[2]] / x['PS'], axis=1)
            df.drop(columns='PS', axis=1, inplace=True)
            df2 = df
            df = df.groupby(pd.cut(
                df[self.use_columns[3]], self.theory_data['风速下限'].tolist(), right=False)).mean()
            self._mess[file_path.split('/')[-1].split('.')[0]] = df[self.use_columns[2]]
            if self.data_path[0] == file_path:
                self._u = df2.columns.tolist()
                q.put(self._u)
            q.put((df, df2))
            q.put(self._mess)
            # print("put the {0}".format(file_path.rsplit('/', 1)[-1]))

    def filt_method_wind_speed(self, df):
        # 新筛选条写法
        # df.mask((df['平均风速(m/s)'] >=0)&(df['平均风速(m/s)']<5.25)&(df['平均电网有功功率']<800)).dropna(axis=0,subset=['平均电网有功功率'])
        _columns = self.use_columns
        theory = self.theory_data['过滤系数']
        df.mask(
            (df[_columns[3]] >= 0) & (df[_columns[3]] < 0.25)
            & (df[_columns[2]] < theory[0]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 0.25) & (df[_columns[3]] < 0.75)
            & (df[_columns[2]] < theory[1]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 0.75) & (df[_columns[3]] < 1.25)
            & (df[_columns[2]] < theory[2]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 1.25) & (df[_columns[3]] < 1.75)
            & (df[_columns[2]] < theory[3]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 1.75) & (df[_columns[3]] < 2.25)
            & (df[_columns[2]] < theory[4]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 2.25) & (df[_columns[3]] < 2.75)
            & (df[_columns[2]] < theory[5]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 2.75) & (df[_columns[3]] < 3.25)
            & (df[_columns[2]] < theory[6]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 3.25) & (df[_columns[3]] < 3.75)
            & (df[_columns[2]] < theory[7]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 3.75) & (df[_columns[3]] < 4.25)
            & (df[_columns[2]] < theory[8]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 4.25) & (df[_columns[3]] < 4.75)
            & (df[_columns[2]] < theory[9]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 4.75) & (df[_columns[3]] < 5.25)
            & (df[_columns[2]] < theory[10]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 5.25) & (df[_columns[3]] < 5.75)
            & (df[_columns[2]] < theory[11]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 5.75) & (df[_columns[3]] < 6.25)
            & (df[_columns[2]] < theory[12]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 6.25) & (df[_columns[3]] < 6.75)
            & (df[_columns[2]] < theory[13]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 6.75) & (df[_columns[3]] < 7.25)
            & (df[_columns[2]] < theory[14]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 7.25) & (df[_columns[3]] < 7.75)
            & (df[_columns[2]] < theory[15]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 7.75) & (df[_columns[3]] < 8.25)
            & (df[_columns[2]] < theory[16]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 8.25) & (df[_columns[3]] < 8.75)
            & (df[_columns[2]] < theory[17]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 8.75) & (df[_columns[3]] < 9.25)
            & (df[_columns[2]] < theory[18]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 9.25) & (df[_columns[3]] < 9.75)
            & (df[_columns[2]] < theory[19]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 9.75) & (df[_columns[3]] < 10.25)
            & (df[_columns[2]] < theory[20]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 10.25) & (df[_columns[3]] < 10.75)
            & (df[_columns[2]] < theory[21]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 10.75) & (df[_columns[3]] < 11.25)
            & (df[_columns[2]] < theory[22]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 11.25) & (df[_columns[3]] < 11.75)
            & (df[_columns[2]] < theory[23]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 11.75) & (df[_columns[3]] < 12.25)
            & (df[_columns[2]] < theory[24]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 12.25) & (df[_columns[3]] < 12.75)
            & (df[_columns[2]] < theory[25]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 12.75) & (df[_columns[3]] < 13.25)
            & (df[_columns[2]] < theory[26]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 13.25) & (df[_columns[3]] < 13.75)
            & (df[_columns[2]] < theory[27]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 13.75) & (df[_columns[3]] < 14.25)
            & (df[_columns[2]] < theory[28]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 14.25) & (df[_columns[3]] < 14.75)
            & (df[_columns[2]] < theory[29]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 14.75) & (df[_columns[3]] < 15.25)
            & (df[_columns[2]] < theory[30]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 15.25) & (df[_columns[3]] < 15.75)
            & (df[_columns[2]] < theory[31]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 15.75) & (df[_columns[3]] < 16.25)
            & (df[_columns[2]] < theory[32]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 16.25) & (df[_columns[3]] < 16.75)
            & (df[_columns[2]] < theory[33]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 16.75) & (df[_columns[3]] < 17.25)
            & (df[_columns[2]] < theory[34]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 17.25) & (df[_columns[3]] < 17.75)
            & (df[_columns[2]] < theory[35]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 17.75) & (df[_columns[3]] < 18.25)
            & (df[_columns[2]] < theory[36]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 18.25) & (df[_columns[3]] < 18.75)
            & (df[_columns[2]] < theory[37]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 18.75) & (df[_columns[3]] < 19.25)
            & (df[_columns[2]] < theory[38]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 19.25) & (df[_columns[3]] < 19.75)
            & (df[_columns[2]] < theory[39]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 19.75) & (df[_columns[3]] < 20.25)
            & (df[_columns[2]] < theory[40]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 20.25) & (df[_columns[3]] < 20.75)
            & (df[_columns[2]] < theory[41]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 20.75) & (df[_columns[3]] < 21.25)
            & (df[_columns[2]] < theory[42]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 21.25) & (df[_columns[3]] < 21.75)
            & (df[_columns[2]] < theory[43]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 21.75) & (df[_columns[3]] < 22.25)
            & (df[_columns[2]] < theory[44]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 22.25) & (df[_columns[3]] < 22.75)
            & (df[_columns[2]] < theory[45]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 22.75) & (df[_columns[3]] < 23.25)
            & (df[_columns[2]] < theory[46]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 23.25) & (df[_columns[3]] < 23.75)
            & (df[_columns[2]] < theory[47]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 23.75) & (df[_columns[3]] < 24.25)
            & (df[_columns[2]] < theory[48]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 24.25) & (df[_columns[3]] < 24.75)
            & (df[_columns[2]] < theory[49]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 24.75) & (df[_columns[3]] < 25.25)
            & (df[_columns[2]] < theory[50]), inplace=True
            )
        df.mask(
            (df[_columns[3]] >= 25.25) & (df[_columns[3]] < 25.75)
            & (df[_columns[2]] < theory[51]), inplace=True
            )

        df.dropna(axis=0, subset=[_columns[2]], inplace=True)
        return df


if __name__ == '__main__':
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"
    # path = ['D:\\外罗功率曲线分析\\8#.csv']
    path = ['D:\\滨海\\分钟数据\\CX09F.csv']
    use_c = ['风机', '平均桨叶角度1a', '平均电网有功功率', '平均风速(m/s)', '平均叶轮转速1']
    data = QMyData(use_c, '滨海', data_path=path)
    f1 = data.dealData(False)
    f2 = data.dealData(True)
