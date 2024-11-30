# მომხმარებელს input ის მეშვეობით შემოატანინეთ 2 რიცხვი და შემდეგ ამ ორ რიცხვს შორის ჩაატარე ყველა არითმეტიკული მოქმედება 
num1 = int(input("enter first number: "))
num2 = int(input("enter second numbber: "))

print(num1 - num2)
print(num1 + num2)
print(num1 / num2)
print(num1 % num2)
print(num1 * num2)
print(num1 // num2)
# მომხმარებელს input -ის საშუალებით შემოატანინეთ სახელი და გვარი შემდეგ კი დაუპრინტეთ გრძელი წინადადება 
name = input("enter your name: ")
age = input("enter your age: ")

print("gamarjoba, me var " + name + " " + age + " " + "wlis")
# მომხმარებელს შემოატანინეთ სახელი გვარი, ქალაქი საყვარელი ფერი და საყვარელი საჭმელი. შემდეგ კი ეცადეთ რომ შექმნათ ერთ დიდი გამართული წინადადება
name = input("enter your name: ")
surname = input("enter your surname: ")
city = input("enter your city: ")
color = input("enter your favourite color: ")
food = input("enter your favourite food: ")

print("gamarjoba, chemi saxeli da gvaria " + name + " " + surname + ", adgili sadac me vimyofebi aris " + city + ". chemi sayvareli feria " + color + ", chemi sayvareli sawmelia " + food)