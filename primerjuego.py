import random

print (' Bienvenido a Adivina el Numero! '.center(104, "*") )
print ('*','Tienes que adivinar un numero entre el 0 y el 100'.center(100),'*',)
print ('*','Tienes 7 intentos, el juego te dira como pista si el numero'.center(100),'*',)
print ('*','que debes adivinar es menor o mayor al que introduzcas'.center(100),'*',)
print (' BUENA SUERTE!. '.center(104, "*"))

def lee_entero():
    while True :
        valor = input('Ingrese un número entre 0 y 100: ')
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print ('ATENCIÓN: Debe ingresar un número entre 0 y 100.')
            
def jugar():
    numero=random.randrange(0, 100)
    propuesta = lee_entero()
    intentos = 1
    while propuesta != numero and intentos <=6 :    
        if propuesta > numero:
            print(' El numero secreto es menor '.center(40, "<"))
        elif propuesta < numero:
            print(' El numero secreto es mayor '.center(40, ">"))
        print('Te quedan',7-intentos,' vidas')
        print('Intenta con otro numero')
        propuesta = lee_entero()
        intentos = intentos + 1
    if propuesta == numero:
        print (f'¡Felicitaciones! Adivinaste el numero en {intentos} intentos.'.center(100, "*"))
    else:
        print ('El numero era: ', numero)
        print ('¡Suerte la proxima vez!')
    volver=input('Quieres jugar nuevamente? S N: ')
    while (volver != 's') and (volver != 'n') and (volver != 'S') and (volver != 'N'):
        volver=input('Por favor ingrese S N :')
    if (volver =='s') | (volver =='S'):
        jugar()
    else:
        print('Gracias por jugar, hasta pronto!...'.center(100, "*"))
jugar()    
