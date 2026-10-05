age = int(input("Enter your age: "))

if age >= 0 and age <= 120:
    print("Age is valid")

    if age >= 18:
        print("You are eligible for voting")
    else:
        print("You are not eligible for voting")
else:
    print("Age is invalid")
