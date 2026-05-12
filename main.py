from inventory_manager import *
from file_manager import *
from reports import *

products = load_products("products.json")
vendors = load_vendors("vendors.json")
purchase_orders = load_purchase_orders("purchase_orders.json")


def product_menu():
    while True:
        print("\n--- PRODUCT MENU ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Products")
        print("4. Edit Product")
        print("5. Deactivate Product")
        print("6. Low Stock Products")
        print("7. Back")

        choice = input("Choice: ")

        if choice == "1":
            add_product(products)

        elif choice == "2":
            view_products(products)

        elif choice == "3":
            search_products(products)

        elif choice == "4":
            edit_product(products)

        elif choice == "5":
            deactivate_product(products)

        elif choice == "6":
            low_stock_products(products)

        elif choice == "7":
            break

        else:
            print("Invalid choice.")


def vendor_menu():
    while True:
        print("\n--- VENDOR MENU ---")
        print("1. Add Vendor")
        print("2. View Vendors")
        print("3. Search Vendor")
        print("4. Edit Vendor")
        print("5. Back")

        choice = input("Choice: ")

        if choice == "1":
            add_vendor(vendors)

        elif choice == "2":
            view_vendors(vendors)

        elif choice == "3":
            search_vendor(vendors)

        elif choice == "4":
            edit_vendor(vendors)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def po_menu():
    while True:
        print("\n--- PURCHASE ORDER MENU ---")
        print("1. Create Purchase Order")
        print("2. View Purchase Orders")
        print("3. Receive Shipment")
        print("4. Back")

        choice = input("Choice: ")

        if choice == "1":
            create_purchase_order(products, vendors, purchase_orders)

        elif choice == "2":
            view_purchase_orders(purchase_orders)

        elif choice == "3":
            receive_purchase_order(products, purchase_orders)

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def report_menu():
    while True:
        print("\n--- REPORT MENU ---")
        print("1. Full Inventory Report")
        print("2. Low Stock Report")
        print("3. Total Inventory Value")
        print("4. Open Purchase Orders")
        print("5. Received Purchase Orders")
        print("6. Reorder Suggestions")
        print("7. Back")

        choice = input("Choice: ")

        if choice == "1":
            inventory_report(products)

        elif choice == "2":
            low_stock_report(products)

        elif choice == "3":
            inventory_value_report(products)

        elif choice == "4":
            open_po_report(purchase_orders)

        elif choice == "5":
            received_po_report(purchase_orders)

        elif choice == "6":
            reorder_suggestions(products)

        elif choice == "7":
            break

        else:
            print("Invalid choice.")


while True:
    print("\n===== TECHSUPPLY INVENTORY SYSTEM =====")
    print("1. Product Management")
    print("2. Vendor Management")
    print("3. Purchase Orders")
    print("4. Reports")
    print("5. Save Data")
    print("6. Exit")

    choice = input("Choice: ")

    if choice == "1":
        product_menu()

    elif choice == "2":
        vendor_menu()

    elif choice == "3":
        po_menu()

    elif choice == "4":
        report_menu()

    elif choice == "5":
        save_products(products, "products.json")
        save_vendors(vendors, "vendors.json")
        save_purchase_orders(purchase_orders, "purchase_orders.json")
        print("Data saved.")

    elif choice == "6":
        save_products(products, "products.json")
        save_vendors(vendors, "vendors.json")
        save_purchase_orders(purchase_orders, "purchase_orders.json")
        print("Goodbye.")
        break

    else:
        print("Invalid choice.")