#მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი დაითვალეთ მომხმარებლის შემოტანილ რიცხვამდე რიცხვების საშუალო არითმეტიკული
number = int(input("შეიყვანეთ რიცხვი: "))

if number > 0:

    sum_of_numbers = number * (number + 1) // 2
    count_of_numbers = number
    average = sum_of_numbers / count_of_numbers
    print(f"1-დან {number}-მდე რიცხვების საშუალო არითმეტიკულია: {average}")
else:
    print("გთხოვთ, შეიყვანოთ დადებითი ნატურალური რიცხვი.")