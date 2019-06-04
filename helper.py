from main import cargarUsuarios, calcular_distancia

def helper1():
    with open('usuarios_validos.csv') as file:
        data = []
        for line in file:
            data.append(line.rstrip('\n').split(','))

    with open('usuarios_validos2.csv', 'w') as file:
        for dato in data:
            file.write('{},{},{},{},"{}"\n'.format(dato[0], dato[1], dato[2], dato[3], ','.join(dato[4: len(dato)])))

def clean_data_id(path):
    usuarios = cargarUsuarios(path)
    for i in usuarios:
        print(i.nombre, i._uid, i.rid)





#calcular_distancia(cargarUsuarios('usuarios_validos4.csv'))

