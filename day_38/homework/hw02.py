# 3) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია შემდეგ კი ამ ფუნქციამ უნდა დააბრუნოს უმცირესი რიცხვი ამ სიიდან
number = [2, 20, 34, 100, 90, 67, 11, 12 , ]
num = []
def user_number(number):
    if len(number) == 0:
        return "is empty"
    else:
        return min(number)

print(user_number(number))