# hamletuce


def new_func(x):#declara função

 if x < 5: #|if| não precisa de parenteses a n ser que seja algo mais complexo como |if (x>5) and (x<6):|
    print("  Perdeu")

 else:
    print("  Ganhamo", x) # |,| obviamente cria uma sequencia

 y = input(" Recomessar? ")#toda declaração começa como string

 if(y == 'sim') or (y == 'Sim') or (y == 's') or (y == 'S'):
    new_func(x)#reinicia a função


print("  hello there", sep = '')# |print("fala interior")| o |sep = " "| pula a linha

x = int(input(""))# Sempre melhor fazer um input separado

new_func(x)#ativa função
