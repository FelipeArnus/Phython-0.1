#descobrin numero primo e dizer qual o proximo
#FELIPE DE CAMPOS MELLO ARNUS - RM:550923
x = 0
y = 0
c = 0
n = 1

def primo(x,n):
    x = 0
    for c in range(2,n):
        if(0==(n%c)):
            x = x + 1
    if(x==0):
        return 1 #confirmação postitiva
    else:
        return 0 #confirmação negativa

def baixo(a):
    x = 0
    c = 0
    while(c==0):
        x = primo(x,a)
        if(x == 1):#caso b seja primo ele retorna esse para o main
            return a #numero primo mais proximo(para baixo)
        a = a - 1

def alto(b):
    x = 0
    c = 0
    while(c==0):
        x = primo(x,b)
        if(x == 1):#caso b seja primo ele retorna esse para o main
            return b #numero primo mais proximo(pra cima)
        b = b + 1

while(n!=0):
    n = -1
    while(n<0)or(n>1000):
        n = int(input("n: "))

    x = alto(n)
    y = baixo(n)
    if(n!=1)and(n!=0):
        if(x - n)>=(n - y):#mede a distãncia entre a proximidade dos dois numeros primos proximos
            print(f'O numero primo mais proximo de {n} é {y}')
        elif(x - n)<(n - y):
            print(f'O numero primo mais proximo de {n} é {x}')
    elif(n == 1):
        print('O numero primo mais proximo de 1 é 2')
