import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

file = open("tech/402.txt","r")

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