import matplotlib as mp
import pandas as pd


def load_file():
    # load data from file and manage dtypes
    df_fishing = pd.read_csv("captura-puerto-flota-2019.csv",
                            sep=",", encoding="latin1",
                            thousands=".")
    df_fishing["fecha"] = pd.to_datetime(df_fishing["fecha"])
    return df_fishing

def sum_by_month(dataframe):
    # filter colums
    df = dataframe[["fecha", "captura"]]
    
    # group by month
    df = df.groupby("fecha").sum()
    df.sort_values(by="captura", ascending=False, inplace=True)
    df = df[0:20]
    df.sort_values(by="fecha", ascending=True, inplace=True)
    df = df.to_dict()
    df = df["captura"]

    # swap dict names
    name_swap = {'2019-02-01 00:00:00':"february", '2019-01-01 00:00:00': "january",
                 '2019-08-01 00:00:00': "august", '2019-07-01 00:00:00': "july",
                 '2019-06-01 00:00:00': "june", '2019-10-01 00:00:00': "octuber",
                 '2019-04-01 00:00:00': "april", '2019-03-01 00:00:00': "march",
                 '2019-05-01 00:00:00': "may", '2019-09-01 00:00:00': "september",
                 '2019-11-01 00:00:00': "november"}
    df_swaped = {}

    for i in df.keys():
        try:
            df_swaped[name_swap[str(i)]] = df[i]
        except:
            df_swaped[i] = df[i]
    return df_swaped

def sum_by_species(dataframe):
    # filter colums
    df = dataframe[["especie", "captura"]]

    # group by species
    df = df.groupby("especie").sum()
    df.sort_values(by="captura", ascending=False, inplace=True)
    df = df[0:20].to_dict()
    return df["captura"]

def sum_by_state(dataframe):
    # filter colums
    df = dataframe[["provincia", "captura"]]
    
    # group by state
    df = df.groupby("provincia").sum()
    df = df.to_dict()
    return df["captura"]

def sum_by_port(dataframe):
    # filter colums
    df = dataframe[["puerto", "captura"]]
    
    # group by state
    df = df.groupby("puerto").sum()
    df = df.to_dict()
    return df["captura"]


df = load_file()
CAPTURE_BY_MONTH = sum_by_month(df)
CAPTURE_BY_SPECIES = sum_by_species(df)
CAPTURE_BY_STATE = sum_by_state(df)
CAPTURE_BY_PORT = sum_by_port(df)
SIDEBAR_TEXT = """Análisis de Desembarque de
Captura Marítima
(Período 2019)


El presente dashboard presenta
un análisis detallado del
desembarque de captura
marítima en Argentina durante
el año 2019.
La información provista abarca
diversos aspectos, incluyendo
el mes, puerto, estado y
especie de las capturas,
ofreciendo una visión integral
de la actividad pesquera en
aguas marítimas.

-------------------------------------------------
Licencia: Creative Commons
Attribution 4.0.
-------------------------------------------------
Frecuencia de Actualización:
Mensualmente.
-------------------------------------------------
Mantenedor: Dirección Nacional
de Coordinación y
Fiscalización Pesquera.
-------------------------------------------------
Fecha de Publicación Inicial:
23 de octubre de 2019.
-------------------------------------------------
Última Actualización: 29 de
noviembre de 2023.
-------------------------------------------------
Página de Referencia:
https://datos.magyp.gob.ar
-------------------------------------------------
"""


if __name__ == "__main__":
    df = load_file()
    print(sum_by_month(df))
    print(sum_by_species(df))