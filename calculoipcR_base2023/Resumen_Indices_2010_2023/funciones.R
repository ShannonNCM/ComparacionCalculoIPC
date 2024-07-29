#Funciones utiizadas para la comparación de los datos de las bases 2010 y 2023

#Funcion para leer los archivos de excel
read_ind <- function(year, indices, sheet_names) {
  df_list <- vector("list", length(indices))
  
  for (i in indices) {
    file_path <- paste0(year, "/indxbase", year, "_", i, "_2024.xlsx")
    sheet_name <- sheet_names[i]
    df_list[[i]] <- read_excel(file_path, sheet = sheet_name)
  }
  
  return(df_list)
}

