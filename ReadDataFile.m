% Subcode For Main_PowerAnsys��To open the file Created by ligang 2017,11,4

function [data,text] = ReadDataFile(Filepath,Mode)
%Mode=1����ȡ��̬���۹������ߣ�Mode=2����ȡ���������������ݡ�
switch Mode
    case 1  % Excel,��1��Ϊ��ͷ��������Ϊ���ݣ�
        [data,text]=xlsread(Filepath);
        text=text(1,:);
        row=max(isnan(data),[],2);
        data=data(~row,:);    %�����к���NaN�����޳�
    case 2  % Excel����һ��Ϊ��ͷ����һ��Ϊʱ�䣬����Ϊ���ݣ�
        [data,text]=xlsread(Filepath);
        text=text(1,2:end);
        row=max(isnan(data),[],2);
        data=data(~row,:);    %�����к���NaN�����޳�
    otherwise
        msgbox('not find data file','Error','error');
        return;
end


        