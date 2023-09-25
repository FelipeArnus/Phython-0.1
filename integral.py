def funcao(x):
    return 2*x**3 + 3*x
inicio = 0
fim = 2
delta = 0.00001
areazona = 0
while inicio < fim:
    altura = funcao(inicio)
    base = delta 
    areazinha = base * altura
    areazona += areazinha
    inicio += delta