x = 0
y = 1

def adição(a):
    print("+ ")
    b = int(input())
    b = a + b
    return b

def subtração(a):
    print("- ")
    b = int(input())
    b = a - b
    return b

def divisão(a):
    print("% ")
    b = int(input())
    b = a / b
    return b

def multiplicação(a):
    print("x ")
    b = int(input())
    b = a * b
    return b

def menu():
    print()
    x=0
    print("Calculadora:")
    print("1 -Adição")
    print("2 -Subtração")
    print("3 -Multiplicação")
    print("4 -Divisão")
    print("5 -Sair do programa")
    print("Selecione sua opção:")
    while(x != 1)and(x != 2)and(x != 3)and(x!=4)and(x!=5):
        x = int(input("n: "))
    return x


while(x != 5):
    x = menu()
    print()
    print(y)
    match x:
        case 1:
            y = adição(y)
        case 2:
            y = subtração(y)
        case 3:
            y = multiplicação(y)
        case 4:
            y = divisão(y)
    print("= ")
    print(y)
