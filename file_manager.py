import json
from models import *


def save_products(products, filename):

    data = [p.to_dict() for p in products]

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_products(filename):

    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return [Product(**item) for item in data]

    except FileNotFoundError:
        return []


def save_vendors(vendors, filename):

    data = [v.to_dict() for v in vendors]

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_vendors(filename):

    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return [Vendor(**item) for item in data]

    except FileNotFoundError:
        return []


def save_purchase_orders(purchase_orders, filename):

    data = [po.to_dict() for po in purchase_orders]

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_purchase_orders(filename):

    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return [PurchaseOrder(**item) for item in data]

    except FileNotFoundError:
        return []