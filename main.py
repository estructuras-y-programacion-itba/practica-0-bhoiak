
# Tu implementacion va aqui
def hola_mundo():
    return "hola_mundo"

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


def nuevos_dados(tirada1, cambio_dados):

    dados_elegidos = []
    contar = 0
    while contar < int(cambio_dados):
            dado_elegido = (input("Que dado quiere tirar nuevamente? 1 para el 1ro, 2 para el segundo... etc"))
        
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


def generala():
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
    
jugar = generala()


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()

                
    
                
"""   
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
"""
