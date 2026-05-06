import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# ------------------- #
#      Graficos       #
# ------------------- #

# ---- Para latex ---- #

plt.rcParams.update({
    "pgf.texsystem": "xelatex",    # Ya que usas XeLaTeX en VSCodium
    "font.family": "serif",
    "text.usetex": True,           # <--- Esto es clave
    "pgf.rcfonts": False,          # <--- Esto evita que Matplotlib intente imponer sus fuentes
    "pgf.preamble": "\n".join([    # <--- Esto sincroniza las fuentes
         r"\usepackage{fontspec}",
         r"\setmainfont{CMU Serif}",
    ])
})

# ---- Grilla ---- #

plt.rcParams.update({
    'axes.grid':True,
    'grid.linestyle':'--',
    'grid.linewidth':0.5,
    'grid.color':'gray',
    'grid.alpha':0.5
})


# ----------------- #
#       DATOS       #
# ----------------- #

# Los salarios mensuales de los empleados de una determinada empresa, tienen la siguiente distribución:

# Salarios mensuales (en $)  Cantidad de empleados
# 800-1.000                   51
# 1.000-1.200                 87
# 1.200-1.400                 37
# 1.400-1.600                 22
# 1.600-1.800                 12
# 1.800-2.000                 6

# a) Calcular el salario mensual promedio y su desvío estándar.

# b) A partir del próximo mes se retendrán impuestos a los salarios que superen los $1.500 mensuales. Determinar el porcentaje de empleados que se verán afectados por tal retención.

# c) Debido a los continuos reclamos del personal y ante la imposibilidad de conceder un aumento general de salarios, la empresa decide otorgar un aumento de emergencia consistente en $120 mensuales que se abonarán a partir del próximo mes a los empleados que menos ganan. ¿En cuánto debe fijarse el salario máximo para obtener dicho aumento, si la empresa está dispuesta a otorgarlo únicamente al 12% de los empleados?

# d) ¿Y en cuánto debería fijarse dicho salario tope, si el sindicato negocia con la empresa y lograr que el aumento de emergencia se otorgue a la cuarte parte de los empleados?

# e) Calcular el porcentaje de empleados que recibirá este aumento de emergencia, si finalmente se acuerda fijar en $1.000 el salario tope.

# f) Calcular e interpretar los coeficientes de Asimetría y Curtosis.


# --------------------------------------------- #
#       Construcción tabla de frecuencias       #
# --------------------------------------------- #

datos_raw = "800-1.000, 1.000-1.200, 1.200-1.400, 1.400-1.600, 1.600-1.800, 1.800-2.000"

intervalos_sucios = datos_raw.split(',')

salarios_mensuales = []
for item in intervalos_sucios:
    limites = item.strip().replace('.', '').split('-')
    salarios_mensuales.append([int(limites[0]), int(limites[1])])

cant_empleados = [51, 87, 37, 22, 12, 6]

limite_inferior = []
limite_superior = []

for i in range(len(salarios_mensuales)):
    limite_inferior.append(salarios_mensuales[i][0])
    limite_superior.append(salarios_mensuales[i][1])
    

df_tabla_frecuencias = pd.DataFrame(
    {
        #'Intervalo':salarios_mensuales,
        'Li':limite_inferior,
        'Ls':limite_superior,
        'ni':cant_empleados
    }
)

# ---- ci ---- #

df_tabla_frecuencias['ci'] = (df_tabla_frecuencias['Ls'] + df_tabla_frecuencias['Li'])/2

# ---- fi ---- #

df_tabla_frecuencias['fi'] = df_tabla_frecuencias['ni']/df_tabla_frecuencias['ni'].sum()


# ---- Fi ---- #

df_tabla_frecuencias['Fi'] = df_tabla_frecuencias['fi'].cumsum()


# ---- Ni ---- # 

df_tabla_frecuencias['Ni'] = df_tabla_frecuencias['ni'].cumsum()

# --------------------------------------------- #
#          Guardar tabla de frecuencias         #
# --------------------------------------------- #

# with open('tablas/tabla_resumen.tex', 'w', encoding='utf-8') as f:
# # Usamos .style para definir el formato
#     contenido_latex = df_tabla_frecuencias.style.to_latex(
#         column_format='cccccccc',
#         caption="Resumen Estadístico de la Muestra",
#         label="tab:df_tabla_frecuencias",
#         hrules=True,  # Es la forma de la tabla
#         position="h",          # Sugiere posición "here" (aquí)
#         position_float="centering" # <--- ESTO intenta forzar el centrado en el bloque generado
#     )
#     f.write(contenido_latex)


