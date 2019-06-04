import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('tiempo_entre_usuarios.csv')

tiempos = []
distancias = []
for num in range(len(datos)):
    if datos['tiempo'][num]/60 < 30:
        tiempos.append(datos['tiempo'][num]/60)
        distancias.append(datos['distancia'][num]/1000)

plt.scatter(tiempos, distancias)
plt.show()

