edades:dict = {
    "kevin": 28,
    "sergio": 23,
    "camila": 29,
    "pedro": 45
}
print(edades)
print("edades.keys(): ", edades.keys())
print("edades.values(): ", edades.values())
print("max(edades): ", max(edades))
print("max(edades.values()): ", max(edades.values()))
print("min(edades): ", min(edades))
print("min(edades.values()): ", min(edades.values()))

usuario:dict = {
    "nombre": "Pedro",
    "genero": True,
    "edad": 49,
    "estatura": 1.71,
    "notas": [4, 3.2, 3, 2, 5],
    "curso": {
        "nombre": "Logica 1",
        "codigo": 334
    }
}

infomacion_extra:dict = {
    "telefono": 4444444,
    "celular": 54654564,
    "direccion": "CRA 555"
}

usuario.update(infomacion_extra)

#print(usuario["x"]) # Existe siempre la key o necesito generar un error
print(usuario.get("telefono", "sin asignar"))
print(usuario)

producto: dict = {}
print(producto)
producto["categoria"] = "lacteos"
print(producto)

precio:int = int(input("Agrege el precio: "))
producto["precio"] = precio
productos:list = []

producto_1 = {
    "categoria": "Algo",
    "precio": 3400
}
productos.append(producto)
productos.append(producto_1)

print(productos)
print(len(productos))
print(len(producto))
sumatoria: int = 0
for pro in productos:
    sumatoria += pro['precio']
print(sumatoria)
'''
    categoria: str
    precio: int,

    categoria: str
    precio: int

'''
maximo:int = min(productos, key=lambda x: x['precio'])
print(maximo)
m:int = 0
index:int = 0
i = 0
for pro in productos:
    if m > pro['precio']:
       index = i   
    i += 1
print(productos[index])








