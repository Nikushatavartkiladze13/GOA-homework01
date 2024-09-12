sum = 0
difference = 0
division = 0
multipication = 0
print("      sum: ")
for x in range(101):
    for i in range(101):
        sum = x + i
        print(f"{str(x)} + {str(i)} = {sum}")

print("  ")
print("        difference: ")
for x in range(101):
    for i in range(101):
        difference = x - i
        print(f"{str(x)} - {str(i)} = {difference}")

print("  ")
print("     division")
for x in range(1, 101):
    for i in range(1,101):
        division = x / i
        print(f"{str(x)} / {str(i)} = {division}")