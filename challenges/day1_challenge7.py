print("Welcome To The Game!!")

num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is pozitive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")


if num % 2:
    print(f"{num} is odd.")
else:
    print(f"{num} is even.")