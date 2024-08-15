from random import randint

numero:int = randint(1, 50)
intento: int = 1
while(intento < 6):
    respuesta: int = int(input("Ingrese su respuesta: "))
    
    if(numero == respuesta):
        print("Gano!!")
        break
    elif(respuesta > numero):
        print("Frio")
    else:
        print("Caliente")
    intento += 1
