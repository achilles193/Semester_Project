import os
import sys

path='/home/arsh/Desktop/Course_Project/Neutral_Words/'

union_of_words=set()
for dirpath,dirnames,filenames in os.walk(path):
	for files in filenames:
		fin=open(path+files)
		for words in fin:
			splits=words.split()
			if len(splits)>1:
				continue
			words=words.strip()
			union_of_words.add(words)

fout=open('Dictionary.txt','w')
for words in union_of_words:
	fout.write(words+'\n')