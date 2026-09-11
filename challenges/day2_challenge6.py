secret = 7
num = 0

attempts = 0

while secret != num: 
    num = int(input("guess a number between 1 and 10: "))


    if num >= 1 and num <= 10:
        attempts += 1
        if num == secret:
            print(f"{num} is true.")
        else:
            print(f"{num} is false.")
    else:
        print(f"{num} is not between 1 and 10 please try again.")

print(f"you got it in {attempts} attempts.")
