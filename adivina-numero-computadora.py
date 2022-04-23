import random

def adivinaElNumero(x):
    print("======================================")
    print("Bienvenido al juego adivina el numero")
    print("======================================")
    print(f"Selecciona un numero entre 1 y {x} para que la computadora adivine")

    limiteInferior = 1;
    limiteSuperior = x;

    respuesta=""

    while respuesta != "c":
        if limiteInferior != limiteSuperior:
            prediccion = random.randint(limiteInferior,limiteSuperior)
        else:
            prediccion = limiteInferior
        print(f"El numero en el que piensas es :{prediccion}") 
        respuesta = input("El numero es mas grande(A), es mas pequeño(B) o es el correcto(C): ").lower()
        if respuesta == 'a':
            limiteInferior=prediccion + 1
        elif respuesta == 'b':
            limiteSuperior= prediccion - 1

    
    print(f"El numero en el que piensas es {prediccion}")


adivinaElNumero(10)