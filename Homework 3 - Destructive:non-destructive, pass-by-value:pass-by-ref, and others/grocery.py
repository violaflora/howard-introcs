
def grocery_cost(grocery_map, list_of_items):
  price = 0
  for item in list_of_items:
    price = price + grocery_map[item]
  return price
    

if __name__ == "__main__":
    grocery_list = {
        'apple': 0.50,
        'chips': 1.50,
        'milk': 3.25,
        'fish': 9.99,
        'tomato': 0.75,
        'cereal': 2.50,
        'chicken': 5.49,
        'peanut butter': 2.99,
        'jam': 1.95
    }
    list_of_items = ['milk', 'cereal', 'apple']
 # 6.25
    print(grocery_cost(grocery_list, list_of_items))

    grocery_list = {
        'apple': 0.70,
        'chips': 1.50,
        'milk': 3.25,
        'fish': 9.99,
        'tomato': 0.75,
        'cereal': 2.50,
        'chicken': 5.49,
        'peanut butter': 2.99,
        'jam': 1.95
    }
    list_of_items = ['milk', 'cereal', 'apple']
    # 6.45
    print(grocery_cost(grocery_list, list_of_items))