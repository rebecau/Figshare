from asyncio.windows_events import NULL
from numpy import rint
import pandas as pd
from flask.json import dump, load
from itertools import chain


persona  = pd.read_csv(".\data.csv")


registros = pd.read_csv("..\datos_registro.csv")


def get_data():
    return persona

def guardar_datos(data):
    df = pd.DataFrame(data)
    df.to_csv(".\datos_registro.csv",index=False,mode="a",header=False, na_rep="\n")

def get_registro():
    return pd.read_csv("..\datos_registro.csv")

def get_ind():
    data = get_registro()
    indigenas = data[data["Etnia"].str.contains("Indigena")]
    return indigenas

def get_afro():
    data = get_registro()
    afroecuatorianos = data[data["Etnia"].str.contains("Afroecuatoriano")]
    return afroecuatorianos

def get_mez():
    data = get_registro()
    meztizo = data[data["Etnia"].str.contains("Meztizo")]
    return meztizo

def get_eur():
    data = get_registro()
    eurodesendiente =data[data["Etnia"].str.contains("EuroDesendiente")]
    return eurodesendiente

indigena = get_ind()

new_df = indigena.groupby(indigena["ID"])
for group in new_df:
    # df = pd.DataFrame(lista, columns=['ID', 'ETNIA','A', 'E','I'])
    valor=str(group[1])
    valor = " ".join(valor.split())
    lista = valor.split(" ")
    lista = lista[5:]
    matriz = []
    vec = []
    for i in range(len(lista)):
        if i % 6 == 0:
            matriz.append(vec)
            vec=[]
        vec.append(lista[i])
    #     vec=[]
    #     if i > 7:
    #         if i % 7 == 0:
    #             matriz.append(vec)
    #             vec=[]
    #         vec.append(lista[i])
            
    if vec != []:
        matriz.append(vec)
    matriz.pop(0)
    print(matriz)

    # # df = list(chain.from_iterable(matriz))
    # df = pd.DataFrame(matriz)
    # print(df)
    # print(df[2].mean())
    print("######################")
