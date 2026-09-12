# while loop 1.


name = input("Enter your name: ")

while name == "":
    print("You did not enter any name.")
    print("Please try again!!")
    name = input("Enter your name: ")
print(f"Hello {name}")