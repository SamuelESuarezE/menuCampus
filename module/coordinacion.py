from os import system
from .validate import menuNoValid

def menu():
    while True:
        print("CRUD de Coordinacion") 
        print("\t1. Asignacion de Camper a Trainer")
        print("\t2. Remover Camper de Trainer")
        print("\t3. Lista Campers por Trainer")
        print("\t4. Generos de Campers por Trainer")
        print("\t0. Exit")
        opc = int(input())

        match(opc):
            case 1:
                system("clear")
                print("Asignacion de Camper a Trainer")
            case 2:
                system("clear")
                print("Remover Camper de Trainer")
            case 3:
                system("clear")
                print("Lista Campers por Trainer")
            case 4:
                system("clear")
                print("Generos de Campers por Trainer")
            case 0:
                system("clear")
                break
            case _:
                system("clear")
                menuNoValid(opc)
