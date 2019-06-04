from parametros import *
import googlemaps
import pandas as pd
from usuarios import Usuario
import requests
import random

def cargarUsuarios(path):
    dataUsuarios = pd.read_csv(path)

    #print(dataUsuarios.keys())

    usuarios = []

    for num in range(len(dataUsuarios)): #range(len(dataUsuarios))
        nombre = dataUsuarios['nombre'][num]
        appellido_mat = dataUsuarios['apellido_mat'][num]
        appellido_pat = dataUsuarios['apellido_pat'][num]
        direccion = dataUsuarios['direccion'][num]
        lat = dataUsuarios['lat'][num]
        lng = dataUsuarios['lng'][num]
        real_uid = dataUsuarios['id'][num]
        if isinstance(direccion, str):
            usuarios.append(Usuario(nombre, appellido_mat, appellido_pat, direccion, lat, lng, real_uid))
    return usuarios

def calcular_distancia(usuarios):
    gmaps = googlemaps.Client(key=API_KEY)
    for usuario1 in usuarios:
        for usuario2 in usuarios:
            usuario1.calcular_tiempo(usuario2, gmaps)
            pass

    maxLenght = max(len(x.tiempo_a) for x in usuarios)

    usuariosValidos = []
    for usuario in usuarios:
        if len(usuario.tiempo_a) == maxLenght:
            usuariosValidos.append(usuario)

    with open('usuarios_validos.csv', 'w', encoding='utf-8') as file:
        for usuario in usuariosValidos:
            usuario.guardar_usuario(file)

    with open('tiempo_entre_usuarios.csv', 'w', encoding='utf-8') as file:
        for usuario in usuariosValidos:
            usuario.guardar_tiempo_entre(file)


def aCordenadas(path):

    GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

    usuarios = pd.read_csv(path)
    print(usuarios.keys())
    with open('usuarios_validos3.csv', 'w', encoding='utf-8') as file:
        file.write('id,nombre,apellido_mat,apellido_pat,direccion,lat,lng\n')
        print(len(usuarios))
        for num in range(len(usuarios)):
            print(num)
            direccion = usuarios['direccion'][num]
            params = {
                'address': direccion,
                'region': 'chile',
                'key': API_KEY
            }
        # Do the request and get the response data
            req = requests.get(GOOGLE_MAPS_API_URL, params=params)
            res = req.json()

            # Use the first result
            result = res['results'][0]
            geodata = dict()
            geodata['lat'] = result['geometry']['location']['lat'] + random.randint(-100, 100)/50000
            geodata['lng'] = result['geometry']['location']['lng'] + random.randint(-100, 100)/50000
            geodata['address'] = result['formatted_address']
            nombre = usuarios['nombre'][num]
            apellido_mat = usuarios['apellido_mat'][num]
            apellido_pat = usuarios['apellido_pat'][num]

            file.write('{},{},{},{},"{}",{},{}\n'.format(num, nombre, apellido_mat, apellido_pat, geodata['address'], geodata['lat'], geodata['lng']))

#aCordenadas('usuarios_validos2.csv')

#gmaps = googlemaps.Client(key=API_key)
#data = gmaps.distance_matrix('camino punta de aguila 4307', 'alonso de cordova 2860')['rows'][0]['elements'][0]

#print(data)