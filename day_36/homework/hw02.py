# 3)  დაწერე ფუნქცია, რომელიც ამოწმებს, არის თუ არა რიცხვი ნულზე დიდი.


def number():
    user_number = int(input("ჩაწერე რიცხვი: "))
    if user_number > 0 :
        return "0-ზე მეტია"
    else:
        return "0-ზე მეტი არ არის"
print(number())