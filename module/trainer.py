from os import system
from .validate import menuNoValid
from .data import trainerList, generos
import json

def save():
    print("""
     ___________________________
    |                           |
    |     Agregar Trainer       |                    
    |___________________________|      
    """)
    info = {
        "Nombre": input("Ingrese el nombre del trainer: "),
        "Apellido": input("Ingrese el apellido del trainer: "),
        "Edad": input("Ingrese la edad del trainer: "),
        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
    }
    
    trainerList.append(info)
    with open("module/storage/trainer.json", "w") as f:
        data = json.dumps(trainerList, indent=4)
        f.write(data)
    return system("clear"), print("Sucessfully Trainer\n")

def edit():
    while True:
        print("""
     ___________________________
    |                           |
    | Actualizacion de Trainer  |                    
    |___________________________|      
    """)
        codigo = int(input("Ingrese el codigo del trainer que deseas actualizar: "))
        try:
            print(f"""
    ____________________________
                
    ID: {codigo}
    Nombre: {trainerList[codigo].get('Nombre')}
    Apellido: {trainerList[codigo].get('Apellido')}
    Edad: {trainerList[codigo].get('Edad')}
    Genero: {trainerList[codigo].get('Genero')}
    ____________________________
            """)
            print("¿Este es el trainer que deseas actualizar?")
            
            print("\t1. Si\n\t2. No\n\t0. Exit")
            opc = int(input())
            match(opc):
                case 1:
                    print("")
                    info = {
                        "Nombre": input("Ingrese el nombre del trainer: "),
                        "Apellido": input("Ingrese el apellido del trainer: "),
                        "Edad": input("Ingrese la edad del trainer: "),
                        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
                    }

                    trainerList[codigo] = info

                    with open("module/storage/trainer.json", "w") as f:
                        data = json.dumps(trainerList, indent=4)
                        f.write(data)
                    system("clear")
                    print("Trainer edited\n")
                    break
                case 2:
                    system("clear")
                case 0:
                    system("clear")
                    break
        except IndexError:
            system("clear")
            print("Error: Trainer no encontrado.\n")

def search():
    system("clear")
    print("""
 ___________________________
|                           |
|     Lista de Trainers     |                    
|___________________________|      
""")
    for i, train in enumerate(trainerList):
        print(f"""ID: {i}
Nombre: {train.get('Nombre')}
Apellido: {train.get('Apellido')}
Edad: {train.get('Edad')}
Genero: {train.get('Genero')}
____________________________
""")


def delete():
    while True:
        print("""
     ___________________________
    |                           |
    |     Eliminar Trainer      |                    
    |___________________________|      
    """)
        codigo = int(input("Ingrese el codigo del trainer que deseas eliminar: "))
        try:
            print(f"""
    ____________________________
                
    ID: {codigo}
    Nombre: {trainerList[codigo].get('Nombre')}
    Apellido: {trainerList[codigo].get('Apellido')}
    Edad: {trainerList[codigo].get('Edad')}
    Genero: {trainerList[codigo].get('Genero')}
    ____________________________
            """)
            print("¿Este es el trainer que deseas eliminar?")
            
            print("\t1. Si\n\t2. No\n\t0. Exit")
            opc = int(input())
            match(opc):
                case 1:
                    trainerList.pop(codigo)
                    with open("module/storage/trainer.json", "w") as f:
                        data = json.dumps(trainerList, indent=4)
                        f.write(data)
                    system("clear")

                    print("Trainer deleted\n")
                    break
                case 2:
                    system("clear")
                case 0:
                    system("clear")
                    break
        except IndexError:
            system("clear")
            print("Error: Trainer no encontrado.\n")

def menu():
    while True:
        print("CRUD del trainer")
        print("\t1. Guardar trainer")
        print("\t2. Buscar trainer")
        print("\t3. Actualizar trainer")
        print("\t4. Eliminar trainer")
        print("\t0. Atras")
        opc = int(input())
        match(opc):
            case 1:
                system("clear")
                save()
            case 2:
                system("clear")
                search()
            case 3:
                system("clear")
                edit()
            case 4:
                system("clear")
                delete()
            case 0:
                system("clear")
                break
            case _:
                system("clear")
                menuNoValid(opc)