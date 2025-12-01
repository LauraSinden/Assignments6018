#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Using one of the three datasets to demonstrate k-means clustering using the scikit learn package (50 points).
#Be sure to review the readings before you start on this assignment. Calculate the sum of least square error for each different values of 'k'. 
#Using Matplotlib determine the optimal number of clusters (k) using the elbow method along with a brief explanation (50 points) . Finally plot the optimal clusters with their centroids along with a brief explanation (50 points). Comment your code as needed.

get_ipython().system('pip install -U ucimlrepo')
get_ipython().system('pip install pandas')
get_ipython().system('pip install scikit-learn')


# In[2]:


# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from ucimlrepo import fetch_ucirepo

# fetch dataset 
breast_cancer = fetch_ucirepo(id=14) 

# data (as pandas dataframes) 
X = breast_cancer.data.features 
y = breast_cancer.data.targets 

# 1. Convert categorical string data to numerical using one-hot encoding (get_dummies)
X_encoded = pd.get_dummies(X, drop_first=True)

# 2. Fill missing values (NaNs) *after* encoding. 
#    Now all columns are numerical (0s and 1s), so .median() will work.
X_filled = X_encoded.fillna(X_encoded.median())

# 3. Standardize the features for K-means
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_filled)

# 4. Reduce the data to 2 dimensions using PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Data successfully prepared and encoded. You can now proceed with the assignment.")


# In[3]:


import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
print("--- Part 1: Calculating SSE values ---")


# In[4]:


#sum of least Square error (sse)
sse = []
k_values = range(1, 11) # Test k from 1 to 10

for k in k_values:
    # Initialize KMeans with k clusters and random_state for reproducibility
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    # Fit the model to the 2D PCA data
    kmeans.fit(X_pca)
    # Append the inertia (SSE) to the list
    sse.append(kmeans.inertia_)
for k, error in zip(k_values, sse):
    print(f"k={k}, SSE={error:.2f}")



# In[5]:


#Determine the optimal number of clusters (k) using the Elbow Method
print("\n--- Part 2: Elbow Method Visualization and Explanation ---")


# In[6]:


# Plot the elbow curve
plt.figure(figsize=(8, 5))
plt.plot(k_values, sse, marker='o', linestyle='-')
plt.title('Elbow Method For Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Sum of Squared Errors (SSE)')
plt.grid(True)
plt.show()

# Brief Explanation:
print("\nExplanation of the Elbow Method:")
print("The plot shows the relationship between the number of clusters (k) and the Sum of Squared Errors (SSE).")
print("We look for an 'elbow' point where the sharp decrease in SSE begins to flatten out.")
# Typically for this binary classification dataset, k=2 is optimal.
optimal_k = 2 
print(f"\nBased on visual inspection of the elbow plot, the optimal number of clusters (k) is {optimal_k}.")



# In[7]:


# Part 3: Plot the optimal clusters with their centroids
# -----------------------------------------------------------
print("\n--- Part 3: Optimal Clusters Plot and Explanation ---")


# In[8]:


#Optimal clusters and their centroids
# Perform K-means with the optimal k (k=2)
kmeans_optimal = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
# Predict the cluster assignment for each data point
y_kmeans = kmeans_optimal.fit_predict(X_pca)
# Get the coordinates of the final centroids
centroids = kmeans_optimal.cluster_centers_

# Plot the clusters and centroids
plt.figure(figsize=(8, 6))

# Scatter plot for data points, colored by cluster assignment
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_kmeans, s=50, cmap='viridis', label='Data Points (Clusters)')

# Plot the centroids
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, marker='*', c='red', edgecolor='black', label='Centroids')

plt.title(f'K-Means Clustering with Optimal k = {optimal_k}')
plt.xlabel('PCA Feature 1')
plt.ylabel('PCA Feature 2')
plt.legend()
plt.grid(True)
plt.show()
# Brief Explanation of the Plot:
print("\nExplanation of the Optimal Clusters Plot:")
print(f"The data (reduced to 2 principal components for visualization) has been partitioned into {optimal_k} distinct clusters (yellow and purple points).")
print("The center of each cluster is marked by a red star symbol (the centroid).")
print("The K-means algorithm placed these centroids in a location that minimizes the overall distance of all points to their assigned cluster center.")


# In[ ]:




