import os
import sys

fout=open('Dataset.csv','w')
fdict=open('Neutral_Words_5.txt')
ind=0
dict_words_index={}
dict_words=[]
outline=''
for lines in fdict:
	lines=lines.strip()
	dict_words.append(lines)
	dict_words_index[lines]=ind
	ind+=1
	outline+=lines+','
outline+='Present_Condition'
fout.write(outline)
fout.write('\n')

mypath='/home/arsh/Desktop/Course_Project/Training_Scripts/'
conditions=['sadness','anxiety','suicidal-ideation','frustration','depression-emotion']

for present_cond in conditions:
	path=mypath+present_cond+'/'
	for dirpath,dirnames,filenames in os.walk(path):
		for files in filenames:
			cur_arr=[]
			for i in range(ind):
				cur_arr.append(0)

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
					if word in dict_words_index:
						cur_arr[dict_words_index[word]]+=1
			outline=''
			for elems in cur_arr:
				outline+=str(elems)+','
			outline+=present_cond
			fout.write(outline)
			fout.write('\n')
