#Dependencies
#Code is tested to work under Python 2.7 and scikit-learn(0.19.1)



import os
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
import sys
# load the dataset

fpath = os.path.abspath('LabelledData.txt')
file = open(fpath, 'r')

label = []  # label for every sentence
sentence = []  # to store every sentence in file in list

for line in file:
    line = line.rstrip('\n')
    line = line.replace('  ', ' ')
    line = line.replace(' ,,, ', '|')
    line = line.replace('?', '')
    line = line.split("|")
    label.append(line[1])
    sentence.append(line[0])

file.close()

text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', LinearSVC()),])
text_clf.fit(sentence, label)
new_docs = raw_input("Question?")

docs_new =[new_docs]
predicted = text_clf.predict(docs_new)
print new_docs, "=>", predicted

#docs_new = ["what is your name", "what time does the train leave","when was the first wall street journal published"]
#predicted = text_clf.predict(docs_new)
#for doc, category in zip(docs_new, predicted):
    #print('%r => %s' % (doc, category))
