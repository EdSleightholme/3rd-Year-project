function [ output ] = generateDataDiscreteContinuosPopulations(r,startN,endT)
    output= zeros(1);
    for time = 0:endT
        numberIndivuals=(r^time)*startN;
        output(time+1)=(numberIndivuals);
    end
    
        

end

