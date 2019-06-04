from gmplot import *
from parametros import *
import pandas as pd

usuarios = pd.read_csv('usuarios_validos3.csv')
print(len(usuarios))
gmap = gmplot.GoogleMapPlotter(usuarios['lat'][0], usuarios['lng'][0], 5)
#gmap.scatter(usuarios['lat'], usuarios['lng'], '# FF0000', size=40, marker=False)
#gmap.draw('map1.html')
