# for loop
#loop -ერთი და იგივე ინსტრუქცისს გამოყენება მრვალჯერ
#1 მომხმარებელს შემოატანინე რიცხვი და შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ ყვე ნატურალური რიცხვი
num = int(input("enter your number: "))
for num in range(num):
    print(num)

# 2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე შეამოწმებ რიცხვი ლუწია თუ კენტი დაბეჭდეთ რიცხვები და თან გვერძე მიუწერეთ ლუწია თუ კენტი
num = int(input("enter your number: "))
for i in range(1,num, 2):
    print(str(i) + " odd")

num = int(input("enter your number: "))
for i in range(0,num, 2):
    print(str(i) + " even")
#3) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი დაბეჭდეთ მომხმარებლის შემოტანილ რიცხვამდე მხოლოდ ხუთის ჯერადი რიცხვები
num = int(input("enter your number: "))

for i in range(0,num, 5):
    num =+ i
print(num)

# 4) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი დაითვალეთ ამ რიცხვამდე ყველა ნატურალური რიცხვის ჯამი

num = int(input("enter your number"))
for i in range(0,num):
    num =+ i
print(num)
