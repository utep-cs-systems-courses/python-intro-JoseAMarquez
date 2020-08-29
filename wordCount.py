import sys
import re
import os

#check for correct arguments
if len(sys.argv) != 3:
	print('Wrong arguments')
	exit()

#set argument for input file and checks if input file exists
inFileName = sys.argv[1]
if not os.path.exists(inFileName):
	print('Input file dosent exists')
	exit()

#Arguments
outFileName = sys.argv[2]

#array fo words
wordList = {}
#hash table  kley word and value counter
wordCounter = {}

#open input file and covert to a text
print ('Counting Words')
inFile = open(inFileName, 'r')
text = inFile.read()

#Gets all words from the text
wordList = re.findall(r'\w+', text)

#goint into all thw wordlist
for word in wordList:
	#convert all chatacters into lower case so it dont count Hello and hello as 2 different words
	word = word.lower()
	#check if word is in the array
	if word in wordCounter.keys():
		wordCounter[word] += 1
	else:
		wordCounter[word] = 1

#sort and open/creation of file
outFile = open(outFileName, 'w+')
for word in sorted(wordCounter):
	outFile.write('%s %s \n' % (word, wordCounter[word]) )
