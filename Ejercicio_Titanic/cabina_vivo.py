import pandas as pd
import scipy.stats as stats

def cantidad_sobrevivientes(dataset):
    filtrado = dataset['deck'].notnull() == True
    con_cabina = dataset[filtrado]
    sobrevivio = (con_cabina['survived'] == 1).sum()
    no_sobrevivio = (con_cabina['survived'] == 0).sum()
    return sobrevivio, no_sobrevivio

# def proporcion_sobrevivientes(sobrevivientes, no_sobrevivientes, cantidad_total, sobrevivientes_totales):
#     proporcion_cabina = ((math.comb(sobrevivientes_totales, sobrevivientes) * 
#         math.comb((cantidad_total-sobrevivientes_totales), ((sobrevivientes+no_sobrevivientes)-sobrevivientes)))/
#         math.comb(cantidad_total, (sobrevivientes+no_sobrevivientes)))
#     return proporcion_cabina

def prueba_independencia(dataset_cabina, dataset_supervivencia):
    tabla = pd.crosstab(dataset_cabina, dataset_supervivencia)
    chi2,p_valor,dof,esperados = stats.chi2_contingency(tabla)
    return p_valor

def por_categoria(dataset):
    dataset = dataset.dropna()
    grupos = dataset.groupby(['deck','survived']).size()
    return(grupos)
