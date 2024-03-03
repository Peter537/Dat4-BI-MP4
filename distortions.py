from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def distortions(X):
    elbowDistortions = []
    scoreDistortions = []
    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k, n_init=10)
        kmeans.fit(X)
        elbowDistortions.append(kmeans.inertia_)
        if (k != 1):
            score = silhouette_score(X, kmeans.labels_, metric='euclidean', sample_size=len(X))
            scoreDistortions.append(score)

    plt.figure()
    plt.plot(range(1, 10), elbowDistortions)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('Distortion')
    elbow_plot = plt.gcf()

    plt.figure()
    plt.plot(range(2, 10), scoreDistortions)
    plt.title('Silhouette Score')
    plt.xlabel('Number of clusters')
    plt.ylabel('Score')
    silhouette_plot = plt.gcf()

    return elbowDistortions, scoreDistortions, (elbow_plot, silhouette_plot)
