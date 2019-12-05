% Subcode For Main_PowerAnsys，To open the file Created by ligang 2017,11,4

function [data,text] = ReadDataFile(Filepath,Mode)
%Mode=1，读取动态理论功率曲线；Mode=2，读取功率曲线运行数据。
switch Mode
    case 1  % Excel,第1行为表头，其下行为数据；
        [data,text]=xlsread(Filepath);
        text=text(1,:);
        row=max(isnan(data),[],2);
        data=data(~row,:);    %数据中含有NaN的行剔除
    case 2  % Excel，第一行为表头，第一列为时间，其余为数据；
        [data,text]=xlsread(Filepath);
        text=text(1,2:end);
        row=max(isnan(data),[],2);
        data=data(~row,:);    %数据中含有NaN的行剔除
    otherwise
        msgbox('not find data file','Error','error');
        return;
end


        