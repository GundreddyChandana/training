#clean a dirty sentence for the search engine tokenize the sentence and normalize  it ,remove stop words"The quick, BROWN foxes...they are JUMPING over 10 lazy dogs!" 
#output: ["quick","brown","fox","jump","lazi","dog"]


import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def clean_and_process(sentence):

    sentence = sentence.lower()

    sentence = re.sub(r'[^a-z\s]', '', sentence)

    tokens = sentence.split()

    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    

    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    
    return tokens

sentence = "The quick, BROWN foxes...they are JUMPING over 10 lazy dogs!"
result = clean_and_process(sentence)
print(result)