# ------------------------------------------------- #
#       Medidas de centralización y disperción      #
# ------------------------------------------------- #

# ---- Media ---- #

media = (df_tabla_frecuencias['ci'] * df_tabla_frecuencias['ni']).sum() / df_tabla_frecuencias['ni'].sum()

# ---- desviación ---- #

n_1 = df_tabla_frecuencias['ni'].sum()

varianza = ((df_tabla_frecuencias['ni']*(df_tabla_frecuencias['ci']-media)**2)).sum()/ (df_tabla_frecuencias['ni'].sum())

desviacion = np.sqrt(varianza)


# with open('tablas/estadisticos.tex', 'w') as f:
#     f.write(f"\\newcommand{{\\media}}{{{media:.2f}}}\n")
#     f.write(f"\\newcommand{{\\desviacion}}{{{desviacion:.2f}}}\n")
#     f.write(f"\\newcommand{{\\varianza}}{{{varianza:.2f}}}\n")


# ------------------------------------- #
#       Visualizacion de los datos      #
# ------------------------------------- #

# y = df_tabla_frecuencias['ni']
# x = df_tabla_frecuencias['ci']
# ancho = df_tabla_frecuencias['Ls'] - df_tabla_frecuencias['Li']

# fig, ax = plt.subplots(figsize=(5, 5))

# ax.bar(x, y, width=ancho, alpha=0.8, color='skyblue', edgecolor='black', label='Frecuencia')
# ax.plot(x, y, color='royalblue', marker='o', linestyle='--', label='Polígono de Frecuencias')

# ax.set_title('Diagrama de la muestra')
# ax.set_xlabel('Salarios')
# ax.set_ylabel('Empleados')
# ax.legend()


# plt.savefig('./graficos/distribucion.pgf', bbox_inches='tight')


# ------------------------------------------------------- #
#       Cantidad de empleados afectados por impuestos     #
# ------------------------------------------------------- #

# Se quiere determinar el porcentaje de salarios que superen 1500 USD 
# valor objetivo >= 1500 

valor_objetivo = 1500

# ---- Interpolacion ---- #

buscar_valor = (df_tabla_frecuencias['Li'] <= valor_objetivo) & (df_tabla_frecuencias['Ls'] > valor_objetivo)

valor_encontrado = df_tabla_frecuencias[buscar_valor]

amplitud = valor_encontrado['Ls'] - valor_encontrado['Li']

interpolacion = (valor_objetivo - valor_encontrado['Li']) / amplitud * valor_encontrado['ni']

# ---- Proporcion ---- #

valores_superiores_a_objetivo = df_tabla_frecuencias['Li'] > valor_objetivo

valores_superiores = df_tabla_frecuencias[valores_superiores_a_objetivo]

proporcion = (interpolacion + valores_superiores['ni'].sum()) / df_tabla_frecuencias['ni'].sum()
porcentaje = proporcion*100

# with open('tablas/proporcion_a.tex', 'w') as f:
#     f.write(f"\\newcommand{{\\Proporción}}{{{proporcion.iloc[0]:.2f}}}\n")
#     f.write(f"\\newcommand{{\\Porcentaje}}{{{porcentaje.iloc[0]:.2f}}}\n")


# ---- Visualización ---- #

# fig, ax= plt.subplots(figsize=(3,3))

# empleados = df_tabla_frecuencias['ni'].sum()
# sometidos_a_impuestos = valores_superiores['ni'].iloc[:].sum() + interpolacion.iloc[0].sum()
# no_sometidos_a_impuestos = empleados - sometidos_a_impuestos

# titulos = ['Sometidos a impuestos', 'No sometidos a impuestos']
# valores = [sometidos_a_impuestos, no_sometidos_a_impuestos]
# desfase = (0.05, 0)

# ax.pie(
#     valores,
#     labels=titulos,
#     explode=desfase,
#     autopct ='%1.1f%%',
#     shadow =True,
#     wedgeprops ={'linewidth':1.5 ,'edgecolor':'white'},
# )

# ax.set_aspect ('equal') # Para que sea circular
# ax.set_title ('Empleados con respecto al impuesto 1500')
# plt.savefig('./graficos/empleados_respecto_impuesto_1500.pgf', bbox_inches='tight')


# ------------------------------------------------------- #
#       Cantidad de empleados que recibiran aumento       #
# ------------------------------------------------------- #

