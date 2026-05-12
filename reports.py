def inventory_report(products):

    print("\nFULL INVENTORY REPORT")

    for p in products:
        print(f"{p.product_id} | {p.name} | Qty: {p.quantity}")


def low_stock_report(products):

    print("\nLOW STOCK REPORT")

    for p in products:

        if p.quantity <= p.reorder_level:
            print(f"{p.name} needs reorder.")


def inventory_value_report(products):

    total = 0

    for p in products:
        total += p.quantity * p.unit_price

    print(f"Total Inventory Value: ${total:.2f}")


def open_po_report(purchase_orders):

    print("\nOPEN PURCHASE ORDERS")

    for po in purchase_orders:

        if po.status == "OPEN":
            print(po.__dict__)


def received_po_report(purchase_orders):

    print("\nRECEIVED PURCHASE ORDERS")

    for po in purchase_orders:

        if po.status == "RECEIVED":
            print(po.__dict__)


def reorder_suggestions(products):

    print("\nREORDER SUGGESTIONS")

    for p in products:

        if p.quantity <= p.reorder_level:

            print(
                f"{p.name} should reorder "
                f"{p.reorder_quantity} units."
            )