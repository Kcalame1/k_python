from models import *
from datetime import datetime


def add_product(products):

    product_id = input("Product ID: ")

    for p in products:
        if p.product_id == product_id:
            print("Duplicate Product ID.")
            return

    try:
        quantity = int(input("Quantity: "))
        reorder_level = int(input("Reorder Level: "))
        reorder_quantity = int(input("Reorder Quantity: "))
        unit_price = float(input("Unit Price: "))

    except ValueError:
        print("Invalid numeric input.")
        return

    name = input("Name: ")
    category = input("Category: ")
    vendor_id = input("Vendor ID: ")

    product = Product(
        product_id,
        name,
        category,
        quantity,
        reorder_level,
        reorder_quantity,
        unit_price,
        vendor_id
    )

    products.append(product)

    print("Product added.")


def view_products(products):

    for p in products:
        print(p.__dict__)


def search_products(products):

    print("1. Search by ID")
    print("2. Search by Name")
    print("3. Search by Category")
    print("4. Search by Vendor")

    choice = input("Choice: ")

    if choice == "1":

        pid = input("Product ID: ")

        for p in products:
            if p.product_id == pid:
                print(p.__dict__)

    elif choice == "2":

        name = input("Name: ").lower()

        for p in products:
            if name in p.name.lower():
                print(p.__dict__)

    elif choice == "3":

        category = input("Category: ").lower()

        for p in products:
            if category in p.category.lower():
                print(p.__dict__)

    elif choice == "4":

        vendor = input("Vendor ID: ")

        for p in products:
            if p.vendor_id == vendor:
                print(p.__dict__)


def edit_product(products):

    pid = input("Product ID: ")

    for p in products:

        if p.product_id == pid:

            p.name = input("New Name: ")
            p.category = input("New Category: ")
            p.quantity = int(input("New Quantity: "))

            print("Product updated.")
            return

    print("Product not found.")


def deactivate_product(products):

    pid = input("Product ID: ")

    for p in products:

        if p.product_id == pid:
            p.active = False
            print("Product deactivated.")
            return

    print("Product not found.")


def low_stock_products(products):

    for p in products:

        if p.quantity <= p.reorder_level:
            print(f"{p.name} is low stock.")


def add_vendor(vendors):

    vendor_id = input("Vendor ID: ")

    for v in vendors:
        if v.vendor_id == vendor_id:
            print("Duplicate Vendor ID.")
            return

    vendor = Vendor(
        vendor_id,
        input("Vendor Name: "),
        input("Contact Name: "),
        input("Phone: "),
        input("Email: "),
        input("Address: ")
    )

    vendors.append(vendor)

    print("Vendor added.")


def view_vendors(vendors):

    for v in vendors:
        print(v.__dict__)


def search_vendor(vendors):

    vid = input("Vendor ID: ")

    for v in vendors:

        if v.vendor_id == vid:
            print(v.__dict__)
            return

    print("Vendor not found.")


def edit_vendor(vendors):

    vid = input("Vendor ID: ")

    for v in vendors:

        if v.vendor_id == vid:

            v.vendor_name = input("New Vendor Name: ")
            v.phone = input("New Phone: ")

            print("Vendor updated.")
            return


def create_purchase_order(products, vendors, purchase_orders):

    po_number = input("PO Number: ")
    vendor_id = input("Vendor ID: ")

    items = []
    total_cost = 0

    while True:

        product_id = input("Product ID (or done): ")

        if product_id.lower() == "done":
            break

        quantity = int(input("Quantity: "))

        for p in products:

            if p.product_id == product_id:

                cost = quantity * p.unit_price
                total_cost += cost

                items.append({
                    "product_id": product_id,
                    "quantity": quantity,
                    "unit_price": p.unit_price
                })

    po = PurchaseOrder(
        po_number,
        vendor_id,
        str(datetime.now().date()),
        items,
        total_cost
    )

    purchase_orders.append(po)

    print("Purchase order created.")


def view_purchase_orders(purchase_orders):

    for po in purchase_orders:
        print(po.__dict__)


def receive_purchase_order(products, purchase_orders):

    po_number = input("PO Number: ")

    for po in purchase_orders:

        if po.po_number == po_number:

            if po.status == "RECEIVED":
                print("PO already received.")
                return

            for item in po.items:

                for product in products:

                    if product.product_id == item["product_id"]:
                        product.quantity += item["quantity"]

            po.status = "RECEIVED"

            print("Shipment received.")
            return

    print("PO not found.")