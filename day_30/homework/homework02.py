# შექმენით თავდაპირველად ცარიელი სია მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი 1-დან ამ რიცხვამდე დაამატეთ ყველა რიცხვი სიაში გამოიყენეთ for loop და append

number = int(input("enter your number: "))
num = []
for i in range(1,number):
    num.append(i)
print(num)