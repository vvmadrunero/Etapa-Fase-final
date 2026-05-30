# Menú del restaurante
menu = [
    ["Hamburguesa", "Comida", 18000],
    ["Pizza", "Comida", 25000],
    ["Perro Caliente", "Comida", 12000],
    ["Gaseosa", "Bebida", 5000],
    ["Jugo Natural", "Bebida", 8000],
    ["Helado", "Postre", 15000]
]

# Función para calcular el precio final
def calcular_precio(categoria, precio):

    categoria_objetivo = "Comida"
    precio_limite = 15000

    if categoria == categoria_objetivo and precio > precio_limite:
        descuento = precio * 0.15
        precio_final = precio - descuento
    else:
        precio_final = precio

    return precio_final


print("----- MENÚ DEL RESTAURANTE -----")

# Recorrer matriz
for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio = producto[2]

    nuevo_precio = calcular_precio(categoria, precio)

    print("\nProducto:", nombre)
    print("Categoría:", categoria)
    print("Precio base:", precio)
    print("Precio final:", nuevo_precio)