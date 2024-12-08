# მომხმარებელს შევეკითხოთ სახელი და იქამდე არ შემოვუშვათ სახლში სანამ არ იტყვის რომ ქვია სვარჩიკა მაყვალა
user_name = str(input("enter your name:"))
while user_name != "სვარჩიკა მაყვალა":
    user_name = input(" თქვენი სახელი არასწორია შეიყვანეთ თავიდან")

    
user_password= str(input("enter your password: "))

while user_password != "nika1234":
    user_password = input("არ არის პაროლი სწორი გთხოვთ შეიყვანეთ ახალი პაროლი: ")
    