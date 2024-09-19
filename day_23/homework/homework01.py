num = int(input("enter your number: "))
sum = 0
operation_number = 0

for n in range(0,num+1):
    for i in range(0,num+1):
        operation_number += 1
        sum = i + n
        print(f"{str(operation_number)}. {str(i)} + {str(i)} + {str(n)} = {sum}")