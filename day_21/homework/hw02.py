# 2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე შეამოწმებ რიცხვი ლუწია თუ კენტი დაბეჭდეთ რიცხვები და თან გვერძე მიუწერეთ ლუწია თუ კენტი


num = int(input("enter your number: "))
for i in range(1,num, 2):
    print(str(i) + " odd")

num = int(input("enter your number: "))
for i in range(0,num, 2):
    print(str(i) + " even")