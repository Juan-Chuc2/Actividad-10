inventory = {}
quantity_of_profuctos_add = int(input("Ingrese la cantidad de cuantos productos va a añadir: "))
for i in range(quantity_of_profuctos_add):
    print(f"\n Prena {1+i}")
    code = input("Ingrese el codigo de la prenda: ")
    name_of_product = input("Ingrese el nombre de la prenda (3j Pantalon, Playera, etc): ")
    category_product = input("Ingrese de que categoria es la prenda (ej niño,niña,mujer): ")
    size_product = input("Ingrese la talla del producto (ej S, L, M, XL): ")
    unit_price = float(input("Ingrese el precio de la prenda: "))
    stock_quantity = int(input("Ingrese la cantidad de stock: "))
    inventory[code] = {
        "Nombre": name_of_product,
        "Categoria": category_product,
        "Talla": size_product,
        "Precio Unitario": unit_price,
        "Stock": stock_quantity
    }