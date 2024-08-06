print("¡¡¡ Venta de CAFE !!!")

cafe: str = "cafe"
precio: int = 1000
azucar: int = int(input("Azucar 1: Si 0: No: "))

if azucar == 1:
    cafe += " con azucar"
    precio += 200
else:
    cafe += " sin azucar"

leche: str = input("Leche S: Si N: No: ")

if leche.lower() == "s":
    cafe += ", con leche"
    precio += 300
else:
    cafe += ", sin leche"

licor: str = input("Licor R: Ron, A: Amaretto, W: Whiskey: ")

if licor.lower() == "r":
    cafe += " y ron"
    precio += 1000
elif licor.lower() == "a":
    cafe += " y amaretto"
    precio += 1500
elif licor.lower() == "w":
    cafe += " y whiskey"
    precio += 2000
else:
    cafe += ", sin licor"

print(cafe+". Precio $"+str(precio))
