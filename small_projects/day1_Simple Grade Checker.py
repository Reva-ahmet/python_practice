print("Welcome To The Grade Checker")

name = input("Enter your name: ")
print(f"Hello {name}.")

grade = int(input("Enter your grade: "))


if grade < 0 :
    print("This number is a negative number please try again")
elif grade > 100:
    print("this number is bigger then 100 Please try again")
elif grade < 60:
    print("Fail!")
elif grade >= 60 and grade <= 69:
    print("Pass!")
elif grade >= 70 and grade <= 79:
    print("Good!")
elif grade >= 80 and grade <= 89:
    print("Very Good!")
elif grade >= 90 and grade <= 100:
    print("Excellent")

else:
    print("Please try later")
    exit()

