% Subcode For Main_PowerAnsys，To open the file Created by ligang 2017,11,4

function [DataPathName,DataFileName,DataFilePath,FilterIndex]=OpenDataFile(str)
% handles - structure with handles and user data (see GUIDATA)
% DataPathName - Path of the Out file
% DataFileName - Name of the Out file
% DataFilePath - Path & Name of the Out file

persistent Newpath;
if isempty(Newpath)|(Newpath==0)
    Newpath=cd;%当前路径
end
[DataFileName, DataPathName,FilterIndex] = ...
     uigetfile({ '*.xlsx;*.xls','Excel'},...
                '选择要打开的文件',Newpath,...
                'MultiSelect',str);%'off'/'on'
    Newpath=DataPathName;
 if (FilterIndex)
     DataFilePath=strcat(DataPathName,DataFileName);
 else
     DataFilePath=0;
     return;
 end
 
 