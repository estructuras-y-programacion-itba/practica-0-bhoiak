
# Tu implementacion va aqui
import random

#El codigo permite que un jugador juegue su turno como corresponde, es decir, un maximo de 3 tiradas y la posibilidad de elegir cuales dados volver a tirar.
# Luego, el codigo permite evaluar la tirada final para informar al jugador si obtuvo Generala, poker, full house, escalera, o nada especial.
# Asumo que los jugadores llevan el conteo de sus puntos.

def tirar(): #para la primer tirada
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    dado3 = random.randint(1,6)
    dado4 = random.randint(1,6)
    dado5 = random.randint(1,6)
    tiro1 = [dado1, dado2, dado3, dado4, dado5]
    print("El tiro fue: ", dado1, dado2, dado3, dado4, dado5)
 
    return tiro1

def tirar_un_dado():  #para tirar un dado nuevamente
    dado = random.randint(1,6)
    return dado


def nuevos_dados(tirada1, cambio_dados):  #para elegir cuales son los dados que el jugador quiere tirar devuelta en un proximo tiro.

    dados_elegidos = []
    contar = 0
    while contar < int(cambio_dados):
            dado_elegido = (input("Que dado quiere tirar nuevamente? 1 para el 1ro, 2 para el segundo... etc: "))
        
            if dado_elegido not in ["1","2","3","4","5"]:
                print("Listo, sus dados son: ", tirada1) 
                return tirada1
            
            elif dado_elegido in dados_elegidos:
                print("Dado repetido, elija otro.")
            
            else:
                dado_elegido = int(dado_elegido)
                dados_elegidos.append(str(dado_elegido))
                indice = dado_elegido -1
                tirada1[indice] = tirar_un_dado()
                contar += 1

    return tirada1


def generala():    # funcion principal que abarca el turno con las tiradas del jugador al que le toque.
    tirada1 = tirar()
    nuevo_tiro = tirada1
    generala = True
    cant_tiros = 0

    while cant_tiros < 2:
        n = 0
        m = 0
        for i in nuevo_tiro:
            m = m+ 1

            if i == nuevo_tiro[0]:
                n = n+1
        
            if n == 5:   
                generala = True
                print("GENERALA!")
                return
            elif n!= 5 and m == 5:
                generala = False
                cambio_dados = input(("Cuantos dados quiere tirar nuevamente? : "))
                if cambio_dados not in ["1","2","3","4","5"]:
                    print("Listo, sus dados son: ", nuevo_tiro) 
                    return
                
                else:
                    nuevo_tiro = nuevos_dados(nuevo_tiro, cambio_dados)
                    print("Su nuevos dados son: ", nuevo_tiro)
                    cant_tiros += 1
        
    return nuevo_tiro
    
def contar_caras(tirada):      #permite contar los dados que sean iguales en un tiro
    conteos = [0, 0, 0, 0, 0, 0]
    for d in tirada:
        conteos[d - 1] += 1
    return conteos

def es_full(tirada):      #clasifica si es full house
    conteos = contar_caras(tirada)
    hay_3 = False
    hay_2 = False

    for c in conteos:
        if c == 3:
            hay_3 = True
        elif c == 2:
            hay_2 = True

    return hay_3 and hay_2

def es_poker(tirada):   #clasifica si es poker
    conteos = contar_caras(tirada)
    for c in conteos:
        if c == 4:
            return True
    return False

def es_escalera(tirada):    ##clasifica si es escalera
    ordenada = sorted(tirada)
    return ordenada == [1,2,3,4,5] or ordenada == [2,3,4,5,6]

def evaluar_jugada_final(tirada):   #devuelve el nombre del resultado obtenido
    if es_poker(tirada):
        return "Poker"
    elif es_full(tirada):
        return "Full house"
    elif es_escalera(tirada):
        return "Escalera"
    else:
        return "Otro"



def main():
    # Aqui ejecutas tus soluciones
    jugar = generala()
    print("Su resultado del tiro es: ", evaluar_jugada_final(jugar))
    return

# No cambiar a partir de aqui
if __name__ == "__main__":
    main()

