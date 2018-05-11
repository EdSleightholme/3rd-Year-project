[pop1,pop2]=CompetitionForFood( 1,1.1,100,1,1.1,100,0.2,0.5,29 )
hold all
plot(pop1)
plot(pop2)
xlabel('Time units = (t)') % x-axis label
ylabel('Number Individuals in a Popualtion = N(t)') % y-axis label
legend('Popualtion 1','Popualtion 2')
