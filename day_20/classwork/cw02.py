#   3) 1-დან 100-მდე დაითვალეთ ხუთის ჯერადი რიცხვების ჯამი გამოიყენეთ if, else გამოგადგებათ % ნიშანი

sum = 0 

for number in range(1, 100):
    if number % 5 == 0:
        continue
    sum += number
print(sum)