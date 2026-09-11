secret = 7
num = 0

while secret != num: 
    num = int(input("guess a number between 1 and 10: "))

    if num == secret:
        print(f"{num} is true.")
    else:
        print(f"{num} is false.")
