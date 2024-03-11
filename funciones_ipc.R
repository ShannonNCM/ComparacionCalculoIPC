#Script con las funciones utilizadas para los calculos del ipc

#funcion para asignar los codigos de subclase, clase, grupo y division
cod_grupos <- function(x){
  data.frame(x %>% 
              mutate(cod_subclase = substr(cod_prod, 1, nchar(cod_prod) - 2), .before = cod_prod) %>% 
              mutate(cod_clase = substr(cod_prod, 1, nchar(cod_prod) - 3), .before = cod_subclase) %>%
              mutate(cod_grupo = substr(cod_prod, 1, nchar(cod_prod) - 4), .before = cod_clase) %>%
              mutate(cod_div = substr(cod_prod, 1, nchar(cod_prod) - 5), .before = cod_grupo))
}


#Funcion para obtener las ponderaciones de las distitas categorias
pondcat <- function(x){
  ponderaciones %>% 
    filter(tipo_grupo == x) %>% 
    select(region_id, grupo_codigo, grupo_nombre, ponderacion_region, indice_anterior) %>% 
    rename(region = region_id) %>% 
    mutate(grupo_codigo = as.character(grupo_codigo))
} 

#funcion para calcular la variacion del precio de un producto
variacion <- function(x){
  data.frame(x %>% 
              mutate(var_prod = (precio_actual/cantidad_actual)*(cantidad_anterior/precio_anterior)))
}



#funcion para generar el excel con los indices
exportarexcel <- function(archivo, ...){
  indices <- createWorkbook() # se crea el workbook
  
  nombrehojas <- c("Ind_Producto", "Ind_Subclase", "Ind_Clase", "Ind_Grupo", 
                   "Ind_Div", "Ind_Rep_Prod", "Ind_Rep_Subclase", "Ind_Rep_Clase", 
                   "Ind_Rep_Grupo", "Ind_Rep_Div","Ind_Gen", "Ind_Rep", 
                   "Incid_Prod", "Incid_Div", "Incid_Reg", "No_cotizados")
  
  for (i in 1:16) {
    addWorksheet(indices, sheetName = nombrehojas[i])
  }
  
  writeData(indices, sheet = 1, ind_prod01)
  writeData(indices, sheet = 2, ind_subclase)
  writeData(indices, sheet = 3, ind_clase)
  writeData(indices, sheet = 4, ind_grupo)
  writeData(indices, sheet = 5, ind_div)
  writeData(indices, sheet = 6, ind_rep_prod)
  writeData(indices, sheet = 7, ind_rep_subclase)
  writeData(indices, sheet = 8, ind_rep_clase)
  writeData(indices, sheet = 9, ind_rep_grupo)
  writeData(indices, sheet = 10, ind_rep_div)
  writeData(indices, sheet = 11, ind_gen)
  writeData(indices, sheet = 12, ind_rep)
  writeData(indices, sheet = 13, incid_prod)
  writeData(indices, sheet = 14, incid_div)
  writeData(indices, sheet = 15, incid_reg)
  writeData(indices, sheet = 16, prod_faltantes)
  
  saveWorkbook(indices, archivo, overwrite = TRUE)
}