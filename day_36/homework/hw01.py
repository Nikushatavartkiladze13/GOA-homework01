# 2)  დაწერე ფუნქცია, რომელიც ამოწმებს, არის თუ არა რიცხვი ლუწი.


def user_number():
    number = int(input("enter your number: "))
    if number % 2 == 0:
        return "even"
    else:
        return " Odd"
print(user_number())