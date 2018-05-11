function [ output ] = DiscreteLogisticModel( startPop,rate,capcity,endT )

output= zeros(1);
output(1)=startPop
 for time = 1:endT
     output(time+1)=output(time)+rate*output(time)*((capcity-output(time))/(capcity));   
 end
 
end

