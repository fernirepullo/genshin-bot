import pandas as pd

pd.set_option('display.max_colwidth', None)

df_infoPersonaje = pd.read_csv("infoPersonaje.csv")


def getPersonaje():
    ar = []

    nombre = input("Introduzca el nombre: ")

    if nombre == "":
        print("No ha introducido el nombre")

    else:
        loc_Personaje = df_infoPersonaje.loc[df_infoPersonaje['Personaje'] == nombre]
        print(loc_Personaje)

    return ar


getPersonaje()
