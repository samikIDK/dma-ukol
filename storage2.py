products = [
    {
        "price": 50,
        "name": "Audi",

    },
    {
        "price": 30,
        "name": "BMW",
    },
    {
        "price": 50,
        "name": "Škoda",
    }
]


def print_products():
    for product in products:
        print(f"Název produktu: {product['name']}, {product['price']}Kč")




def add_product():
    product_name = input("Název produktu:")
    product_price = input("cena:")
    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product2)

def search_product():
    search = input("Co hledáte?: ").lower()
    try:
        price_search = float(search)
        results = [product for product in products
                   if product['price'] == price_search]
    except ValueError:
        results = [product for product in products
                   if search in product['name'].lower()]

    if results:
        for product in results:
            print(f"Našel jsem: {product['name']} - {product['price']}Kč")
    else:
        print("Nic jsem nenašel.")


def sum_price():
    sum = 0
    for product in products:
        sum += product['price']
    print(f"Celková cena všech produktů: {sum}Kč")



def min_product_price():
    min_price = min(product['price'] for product in products)
    result = [
            product for product in products
            if product['price'] == min_price
    ]
    for product in result:
        print(f"Nejlevnější produkt: {product['name']} - {product['price']}Kč")



def max_product_price():
    max_price = max(product['price'] for product in products)
    result = [
            product for product in products
            if product['price'] == max_price
    ]
    for product in result:
        print(f"Nejlevnější produkt: {product['name']} - {product['price']}Kč")

def average_price():
    average = sum(product['price'] for product in products)/len(products)
    print(f"Průměrná cena produktů: {average}Kč")

def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Hlédání produktu")
    print("4. Celková cena všech produktů")
    print("5. Nejlevnější produkt")
    print("6. Nejdražší produkt")
    print("7. Průměrná cena")
    print("8. Úprava produktů")
    print("Zadej 9 pokud chceš odejít ze skladu\n")

    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání položky")
        add_product()
        print("")
        menu()

    elif choice == 3:
        search_product()
        print("")
        menu()

    elif choice == 4:
        sum_price()
        print("")
        menu()

    elif choice == 5:
        min_product_price()
        print("")
        menu()
    elif choice == 6:
        max_product_price()
        print("")
        menu()
    elif choice == 7:
        average_price()
        print("")
        menu()
    elif choice == 8:
        print("")
        menu()

    elif choice == 9:
        print("Konec")
        exit()

    else:
        print("Zadal jsi špatně!\n")


menu()
