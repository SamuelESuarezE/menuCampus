from os import system
from .data import camperList, generos
from .validate import menuNoValid
import json

def save():
    print("""
     ___________________________
    |                           |
    |     Agregar Camper        |                    
    |___________________________|      
    """)
    info = {
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido": input("Ingrese el apellido del camper: "),
        "Edad": input("Ingrese la edad del camper: "),
        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
    }
    
    camperList.append(info)
    with open("module/storage/camper.json", "w") as f:
        data = json.dumps(camperList, indent=4)
        f.write(data)
    return system("clear"), print("Sucessfully Camper")

def edit():
    while True:
        print("""
     ___________________________
    |                           |
    |  Actualizacion de Camper  |                    
    |___________________________|      
    """)
        codigo = int(input("Ingrese el codigo del camper que deseas actualizar: "))
        
        try:
            print(f"""
    ____________________________
                         
    ID: {codigo}
    Nombre: {camperList[codigo].get('Nombre')}
    Apellido: {camperList[codigo].get('Apellido')}
    Edad: {camperList[codigo].get('Edad')}
    Genero: {camperList[codigo].get('Genero')}
    ____________________________
            """)
            print("¿Este es el camper que deseas actualizar?")
            
            print("\t1. Si\n\t2. No\n\t0. Exit")
            opc = int(input())
            match(opc):
                case 1:
                    print("")
                    info = {
                        "Nombre": input("Ingrese el nombre del camper: "),
                        "Apellido": input("Ingrese el apellido del camper: "),
                        "Edad": input("Ingrese la edad del camper: "),
                        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
                    }

                    camperList[codigo] = info

                    with open("module/storage/camper.json", "w") as f:
                        data = json.dumps(camperList, indent=4)
                        f.write(data)
                    system("clear")
                    print("Camper edited\n")
                    break
                case 2:
                    system("clear")
                case 0:
                    system("clear")
                    break
        except IndexError:
            system("clear")
            print("Error: Camper no encontrado.")
            
def search():
    system("clear")
    print("""
 ___________________________
|                           |
|     Lista de Campers      |                    
|___________________________|      
""")
    for i, camp in enumerate(camperList):
        print(f"""ID: {i}
Nombre: {camp.get('Nombre')}
Apellido: {camp.get('Apellido')}
Edad: {camp.get('Edad')}
Genero: {camp.get('Genero')}
____________________________
""")


def delete():
    while True:
        print("""
     ___________________________
    |                           |
    |      Eliminar Camper      |                    
    |___________________________|      
    """)
        codigo = int(input("Ingrese el codigo del camper que deseas eliminar: "))
        try:
            print(f"""
     ____________________________
           
    ID: {codigo}
    Nombre: {camperList[codigo].get('Nombre')}
    Apellido: {camperList[codigo].get('Apellido')}
    Edad: {camperList[codigo].get('Edad')}
    Genero: {camperList[codigo].get('Genero')}
    ____________________________
            """)
            print("¿Este es el camper que deseas eliminar?")
            
            print("\t1. Si\n\t2. No\n\t0. Exit")
            opc = int(input())
            match(opc):
                case 1:
                    camperList.pop(codigo)
                    with open("module/storage/camper.json", "w") as f:
                        data = json.dumps(camperList, indent=4)
                        f.write(data)
                    system("clear")

                    print("Camper deleted\n")
                    break
                case 2:
                    system("clear")
                case 0:
                    system("clear")
                    break
        except IndexError:
            system("clear")
            print("Error: Camper no encontrado.")

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



