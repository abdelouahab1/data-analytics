def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state} {zip}")

def add_numbers(*args):
    result = sum(args)
    numbers = " + ".join(str(number) for number in args)

    print(f"{numbers} = {result}")


def display_receipt(total_due, amount_paid):
    change = amount_paid - total_due

    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if change >= 0:
        print(f"Change Due: ${change:.2f}")
    else:
        print(f"Remaining Balance: ${abs(change):.2f}")


    display_mailing_label(
    "Faiz Khan",
    "123 Main Street",
    "Oakland",
    "CA",
    "94601"
)

print()

display_mailing_label(
    "Arash Sayeed",
    "456 Market Street",
    "San Francisco",
    "CA",
    "94105"
)


# One number
add_numbers(10)

# Two numbers
add_numbers(10, 20)

# More than two numbers
add_numbers(5, 10, 15, 20, 25)


# First test: Overpay
display_receipt(50, 60)

print()

# Second test: Exact payment
display_receipt(50, 50)

print()

# Third test: Underpay
display_receipt(50, 40)

