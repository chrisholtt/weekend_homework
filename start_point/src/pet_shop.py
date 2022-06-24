# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(list):
    return list["name"]


def get_total_cash(dict):
    return dict["admin"]["total_cash"]


# def add_or_remove_cash(dict, cash):
#     prev_ammount = dict["admin"]["total_cash"]
#     prev_ammount += cash
#     return prev_ammount

def add_or_remove_cash(dict, cash):
    dict["admin"]["total_cash"] += cash
