function [ outputHost,outputParasite ] = functionHostParasite( startHost,startParasite,lamda,a,c,tMax )
output1= zeros(1);
output2= zeros(1);
outputHost(1)=startHost;
outputParasite(1)=startParasite;
for t=1:tMax
    outputHost(t+1)=lamda*outputHost(t)*exp(-a*outputParasite(t));
    outputParasite(t+1)=c*outputHost(t)*(1-exp(-a*outputParasite(t)));
end


    
end

