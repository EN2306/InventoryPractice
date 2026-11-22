
products = [
    {"name": "Keyboard", "price": "25.50", "stock": "8", "min_stock": "10"},
    {"name": "Mouse", "price": "12.90", "stock": "15", "min_stock": "5"},
    {"name": "Monitor", "price": "189.90", "stock": "3", "min_stock": "6"},
    {"name": "USB Cable", "price": "4.50", "stock": "20", "min_stock": "10"}
]

def calc_inventory_value(products):
    total = 0.0
    for item in products:
        total += float(item['price'])*float(item['stock'])
    return total
def get_low_stock(products):
    r=[]
    for item in products:
        if float(item['min_stock']) > float(item['stock']):
            r.append(item)
    return r

def calc_restock_cost(products):
    rc =0.0
    p = get_low_stock(products)
    for item in p:
        rc+=(float(item['min_stock'])-float(item['stock']))*float(item['price'])
    return rc


def get_most_expensive(products):
    if len(products) == 0:
        return None

    highest = float(products[0]["price"])
    e = products[0]

    for item in products:
        if float(item["price"]) > highest:
            highest = float(item["price"])
            e = item

    return e



def format_product(product):
    return f"{product['name']} - ${float(product['price']):.2f} - {product['stock']} units"




def main():
    print("----- Inventory Management System -----")
    print("1 - Display all products")
    print("2 - Display inventory value")
    print("3 - Display low-stock products")
    print("4 - Display restocking cost")
    print("5 - Display most expensive product")

    s = input("Enter selection => ")

    if s == "1":
        for p in products:
            print(format_product(p))

    elif s == "2":
        print(f"${calc_inventory_value(products):.2f}")

    elif s == "3":
        print(get_low_stock(products))

    elif s == "4":
        print(f"${calc_restock_cost(products):.2f}")

    elif s == "5":
        print(get_most_expensive(products))

if __name__ == "__main__":
    main()
