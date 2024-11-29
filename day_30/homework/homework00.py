#1) შექმენით სია რომელშიც იქნება მინიმუმ 10 სახელი შემდეგ ამ სიიდან ამოშალეთ ისეთი სახელები რომლის სიგრძეც იქნება 10ზე მეტი და დააბრუნეთ გაფილტრული სია გამოიყენეთ for loop და ნასწავლი ფუნქციები


name_list = ['nika', 'dato', 'gabrieli','giorgi','saba','luka','mate','sandro','cotne','shalva']
empty_list = []


for i in name_list:
    if len(i) <= 10:
        empty_list.append(i)
print(empty_list)
