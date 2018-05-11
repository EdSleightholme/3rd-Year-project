[ outputSuspetable,outputInfected,outputRemoved,outputTotal ] = functionEpidmic( 200,0.01,1,25 );
hold all
plot(outputSuspetable)
plot(outputInfected)
plot(outputRemoved)
%plot(outputTotal)
xlabel('Time units = (t)') % x-axis label
ylabel('Number Individuals in a Popualtion') % y-axis label
legend('Suspetable Population','Infected Population','Removed Population')
