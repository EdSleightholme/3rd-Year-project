hold all
plot(generateDataDiscreteContinuosPopulations(1.1,10,10))
plot(generateDataDiscreteContinuosPopulations(0.9,10,10))
plot(generateDataDiscreteContinuosPopulations(1,10,10))
legend('R=1.1','R=0.9','R=1')
xlabel('Time units = (t)') % x-axis label
ylabel('Number Individuals in a Popualtion = N(t)') % y-axis label