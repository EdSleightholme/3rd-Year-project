function [ population ] = ComputeHushingsonModel( populationZero,rate,carrying,T,maxTime)
currentPop=populationZero;
population=zeros(1);
population(1)=currentPop;

for time=2:maxTime
    try
        temp = 1- ( (population(time-T)) /(carrying));
    catch
        temp = 1- ( (population(time-1)) /(carrying));
    end
    change = rate*population(time-1)*temp;
    currentPop=change+currentPop;
    population(time)=currentPop;
    %if (currentPop<=0)
    %    break
    %end
end

end

