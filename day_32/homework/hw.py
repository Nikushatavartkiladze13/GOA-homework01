# 1) შექმენით რიცხვებით სავსე სია, შემდეგ დაწერეთ კოდი რომელიც დაბეჭდავს ამ სიიდან ყველაზე უდიდეს რიცხვს გამოგადგებათ for loop ი კარგად დაფიქრდით და გაიაზრეთ

numbers = [12,14,98,100,300,350,40,1000,20000,300,500,15,20,30,24,35]
num = []


for i in range(len(numbers)):
    numbers.sort()
    num.append(numbers[-1])
print(num)
