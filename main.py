
# Tu implementacion va aqui
def hola_mundo():
    return "hola_mundo"


def main():
    # Aqui ejecutas tus soluciones
    print(hola_mundo())


def main():
    # Aqui ejecutas tus soluciones
    print(hola_mundo())

import random

def tirar():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    dado3 = random.randint(1,6)
    dado4 = random.randint(1,6)
    dado5 = random.randint(1,6)
    tiro1 = [dado1, dado2, dado3, dado4, dado5]
    print("El tiro fue: ", dado1, dado2, dado3, dado4, dado5)
 
    return tiro1

def tirar_un_dado():
    dado = random.randint(1,6)
    return dado


def nuevos_dados(dado_elegido, tirada1):

    if dado_elegido not in ["1","2","3","4","5"]:
                print("Listo, sus dados son: ", tirada1) 
                return tirada1

    else: 
          dado_elegido = int(dado_elegido)
          indice = dado_elegido -1
          tirada1[indice] = tirar_un_dado()   

    return tirada1


def generala():
    tirada1 = tirar()
    generala = True
    n = 0

    for i in tirada1:
        if i == tirada1[0]:
            n = n+1
            if n != 5:   
                generala = False

        else:
            print("GENERALA!")
            return
    
    if generala == False:
        cambio_dados = input(("Cuantos dados quiere tirar nuevamente? : "))
        if cambio_dados not in ["1","2","3","4","5"]:
            print("Listo, sus dados son: ", tirada1) 
            return
        
        else:

            contar = 0    
            while contar < int(cambio_dados):
                dado_elegido = input(("Que dado quiere cambiar? (poner 1 o 2 o 3... segun el dado que quiera tirar) : "))
                if dado_elegido not in ["1","2","3","4","5"]:
                    print("Listo, sus dados son: ", tirada1) 
                    return

                if dado_elegido == "1":
                    nuevo_tiro = nuevos_dados(dado_elegido, tirada1)
                    print("Su nuevos dados son: ", nuevo_tiro)
                    contar += 1
                
                if dado_elegido == "2":
                    nuevo_tiro = nuevos_dados(dado_elegido, tirada1)
                    print("Su nuevos dados son: ", nuevo_tiro)
                    contar += 1

                if dado_elegido == "3":
                    nuevo_tiro = nuevos_dados(dado_elegido, tirada1)
                    print("Su nuevos dados son: ", nuevo_tiro)
                    contar += 1

                if dado_elegido == "4":
                    nuevo_tiro = nuevos_dados(dado_elegido, tirada1)
                    print("Su nuevos dados son: ", nuevo_tiro)
                    contar += 1

                elif dado_elegido == "5":
                    nuevo_tiro = nuevos_dados(dado_elegido, tirada1)
                    print("Su nuevos dados son: ", nuevo_tiro)
                    contar += 1
    #en realidad deberia meter el contar en la otra funcion para poder usarla cada vez que quiera hacer un nuevo tiro, y ese nuevo tiro gruardarlo en mi lista tirada1.                
        return nuevo_tiro
    

# No cambiar a partir de aqui
if __name__ == "__main__":
    main()
