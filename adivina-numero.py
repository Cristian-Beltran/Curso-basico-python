import random


def adivinaElNumero(x):
    print("=====================") 
    print("Bienvenido/a al juego")
    print("=====================") 
    print("Tu meta es adivinar el numero generado por la maquina")
    
    numeroAleatorio = random.randint(1,x) #Numero aleatorio entre 1 y x

    prediccion = 0

    while(prediccion != numeroAleatorio):
        prediccion = int(input(f"Ingrese un numero entre 1 y {x}: "))
        if(prediccion > numeroAleatorio):
            print("Intenta otra vez este numero es muy grande")
        else:
            print("Intenta otra vez este numero es muy pequeño")
    
    print(f"Feliciataciones adivinaste el numero {numeroAleatorio}")


adivinaElNumero(10);