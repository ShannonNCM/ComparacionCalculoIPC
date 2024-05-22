'''Funciones usadas en el jupyternb para la realizacion de graficas de comparacion'''

import matplotlib.pyplot as plt

meses = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

def grafica(datos, nombre_mes, tipo : str, anio):
    ax = datos.plot(kind='barh', x='ArtNom', y='Cant_2023', legend=True, color='skyblue', position=0, width=0.4)
    datos.plot(kind='barh', x='ArtNom', y='Cant_2024', legend=True, color='orange', ax=ax, position=1, width=0.4)
    ax.invert_yaxis()
    ax.set_ylabel('')  # Remove y-axis label
    plt.xlabel('Cantidad')
    plt.title(f'Articulos {tipo} frecuentes respecto a {nombre_mes} {anio}')
    plt.yticks(fontsize=7)
    plt.legend(['2023', '2024'])