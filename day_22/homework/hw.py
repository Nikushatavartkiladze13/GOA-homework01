# სარეგისტრაციო ფორმა
user_name = str(input("enter your name:"))
while user_name != user_name:
    user_name = input("Your name is incorrect, please enter it again")

    
user_password= str(input("enter your password: "))

while user_password != user_password:
    user_password = input("Your password is incorrect, please try again:")

repeat_password = str(input("Repeat the password: "))
while repeat_password != user_password:
    repeat_password = input("Your password is incorrect, please try again: ")

user_email = (str(input("enter your email: ")))
while user_email != user_email:
    user_email = input("Your email is invalid")