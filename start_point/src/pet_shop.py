# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(list):
    return list["name"]


def get_total_cash(dict):
    return dict["admin"]["total_cash"]


def add_or_remove_cash(dict, cash):
    dict["admin"]["total_cash"] += cash


def get_pets_sold(dict):
    return dict["admin"]["pets_sold"]


def increase_pets_sold(dict, number_of_pets):
    dict["admin"]["pets_sold"] += number_of_pets
    return dict


def get_stock_count(dict):
    stock_number = len(dict["pets"])
    return stock_number


def get_pets_by_breed(dict, breed):
    pets_with_name = []
    for item in dict["pets"]:
        if item["breed"] == breed:
            pets_with_name.append(item)
    return pets_with_name


def find_pet_by_name(dict, name):
    for item in dict["pets"]:
        if item["name"] == name:
            return item
    return


def remove_pet_by_name(dict, name):
    index = -1
    for item in dict["pets"]:
        index += 1
        if item["name"] == name:
            dict["pets"].pop(index)
    return dict


def add_pet_to_stock(dict, new_pet):
    dict["pets"].append(new_pet)
    return dict


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, amount):
    customer["cash"] -= amount
    return customer


def get_customer_pet_count(customer):
    pet_count = 0
    pet_count += len(customer["pets"])
    return pet_count


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    return customer


def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False


def sell_pet_to_customer(dict, pet, customer):
    if not pet:
        return
    if customer_can_afford_pet(customer, pet) == True:
        customer["cash"] -= pet["price"]
        customer["pets"].append(pet)
        dict["admin"]["pets_sold"] += 1
        dict["admin"]["total_cash"] += pet["price"]
        return customer
