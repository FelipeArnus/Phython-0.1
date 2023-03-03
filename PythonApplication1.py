# hamletuce


def new_func(x):#declara função

 if x < 5: #|if| não precisa de parenteses a n ser que seja algo mais complexo como |if (x>5) and (x<6):|
    print("  Perdeu")

 else:
    print("  Ganhamo", x) # |,| obviamente cria uma sequencia

    new_func(x)#termina função
print("  hello there", sep = '')# |print("fala interior")| o |sep = " "| pula a linha

x = int(input(""))# Sempre melhor fazer um input separado

new_func(x)#ativa função
