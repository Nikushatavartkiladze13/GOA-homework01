# 4) მომხმარებელს შეაყვანინეთ რიცხვი და განაგრძეთ კითხვა მანამ, სანამ არ შეიტანს დადებით რიცხვს.

number = int(input("შეიყვანეთ დადებითი რიცხვი: "))

while number <= 0:
    print("შეიყვანეთ დადებითი რიცხვი!")
    number = int(input("შეიყვანეთ დადებითი რიცხვი: "))

print(f"თქვენ შეიყვანეთ დადებითი რიცხვი: {number}")