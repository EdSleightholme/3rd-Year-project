[popPrey,popPred ]=functionPredPreyDiscrete( 0.99,0.99,1,1,1,1,10,100000 );
hold all
plot(popPrey);
plot(popPred);
legend('Prey Population','Preditor Population')
xlabel('Time units = (t)') % x-axis label
ylabel('Number Individuals in a Popualtion') % y-axis