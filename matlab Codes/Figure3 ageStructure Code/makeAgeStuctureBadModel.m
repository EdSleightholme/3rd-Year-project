[popT,popZ,popO]=functionToMakeAgeStucture(10,1.1,10,1.1,0.5,20);
[popT2,popZ2,popO2]=functionToMakeAgeStucture(10,1.1,0,1.1,0.5,20);
ratios=zeros(size(popZ));
s=size(popZ)
for x = 1:s(2)
    ratios(x)=popZ(x)/popO(x);
end

hold all
plot(popZ);
plot(popO);
plot(popT);
legend('Population Of  0 Year olds','Population Of  1 Year olds','Total population Size')
xlabel('Time units = (t)') % x-axis label
ylabel('Number Individuals in a Popualtion') % y-axis label