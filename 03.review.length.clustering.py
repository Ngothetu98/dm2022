import json
import numpy as np

# open the file
review_file = open("/Users/macbook/Desktop/USTH-Semester3/Data_mining/ThaySon/archive/yelp_academic_dataset_review.json")

data = []
count = 0

# Load the data
with review_file as f:
    for line in f:
        count = count + 1
        if count == 1000:
            break
        data.append(json.loads(line))

maxtrix_text_length = []

print(len(data))
# Extract the text from the data
texts = [d['text'] for d in data]
#print(texts)
print(len(texts))

class Cluster:
    def __init__(self, cluster):
        self.cluster = []
        self.cluster.append(cluster)

    def __repr__(self):
        return str(self.cluster)

    def getClusterDistance(self, cluster, dist = 0):
        cluster1 = self.cluster
        cluster2 = cluster.cluster
        dist1 = 0
        for i in cluster1:
            for j in cluster2:
                
                if i != j:
                    dist1 = abs(i - j)
                    if dist1 < dist:
                        dist = dist1
        return dist

#calculate the distance between the text length
for i in range(len(texts)):
    for j in range(len(texts)):
        if i != j:
            maxtrix_text_length.append(abs(len(texts[i]) - len(texts[j])))

class Clusters:
    def __init__(self, cluster):
        self.cluster = []
        self.cluster.append(cluster)
        pass

#find the max and min distance
maxtrix_text_length = np.array(maxtrix_text_length)
min_distance = np.min(maxtrix_text_length)
max_distance = np.max(maxtrix_text_length)
print(maxtrix_text_length)
print("min distance: ", min_distance)
print("max distance: ", max_distance)

#calculate the Agglomerative Hierarchical Clustering by using the distance between the text length




