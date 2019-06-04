from gurobipy import *
from clustering import cluster
from main import cargarUsuarios
import pandas as pd

for i in range(10000):
    print("----------------------------------",i)
    usuarios1 = cargarUsuarios('usuarios_validos4.csv')
    #print(cluster.labels_)

    grupos = {x:[] for x in range(5)}
    for i in range(len(usuarios1)):
        grupos[cluster.labels_[i]].append(usuarios1[i])




    usuarios = [x.rid for x in grupos[2]]
    vehiculos = [x.rid for x in grupos[2] if x.maneja]

    #print(usuarios)
    #print(vehiculos)

    data = pd.read_csv('tiempo_entre_usuarios.csv')
    Tji = {x: {} for x in range(69)}
    for user in range(69):
        for num in range(len(data)):
            if data['id1'][num] == user:
                Tji[user].update({data['id2'][num]: data['tiempo'][num]})



    TOT = len(usuarios)
    CD = 5 * len(vehiculos)

    Cantidad_usuarios = int(min(TOT, CD))
    print(Cantidad_usuarios, len(vehiculos))
    print(vehiculos)

    m = Model("")
    x_vi = m.addVars(vehiculos, usuarios, vtype=GRB.BINARY, name="autos")
    y_vij = m.addVars(vehiculos, usuarios, usuarios, vtype=GRB.BINARY, name="orden")

    m.addConstrs((quicksum(x_vi[car, user] for car in vehiculos) <= 1 for user in usuarios), name="1")

    m.addConstrs((quicksum(x_vi[car, user] for user in usuarios) <= 5 for car in vehiculos), name="2")

    m.addConstrs((x_vi[auto, auto] == 1 for auto in vehiculos), name="3")

    m.addConstr((quicksum(x_vi[car, user] for user in usuarios for car in vehiculos) == Cantidad_usuarios), name="4")

    m.addConstrs((quicksum(y_vij[auto, user, user2] for user in usuarios if user != user3) >= y_vij[auto, user2, user3] for user3 in usuarios
                  for user2 in usuarios for auto in vehiculos if user2 != auto))

    m.addConstrs((quicksum(y_vij[auto, user1, user2] for user1 in usuarios) == x_vi[auto, user2] for user2 in usuarios for auto in vehiculos if auto != user2))
    #m.addConstrs((quicksum(y_vij[auto, user2, user1] for user2 in usuarios) == x_vi[auto, user1] for user1 in usuarios for auto in vehiculos))

    m.addConstrs((quicksum(y_vij[auto, auto, user] for user in usuarios) == 1 for auto in vehiculos))

    m.addConstrs(quicksum(y_vij[auto, user, user] for auto in vehiculos) == 0 for user in usuarios)

    #m.addConstrs(quicksum(y_vij[auto, user, auto1] for auto in vehiculos for user in usuarios) == 0 for auto1 in vehiculos)

    m.addConstrs(quicksum(y_vij[auto, user, user2] for user2 in usuarios for auto in vehiculos) <= 1 for user in usuarios)

    obj = quicksum(y_vij[car, user1, user2] * Tji[user1][user2] for user1 in usuarios for user2 in usuarios for car in vehiculos)

    m.setObjective(obj, GRB.MINIMIZE)

    m.optimize()
for v in m.getVars():
    if v.X == 1:
        print(v)
