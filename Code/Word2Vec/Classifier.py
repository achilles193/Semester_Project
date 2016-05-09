import os
import sys
import gensim,logging

#mypath='/home/arsh/Desktop/Course_Project/'
mypath='../Parsing/'
conditions=['sadness','anxiety','suicidal-ideation','frustration','depression-emotion']

#model = gensim.models.Word2Vec.load('/home/arsh/Desktop/Course_Project/W2VModel/Overall_model_5')

similar={}
total_files=[]
test_files=[]
test_files_map={}

for present_cond in conditions:
	cnt=0
	path=mypath+'Transcripts/'+present_cond+'/'
#	print path
	for dirpath,dirnames,filenames in os.walk(path):
		print filenames
		for files in filenames:
			print files
			cnt+=1
	total_files.append(cnt)

print total_files
for vals in total_files:
	test_files.append(vals/5)

test_files_map['sadness']=test_files[0]
test_files_map['anxiety']=test_files[1]
test_files_map['suicidal-ideation']=test_files[2]
test_files_map['frustration']=test_files[3]
test_files_map['depression-emotion']=test_files[4]

#dict_path='/home/arsh/Desktop/Course_Project/Dictionary_Words/'
dict_path='../Dictionary_Words/'

for present_cond1 in conditions:
	print present_cond1
	print 'Total Files =' + str(test_files_map[present_cond1])
	cor_cls=0
	mis_cls=0
	path=mypath+'Transcripts/'+present_cond1+'/'
	for dirpath,dirnames,filenames in os.walk(path):
		for files in filenames:
			similar={}
			if test_files_map[present_cond1]==0:
				break
			test_files_map[present_cond1]-=1
			for present_cond in conditions:
				avg_sim=0.0
				fin=open(path+files)
				total_words=0
				for lines in fin:
					splitted=lines.split()
					for words in splitted:
						total_words+=1
						words=words.lower()
						trimmed=""
						for chars in words:
							if chars>='a' and chars<='z':
								trimmed+=chars
						words=trimmed

						max_sim=-2.0
						dict_fin=open(dict_path+present_cond+'_Words.txt')
						for dict_words in dict_fin:
							dict_words=dict_words.strip()
							try:
								cur_sim=model.similarity(dict_words,words)
								if cur_sim>max_sim:
									max_sim=cur_sim
							except:
								continue
						avg_sim+=max_sim
				avg_sim=avg_sim/total_words
				similar[present_cond]=avg_sim;
			max_cond="sadness"
			for key in similar:
				if similar[key]>similar[max_cond]:
					max_cond=key
			if max_cond==present_cond1:
				cor_cls+=1
			else:
				mis_cls+=1
	print 'Correctly Classified='+str(cor_cls)				
	print 'MisClassified='+str(mis_cls)

#print similar