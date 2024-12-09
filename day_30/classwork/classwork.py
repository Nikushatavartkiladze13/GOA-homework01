#  შექმენით მენტორების სახელების სია და ჩვეულებრივი სახელებისთვის განკუთვნილი სია შემდეგ მომხმარებელს შემოატანინეთ სახელი თუ ეს სახელი იქნება რომელიმე მენტორის სახელი ამ შემთხვევაში ეს სახელი დაემატოს მენტორებისთვის განკუთვნილ სიაში სხვა შემთხვევაში თუარიქნება ეს სახელი მენტორის სახელი დაემატოს ჩვეულებრივი სახელების სიაში შემდეგ კი ორივე დაბეჭდეთ


mentor_list = ['Gabriel','davit janezashvili','zuka abashidze','Luka thkvaradze']
empty_list = []

user_name = input("enter your name: ")

if user_name != mentor_list:
    print("No")
else:
    empty_list.append(user_name)