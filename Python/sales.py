
import csv


def read_data():
    with open("transactions.csv", "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def calculations():
    gross = []
    discount = []
    net = []
    total_units_sold = 0

    for transaction in read_data():
        price = float(transaction["price"])
        quantity = int(transaction["quantity"])
        discount_rate = float(transaction["discount"])

        gross.append(price * quantity)

        discount.append(price * discount_rate * quantity)

        net.append(price * quantity - price * discount_rate * quantity)

        total_units_sold += quantity

    total_gross = sum(gross)
    total_discount = sum(discount)
    total_net = sum(net)

    return total_gross, total_discount, total_net, total_units_sold


def insights():
    data = read_data()

    best_selling = max(
        data,
        key=lambda transaction: int(transaction["quantity"])
    )

    print(
        f"Best Selling Product by Quantity: "
        f"{best_selling['product']} "
        f"({best_selling['quantity']} units)"
    )


total_gross, total_discount, total_net, total_units_sold = calculations()

print(f"Total Gross Sales: {total_gross:.2f}")
print(f"Total Discount: {total_discount:.2f}")
print(f"Total Net Sales: {total_net:.2f}")
print(f"Total Units Sold: {total_units_sold}")

insights()

    