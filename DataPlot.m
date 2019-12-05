% Subcode For Main_PowerAnsys，To open the file Created by ligang 2017,11,4

function []=DataPlot(Files,PAR)
    Color_Line ={'-r','-y','-m','-b','-c','-g'};
    Color_Point={'.b','.c','.g','.r','.y','.m'};
    Files_Num=length(Files);
    for i=1:Files_Num
        legend_str=Files(i).Filename;
        [~,legend_str,~]=fileparts(legend_str);     %取出文件名，去掉扩展名
        legend_str1{i}=strrep(legend_str,'_','\_'); %命令 STRREP(S1,S2,S3) 在字符串S1里所有的S2被S3代替，使下划线正常显示。
    end
    [~,legend_str2,~]=fileparts(PAR.Filename1);    %DynamicPowerCurve
    legend_str2=strrep(legend_str2,'_','\_'); 
    clc;
    H1=figure(1);H2=figure(2);H3=figure(3);H4=figure(4);H5=figure(5);H6=figure(6);H7=figure(7);
    close(H1);close(H2);close(H3);close(H4);close(H5);close(H6);close(H7);
    switch 3
        case 3
            %机组风速-功率曲线
            figure(1);hold on;
            for i=1:Files_Num
                plot(Files(i).WindSpeedStand,Files(i).GenPower,Color_Point{i});
            end
            for i=1:Files_Num
                plot(Files(i).WindSpeedStandAverage,Files(i).GenPowerAverage,Color_Line{i},'LineWidth',1);
            end
            plot(PAR.data(:,1),PAR.data(:,2),'-k','LineWidth',1);
            grid on;hold off;xlabel('风速[m/s]');ylabel('功率 [kW]');legend({legend_str1{:},legend_str1{:},legend_str2},'location','best');title('机组风速-功率曲线');
            xlim([0,16])
            %机组风速-转速曲线
            figure(2);hold on;
            for i=1:Files_Num
                plot(Files(i).WindSpeedStand,Files(i).GenSpeed,Color_Point{i});
            end
            for i=1:Files_Num
                plot(Files(i).WindSpeedStandAverage,Files(i).GenSpeedAverage,Color_Line{i},'LineWidth',1);
            end
            grid on;hold off;xlabel('风速[m/s]');ylabel('转速 [rpm]');legend({legend_str1{:},legend_str1{:}},'location','best');title('机组风速-转速曲线');
            xlim([0,16])
            %机组风速-桨叶角度
            figure(3);hold on;
            for i=1:Files_Num
                plot(Files(i).WindSpeedStand,Files(i).PitchAngle,Color_Point{i});
            end
            for i=1:Files_Num
                plot(Files(i).WindSpeedStandAverage,Files(i).PitchAngleAverage,Color_Line{i},'LineWidth',1);
            end
            grid on;hold off;xlabel('风速[m/s]');ylabel('桨叶角度 [deg]');legend({legend_str1{:},legend_str1{:}},'location','best');title('机组风速-桨叶角度');
            xlim([0,16])
            %机组转速-扭矩曲线
            figure(4);hold on;
            for i=1:Files_Num
                plot(Files(i).GenSpeed,Files(i).GenTorque,Color_Point{i});
            end
            for i=1:Files_Num
                plot(Files(i).GenSpeedAverage,Files(i).GenTorqueAverage,Color_Line{i},'LineWidth',1);
            end
            grid on;hold off;xlabel('发电机转速[rpm]');ylabel('扭矩 [kN.m]');legend({legend_str1{:},legend_str1{:}},'location','best');title('机组转速-扭矩曲线');
            %机组风速-Cp曲线
            figure(5);hold on;
            for i=1:Files_Num
                plot(Files(i).WindSpeedStand,Files(i).Cp,Color_Point{i});
            end
            for i=1:Files_Num
                plot(Files(i).WindSpeedStandAverage,Files(i).CpAverage,Color_Line{i},'LineWidth',1);
            end
            grid on;hold off;xlabel('风速[m/s]');ylabel('Cp [风能利用系数]');legend({legend_str1{:},legend_str1{:}},'location','best');title('机组风速-Cp曲线');ylim([0,1]);
            xlim([0,16])
            %机组风速-Lambda曲线
            figure(6);hold on;
            for i=1:Files_Num
                plot(Files(i).WindSpeedStand,Files(i).Lambda,Color_Point{i});
            end
            for i=1:Files_Num
                plot(Files(i).WindSpeedStandAverage,Files(i).LambdaAverage,Color_Line{i},'LineWidth',1);
            end
            grid on;hold off;xlabel('风速[m/s]');ylabel('Lambda [叶尖速比]');legend({legend_str1{:},legend_str1{:}},'location','best');title('机组风速-Lambda曲线');ylim([4,16]);   
            xlim([0,16])
            %机组Cp-Lambda曲线
            figure(7);hold on;
            for i=1:Files_Num
                plot(Files(i).Lambda,Files(i).Cp,Color_Point{i});
            end
            for i=1:Files_Num
                plot(Files(i).LambdaAverage,Files(i).CpAverage,Color_Line{i},'LineWidth',1);
            end
            grid on;hold off;xlabel('Lambda[-]');ylabel('Cp[叶尖速比]');legend({legend_str1{:},legend_str1{:}},'location','best');title('叶尖速比-Cp曲线');ylim([0,1]);
            xlim([0,16])
    end