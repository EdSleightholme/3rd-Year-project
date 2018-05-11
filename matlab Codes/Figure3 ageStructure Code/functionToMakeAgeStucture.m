function [ popTotal,popYearZ,popYearO ] = functionToMakeAgeStucture(startYearZ,birthRateYearZ,startYearO,birthRateYearO,surivalRateOtoZ,maxTime )
    popYearZ=zeros(1);
    popYearO=zeros(1);
    popTotal=zeros(1);
    popYearZ(1)=startYearZ;
    popYearO(1)=startYearO;
    popTotal(1)=startYearZ+startYearO;
    for time = 2:maxTime
        popYearZ(time) = popYearZ(time-1)*birthRateYearZ + popYearO(time-1)*birthRateYearO;
        popYearO(time) = popYearZ(time-1)*surivalRateOtoZ;
        popTotal(time) = popYearZ(time)+popYearO(time);
    end
end

