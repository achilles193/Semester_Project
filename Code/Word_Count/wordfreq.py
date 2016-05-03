import os
import operator
from stop_words import get_stop_words

stop_words = get_stop_words('english')
stop_words.append('client')
stop_words.append('therapist')

mypath='/home/arsh/Desktop/Course_Project/Transcripts/'
conditions=['sadness','anxiety','suicidal-ideation','frustration','depression-emotion']

for present_cond in conditions:
	freq_map={}
	path=mypath+present_cond+'/'
	dest_path='/home/arsh/Desktop/Course_Project/Frequency_Count/'
	for dirpath,dirnames,filenames in os.walk(path):
		for files in filenames:
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
					if word not in freq_map:
						freq_map[word]=1
					else:
						freq_map[word]+=1
	fout=open(present_cond+'_Frequency.txt','w')
	sorted_inc=sorted(freq_map.items(), key=operator.itemgetter(1))
	sorted_dec=sorted(freq_map.items(), key=operator.itemgetter(1),reverse=True)
	outline='Top 50 Most Frequent Words'+'\n'
	fout.write(outline);
	cnt=0
	for items in sorted_dec:
		cnt+=1
		outline=""
		outline='word: '+items[0]+' Freq: '+str(items[1])
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
		outline='word: '+items[0]+' Freq: '+str(items[1])
		fout.write(outline)
		fout.write('\n')		
		if cnt==50:
			break
