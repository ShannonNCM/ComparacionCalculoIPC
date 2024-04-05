#Funciones utilizadas para realizar el calculo

#funcion para asignar los codigos de subclase, clase, grupo y division
def pondcat(x, ponderaciones):
    grupo = ponderaciones[ponderaciones['tipo_grupo'] == x]
    newdata = grupo[['region_id', 'grupo_codigo', 'grupo_nombre', 'ponderacion_region', 'indice_anterior']]
    newdata = newdata.rename(columns={'region_id': 'region'})
    newdata['grupo_codigo'] = newdata['grupo_codigo'].astype(str)
    return newdata