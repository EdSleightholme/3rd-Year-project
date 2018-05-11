import csv
import pygame
import glob

def main(): #draws all files in input folder to screen and saves them in output folder
	pygame.init()
	size = (100,100) #set size screen
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	GREEN = (0, 255, 0)
	RED = (255, 0, 0) #set colors
	screen = pygame.display.set_mode(size)
	clock = pygame.time.Clock()
	stateCount=0
	for fileName in glob.glob("input\*.csv"): #get all input files
		stateCount=stateCount+1
		print('Processing File' + fileName)#which file beign processed
		allCSVData = open(fileName, 'r').read()
		listOfStateData=allCSVData.split("\n")
		screen.fill(WHITE)
		for y,row in enumerate(listOfStateData): 
			row=row.split(",")
			for x,cell in enumerate(row):
				if (cell=='1'):
					pygame.draw.rect(screen, RED, [x*5, y*5, 5, 5])
				if (cell=='2'):
					pygame.draw.rect(screen, GREEN, [x*5, y*5, 5, 5])
		fileName=fileName[:-4]
		fileName=fileName[6:]
		pygame.image.save(screen, 'output/'+str(fileName)+'.jpeg')#save image
		pygame.display.flip()#display file
		clock.tick(10000)


	pygame.quit()


# Standard boilerplate to call the main() function
if __name__ == '__main__':
	main()
