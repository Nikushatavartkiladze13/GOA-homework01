#  განუწყვეტლივ სთხოვეთ მომხმარებელს მისი სახელი, სანამ არ შეიყვანს "quit"-ს.
user_name = input("enter your name: ")

while user_name != "quit":
    user_name = input("enter your name: ")
    if user_name == "quit":
        print('thanks')
    else:
        print("enter your name: ")
