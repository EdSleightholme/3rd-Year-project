from random import *
import csv
def main():
	#SET SIZE OF ENVIROMENT
	w, h = 100, 100;#size of enviroment
	enviroment = [[0 for x in range(w)] for y in range(h)] 
	for x in range(0,w):
		for y in range(0,h):
			enviroment[x][y]=0								#preload value in enviroment
	enviroment[int(w/4)][int(h/4)]=1						#load in statr location for population 1
	enviroment[int(w/4)*3][int(h/4)*3]=2					#load in statr location for population 2
	count=0													#count for number indivuals in a population
	stateCount=0											#number of turns the simulation has been running
	open('output/_Stats.csv', 'w+',newline='')				# clear stats file



	while(stateCount<500):	
		print(stateCount)									#loop until population reachs limit of whole grid
		stateCount=stateCount+1	
		count1 =0
		count2 =0
		for x in range(0,w):								#count number indivuals of pop1 in enviroment
			for y in range(0,h):
				if (enviroment[x][y]==1):
					count1=count1+1
				if (enviroment[x][y]==2):
					count2=count2+1
		
		for x in range(0,w):								#run chance birth for each indivual of pop1 
			for y in range(0,h):
				if (enviroment[x][y]==1):
					enviromentTemp=birth(enviroment,x,y,w,h,50)
				if (enviroment[x][y]==2):
					enviromentTemp=birth(enviroment,x,y,w,h,25)

		afterBirthCount1 =0									#count number indivuals in enviroment of pop1 
		afterBirthCount2 =0								
		for x in range(0,w):
			for y in range(0,h):
				if (enviromentTemp[x][y]==1):
					afterBirthCount1=afterBirthCount1+1
				if (enviromentTemp[x][y]==2):
					afterBirthCount2=afterBirthCount2+1
		#do death of cell
		for x in range(0,w):								#remove all indivuals that need to die of pop1 
			for y in range(0,h):
				if (enviromentTemp[x][y]>0):
					enviromentTemp=death(enviromentTemp,x,y,w,h)

		afterDeathCount1 =0									#count number indivuals in enviroment of pop1 
		afterDeathCount2 =0									
		for x in range(0,w):
			for y in range(0,h):
				if (enviromentTemp[x][y]==1):
					afterDeathCount1=afterDeathCount1+1
				if (enviromentTemp[x][y]==2):
					afterDeathCount2=afterDeathCount2+1
		enviroment=	enviromentTemp	
		numberBirth1=afterBirthCount1-count1 					#calucte number births in last turn
		numberDeath1=afterBirthCount1-afterDeathCount1			#calucte number deaths in last turn
		numberInviduals1=afterDeathCount1					#number indivuals in current simulation
		numberBirth2=afterBirthCount2-count2 					#calucte number births in last turn
		numberDeath2=afterBirthCount2-afterDeathCount2			#calucte number deaths in last turn
		numberInviduals2=afterDeathCount2	
		updateStats(enviroment,numberInviduals1,numberDeath1,numberBirth1,numberInviduals2,numberDeath2,numberBirth2)	#update stats
		#save State to file
		stateTitle='output/State' +str(stateCount)+'.csv'
		writeStateToFile(stateTitle,enviroment)
		

def birth(birthEnviroment,xpos,ypos,envSizeW,envSizeH,birthRate): 
	chance=randint(1, 100) 						#chance of breeding of pop1 
	if (chance<birthRate):	
		toBreed=birthEnviroment[xpos][ypos]							
		toLookx=xpos
		toLooky=ypos
		whereToBreedTo=randint(0,80)
		whereToBreedTo=whereToBreedTo%4			#find space around cell to try breed in to
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
			birthEnviroment[toLookx][toLooky]=toBreed		#set population space to alive indivual
	return birthEnviroment

def death(deathEnviroment,xpos,ypos,envSizeW,envSizeH):	#if cell is surrounded by 4cells cell looking at dies
	count=0
	tempx=xpos
	tempy=ypos
	if(tempx+1>=len(deathEnviroment)):
		tempx=-1
	if(deathEnviroment[tempx+1][tempy]==1):
		count=count+1

	tempx=xpos
	if(tempx-1<0):#count cells around origin cell
		tempx=envSizeW-1
	if(deathEnviroment[tempx][ypos]==1):
		count=count+1

	if(tempy-1<0):
		tempy=envSizeH
	if(deathEnviroment[xpos][tempy-1]==1):
		count=count+1

	tempy=ypos
	if(tempy+1>=len(deathEnviroment[0])):
		tempy=-1
	if(deathEnviroment[xpos][tempy+1]==1):
		count=count+1


	if(count==4):
		deathEnviroment[xpos][ypos]=0			#kill cell
	return deathEnviroment

def writeStateToFile(title,enviroment):#write enviroment file to a csv
	finalOutputFile = open(title, 'w+',newline='')
	with finalOutputFile:
		writer = csv.writer(finalOutputFile)
		for oneRow in enviroment :
			#print(len(oneCsvFile))
			writer.writerow(oneRow)

def updateStats(enviroment,numberInviduals,numberDeath,numberBirth,numberInviduals2,numberDeath2,numberBirth2):#update stats file to a csv
	finalOutputFile = open('output/_Stats.csv', 'a+',newline='')
	with finalOutputFile:
		writer = csv.writer(finalOutputFile)
		writer.writerow([numberInviduals,numberDeath,numberBirth,numberInviduals2,numberBirth2,numberDeath2])
	
# Standard boilerplate to call the main() function
if __name__ == '__main__':
	main()
