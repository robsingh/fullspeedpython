"""
Write a function dict_merge_sum that takes two dictionaries d1 and d2 as parameters. 
The values of both dictionaries are numerical. The function should return the merged sum dictionary m of those dictionaries. 
If a key k is both in d1 and d2, the corresponding values will be added and included in the dictionary m. If k is only contained in one of the dictionaries,
the k and the corresponding value will be included in m

"""
"""
def dict_merge_sum(d1:dict,d2:dict) -> dict:
    merged_dict = {}

    for key,value in d1.items():
        merged_dict[key] = merged_dict.get(key, 0) + int(value)

    for key,value in d2.items():
        merged_dict[key] = merged_dict.get(key, 0) + int(value)

    return merged_dict

    # another way
    merged_sum = d1.copy()
    for key,value in d2.items():
        if key in d1:
            d1[key] += value
        else:
            d1[key] = value
    return merged_sum
   

d1 = {'a':'1','b':'2','c':'3'}
d2 = {'a':'4','d':'5','e':'6'}
merged_sum = dict_merge_sum(d1,d2)
print(merged_sum)
"""
"""
Exercise 2
Given is the following simplified data of a supermarket:

supermarket = { "milk": {"quantity": 20, "price": 1.19},
               "biscuits":  {"quantity": 32, "price": 1.45},
               "butter":  {"quantity": 20, "price": 2.29},
               "cheese":  {"quantity": 15, "price": 1.90},
               "bread":  {"quantity": 15, "price": 2.59},
               "cookies":  {"quantity": 20, "price": 4.99},
               "yogurt": {"quantity": 18, "price": 3.65},
               "apples":  {"quantity": 35, "price": 3.15},
               "oranges":  {"quantity": 40, "price": 0.99},
               "bananas": {"quantity": 23, "price": 1.29}}

To be ready for an imminent crisis you decide to buy everything. This isn't particularly social behavior, 
but for the sake of the task, let's imagine it. The question is how much will you have to pay?
"""

"""def total_price(supermarket):
    total_value = 0
    for value in supermarket:
        quantity = supermarket[value]["quantity"]
        price = supermarket[value]["price"]
        total_value += quantity * price
    return total_value

supermarket =  {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits":  {"quantity": 32, "price": 1.45},
    "butter":  {"quantity": 20, "price": 2.29},
    "cheese":  {"quantity": 15, "price": 1.90},
    "bread":  {"quantity": 15, "price": 2.59},
    "cookies":  {"quantity": 20, "price": 4.99},
    "yogurt": {"quantity": 18, "price": 3.65},
    "apples":  {"quantity": 35, "price": 3.15},
    "oranges":  {"quantity": 40, "price": 0.99},
    "bananas": {"quantity": 23, "price": 1.29}
    }

print(total_price(supermarket))
"""

"""
Create a virtual supermarket. For every article there is a price per article and a quantity, i.e. the stock. 
(Hint: you can use the one from the previous exercise!)
Create shopping lists for customers. The shopping lists contain articles plus the quantity.
The customers fill their carts, one after the other. Check if enough goods are available! Create a receipt for each customer.
"""

def create_receipt(supermarket,customers, shopping_list):
    # filling up the cart
    carts = {}
    for customer in customers:
        carts[customer] = []
        for article, quantity in shopping_lists[customer]:
            if article in supermarket:
                if supermarket[article]["quantity"] < quantity:
                    quantity = supermarket[article]["quantity"]
                if quantity:
                    supermarket[article]["quantity"] -= quantity
                    carts[customer].append((article, quantity))
    # for customer in customers:
    #     print(carts[customer])

    print("CHECKOUT......")

    for customer in customers:
        print("\nCheckout for: " + customer + ":")
        total_sum = 0
        for name, quantity in carts[customer]:
            unit_price = supermarket[name]["price"]
            item_sum = quantity * unit_price
            print(f"{quantity:3d} {name:12s} {unit_price:8.2f} {item_sum:8.2f}")
            total_sum += item_sum
        print(f"Total Sum:              {total_sum:11.2f}")


supermarket =  {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits":  {"quantity": 32, "price": 1.45},
    "butter":  {"quantity": 20, "price": 2.29},
    "cheese":  {"quantity": 15, "price": 1.90},
    "bread":  {"quantity": 15, "price": 2.59},
    "cookies":  {"quantity": 20, "price": 4.99},
    "yogurt": {"quantity": 18, "price": 3.65},
    "apples":  {"quantity": 35, "price": 3.15},
    "oranges":  {"quantity": 40, "price": 0.99},
    "bananas": {"quantity": 23, "price": 1.29}
    }

customers = ["Frank", "Rob", "Paul"]
shopping_lists = {
    "Frank" : [('milk', 5), ('apples', 5), ('butter', 1), ('cookies', 1)],
    "Rob":  [('apples', 2), ('cheese', 4), ('bread', 2), ('pears', 3), 
             ('bananas', 4), ('oranges', 1), ('cherries', 4)],
    "Paul":  [('biscuits', 2), ('apples', 3), ('yogurt', 2), ('pears', 1), 
             ('butter', 3), ('cheese', 1), ('milk', 1), ('cookies', 4)]
    }

(create_receipt(supermarket, customers, shopping_lists))