# Clustering

## K Means

K means works in two steps:
### Assignment
Create two random points as cluster centers. Draw orthogonal line at the midpoint of the line between those two centers. 
All the points on one side of the line are assigned to one center and the others to the other center. Each point has a distance
to its center that can be thought of as a rubberband.

### Optimization
Minimize the quadratic distances from points to random cluster centers and then move the center and iterate. This iteration of
assignment and optimization arrives at the center points of the clusters.

K means is somewhat dependent on initial condition of where to start the initial centroids. Good for very large sample sizes
with medium number of clusters. It is a general purpose algorithm with even cluster sizes and flat geometry. It uses distance
between points. The greater number of clusters, the greater chance of a local minimum, and so the greater need for a higher 
n_init.


`from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0],
             [10, 2], [10, 4], [10, 0]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
kmeans.labels_`
`n_clusters` parameter sets number of centroids
`max_iter` defaults to 300 and may be too much for easy cases
`n_init` defaults to 10 and may be two few for troublesome cases


## Affinity propagation
damping, sample preference
Not scalable with n_samples
Many clusters, uneven cluster size, non-flat geometry, inductive
Graph distance (e.g. nearest-neighbor graph)

## Mean-shift
bandwidth
Not scalable with n_samples
Many clusters, uneven cluster size, non-flat geometry, inductive
Distances between points

## Spectral clustering
number of clusters
Medium n_samples, small n_clusters
Few clusters, even cluster size, non-flat geometry, transductive
Graph distance (e.g. nearest-neighbor graph)

## Ward hierarchical clustering
number of clusters or distance threshold
Large n_samples and n_clusters
Many clusters, possibly connectivity constraints, transductive
Distances between points

## Agglomerative clustering
number of clusters or distance threshold, linkage type, distance
Large n_samples and n_clusters
Many clusters, possibly connectivity constraints, non Euclidean
distances, transductive
Any pairwise distance

## DBSCAN
neighborhood size
Very large n_samples, medium n_clusters
Non-flat geometry, uneven cluster sizes, outlier removal,
transductive
Distances between nearest points

## OPTICS
minimum cluster membership
Very large n_samples, large n_clusters
Non-flat geometry, uneven cluster sizes, variable cluster density,
outlier removal, transductive
Distances between points

## Gaussian mixtures
many
Not scalable
Flat geometry, good for density estimation, inductive
Mahalanobis distances to  centers

## BIRCH
branching factor, threshold, optional global clusterer.
Large n_clusters and n_samples
Large dataset, outlier removal, data reduction, inductive
Euclidean distance between points



# Dimensionality Reduction
