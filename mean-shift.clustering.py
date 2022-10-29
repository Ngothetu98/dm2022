import json
import numpy as np
import math
from random import seed, randint

# open the file

data = []
with open('/Users/macbook/Desktop/USTH-Semester3/Data_mining/ThaySon/archive/yelp_academic_dataset_review.json') as f:
    i = 0
    for line in f:
        if i < 10:
            data.append(len(json.loads(line)['text']))
            i += 1
            #print(len(line))
    print(data)  
    
    
a = "Ngo The Tu"
print(a)