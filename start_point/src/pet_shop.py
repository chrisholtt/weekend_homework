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
