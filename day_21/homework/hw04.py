# 4) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი დაითვალეთ ამ რიცხვამდე ყველა ნატურალური რიცხვის ჯამი


number = int(input("შეიყვანეთ რიცხვი: "))

if number > 0:
    sum_of_numbers = 0
    for i in range(1, number + 1):
        sum_of_numbers += i
    print(f"1-დან {number}-მდე ნატურალური რიცხვების ჯამი არის: {sum_of_numbers}")
else:
    print("გთხოვთ, შეიყვანოთ დადებითი ნატურალური რიცხვი.")
