# create a function called make_menu that takes two lists

def make_menu(names, prices):
    menu = []
    for i in range(len(menu_items)):
        food = menu_items[i]
        price = prices[i]
        full = food + ": $" + str(price)
        menu.append(full)
    return menu

    
if __name__ == '__main__':
    menu_items = []
    prices = []
    while True:
        item = input().strip()
        if item == "":
            break
        price = float(input().strip())
        menu_items.append(item)
        prices.append(price)
    
    print(make_menu(menu_items, prices))

