"""
CISC 3130
Name: Abu Antor
Date: 12/12/2019
"""

#import support libraries
import matplotlib.pyplot as plot, base64
from io import BytesIO
import numpy as numpy


def fileToDict(file):
	fileOpen = open(file, "r" )
	if fileOpen.mode == "r":
		lyrics = fileOpen.read() #open the lyrics file
		wordList = lyrics.replace(",", " ") #strip commas from the lyrics
		wordList = wordList.split() #split the string into individual words
		wrdFrq = [] #This will hold the frequency of occurence

	for i in wordList:
	    wrdFrq.append(wordList.count(i)) #populate the frequency list

    
	wordDict = dict(list(zip(wordList, wrdFrq))) #combine wordList and wrdFrq to create dictionary

	return wordDict 


#function below plots a bargraph
def getBarGraph(data):

	plot.bar(range(len(data)), data.values(), align = 'center', linewidth=100)

	plot.xticks(range(len(data)), list(data.keys()), rotation=90, fontsize = 4)

	barTmpFile = BytesIO()

	barGraph = plot.savefig(barTmpFile, format='png', bbox = 'tight', dpi=200)

	barTmpFile.seek(0)
	plot.close()

	return barTmpFile

#The code below is a function to to plot donut chart, it takes as input a dictionary of the words(and frequency) and plots the chart


#The code below is sort of our main method
def main():
	print("Hello Sit tight while I do the magic\n")
	
	

	skylarWords = fileToDict('skylargreywords.txt') #lyrics to dictionary
	

	barTmpFile = getBarGraph(skylarWords)

	barPNGEnc = base64.b64encode(barTmpFile.getvalue()) #encoding the byte64 files

    #code below is our html file
	
	htmlBar = '<!Doctype html><html><head></head><link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" /><body><h1 class="text-center">Bar graph of Skylar Grey: Words lyrics</h1>' + '<img src="data:image/png;base64,{}" class="text-center">'.format(barPNGEnc.decode('utf-8')) + '</body></html>'

	with open('wordFrequencyBar.html','w') as htmlFile:
		htmlFile.write(htmlBar)

	print("Done, check the file 'wordFrequencyBar.html' in the current directory\n")
    
#The code below fires up the program
if __name__ == '__main__':
	main()



