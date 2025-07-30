inventory = {}
quantity_of_profuctos_add = int(input("Ingrese la cantidad de cuantos productos va a añadir: "))
for i in range(quantity_of_profuctos_add):
    print(f"\n Prenda {1+i}")
    code = input("Ingrese el codigo de la prenda: ")
    while code in inventory:
        print(f"El codigo {code} de la prenda ya existe en el inventario")
        code = input("Ingrese el codigo de la prenda: ")
    name_of_product = input("Ingrese el nombre de la prenda (ej Pantalon, Playera, etc): ")
    category_product = input("Ingrese de que categoria es la prenda (ej niño,niña,mujer): ")
    size_product = input("Ingrese la talla del producto (ej S, L, M, XL): ")
    unit_price = float(input("Ingrese el precio de la prenda: "))
    while unit_price <= 0:
        print(f"El percio {unit_price} no es mayor a cero, porfavor intentelo otra vez")
        unit_price = float(input("Ingrese el precio de la prenda: "))
    stock_quantity = int(input("Ingrese la cantidad de stock: "))
    while stock_quantity <0 and stock_quantity != int:
        print(f"La cantidad {stock_quantity} de stock no es entera o positiva, Vuelva a intentarlo")
        stock_quantity = int(input("Ingrese la cantidad de stock: "))
    inventory[code] = {
        "Nombre": name_of_product,
        "Categoria": category_product,
        "Talla": size_product,
        "Precio Unitario": unit_price,
        "Stock": stock_quantity
    }