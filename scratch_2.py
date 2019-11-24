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

assumption = [["Bill","24","31.10.1999","M"],["Craig","19","18.05.1992","M"],
              ["Susan","54","11.12.1985","F"], ["Ryan","14,04.02.1994","N/A"],
              ["Bill","67","15.06.1990","M"]]



for i in store:
    for x in i:
        if x[1] == "NNP":
            for z in assumption:
                if x[0] == z[0]:
                    print(x[0])