import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

from main import cargarUsuarios
usuarios = cargarUsuarios('usuarios_validos4.csv')


data = []
for i in usuarios:
    data.append([i.lng, i.lat])
    if int(i.lat) > -30:
        print(i._uid)

X = np.array(data, dtype=float)

labels = range(1, len(data))
plt.figure(figsize=(10, 7))
plt.subplots_adjust(bottom=0.1)
plt.scatter(X[:,0],X[:,1], label='True Position', s=1)

for label, x, y in zip(labels, X[:, 0], X[:, 1]):
    plt.annotate(
        label,
        xy=(x, y), xytext=(-3, 3),
        textcoords='offset points', ha='right', va='bottom')

#plt.xlim(-33.70, -32.70)
#plt.ylim(-71.3, -70.3)
#plt.show()

cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
cluster.fit_predict(X)

#print(cluster.labels_)
plt.scatter(X[:,0],X[:,1], c=cluster.labels_, cmap='rainbow')
plt.ylim(-33.32, -33.15)
plt.xlim(-70.82, -70.65)
#plt.show()