totalidad_empleados = df_tabla_frecuencias['ni'].sum()

reciben_aumento = 0.12*totalidad_empleados

# Mascara
indice_reciben_aumento = df_tabla_frecuencias[df_tabla_frecuencias['Ni'] >= reciben_aumento].index[0]

# Datos
limite_inferior_recibir_aumento = df_tabla_frecuencias['Li'].iloc[indice_reciben_aumento]
limite_superior_recibir_aumento = df_tabla_frecuencias['Ls'].iloc[indice_reciben_aumento]

amplitud = limite_superior_recibir_aumento-limite_inferior_recibir_aumento

# Para obtener la cantidad acumulada anterior
cantidad_acumulada_anterior = None
if indice_reciben_aumento == 0:
    cantidad_acumulada_anterior = 0
else:
    cantidad_acumulada_anterior = df_tabla_frecuencias['Ni'].iloc[(indice_reciben_aumento-1)]

# Interpolacion
interpolacion_p12 = limite_inferior_recibir_aumento + (
    (reciben_aumento-cantidad_acumulada_anterior)/df_tabla_frecuencias['ni'].iloc[indice_reciben_aumento]
    )*amplitud


# ------------- Caso sindicato consiga 25%  ------------- #

aumento_sindicato = 0.25*totalidad_empleados

# Mascara
indice_aumento_sindical = df_tabla_frecuencias[df_tabla_frecuencias['Ni']>=aumento_sindicato].index[0]

# Datos
limite_inferior_sindical = df_tabla_frecuencias['Li'].iloc[indice_aumento_sindical]
limite_superior_sindical = df_tabla_frecuencias['Ls'].iloc[indice_aumento_sindical]

amplitud = limite_superior_sindical - limite_inferior_sindical

# Cantidad acumulada anterior
cantidad_acumulada_anterior_sindical = None
if indice_aumento_sindical == 0:
    cantidad_acumulada_anterior_sindical = 0
else:
   cantidad_acumulada_anterior_sindical = df_tabla_frecuencias['Ni'].iloc[indice_aumento_sindical-1]

# Interpolacion 25
interpolacion_p25 = limite_inferior_sindical + (
    (aumento_sindicato-cantidad_acumulada_anterior_sindical)
    / df_tabla_frecuencias['ni'].iloc[indice_aumento_sindical]
    * amplitud
)

# ------------- Salario Tope 1000  ------------- #

salario_menor_a_1000 = df_tabla_frecuencias[df_tabla_frecuencias['Ls']<= 1000].index[-1]
porcentaje_menor_mil = df_tabla_frecuencias['Ni'].iloc[salario_menor_a_1000]/totalidad_empleados * 100

with open('tablas/aumento_salario.tex', 'w') as f:
    f.write(f"\\newcommand{{\\InterpolacionPdoce}}{{{interpolacion_p12:.2f}}}\n")
    f.write(f"\\newcommand{{\\InterpolacionPveinticinco}}{{{interpolacion_p25:.2f}}}\n")
    f.write(f"\\newcommand{{\\PorcentajeMenorAMil}}{{{porcentaje_menor_mil:.2f}}}\n")

# ------------- Percentil 75%  ------------- #

cantidad_p75 = 0.75*totalidad_empleados

# Mascara
indice_p75 = df_tabla_frecuencias[df_tabla_frecuencias['Ni']>=cantidad_p75].index[0]

# Datos
limite_inferior_p75 = df_tabla_frecuencias['Li'].iloc[indice_p75]
limite_superior_p75 = df_tabla_frecuencias['Ls'].iloc[indice_p75]

amplitud = limite_superior_p75 - limite_inferior_p75

# Cantidad acumulada anterior
cantidad_acumulada_anterior_p75 = None
if indice_p75 == 0:
    cantidad_acumulada_anterior_p75 = 0
else:
   cantidad_acumulada_anterior_p75= df_tabla_frecuencias['Ni'].iloc[indice_p75-1]

# Interpolacion 75
interpolacion_p75 = limite_inferior_p75 + (
    (cantidad_p75-cantidad_acumulada_anterior_p75)
    / df_tabla_frecuencias['ni'].iloc[indice_p75]
    * amplitud
)


# ---- Visualización ---- #

# Datos:
# valor_minimo = df_tabla_frecuencias['Li'].iloc[0]
# valor_maximo = df_tabla_frecuencias['Ls'].iloc[-1]
# interpolacion_p50 = media

