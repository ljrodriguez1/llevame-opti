import random

class Usuario:
    uid = 0

    def __init__(self, nombre: str, apellido_mat: str, apellido_pat: str, direccion: str, lat: int, lng: int, rid: int):
        self.nombre = nombre
        self.appellido_mat = apellido_mat
        self.appellido_pat = apellido_pat
        self.direccion = direccion
        self.tiempo_a = {}
        self._uid = Usuario.uid
        self.lat = lat
        self.lng = lng
        self.rid = rid
        Usuario.uid += 1
        self.maneja = False
        num = random.randint(1, 100)
        if num <= 15:
            self.maneja = True

    def calcular_tiempo(self, usuario, gmap):
        datos = gmap.distance_matrix(self.direccion, usuario.direccion)['rows'][0]['elements'][0]
        if datos['status'] == 'OK':
            dict_usuario = {
                'distancia': datos["distance"]['value'],
                'duracion': datos["duration"]['value']
            }
            self.tiempo_a.update({usuario: dict_usuario})


    def guardar_usuario(self, archivo):
        text = "{},{},{},{},'{}'\n".format(self._uid, self.nombre, self.appellido_mat, self.appellido_pat, self.direccion)
        archivo.write(text)

    def guardar_tiempo_entre(self, archivo):
        for key in self.tiempo_a.keys():
            text = "{},{},{},{}\n".format(self.rid, key.rid, self.tiempo_a[key]['distancia'], self.tiempo_a[key]['duracion'])
            archivo.write(text)
