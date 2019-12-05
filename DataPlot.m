% Subcode For Main_PowerAnsys��To open the file Created by ligang 2017,11,4

function []=DataPlot(Files,PAR)
    Color_Line ={'-r','-y','-m','-b','-c','-g'};
    Color_Point={'.b','.c','.g','.r','.y','.m'};
    Files_Num=length(Files);
    for i=1:Files_Num
        legend_str=Files(i).Filename;
        [~,legend_str,~]=fileparts(legend_str);     %ȡ���ļ�����ȥ����չ��
        legend_str1{i}=strrep(legend_str,'_','\_'); %���� STRREP(S1,S2,S3) ���ַ���S1�����е�S2��S3���棬ʹ�»���������ʾ��
    end
    [~,legend_str2,~]=fileparts(PAR.Filename1);    %DynamicPowerCurve
    legend_str2=strrep(legend_str2,'_','\_'); 
    clc;
    H1=figure(1);H2=figure(2);H3=figure(3);H4=figure(4);H5=figure(5);H6=figure(6);H7=figure(7);
    close(H1);close(H2);close(H3);close(H4);close(H5);close(H6);close(H7);
    switch 3
        case 3
            %�������-��������
            figure(1);hold on;
            for i=1:Files_Num
                plot(Files(i).WindSpeedStand,Files(i).GenPower,Color_Point{i});
            end
            for i=1:Files_Num
                plot(Files(i).WindSpeedStandAverage,Files(i).GenPowerAverage,Color_Line{i},'LineWidth',1);
            end
            plot(PAR.data(:,1),PAR.data(:,2),'-k','LineWidth',1);
            grid on;hold off;xlabel('����[m/s]');ylabel('���� [kW]');legend({legend_str1{:},legend_str1{:},legend_str2},'location','best');title('�������-��������');
            xlim([0,16])
            %�������-ת������
            figure(2);hold on;
            for i=1:Files_Num
                plot(Files(i).WindSpeedStand,Files(i).GenSpeed,Color_Point{i});
            end
            for i=1:Files_Num
                plot(Files(i).WindSpeedStandAverage,Files(i).GenSpeedAverage,Color_Line{i},'LineWidth',1);
            end
            grid on;hold off;xlabel('����[m/s]');ylabel('ת�� [rpm]');legend({legend_str1{:},legend_str1{:}},'location','best');title('�������-ת������');
            xlim([0,16])
            %�������-��Ҷ�Ƕ�
            figure(3);hold on;
            for i=1:Files_Num
                plot(Files(i).WindSpeedStand,Files(i).PitchAngle,Color_Point{i});
            end
            for i=1:Files_Num
                plot(Files(i).WindSpeedStandAverage,Files(i).PitchAngleAverage,Color_Line{i},'LineWidth',1);
            end
            grid on;hold off;xlabel('����[m/s]');ylabel('��Ҷ�Ƕ� [deg]');legend({legend_str1{:},legend_str1{:}},'location','best');title('�������-��Ҷ�Ƕ�');
            xlim([0,16])
            %����ת��-Ť������
            figure(4);hold on;
            for i=1:Files_Num
                plot(Files(i).GenSpeed,Files(i).GenTorque,Color_Point{i});
            end
            for i=1:Files_Num
                plot(Files(i).GenSpeedAverage,Files(i).GenTorqueAverage,Color_Line{i},'LineWidth',1);
            end
            grid on;hold off;xlabel('�����ת��[rpm]');ylabel('Ť�� [kN.m]');legend({legend_str1{:},legend_str1{:}},'location','best');title('����ת��-Ť������');
            %�������-Cp����
            figure(5);hold on;
            for i=1:Files_Num
                plot(Files(i).WindSpeedStand,Files(i).Cp,Color_Point{i});
            end
            for i=1:Files_Num
                plot(Files(i).WindSpeedStandAverage,Files(i).CpAverage,Color_Line{i},'LineWidth',1);
            end
            grid on;hold off;xlabel('����[m/s]');ylabel('Cp [��������ϵ��]');legend({legend_str1{:},legend_str1{:}},'location','best');title('�������-Cp����');ylim([0,1]);
            xlim([0,16])
            %�������-Lambda����
            figure(6);hold on;
            for i=1:Files_Num
                plot(Files(i).WindSpeedStand,Files(i).Lambda,Color_Point{i});
            end
            for i=1:Files_Num
                plot(Files(i).WindSpeedStandAverage,Files(i).LambdaAverage,Color_Line{i},'LineWidth',1);
            end
            grid on;hold off;xlabel('����[m/s]');ylabel('Lambda [Ҷ���ٱ�]');legend({legend_str1{:},legend_str1{:}},'location','best');title('�������-Lambda����');ylim([4,16]);   
            xlim([0,16])
            %����Cp-Lambda����
            figure(7);hold on;
            for i=1:Files_Num
                plot(Files(i).Lambda,Files(i).Cp,Color_Point{i});
            end
            for i=1:Files_Num
                plot(Files(i).LambdaAverage,Files(i).CpAverage,Color_Line{i},'LineWidth',1);
            end
            grid on;hold off;xlabel('Lambda[-]');ylabel('Cp[Ҷ���ٱ�]');legend({legend_str1{:},legend_str1{:}},'location','best');title('Ҷ���ٱ�-Cp����');ylim([0,1]);
            xlim([0,16])
    end