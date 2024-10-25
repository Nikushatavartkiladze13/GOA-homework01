# დაწერე ფუნქცია რომელიც იღებს ორ რიცხვს და ამოწმებს, უდრის თუ არა ისინი ერთნაბეთს

def user_number():
    number = int(input("enetryour number: "))
    number01 = int(input("enetryour number01: "))
    if number != number01:
        return "does not equal"
    else:
        return "is equal to"
print(user_number())