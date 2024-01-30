from os import system
from .data import camper, generos
from .validate import menuNoValid

def save():
    info = {
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido": input("Ingrese el apellido del camper: "),
        "Edad": input("Ingrese la edad del camper: "),
        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
    }
    camper.append(info)
    return print("Sucessfully Camper"), system("clear")

def edit():
    print("Edit to camper\n")

def search():
    for camp in camper:
        print(f"Nombre: {camp.get('Nombre')}")
        print(f"Apellido: {camp.get('Apellido')}")
        print(f"Edad: {camp.get('Edad')}")
        print(f"Genero: {camp.get('Genero')}\n")
        
    
    print("The camper is available\n")

def delete():
    print("Camper deleted\n")

def menu():
    while True:
        print("CRUD del camper")
        print("\t1. Guardar camper")
        print("\t2. Buscar camper")
        print("\t3. Actualizar camper")
        print("\t4. Eliminar camper")
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
                menuNoValid(opc)



