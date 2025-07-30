inventory = {}
quantity_of_profuctos_add = int(input("Ingrese la cantidad de cuantos productos va a añadir: "))
for i in range(quantity_of_profuctos_add):
    print(f"\n Prenda {1+i}")
    code = input("Ingrese el codigo de la prenda: ")
    while code in inventory:
        print(f"El codigo {code} de la prenda ya existe en el inventario")
        code = input("Ingrese el codigo de la prenda: ")
    name_of_product = input("Ingrese el nombre de la prenda (ej Pantalon, Playera, etc): ")
    category_product = input("Ingrese de que categoria es la prenda (ej niño,niña,mujer): ").lower()
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
        "name_of_product": name_of_product,
        "category_product": category_product,
        "size_product": size_product,
        "unit_price": unit_price,
        "stock_quantity": stock_quantity
    }
print(f"\n ===Lista Completa de productos===")
for code,product in inventory.items():
    print(f"\n Codigo de la prenda: {code}")
    print(f"Nombre de la prenda: {product.get('name_of_product')}")
    print(f" Categoria de la prenda: {product.get('category_product', 'no esta definido')}")
    print(f"Talla de la prenda: {product.get('size_product', 'no esta definido')}")
    print(f"Precio de la prenda: {product.get('unit_price', 'no esta definido')}")
    print(f"Cantidad de prendas {product.get('stock_quantity', 'no esta definido')}")

if inventory:
    print("\n Busqueda de una prenda")
    search_product = input("Ingrese el codigo de la prenda a buscar: ")
    if search_product in inventory:
        print(f"Nombre de la prenda: {inventory[search_product]['name_of_product']}")
        print(f" Categoria de la prenda: {inventory[search_product]['category_product']}")
        print(f"Talla de la prenda: {inventory[search_product]['size_product']}")
        print(f"Precio de la prenda: {inventory[search_product]['unit_price']}")
        print(f"Cantidad de prendas {inventory[search_product]['stock_quantity']}")
    else:
        print(f"el codigo {search_product} no existe")
else:
    print("No se encontro ningun dato registrado en inventario ")
print("\n Calcular el precio total del inventario")
value_final = 0
for price in inventory.values():
    price_ = price['unit_price']
    stock = price[ 'stock_quantity']
    value_final += price_*stock
    print(f"El precio total del inventario Q{value_final}")

h =0
m =0
no=0
na=0
for datos in inventory.values():
    categoria = datos['category_product']
    if  categoria == "hombre":
        h +=1
    elif categoria == "mujer" :
        m +=1
    elif categoria =="niño":
        no +=1
    elif categoria == "niña":
        na += 1
print("\n Productos por cada categoria")
print(f"Cantidad de la categoria Hombre es: {h}")
print(f"Cantidad de la categoria Mujer es: {m}")
print(f"Cantidad de la categoria Niña es: {na}")
print(f"Cantidad de la categoria Niño es: {no}")