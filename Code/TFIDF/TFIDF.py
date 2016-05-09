import os
import operator
import math
from stop_words import get_stop_words

stop_words = get_stop_words('english')
stop_words.append('client')
stop_words.append('therapist')

#mypath='/home/arsh/Desktop/Course_Project/Transcripts/'
mypath='../Parsing/Transcripts/'
conditions=['sadness','anxiety','suicidal-ideation','frustration','depression-emotion']

for present_cond in conditions:
	total_files=0
	freq_map={}
	path=mypath+present_cond+'/'
	dest_path='/home/arsh/Desktop/Course_Project/Frequency_Count/'
	for dirpath,dirnames,filenames in os.walk(path):
		doc_freq={}
		for files in filenames:
			word_map={}
			total_files+=1
			fin=open(path+files)
			for lines in fin:
				words=lines.split()
				for word in words:
					word=word.strip()
					word=word.lower()
					trimmed_word=""
					for chars in word:
						if chars>='a' and chars<='z':
							trimmed_word+=chars
					word=trimmed_word
					if len(word)<=3:
						continue
					if word in stop_words:
						continue
					if word not in word_map:
						word_map[word]=1
					if word not in freq_map:
						freq_map[word]=1
					else:
						freq_map[word]+=1
			
			for key in word_map:
				if key not in doc_freq:
					doc_freq[key]=1
				else:
					doc_freq[key]+=1
	tfidfmap={}				
	for keys in freq_map:
		inv=total_files/float(doc_freq[keys])
		tfidfmap[keys]=freq_map[keys]*math.log(inv)
	fout=open(present_cond+'_tfidf.txt','w')
	sorted_inc=sorted(tfidfmap.items(), key=operator.itemgetter(1))
	sorted_dec=sorted(tfidfmap.items(), key=operator.itemgetter(1),reverse=True)
	outline='Top 50 Most Frequent Words'+'\n'
	fout.write(outline);
	cnt=0
	for items in sorted_dec:
		cnt+=1
		outline=""
		outline='word: '+items[0]+' tfidf: '+str(items[1])
		fout.write(outline)
		fout.write('\n')		
		if cnt==50:
			break

	fout.write('\n')		
	outline='Top 50 Least Frequent Words'+'\n'
	fout.write(outline);
	cnt=0
	for items in sorted_inc:
		cnt+=1
		outline=""
		outline='word: '+items[0]+' tfidf: '+str(items[1])
		fout.write(outline)
		fout.write('\n')		
		if cnt==50:
			break
