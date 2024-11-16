sum = 0 

for number in range(1, 100):
    if number % 5 == 0:
        continue
    sum += number
print(sum)