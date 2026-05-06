import math
import numpy as np
from scipy.stats import norm

# Distribucion binimial

def comb (n, x):
    combinatoria = math.comb(n, x)
    return combinatoria

def calc_binom (comb,n, x, p, q):
    formula_binomial = comb * (p)**x * (q)**(n-x)
    return formula_binomial

n = 7
x = ...
p = 0.4
q = 0.6

valores = []

# for x in range (n+1):
#     calculo = calc_binom(comb(n, x), n, x, p, q)
#     valores.append(calculo)

# ---- Ejemplo ---- #

# P (15-6<X)
# p_valor = 0
# for valor in range(len(valores)):
#     if valor >= (15-6):
#         p_valor += valores[valor]
    
# print(p_valor)

# p_valor = 0
# for valor in range(len(valores)):
#     if valor == 3:
#         p_valor += valores[valor]
    
# print(p_valor)

# ---- Medidas de tendencia central ---- #

# media = n * p
# desvio = math.sqrt(n*p*q)

# print(media, desvio)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#           Hipergeometrica             #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# def calc_hipergeometrica(k, x, N, n):
#     numerador = math.comb(k, x) * math.comb((N-k),(n-x))
#     denominador = math.comb(N, n)
#     return (numerador/denominador)

# k = 4
# x = 3
# N = 10
# n = 7

# resultado = calc_hipergeometrica(k, x, N, n)
# print(resultado)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#           Normal            #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

media = 0.60
desvio = 0.15

# p_condicion = 1 - norm.cdf(0.51, loc=media, scale=desvio)

# p_interseccion = norm.cdf(0.90, loc=media, scale=desvio) - norm.cdf(0.51, loc=media, scale=desvio)

# resultado_final = p_interseccion / p_condicion

resultado_final = norm.cdf(0.99, loc=media, scale=desvio)

print(resultado_final)
