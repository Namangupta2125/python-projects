import random
def game(a,b):
    if a==b:
        return "DRAW"
    else:
        return "YOU WON THE GAME" if (a=='r' and b =='s')or(a=='p' and b =='r')or(a=='s' and b =='p') else "YOU LOOSE SORRY "

print("WELCOME TO THE GAME ")
flag =True
while flag:
    print("................................................G.A.M.E.............................................")
    flag1 = True
    while flag1:
        k = input(''' Make a choice
        for rock use 'r'
        for paper use 'p'
        for scissors use 's' ''')
        if k== 'r' or k=='p' or k=='s':
            flag1=False
        else:
            print(f"YOU HAVE ENTERED A WRONG CHOICE THAT IS {k} PLEASE TRY THAT AGAIN ")

    p = random.randint(0,100)
    if p<=33 and p>=0:
        p = 'r'
    elif p>33 and p<=66:
        p = 'p'
    else:
        p = 's'
    print(game(k,p))
    c = input("do you want to try again y or n ")
    if c == 'n':
        print("THANKS FOR VISITING COME BACK SOON")
        flag =False