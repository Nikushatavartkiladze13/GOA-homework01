# slicing - დაჭრა

#my_list = ["gabrieli","nika","giorgi","luka","daviti","gigi","data","shalva","zuka","zezva","makvala","nugzara","demetre","merabi","omari"]
#print(my_list[2 : 7])
#print(my_list[: 7])
#print(my_list[7:])

my_list = ["gabrieli","daviti","giorgi","nika","luka","beqa"]
final_list = []
for i in range(len(my_list)):
    if my_list[i][0] != "g":
        final_list.append(my_list[i])
print(final_list)
