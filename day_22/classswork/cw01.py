# მომხმარებელს შემოატანინეთ რიცხვი შემდეგ while loop ის გამოყენებით 1-დან მომხმარების შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ ხუთის ჯერადი რიცხვები


number = int(input("შეიყვანეთ რიცხვი: "))


i = 1
while i <= number:
    if i % 5 == 0:
        print(i)
    i += 1