def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price


def main():
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percent)

    if final_price == original_price:
        print("No discount applied. Final price:", final_price)
    else:
        print("Discount applied. Final price:", final_price)


if __name__ == "__main__":
    main()


"""The line if __name__ == "__main__":
is a common Python idiom used to determine if the Python script is being run as the main program
or if it's being imported as a module into another script.
Here's what it does:
__name__ is a special built-in variable in Python that holds the name of the current module.
When Python runs a script, it sets the __name__ variable of that script to "__main__".
When a script is imported as a module into another script,
the __name__ variable is set to the name of the module (i.e., the filename without the .py extension).
So, if __name__ == "__main__": allows you to write code that will only run when the script is executed directly,
not when it's imported as a module."""
