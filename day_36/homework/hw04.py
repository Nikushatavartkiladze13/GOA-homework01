# 5)  დაწერე ფუნქცია, რომელიც იღებს ორ სტრინგს და მოახდინეთ კონკატენაცია

def user_name():
    First_Name =input("enter your First Name: ")
    Last_Name = input("enter your Last Name: ")
    return "Hello "+ First_Name + " " + Last_Name
print(user_name())