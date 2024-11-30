# 1) მომხმარებელს შემოატანინოთ რიცხვი, შემდეგ კი დაბეჭდეთ ეს რიცხვი კენტია თუ ლუწი

user_number = int(input("enter your number: "))


if user_number % 5 == 0:
    print("ის არი 5ის ჯერადი")
else:
    print('არ არის ხუთის ჯერადი')