# დაწერეთ ფუნქცია რომელიც მომხმარებლისგან იღებს რიცხვს და თუ რიცხვი 1-დან 10-მდეა დაბეჭდავს თუარა დაუბეჭდავს "არასწორი რიცხვი" 

def number():
    num = int(input("enter your number: "))
    if num >=1 and num <=10:
        print(num) 
    else:
        print("არასწორი რიცხვია ")
number()