import os
import sys
import gensim,logging

mypath='/home/arsh/Desktop/Course_Project/'
dict_path='/home/arsh/Desktop/Course_Project/Dictionary_Words/'
conditions=['sadness','anxiety','suicidal-ideation','frustration','depression-emotion']

model = gensim.models.Word2Vec.load('/home/arsh/Desktop/Course_Project/W2VModel/Overall_model_5')

similar={}
test_file="test.txt"
total_words=0

for present_cond in conditions:
	fin=open(test_file)
	avg_sim=0.0
	for lines in fin:
		words=lines.split()
		for word in words:
			total_words+=1
			word=word.strip()
			word=word.lower()
			trimmed=""
			for chars in word:
				if chars>='a' and chars<='z':
					trimmed+=chars
			word=trimmed
			max_sim=-2.0
			dict_fin=open(dict_path+present_cond+'_Words.txt')
			for dict_words in dict_fin:
				dict_words=dict_words.strip()
				try:
					cur_sim=model.similarity(dict_words,word)
					if cur_sim>max_sim:
						max_sim=cur_sim
				except:
					continue
			avg_sim+=max_sim
	avg_sim=avg_sim/total_words
	similar[present_cond]=avg_sim
print similar