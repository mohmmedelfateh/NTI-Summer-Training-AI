import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt1

# lode and Preparing data
df = pd.read_csv("Mall_Customers.csv")
x = df.iloc[:, 1:5]

# Convert features to truth table columns, eliminating unnecessary columns
CT = ColumnTransformer([('first', OneHotEncoder(), [0])], remainder='passthrough')
x = CT.fit_transform(x)
x = x

# This  for loop tries a different number of clusters and stores the WCSS inside a list
# WCSS Stands for the sum of the squares of distances of the data points in each and every cluster from its centroid.
wcss = []  # Within-Cluster-Sum-of-Squares
for i in range(1, 11):
    km = KMeans(n_clusters=i, max_iter=300)
    km.fit(x)
    wcss.append(km.inertia_)

plt1.plot(range(1, 11), wcss)
plt1.xlabel('Number of clusters')
plt1.ylabel('WCSS')
plt1.show()

"""
From the diagram, we can see that the best number of groups that can be formed is three.
This means that this mall has three groups of customers.
"""


# Here we draw our there groups
kmeans = KMeans(3)
identified_clusters = kmeans.fit_predict(x)
data_with_clusters = df.copy()
print(identified_clusters)
data_with_clusters['Clusters'] = identified_clusters
plt1.scatter(data_with_clusters['Spending Score (1-100)'],data_with_clusters['Annual Income (k$)'], c=data_with_clusters['Clusters'], cmap='rainbow')
plt1.xlabel('Spending Score (1-100)')
plt1.ylabel('Annual Income (k$)')
plt1.show()

"""
For more if you interest:
https://www.analyticsvidhya.com/blog/2021/04/k-means-clustering-simplified-in-python/
"""