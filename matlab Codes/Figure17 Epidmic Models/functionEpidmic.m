function [ outputSuspetable,outputInfected,outputRemoved,outputTotal ] = functionEpidmic( totalPopulationSize,contactRate,removalRate,tMax )
outputSuspetable= zeros(1);
outputInfected= zeros(1);
outputRemoved=zeros(1);

outputSuspetable(1)=totalPopulationSize-1;
outputInfected(1)=1;
outputRemoved(1)=0;
outputTotal(1)=totalPopulationSize;
for t=1:tMax
    
    changeS = -(contactRate*outputSuspetable(t)*outputInfected(t));
   % if (changeS>0)
    %    changeS=0;
 %   end

    changeI = (contactRate*outputSuspetable(t)*outputInfected(t)) - (removalRate*outputInfected(t));

    changeR = removalRate*outputInfected(t);

    
    outputSuspetable(t+1)=outputSuspetable(t)+changeS;
    outputInfected(t+1)=outputInfected(t)+changeI;
    outputRemoved(t+1)=outputRemoved(t)+changeR;
    outputTotal(t+1)=outputSuspetable(t+1)+outputInfected(t+1)+outputRemoved(t+1);
end


    
end