% Subcode For Main_PowerAnsys，To open the file Created by ligang 2017,11,4

function [Files]=DataProcess(Files,PAR)
PI=pi();
CON_Sample=24;
for i=1:length(Files)
    %变量导入
    if( PAR.WindSpeedEnable )
        Index=strcmp(PAR.WindSpeedName,Files(i).text);
        Files(i).WindSpeed  =Files(i).data(:,Index);
    end
    if( PAR.GenPowerEnable )
        Index=strcmp(PAR.GenPowerName,Files(i).text);
        Files(i).GenPower   =Files(i).data(:,Index);
    end
    if( PAR.GenSpeedEnable )
        Index=strcmp(PAR.GenSpeedName,Files(i).text);
        Files(i).GenSpeed   =Files(i).data(:,Index);
    end
    if( PAR.GenTorqueEnable )
        Index=strcmp(PAR.GenTorqueName,Files(i).text);
        Files(i).GenTorque  =Files(i).data(:,Index)./1000;%单位kNm
    end
    if( PAR.PitchAngleEnable )
        Index=strcmp(PAR.PitchAngleName,Files(i).text);
        Files(i).PitchAngle =Files(i).data(:,Index);
    end
    if( PAR.TempOutdoorEnable )
        Index=strcmp(PAR.TempOutdoorName,Files(i).text);
        Files(i).TempOutdoor=Files(i).data(:,Index);
    end
    %数据前处理
%     Scale1=(Files(i).WindSpeed<=PAR.TWindScale(1,1)).*PAR.TWindScale(2,1);
%     Scale2=(Files(i).WindSpeed>PAR.TWindScale(1,1) & Files(i).WindSpeed<=PAR.TWindScale(1,2)).*PAR.TWindScale(2,2);
%     Scale3=(Files(i).WindSpeed>PAR.TWindScale(1,2) & Files(i).WindSpeed<=PAR.TWindScale(1,3)).*PAR.TWindScale(2,3);
%     Scale4=(Files(i).WindSpeed>PAR.TWindScale(1,3) & Files(i).WindSpeed<=PAR.TWindScale(1,4)).*PAR.TWindScale(2,4);
%     Scale5=(Files(i).WindSpeed>PAR.TWindScale(1,4) & Files(i).WindSpeed<=PAR.TWindScale(1,5)).*PAR.TWindScale(2,5);
%     Scale6=(Files(i).WindSpeed>PAR.TWindScale(1,5)).*PAR.TWindScale(2,5);
%     Scale=Scale1+Scale2+Scale3+Scale4+Scale5+Scale6;
    Scale=myinterp(PAR.TWindScale(1,:),PAR.TWindScale(2,:),Files(i).WindSpeed);
    Files(i).WindSpeed=Files(i).WindSpeed./Scale;
    BoolFilter0=Files(i).GenPower>5 & Files(i).GenPower<=PAR.NominalPowerkW*1.05;
    if( PAR.FilterEnable1 ) BoolFilter1=~(Files(i).GenPower<PAR.Filter1.GenPower & Files(i).PitchAngle>PAR.Filter1.PitchAngle);else BoolFilter1=BoolFilter0;end
    if( PAR.FilterEnable2 ) BoolFilter2=~(Files(i).GenPower<PAR.Filter2.GenPower & Files(i).PitchAngle>PAR.Filter2.PitchAngle);else BoolFilter2=BoolFilter0;end
    if( PAR.FilterEnable3 ) BoolFilter3=~(Files(i).GenPower<PAR.Filter3.GenPower & Files(i).PitchAngle>PAR.Filter3.PitchAngle);else BoolFilter3=BoolFilter0;end
    if( PAR.FilterEnable4 ) BoolFilter4=~(Files(i).WindSpeed<PAR.Filter4.WindSpeed & Files(i).PitchAngle>PAR.Filter4.PitchAngle);else BoolFilter4=BoolFilter0;end
    if( PAR.FilterEnable5 ) BoolFilter5=~(Files(i).WindSpeed<PAR.Filter5.WindSpeed & Files(i).PitchAngle>PAR.Filter5.PitchAngle);else BoolFilter5=BoolFilter0;end
    if( PAR.FilterEnable6 ) BoolFilter6=~(Files(i).WindSpeed<PAR.Filter6.WindSpeed & Files(i).PitchAngle>PAR.Filter6.PitchAngle);else BoolFilter6=BoolFilter0;end
    BoolFilter=BoolFilter0 & BoolFilter1 & BoolFilter2 & BoolFilter3 & BoolFilter4 & BoolFilter5 & BoolFilter6;
    if( PAR.WindSpeedEnable )
        Files(i).WindSpeed  =Files(i).WindSpeed(BoolFilter);
    end
    if( PAR.GenPowerEnable )
        Files(i).GenPower   =Files(i).GenPower(BoolFilter);
    end
    if( PAR.GenSpeedEnable )
        Files(i).GenSpeed   =Files(i).GenSpeed(BoolFilter);
    end
    if( PAR.GenTorqueEnable )
        Files(i).GenTorque  =Files(i).GenTorque(BoolFilter);
    end
    if( PAR.PitchAngleEnable )
        Files(i).PitchAngle =Files(i).PitchAngle(BoolFilter);
    end
    if( PAR.TempOutdoorEnable )
        Files(i).TempOutdoor=Files(i).TempOutdoor(BoolFilter);
    end
    %根据温度、海拔高度求空气密度
    t=Files(i).TempOutdoor;  h=PAR.LocalAltitude;
    Files(i).Pressure =exp(5.25885*log(288.15-6.5*10^-3*h)-18.25731)*10^-6;     %单位MP
    Files(i).Rou      = 1.293*(273.15)*Files(i).Pressure./((273.15+t)*0.101325);  %单位kg/m^3
    %风速折算到标准空气密度
    AirDensityRatio=Files(i).Rou./PAR.StandardAirDensity;
    Files(i).WindSpeedStand=Files(i).WindSpeed.*nthroot(AirDensityRatio,3);
    %计算Lambda、Cp
    RotorSpeed      =Files(i).GenSpeed./PAR.GearRatio;
    R               =PAR.RotorDiameter/2;
    TipSpeed        =RotorSpeed*PI*R./30;
    Files(i).Lambda =TipSpeed./Files(i).WindSpeedStand ;%TipSpeedRatio
    Files(i).Cp     =Files(i).GenPower*1000./(0.5*Files(i).Rou.*Files(i).WindSpeed.^3*PI*R^2);
    %计算平均值
    [Files(i).WindSpeedStandAverage,Files(i).GenPowerAverage]    =fenqu(Files(i).WindSpeedStand,Files(i).GenPower,2.75,14.25,CON_Sample);
    [~                      ,Files(i).GenSpeedAverage]      =fenqu(Files(i).WindSpeedStand,Files(i).GenSpeed,2.75,14.25,CON_Sample);
    [~                      ,Files(i).GenTorqueAverage]     =fenqu(Files(i).WindSpeedStand,Files(i).GenTorque,2.75,14.25,CON_Sample);
    [~                      ,Files(i).PitchAngleAverage]    =fenqu(Files(i).WindSpeedStand,Files(i).PitchAngle,2.75,14.25,CON_Sample);
    [~                      ,Files(i).LambdaAverage]        =fenqu(Files(i).WindSpeedStand,Files(i).Lambda,2.75,14.25,CON_Sample);
    [~                      ,Files(i).CpAverage]            =fenqu(Files(i).WindSpeedStand,Files(i).Cp,2.75,14.25,CON_Sample);
    [~                      ,Files(i).RouAverage]           =fenqu(Files(i).WindSpeedStand,Files(i).Rou,2.75,14.25,CON_Sample);
