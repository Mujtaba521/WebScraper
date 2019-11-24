import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))
store = []
with open('data.txt', 'r') as textFile:
    for sentence in textFile:
        words = word_tokenize(sentence)
        filtered_sentence = []
        for w in words:
            if w not in stop_words:
                filtered_sentence.append(w)
                newStore = nltk.pos_tag(filtered_sentence)
        store.append(newStore)

for i in store:
    for x in i:
        if x[1] == "NNP":
            print(x[0])

