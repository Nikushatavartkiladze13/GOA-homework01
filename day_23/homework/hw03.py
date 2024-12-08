# 3) მომხმარებელს შემოატანინეთ ორი რიცხვი ხოლო ამის შემდეგ for loop - ის გამოყენებით გამოიტანეთ ამ რიცხვებს შორის ჯამი და ნამრავლი.


num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

sum_of_numbers = 0
product_of_numbers = 1


for i in range(min(num1, num2), max(num1, num2) + 1):
    sum_of_numbers += i   
    product_of_numbers *= i  


print(f"{num1}-დან {num2}-მდე რიცხვების ჯამი არის: {sum_of_numbers}")
print(f"{num1}-დან {num2}-მდე რიცხვების ნამრავლი არის: {product_of_numbers}")