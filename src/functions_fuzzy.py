
from math import e, pow, sin

import numpy as np

def func_nao_linear(x):
    return np.exp(-x/5) + 0.5 * np.sin(x)




def parametrosGaussiana(valores):
    sigmazinho = round((valores[-1] - valores[0])/3, 1)

    centro = round(valores[1], 1)

    return sigmazinho, centro


def Triangular(x, a, b, c):

    nao_SAT_error = ValueError("Os valores de a, b e c geram Insatisfazibilidade da função triângular") 

    x = asarray(x)              #Garantindo que o valor de x passado será um array, mesmo que seja um único valor
    
    if a <= b <= c:
        if x <= a or x >= c:        #  x <= a  OU  x >= c 
            return 0
        elif x <= b and x >= a:     # a <= x <= b
            return (x - a)/(b - a)
        elif  x >= b and x <= c:    # b <= x <= c
            return (c - x)/(c - b)
        else:
            raise nao_SAT_error
    
    else:
        raise nao_SAT_error

def trapezoidal(x, a, b, c, d):
    """
    Calcula a pertinência trapezoidal para UM valor ou VÁRIOS valores de x.
    Funciona com números individuais E arrays do numpy!
    """

    x = np.array(x) if type(x) == list else x

    # Inicializa o resultado com zeros
    result = np.zeros_like(x)
    
    # Região de subida (a < x < b)
    mask = (x > a) & (x < b)
    result[mask] = (x[mask] - a) / (b - a)
    
    # Região do topo (b <= x <= c)
    mask = (x >= b) & (x <= c)
    result[mask] = 1.0
    
    # Região de descida (c < x < d)
    mask = (x > c) & (x < d)
    result[mask] = (d - x[mask]) / (d - c)
    
    return result
def Trapezoidal(x, a, b, c, d):
    
    # if type(x) == list:
    #     print("aqui!!")
    #     return minimum(maximum(minimum((x - a)/(b - a), 1), maximum(minimum((d - x)/(d - c), 1), 0)))

    nao_SAT_error = ValueError("Os valores de a, b e c geram Insatisfazibilidade da função Trapezoidal") 

    # x = asarray(x)              #Garantindo que o valor de x passado será um array, mesmo que seja um único valor
    
    if a <= b <= c:        
        if x <= a or x >= d:        #  x <= a 
            return 0
        elif x <= b and x >= a:     # a <= x <= b
            return (x - a)/(b - a)
        elif x <= b and x <= c:
            return 1
        elif  x >= c and x <= d:    # b <= x <= c
            return (d - x)/(d - c)
        else:
            raise nao_SAT_error

    else:
    # a <= b <= c
        raise nao_SAT_error


def Gaussiana(x, sigmazinho, c):


    nao_SAT_error = ValueError("Os valores de a, b e c geram Insatisfazibilidade da função Gaussiana")

    num = -(x-c)**2
    den = 2 * sigmazinho**2

    return exp(num/den)


def Sigmoidal(x, a, c):

    nao_SAT_error = ValueError("Os valores de a, b e c geram Insatisfazibilidade da função Sigmoidal") 

    den = 1 + exp(-a*(x-c))

    return 1/den


def Sino_Generalizada(x, a, b, c):

    nao_SAT_error = ValueError("Os valores de a, b e c geram Insatisfazibilidade da função Sino Generalizada") 

    den = 1 + abs((x-c)/a) ** (2*b)

    return 1/den


def FuncS(x, a, b):

    nao_SAT_error = ValueError("Os valores de a, b e c geram Insatisfazibilidade da função Z") 

    if x<= a:
        return 0

    elif x <= (a+b)/2:
        return 2 * ((x-a)/(b-a))**2
    
    elif x < b:
        return 1 - (2 * ((b-x)/(b-a))**2)
    
    elif x >= b:
        return 1
    
    else:
        raise nao_SAT_error


def FuncZ(x, a, b):
    nao_SAT_error = ValueError("Os valores de a, b e c geram Insatisfazibilidade da função Z") 

    if x<= a:
        return 0

    elif x <= (a+b)/2:
        return 1 - (2 * ((x-a)/(b-a))**2)
    
    elif x < b:
        return (2 * ((b-x)/(b-a))**2)
    
    elif x >= b:
        return 1
    
    else:
        raise nao_SAT_error


def Cauchy(x, x0, gamma):
    
    den = 3.141592653689 * ( (x - x0 )**2 + gamma**2) * gamma

    return 1.0/den


def Gaussiana_Dupla(x, Amplitude1, Amplitude2, Media1, Media2, Sigma1, Sigma2):
    num1 = Amplitude1 * exp(- (x - Media1)**2)
    den1 = (2 * Sigma1 ** 2)

    num2 = Amplitude2 * exp(- (x - Media2)**2)
    den2 = (2 * Sigma2 ** 2)

    output = num1/den1 + num2/den2

    return output


def UserFunction1(x):

    num = sin(x)
    den = sqrt(x) * 1/x

    return num/den


def UserFunction2(x):

    power = 1-sin(x)
    num = x**(2-x)
    den = 3*x

    return (num**power)/den
