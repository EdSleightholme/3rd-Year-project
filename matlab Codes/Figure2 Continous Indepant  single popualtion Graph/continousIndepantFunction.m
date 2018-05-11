function [ output ] = continousIndepantFunction(r,startingPop,endT )
    
 output= zeros(1);
    for time = 0:endT
     numberIndivuals=startingPop*exp(r*time);
     output(time+1)=(numberIndivuals);   
    end

end

