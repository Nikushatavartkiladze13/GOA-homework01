#მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი დაბეჭდეთ მომხმარებლის შემოტანილ რიცხვამდე მხოლოდ ხუთის ჯერადი რიცხვები

num = int(input("enter your num: " ))

for i in range(0, num):
    if i % 5  == 0:
        print(i)
    else:
        continue