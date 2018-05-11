function [ output1,output2 ] = CompetitionForFood( popStart1,rate1,capcity1,popStart2,rate2,capcity2,effect12,effect21,maxT )
output1= zeros(1);
output2= zeros(1);
output1(1)=popStart1;
output2(1)=popStart2;
    for time = 1:maxT
	change1 = ((rate1*output1(time))/capcity1)*(capcity1-output1(time)-effect12*output2(time));
	change2 = ((rate2*output2(time))/capcity2)*(capcity2-output2(time)-effect21*output1(time)); 
    output1(time+1)=output1(time)+change1;
    output2(time+1)=output2(time)+change2;
    end
end

