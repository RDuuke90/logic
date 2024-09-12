vehiculos: list = []
while True:
    print("======= MENU ========")
    print("1 -> Crear un vehiculo")
    print("2 -> Lista vehiculos")
    print("3 -> Buscar placa")
    print("4 -> Salir")
    print("=====================")

    opcion:int = int(input("Seleccion opcion: "))

    if(opcion == 1):
        modelo:int = int(input("Ingrese el modelo del vehiculo"))
        marca:str = input("Ingrese la marca del vehiculo")
        placa:str = input("Ingrese la placa del vehiculo")

        
        vehiculo:dict = {
            "modelo": modelo,
            "marca": marca,
            "placa": placa
        }

        existe:bool = False

        if(len(vehiculos) == 0):
            vehiculos.append(vehiculo)
        else:
            for in_vehiculo in vehiculos:
                if in_vehiculo.get('placa') == placa:
                    print("La placa existe: ", vehiculo["placa"])
                    existe = True
                    break
            if(existe is False):
                vehiculos.append(vehiculo) 

    elif(opcion == 2):
        if(len(vehiculos) == 0):
            print("No hay vehiculos")
            continue
        print(vehiculos)

    elif(opcion == 3):
        if(len(vehiculos) == 0):
            print("No hay vehiculos")
            continue
        placa: str = input("Ingrese la placa: ")
        for vehiculo in vehiculos:
            if vehiculo['placa'] == placa:
                print(vehiculo)
                break

    elif(opcion == 4):
        print("Saliendo del sistema!")
        break

    else:
        print("Opcion no valida!")

