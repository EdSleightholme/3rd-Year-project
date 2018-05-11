[outputHost,outputParasite]=functionHostParasite( 100,100,1.1,0.001,3,60 );
hold all
plot(outputHost)
plot(outputParasite)
xlabel('Time units = (t)') % x-axis label
ylabel('Number Individuals in a Popualtion') % y-axis label
legend('Population of Hosts','Population of Parasites')
