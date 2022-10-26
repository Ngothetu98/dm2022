import math
# Regular expression operations¶
import re
import json
import string

# import file
data_file = []
with open("/Users/macbook/Desktop/USTH-Master3/Data_mining/ThaySon/archive/yelp_academic_dataset_review.json") as f:
     datas = f.readline()

text = ""
word = ""
for data in data_file:
     data.append(json.loads(data))['text']
     # text += obj.get("text")
     if len(data) == 1000:
          break
     data_file.close()
print(len(data))

# change non-word letters to space
text = re.sub(r"\W","",text)

# get words from texts
# Normalized, Word-counted
words = text.split()
once_WORD = ()
for word in words:
    if word in once_WORD:
        once_WORD[word] +=1
    else:
        print(f"new word {word}")
        once_WORD[word] = 1
    if len(once_WORD) > 100:
        break;
print(once_WORD)

# DF function
def df(w,text):
     if w in text:
          return 1
     return 0

# Tf words in a document
def caculate_tf(w, doc):
    return doc[w]

# IDF word documents
def caculate_idf(w, text):
    return math.log(1/df(w,text))


# TF-IDF values of a review
def caculate_tf_idf(w, text, doc):
     return caculate_tf(w, doc) * caculate_idf(w, text)



