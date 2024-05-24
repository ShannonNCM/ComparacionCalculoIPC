'''Funciones usadas en el jupyternb para la realizacion de graficas de comparacion'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

meses = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

def grafica(datos, nombre_mes, tipo : str, anio):
    ax = datos.plot(kind='barh', x='ArtNom', y='Cant_2023', legend=True, color='#629fca', position=0, width=0.4)
    datos.plot(kind='barh', x='ArtNom', y='Cant_2024', legend=True, color='lightcoral', ax=ax, position=1, width=0.4)
    ax.invert_yaxis()
    ax.set_ylabel('')  # Remove y-axis label
    plt.xlabel('Cantidad')
    plt.title(f'Articulos {tipo} recopilados respecto a {nombre_mes} {anio}')
    plt.yticks(fontsize=7)
    plt.legend(['2023', '2024'])

reg_cods = ['01', '02', '03', '04', '05', '06', '07', '08']

def grafreg(regcod, contreg01, contreg02, nombre_mes, anio, numero):
    #aqui filtramos las regiones de cada conjunto que tiene los conteos de los articulos
    reg01 = contreg01[contreg01['RegCod'] == regcod]
    reg02 = contreg02[contreg02['RegCod'] == regcod]
    #se generan dataframes donde estan los 20 articulos mas frecuentes y los 20 menos frecuentes con respecto al año anterior
    topreg = pd.merge(reg01, reg02, on=['ArtNom', 'RegCod'], how='inner', suffixes=('_2023', '_2024')).fillna(0).head(numero).sort_values(by='Cant_2023', ascending=False)
    lastreg = pd.merge(reg01, reg02, on=['ArtNom', 'RegCod'], how='inner', suffixes=('_2023', '_2024')).fillna(0).tail(numero).sort_values(by='Cant_2023', ascending=False)
    
    #esta es la funcion que se utiiza para graficar los datos para cada region
    def grafica(datos, nombre_mes, tipo: str, anio):
        ax = datos.plot(kind='barh', x='ArtNom', y='Cant_2023', legend=True, color='#629fca', position=0, width=0.4)
        datos.plot(kind='barh', x='ArtNom', y='Cant_2024', legend=True, color='lightcoral', ax=ax, position=1, width=0.4)
        ax.invert_yaxis()
        ax.set_ylabel('')  # Remove y-axis label
        plt.xlabel('Cantidad')
        plt.title(f'Articulos {tipo} recopilados en la región {regcod} respecto a {nombre_mes} {anio}')
        plt.yticks(fontsize=7)
        plt.legend(['2023', '2024'])

    #se grafican los mas frecuentes
    grafica(topreg, nombre_mes, 'mas', anio)
    #se grafican los menos frecuentes
    grafica(lastreg, nombre_mes, 'menos', anio)