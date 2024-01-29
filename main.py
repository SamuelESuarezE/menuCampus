from os import system
import module.camper as camper
import module.trainer as trainer
from module.validate import menuNoValid
def menu():
    print("Sistema de almacenamiento de datos para campus")
    print("\t1. Informacion del camper")
    print("\t2. Informacion del trainer")
    print("\t0. Exit")

while True:
    menu()
    opc = int(input())

    match(opc):
        case 1:
            system("clear")
            camper.menu()
        case 2:
            system("clear")
            trainer.menu()
        case 0:
            system("clear")
            break
        case _:
            system("clear")
            menuNoValid(opc)






