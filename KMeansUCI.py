#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import matplotlib.pyplot as plt

#Note: If there is an IndexError, please run the code once again the error will not come again.

# Function to Calculate Euclidean Distance
def calculate_distance(p_1, p_2):
    # Calculate the Euclidean distance between two points in n-dimensional space
    diffs = [p_1[x] - p_2[x] for x in range(len(p_1))]
    squared_sum = sum([diff ** 2 for diff in diffs])
    return squared_sum ** 0.5

# Function to initialize clusters
def initialize_cluster_points(num_clusters, lines):
    # Initialize clusters with random data points from the input data
    clusters = [[] for _ in range(num_clusters)]
    inputs = []  # List to hold input data points
    try:
        for line in lines:
            # Parse the input line and extract features
            f_vals = [float(val) for val in line.strip().split()]
            dim = len(f_vals) - 1  # Determine dimension length
            f_vals = f_vals[0:dim]
            inputs.append(f_vals)
            # Assign each data point to a random cluster
            index = random.randint(0, num_clusters - 1)
            clusters[index].append(f_vals)
    except:
        print("Error occurred during initialization")
    return dim, clusters, inputs

# Function for generating centroids for each cluster
def generate_centroids(num_clusters, dim, clusters):
    # Calculate centroids for each cluster using the mean of its points
    centroids = []
    try:
        for i in range(num_clusters):
            if clusters[i]:  # Check if cluster is not empty
                centroid = [sum(coord)/len(coord) for coord in zip(*clusters[i])]
                centroids.append(centroid)
            else:
                # If cluster is empty, select a random point from the dataset as centroid
                index = random.randint(0, len(clusters)-1)
                centroids.append(clusters[index][0])  # Choose the first point
    except:
        print("Error occurred during centroid generation")
    return centroids

# Function to calculate the centroid for each cluster
def calculate_new_centroids(num_clusters, dim, clusters):
    # Calculate the centroid for each cluster using the mean of its points
    centroids = []
    try:
        for i in range(num_clusters):
            if len(clusters[i]) > 0:
                centroid = [sum(coord)/len(coord) for coord in zip(*clusters[i])]
                centroids.append(centroid)
    except:
        print("Error occurred during centroid calculation")
    return centroids

# Get user input
data_file = input("Enter the path of the data file: ")
num_clusters = int(input("Enter the number of clusters (K): "))

# Read input file
try:
    with open(data_file, 'r') as file_open:
        lines = file_open.readlines()
except FileNotFoundError:
    print("File not found. Please provide a valid file path.")
    raise

# Perform k-means clustering for K values ranging from 2 to 10
errors = []
for k in range(2, 11):
    num_iterations = 20  # Fixed number of iterations
    random.seed()

    dimension, clusters, inputs = initialize_cluster_points(k, lines)

    centroids = generate_centroids(k, dimension, clusters)

    # Run iterations
    for _ in range(num_iterations):
        clusters = [[] for _ in range(k)]

        # Assign points to clusters based on the nearest centroid
        for point in inputs:
            min_dist = float('inf')
            idx = 0
            for j in range(k):
                distance = calculate_distance(point, centroids[j])
                if distance < min_dist:
                    min_dist = distance
                    idx = j
            clusters[idx].append(point)

        # Update centroids based on the new cluster assignments
        centroids = calculate_new_centroids(k, dimension, clusters)

    # Calculate the total error after 20 iterations
    error = sum([sum([calculate_distance(point, centroids[i]) for point in clusters[i]]) for i in range(k)])
    errors.append(error)

    # Print the error for the current K value
    print(f"For k = {k} After 20 iterations: Error = {error:.4f}")

# Plotting Error vs. K chart
plt.plot(range(2, 11), errors, marker='o')
plt.xlabel('K (Number of Clusters)')
plt.ylabel('Error')
plt.title('Error vs. K')
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




