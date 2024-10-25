# 4)  დაწერე ფუნქცია, რომელიც მიიღებს სიას და აბრუნებს მასში მყოფი ელემენტების რაოდენობას.


def user_list():
    my_list = ["nika",'luka',"mari","nini",'saba','sandro',"svarchikamakvala"]
    return len(my_list)
print(user_list())