# stats = [{
#     'label': 'Salarios Empleados',
#     'whislo': valor_minimo,    # Bigote inferior (mínimo)
#     'q1':     interpolacion_p25,                  # Borde inferior caja (P25)
#     'med':    interpolacion_p50,                  # Línea central (Mediana)
#     'q3':     interpolacion_p75,                  # Borde superior caja (P75)
#     'whishi': valor_maximo,    # Bigote superior (máximo)
#     'fliers': [] 
# }]

# fig, ax = plt.subplots(figsize=(4, 4))
# ax.bxp(stats)

# plt.axhline(interpolacion_p12, color='red', linestyle='--', label=f'P12: {interpolacion_p12:.2f}')
# plt.axhline(interpolacion_p25, color='green', linestyle='--', label=f'P25: {interpolacion_p25:.2f}')

# plt.legend()
# plt.title("Distribución Salarial basada en Intervalos")
# plt.ylabel("Salario")
# plt.savefig('./graficos/aument_salaral.pgf', bbox_inches='tight')



# ------------------------------------ #
#       coeficiente de asimetría       #
# ------------------------------------ #

# ---- Fisher ---- #

coeficiente_fisher_numerador = (df_tabla_frecuencias['ni']*(df_tabla_frecuencias['ci']-media)**3).sum()

coeficiente_fisher_denominador = totalidad_empleados*desviacion**3

coeficiente_fisher = coeficiente_fisher_numerador/coeficiente_fisher_denominador

if coeficiente_fisher > 0:
    tipo_fisher = 'Asimetria positiva'
elif coeficiente_fisher < 0:
    tipo_fisher = 'Asimetria negativa'
elif coeficiente_fisher == 0:
    tipo_fisher = 'Simetrica'

# ---- Pearson ---- #

indice_moda = np.where(df_tabla_frecuencias['ni'] == df_tabla_frecuencias['ni'].max())
indice_moda = indice_moda[0][0]

aj = df_tabla_frecuencias['Li'].iloc[indice_moda]
aj_1 = df_tabla_frecuencias['Ls'].iloc[indice_moda]

if indice_moda == 0:
    n_anterior = 0
else: 
    n_anterior = df_tabla_frecuencias['ni'].iloc[indice_moda-1]

n_siguiente = df_tabla_frecuencias['ni'].iloc[indice_moda+1]

# Gammas
gamma_1 = df_tabla_frecuencias['ni'].iloc[indice_moda]-n_anterior
gamma_2 = df_tabla_frecuencias['ni'].iloc[indice_moda]-n_siguiente

moda = aj+(gamma_1/(gamma_1+gamma_2))*(aj_1-aj)

coeficiente_pearson = (media-moda)/desviacion

if coeficiente_pearson > 0:
    tipo_pearson = 'Sesgo a la derecha'
elif coeficiente_pearson < 0:
    tipo_pearson = 'Sesgo a la izquierda'
elif coeficiente_pearson == 0:
    tipo_pearson = 'Simetrica'


# ----------------------------------- #
#       coeficiente de curtosis       #
# ----------------------------------- #

numerador_curtosis = (df_tabla_frecuencias['ni']*(df_tabla_frecuencias['ci']-media)**4).sum()

denominador_curtosis = totalidad_empleados * (desviacion**4)

coeficiente_curtosis = (numerador_curtosis/denominador_curtosis)

if coeficiente_curtosis > 0:
    tipo_curtosis = 'Leptocurtica'
elif coeficiente_curtosis < 0:
    tipo_curtosis = 'Platicurtica'
elif coeficiente_curtosis == 0:
    tipo_curtosis = 'Mesocurtica'



with open('tablas/coeficientes.tex', 'w') as f:
    # Fisher
    f.write(f"\\newcommand{{\\CoeficienteFisherTipo}}{{{tipo_fisher}}}\n")
    f.write(f"\\newcommand{{\\CoeficienteFisher}}{{{coeficiente_fisher:.2f}}}\n")
    # Pearson
    f.write(f"\\newcommand{{\\CoeficientePearsonTipo}}{{{tipo_pearson}}}\n")
    f.write(f"\\newcommand{{\\CoeficientePearson}}{{{coeficiente_pearson:.2f}}}\n")
    # Curtosis
    f.write(f"\\newcommand{{\\CoeficienteCurtosisTipo}}{{{tipo_curtosis}}}\n")
    f.write(f"\\newcommand{{\\CoeficienteCurtosis}}{{{coeficiente_curtosis:.2f}}}\n")

