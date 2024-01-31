from os import system
import module.camper as camper
import module.trainer as trainer
import module.coordinacion as coord
from module.validate import menuNoValid
import json

def menu():
    system("clear")
    print("Sistema de almacenamiento de datos para campus")
    print("\t1. Informacion del camper")
    print("\t2. Informacion del trainer")
    print("\t3. Coordinacion")
    print("\t0. Exit")

while True:
    menu()
    opc = int(input())

    match(opc):
        case 1:
            with open("module/storage/camper.json", "r") as f:
                camper.camperList = json.loads(f.read())
            system("clear")
            camper.menu()
        case 2:
            with open("module/storage/trainer.json", "r") as f:
                trainer.trainerList = json.loads(f.read())
            system("clear")
            trainer.menu()
        case 3:
            system("clear")
            coord.menu()
        case 0:
            system("clear")
            break
        case _:
            system("clear")
            menuNoValid(opc)






