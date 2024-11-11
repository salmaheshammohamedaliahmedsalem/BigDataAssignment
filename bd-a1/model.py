import pandas as pd
from sklearn.cluster import KMeans

# Load the preprocessed data
data = pd.read_csv('/home/doc-bd-a1/res_dpre.csv')

# Select columns for K-means with the correct column names
features = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]

# Apply K-means
kmeans = KMeans(n_clusters=3)
data['cluster'] = kmeans.fit_predict(features)

# Save cluster counts
cluster_counts = data['cluster'].value_counts()
with open('/home/doc-bd-a1/k.txt', 'w') as file:
    file.write(str(cluster_counts))

print("Cluster counts saved to k.txt")
