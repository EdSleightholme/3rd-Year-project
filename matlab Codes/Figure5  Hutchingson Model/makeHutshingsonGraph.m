
tValueOne=ComputeHushingsonModel(2,0.5,100,1,70);
tValueTwo=ComputeHushingsonModel(2,0.5,100,2,70);
tValueThree=ComputeHushingsonModel(2,0.5,100,3,70);
tValueFour=ComputeHushingsonModel(2,0.5,100,6,200);
hold all
plot(tValueOne);
plot(tValueTwo);
plot(tValueThree);
plot(tValueFour);
xlabel('Time units (t)')
ylabel('Number of Indivuals (N(T))')
legend('T=1','T=2','T=3','T=4')

%make graph that shows how long takes diffenertn values of T to level at K
%value plot(ComputeHushingsonModel(2,0.5,100,10,200))