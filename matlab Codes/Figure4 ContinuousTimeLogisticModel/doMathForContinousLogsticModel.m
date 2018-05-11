function [ output ] = doMathForContinousLogsticModel( startPop,carryCapity,rate,maxT )
    output= zeros(1);
    output(1)=startPop;
    for time = 2:maxT 
    output(time)=(startPop*exp(rate*time))/ (1+startPop*(exp(rate *time)-1)/(carryCapity) );
    
    end

end

