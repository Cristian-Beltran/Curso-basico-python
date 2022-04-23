import random


def jugar(partidas):
    print("============================================")
    print("Bienvenido al juego de piedra papel o tijera")
    print("============================================")
    opciones = ["Piedra","Papel","Tijera"]
    win = 0 
    lose = 0
    while (win <= int(partidas/2)) and (lose <= int(partidas/2)):
        usuario = int(input("Ingrese una opcion Piedra(0), Papel(1) o Tijera(2) \n"))
        maquina = random.randint(0,2)
        if usuario >=0 and usuario <3:
            if(usuario == maquina):
                print(f"El resultado es un empate Usuario: {opciones[usuario]} y Maquina: {opciones[maquina]}\n") 
            elif jugadorgano(usuario,maquina):
                print(f"Yeiii ganaste Usuario: {opciones[usuario]} y Maquina: {opciones[maquina]} \n")
                win=win+1
            else:
                print(f"Que mal perdiste Usuario: {opciones[usuario]} y Maquina: {opciones[maquina]} \n")
                lose=lose+1
            print(f"Usuario: {win}   y    Maquina: {lose} \n")
        else:
            print("Numero ingresado fuera del rango\n")
    
    if win>=int(partidas/2):
        print("El ganador del juego es el usuario")
    else:
        print("El ganador del juego es la maquina")

def jugadorgano(usuario,maquina):
    result = False
    if (usuario == 0 and maquina==2) or (usuario == 1 and maquina==0) or (usuario == 2 and maquina==1):
        result = True
    return result
        
jugar(3)
