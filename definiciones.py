def suma(a:int, b:int) -> int:
    return a + b

def Pi() -> float:
    return 3.1416

def saludo(nombre:str):
    print(f"Hola {nombre}")

def final():
    exit(0)

def cm_to_mt(cm:int) -> float:
    return cm/100

print(cm_to_mt(170))
resultado:int = suma(10, 3)
numero_pi: float = Pi()
print(resultado)
print(numero_pi)
saludo("Jorge")
final()
