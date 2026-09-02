print("Welcome to even_num or odd_num game")

yes_no = input("Are You Ready: ").strip().lower()

if yes_no == "yes":
    print("let us play")
elif yes_no == "no":
    print("Maby next time")
    exit()
else:
    exit()

num = int(input("Enter a number: "))

if num % 2 :
    print(f"{num} is odd")
else:
    print(f"{num} is even")