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

#funcion para calcular los indices de cada grupo
def indices(nd_prod, cod_subclase):
    result = nd_prod[['region', cod_subclase, 'grupo_nombre', 'ponderacion_region', 'ind_prod']].rename(columns={cod_subclase: 'grupo_codigo'}).groupby(['region', 'grupo_codigo']).apply(lambda x: pd.Series({
            'sum1': (x['ind_prod'] * x['ponderacion_region']).sum(),
            'sum2': x['ponderacion_region'].sum()
        })).reset_index()

    result['ind'] = result['sum1'] / result['sum2']
    result = result[['region', 'grupo_codigo', 'ind']]

    return result