import random
x = (random.randint(0, 100))
y = -1
while x != y:
    y  = int(input("Sisestage arv 1-100: "))
    if x > y:
        print("Arv on suurem")
    elif x < y:
        print("Arv on väiksem")
    else:
        print("See on õige arv")
        