end
%数据存储
save('Files.mat','Files')
end
function [yy]=myinterp(x,y,xx)
yy=ones(size(xx));
Index=xx<x(1);yy(Index)=y(1);
Index=xx>=x(5);yy(Index)=y(5);
Index=xx>=x(1)&xx<x(2);yy(Index)=y(1).*(xx(Index)-x(2))./(x(1)-x(2))+y(2).*(xx(Index)-x(1))./(x(2)-x(1));
Index=xx>=x(2)&xx<x(3);yy(Index)=y(2).*(xx(Index)-x(3))./(x(2)-x(3))+y(3).*(xx(Index)-x(2))./(x(3)-x(2));
Index=xx>=x(3)&xx<x(4);yy(Index)=y(3).*(xx(Index)-x(4))./(x(3)-x(4))+y(4).*(xx(Index)-x(3))./(x(4)-x(3));
Index=xx>=x(4)&xx<x(5);yy(Index)=y(4).*(xx(Index)-x(5))./(x(4)-x(5))+y(5).*(xx(Index)-x(4))./(x(5)-x(4));
end
function [xx,yy]=fenqu(x,y,xmin,xmax,num)

    xqu=linspace(xmin,xmax,num);
    step=xqu(2)-xqu(1);
    xx=xqu(1:end-1)+step/2;
    for k=1:length(xqu)-1
        idx = find (x>=xqu(k)&x<xqu(k+1));
        yt(k)=mean(y(idx));
        xt(k)=mean(x(idx));
    end
    xx=xt';
    yy=yt';
end