import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ~~~~~~~~~~~~~~~~~~~~~~~~~ #
#       Carga Dataset       #
# ~~~~~~~~~~~~~~~~~~~~~~~~~ #

df_titanic_general = sns.load_dataset('titanic')


# ------ Informacion del dataset ------- #

# df_titanic_info = pd.DataFrame({
#     'Column':df_titanic_general.columns.str.replace('_', r'\_', regex=False),
#     'Not-Null':df_titanic_general.count().values,
#     'Type':df_titanic_general.dtypes.values
# })

# with open('Documento/Tablas/tabla_info.tex', 'w', encoding='utf-8') as f:
#     contenido_latex = df_titanic_info.style.to_latex(
#         column_format='cccc',
#         caption="Informacion sobre los contenidos de cada columna",
#         label="tab:df_tabla_metodo_info",
#         hrules=True,  # Es la forma de la tabla
#         position="h",          # Sugiere posición "here" (aquí)
#         position_float="centering" # <--- ESTO intenta forzar el centrado en el bloque generado
#     )
#     f.write(contenido_latex)


# ---- Ver si cabina es importante ---- #

# Creamos el dataset solo con la cabina y si sobrevivieron
df_titanic_cabina = df_titanic_general[['deck','survived']]

# Creamos una mascara para ver los que tienen informacion en cuanto a df_tenia_cabina:
filtrado_por_cabina = df_titanic_cabina['deck'].notnull() == True

# Data frame en caso que 'Si' sobrevivio
df_tenia_cabina = df_titanic_cabina[filtrado_por_cabina]


df_con_cabina_sobrevivio = (df_tenia_cabina['survived'] == 1).sum()
df_con_cabina_no_sobrevivio = (df_tenia_cabina['survived'] == 0).sum()

print(df_con_cabina_sobrevivio,df_con_cabina_no_sobrevivio) 