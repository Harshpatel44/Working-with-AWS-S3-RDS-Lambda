import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords



def f1():
    file = open("001.txt", "r")
    ps = PorterStemmer()
    dictionary={}

    words = word_tokenize(file.read())
    stop_words = set(stopwords.words("english"))
    for i in words:
        if (i not in stop_words):
            if(ps.stem(i) in dictionary):
                dictionary[ps.stem(i)]+=1
            else:
                dictionary[ps.stem(i)]=1
    print(dictionary)



def f2():
    file = open("001.txt", "r")
    dictionary={}
    sentences = nltk.sent_tokenize(file.read())
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(words)
        for i in tagged:
            if(i[1]=='NNP'):
                if(i[0] in dictionary):
                    dictionary[i[0]] = dictionary[i[0]] +1
                else:
                    dictionary[i[0]] = 1
    print(dictionary)
f2()