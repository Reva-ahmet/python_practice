# while loop 3.

food = input("Enter Food You Like (q to quit)").lower()

while not food == "q":
    print(f"You like {food}")
    food = input("Enter Another Food You Like (q to quit)").lower()

print("bye")