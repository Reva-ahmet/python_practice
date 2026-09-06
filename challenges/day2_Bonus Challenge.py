num = 1
total = 0
even_count = 0
odd_count = 0
user_num = int(input("Enter a positive number: "))



while num <= user_num:
    total += num

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num += 1

print(f"Total: {total}")
print(f"Even_num: {even_count}")
print(f"Odd_num: {odd_count}")





    