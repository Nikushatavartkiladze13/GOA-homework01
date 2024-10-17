# შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცხვს და დააბრუნებს True, თუ ის ლუწია  და False, თუ არა.
def user_number():
    number = int(input("enter our number: "))
    if number % 2 ==0:
        print(True)
    else:
        print(False)
user_number()