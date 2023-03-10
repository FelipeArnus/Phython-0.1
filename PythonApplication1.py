# hamletuce


def func_test0(x):#declara função

 if x < 5: #|if| não precisa de parenteses a n ser que seja algo mais complexo como |if (x>5) and (x<6):|
    print("  Perdeu")

 else:
    print("  Ganhamo", x) # |,| obviamente cria uma sequencia

 y = input(" Terminar? ")#toda declaração começa como string

 if(y == 'sim') or (y == 'Sim') or (y == 's') or (y == 'S'):
     print(' ', sep = ' ')
     
 main()#retorna para main

def main():

print("  hello there", sep = '') #|print("fala interior")| o |sep = " "| pula a linha

x = int(input(""))# Sempre melhor fazer um input separado

func_test0(x)#ativa função

print(" terminou ", sep = ' ')
