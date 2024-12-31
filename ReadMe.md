# K-Means Clustering Program

This program implements the **K-Means Clustering** algorithm to cluster data points into `K` clusters and calculate the clustering error. It iterates the clustering process multiple times to optimize the centroids and minimize the error. The program also generates a plot of Error vs. K to help determine the optimal number of clusters.

## Features
1. **Dynamic Cluster Count**:
   - Allows the user to input the desired number of clusters (`K`) for clustering.
   - Automatically tests clustering for values of `K` ranging from 2 to 10.

2. **Centroid Initialization and Calculation**:
   - Randomly assigns initial centroids.
   - Calculates new centroids iteratively based on cluster assignments.

3. **Error Calculation**:
   - Computes the total error as the sum of the Euclidean distances between points and their assigned centroids.

4. **Visualization**:
   - Plots the relationship between the number of clusters (`K`) and the clustering error, helping visualize the "elbow method" to find the optimal `K`.

## Usage
1. **Input**:
   - Provide the path to a text file containing the data points. Each line in the file should represent a data point, with space-separated numerical values for its dimensions.
   - Specify the number of clusters (`K`) to perform the clustering.

2. **Output**:
   - Displays the clustering error for each `K` value.
   - Generates a plot of Error vs. K.

## Steps Performed
1. Reads the input data from a text file.
2. Initializes `K` clusters with random points.
3. Iteratively assigns points to the nearest cluster and recalculates centroids.
4. Calculates the clustering error after a fixed number of iterations (20).
5. Repeats the process for `K` values from 2 to 10 and plots the results.

## Requirements
- Python 3.x
- Libraries:
  - `matplotlib`: For plotting Error vs. K graph.
  - `random`: For generating random cluster assignments.

## Running the Program
1. Place the input data file in a known location.
2. Run the program and provide:
   - The file path to the data file.
   - The desired number of clusters (`K`).
3. View the clustering results and the Error vs. K plot.

## Notes
- Ensure the input file is formatted correctly, with each data point on a new line and values separated by spaces.
- If an `IndexError` occurs during execution, re-run the program as it may be caused by random centroid initialization.
- The program is configured for numerical data and assumes all points are in the same dimensional space.
