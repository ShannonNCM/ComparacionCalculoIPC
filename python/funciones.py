import pandas as pd

#Funciones utilizadas para realizar el calculo

#funcion para asignar los codigos de subclase, clase, grupo y division
def pondcat(x, ponderaciones):
    grupo = ponderaciones[ponderaciones['tipo_grupo'] == x]
    newdata = grupo[['region_id', 'grupo_codigo', 'grupo_nombre', 'ponderacion_region', 'indice_anterior']]
    newdata = newdata.rename(columns={'region_id': 'region'})
    newdata['grupo_codigo'] = newdata['grupo_codigo'].astype(str)
    return newdata

def variacion(x):
    x['var_prod'] = (x['precio_actual'] / x['cantidad_actual']) * (x['cantidad_anterior'] / x['precio_anterior'])
    return x

def cod_grupos(x):
    x['cod_subclase'] = x['cod_prod'].str.slice(stop=-2)
    x['cod_clase'] = x['cod_prod'].str.slice(stop=-3)
    x['cod_grupo'] = x['cod_prod'].str.slice(stop=-4)
    x['cod_div'] = x['cod_prod'].str.slice(stop=-5)
    return x

#funcion para calcular los indices de cada grupo por region
def indices(x, y):
    indice = x[['region', y, 'grupo_nombre', 'ponderacion_region', 'ind_prod']].rename(columns={y: 'grupo_codigo'}).groupby(['region', 'grupo_codigo']).apply(lambda x: pd.Series({
            'sum1': (x['ind_prod'] * x['ponderacion_region']).sum(),
            'sum2': x['ponderacion_region'].sum()
        })).reset_index()

    indice['ind'] = indice['sum1'] / indice['sum2']
    indice = indice[['region', 'grupo_codigo', 'ind']]

    return indice

#funcion para calcular los indices de cada grupo a nivel republica
def indicerep(df, y):
    indice = df.groupby(y).apply(lambda x: pd.Series({
        'sum1': (x['ponderacion_region'] * x['ind_prod']).sum(),
        'sum2': x['ponderacion_region'].sum()
    })).reset_index()

    indice['ind_prod_rep'] = indice['sum1'] / indice['sum2']
    indice.dropna(inplace=True)
    indice = indice[[y, 'ind_prod_rep']]

    return indice

#funcion para calcular el indice por region a nivel nacional
def indicenac(df):
    indice = df.groupby('region').apply(lambda x: pd.Series({
        'sum1': (x['ponderacion_region'] * x['ind_prod']).sum(),
        'sum2': x['ponderacion_region'].sum()
    })).reset_index()

    indice['ind_prod_rep'] = indice['sum1'] / indice['sum2']
    indice.dropna(inplace=True)
    indice = indice[['region', 'ind_prod_rep']]

    return indice

