import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ~~~~~~~~~~~~~~~~~~~ #
#       Imports       #
# ~~~~~~~~~~~~~~~~~~~ #
import cabina_vivo

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

cantidad_supervivientes_cabina = cabina_vivo.cantidad_sobrevivientes(df_titanic_general[['deck','survived']])

sobrevive_cabina, no_sobrevive_cabina = cantidad_supervivientes_cabina
print(sobrevive_cabina)

print((df_titanic_general['survived'] == 1).sum())
print((df_titanic_general['survived'] == 0).sum())