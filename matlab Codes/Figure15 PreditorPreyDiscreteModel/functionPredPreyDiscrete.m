function [ popPrey,popPred ] = functionPredPreyDiscrete( preyStart,predStart,r,c,b,k,K,maxT )

popPrey=zeros(1);
popPred=zeros(1);
 
 popPrey(1)=double(preyStart);
 popPred(1)=double(predStart);

 
 for time= 1:maxT
        changePrey=double((r*(popPrey(time)/1000))*(1-((popPrey(time)/1000)/K))-(b*(popPrey(time)/1000)*(popPred(time)/1000)));
        changePred=double((c*(popPred(time)/1000)*(popPrey(time)/1000))-(k*(popPred(time)/1000)));   
        if (popPrey(time)+changePrey>0)
            popPrey(time+1)=double(popPrey(time)+changePrey);
        else
            popPrey(time+1)=0;
        end
        if (popPred(time)+changePred>0)
            popPred(time+1)=double(popPred(time)+changePred);
        else
            popPred(time+1)=0;
        end
 

end

