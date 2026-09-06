print("Welcome to Discount Calculator")

valid = False

while not valid:
    try:
        price = float(input("Enter the price: "))
        valid = True
    except:
        print("Please enter a VALID number")


if price >= 100:
    discount = price * 0.20
    final_price = price - discount
    print(f"The price is {price}, and you got 20% discount.")
    print(f"Your final price is: {final_price}")
elif price >= 50 and price < 100:
    discount = price * 0.10
    final_price = price - discount
    print(f"The price is {price}, and you got 10% discount.")
    print(f"Your final price is: {final_price}")
elif price < 50:
    print(f"The price is {price}, and you got NO discount.")
else:
    print("Please try again")
    exit()

