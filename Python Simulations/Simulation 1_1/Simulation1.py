from random import *
import csv
def main():
	#SET SIZE OF ENVIROMENT
	w, h = 100, 100;#size of enviroment
	enviroment = [[0 for x in range(w)] for y in range(h)] 
	for x in range(0,w):
		for y in range(0,h):
			enviroment[x][y]=0								#preload value in enviroment
	enviroment[int(w/2)][int(h/2)]=1						#load in statr location for population
	count=0													#count for number indivuals in a population
	stateCount=0											#number of turns the simulation has been running
	open('output/_Stats.csv', 'w+',newline='')				# clear stats file



	while(stateCount<500):		
		print(stateCount)							        #loop until population reachs limit of whole grid
		stateCount=stateCount+1	
		count =0
		for x in range(0,w):								#count number indivuals in enviroment
			for y in range(0,h):
				if (enviroment[x][y]==1):
					count=count+1

		
		for x in range(0,w):								#run chance birth for each indivual
			for y in range(0,h):
				if (enviroment[x][y]==1):
					enviromentTemp=birth(enviroment,x,y,w,h)

		afterBirthCount =0									#count number indivuals in enviroment
		for x in range(0,w):
			for y in range(0,h):
				if (enviromentTemp[x][y]==1):
					afterBirthCount=afterBirthCount+1
		enviroment=enviromentTemp
		numberBirth=afterBirthCount-count 	                #calucte number births in last turn
		
		numberInviduals=afterBirthCount                     #number indivuals in current simulation
		
		updateStats(enviroment,numberInviduals,numberDeath,numberBirth)	#update stats
		#save State to file
		stateTitle='output/State' +str(stateCount)+'.csv'
		writeStateToFile(stateTitle,enviroment)
		

def birth(birthEnviroment,xpos,ypos,envSizeW,envSizeH):
	chance=randint(1, 100) 						            #chance of breeding
	if (chance<50):								
		toLookx=xpos
		toLooky=ypos
		whereToBreedTo=randint(0,80)
		whereToBreedTo=whereToBreedTo%4			            #find space around cell to try breed in to
		if(whereToBreedTo==0):
			toLookx=xpos+1
			if(toLookx>envSizeW-1):
				toLookx=0

		elif (whereToBreedTo==1):
			toLookx=xpos-1
			if(toLookx<0):
				toLookx=envSizeW-1

		elif (whereToBreedTo==2):
			toLooky=ypos+1
			if(toLooky>envSizeH-1):
				toLooky=0
		elif (whereToBreedTo==3):
			toLooky=ypos-1
			if(toLooky<-1):
				toLooky=envSizeH-1
		if(birthEnviroment[toLookx][toLooky]==0):
			birthEnviroment[toLookx][toLooky]=1		        #set population space to alive indivual
	return birthEnviroment


def writeStateToFile(title,enviroment):                     #write enviroment to a csv
	finalOutputFile = open(title, 'w+',newline='')
	with finalOutputFile:
		writer = csv.writer(finalOutputFile)
		for oneRow in enviroment :
			writer.writerow(oneRow)

def updateStats(numberInviduals,numberDeath,numberBirth):#update stats file to a csv
	finalOutputFile = open('output/_Stats.csv', 'a+',newline='')
	with finalOutputFile:
		writer = csv.writer(finalOutputFile)
		writer.writerow([numberInviduals,numberDeath,numberBirth])
	
# Standard boilerplate to call the main() function
if __name__ == '__main__':
	main()
