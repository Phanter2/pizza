def start(order):
    subtotal = 0
    tax_rate = 0.095
    print("Customer Order:")
    for i in order:
        print(i.quantity, i.size, i.type, i.price)
        subtotal += i.quantity * i.price
    
    subtotal = round(subtotal, 2)
    tax = round(subtotal * tax_rate, 2)
    print("Subtotal: $" + str(subtotal))
    print("Tax: $" + str(tax))
    print("Total: $" + str(round(tax + subtotal)))
    input("Press ENTER to continue.")

    payment_type = input("Cash or credit? ")
    if payment_type.lower() == "cash":
        pass
    elif payment_type.lower() == "credit":
        pass
    else:
        print("Please enter cash or credit?")
        input("(Press enter to continue)")

    # Get the total price
    # Add tax
    # Accept payment
    # Give change
def save(order):
    with open("pizza.dat", "a") as orders:
        for pizza in order:
            orders.write(f"{pizza.quantity}, {pizza.type}, {pizza.size}, {pizza.price}, ")
        orders.write(f"{total}")
        orders.write("\n")

    print("This is the checkout")
    