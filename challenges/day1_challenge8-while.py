valid = False

while not valid:

    try:
        price = float(input("Enter the price: "))
        print(f"your price is {price}")
        valid = True

    except:
        print("Pleas enter a valid number.")

    

