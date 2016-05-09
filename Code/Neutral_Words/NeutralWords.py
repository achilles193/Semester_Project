import os
import operator

#mypath='/home/arsh/Desktop/Course_Project/Transcripts/'
mypath='../Parsing/Transcripts/'
conditions=['sadness','anxiety','suicidal-ideation','frustration','depression-emotion']

freq_map={}
cat_map={}
cat_cnt={}
neutral_words=set()

for present_cond in conditions:
	path=mypath+present_cond+'/'
	for dirpath,dirnames,filenames in os.walk(path):
		for files in filenames:
			fin=open(path+files)
			for lines in fin:
				words=lines.split()
				for word in words:
					word=word.lower()
					trimmed_word=""
					for chars in word:
						if chars>='a' and chars<='z':
							trimmed_word+=chars
					word=trimmed_word
					if len(word)<=3:
						continue
					if word not in freq_map:
						freq_map[word]=1
					else:
						freq_map[word]+=1
					if word not in cat_map:
						cat_map[word]=present_cond
						cat_cnt[word]=1
					elif cat_map[word]!=present_cond:
						cat_cnt[word]+=1
						cat_map[word]=present_cond
						if cat_cnt[word]>=3:
							neutral_words.add(word)

fout=open('Neutral_Words.txt','w')
for words in neutral_words:
	fout.write(words+'\n')

