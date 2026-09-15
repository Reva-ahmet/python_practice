# while loop 2.

age = int(input("Enter Your Age: "))

while age < 0:
    print("Age can not be less than zero.")
    age = int(input("Enter Your Age: "))

print(f"Your age is {age}")