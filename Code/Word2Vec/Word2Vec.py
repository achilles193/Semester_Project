import os
import gensim,logging

#mypath='/home/arsh/Desktop/Course_Project/Transcripts/'
mypath='../Parsing/Transcripts/'
conditions=['sadness','anxiety','suicidal-ideation','frustration','depression-emotion']


class MySentences(object):
	def __init__(self, dirname):
		self.dirname = dirname

	def __iter__(self):
		for present_cond in conditions:
			path=mypath+present_cond+'/'
			for dirpath,dirnames,filenames in os.walk(path):
				for files in filenames:
					fin=open(path+files)
					for lines in fin:
						lines=lines.lower()
						line=""
						for chars in lines:
							if chars>='a' and chars<='z':
								line+=chars
							elif chars==' ':
								line+=chars
						yield line.split()



logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = MySentences('/some/directory')
model=gensim.models.Word2Vec(sentences, min_count=1,size=200)
#model.save('/home/arsh/Desktop/model')
model.save('../Word2Vec/model')

print model.similarity('happy', 'pair')