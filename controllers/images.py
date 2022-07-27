from asyncio.windows_events import NULL
import pandas as pd
from flask.json import dump, load


persona  = pd.read_csv(".\data.csv")



registros = pd.read_csv(".\datos_registro.csv")


def get_data():
    return persona

def guardar_datos(data):
    # datos = {'ID':[id],'Etnia':[etnia],'Afro-American_percentage':[a],'European_percentage':[e],'Indigenous_percentage':[i]}
    #registros = registros.append(datos, ignore_index=True)
    df = pd.DataFrame(data)
    df.to_csv(".\datos_registro.csv",index=False,mode="a",header=False, na_rep="\n")

def get_registro():
    return pd.read_csv(".\datos_registro.csv")