# დაწერე ფუნქცია, რომელიც input()-ით იღებს ორ რიცხვს და ბეჭდავს, რომელია დიდი.


def user_number():
    number = int(input("enter your number: "))
    num = int(input("enter your number: "))
    if number > num:
        return number
    else:
        return num
print(user_number())
    