import random
import math
a,b = list(map(int,input("please enter the space seperated lower and upper limit ").split()))
flag = True
attempt =0
level =0
while flag:
    print(f"level {level} ")
    level+=1
    k = random.randint(a,b)
    for i in range(int(math.log(b-a))):
        print(f"attempt {i+1} ",f"guess the number from {a} to {b} ")
        p = int(input())
        if k == p:
            print("correct answer ")
            a-=int(math.log(b-a))
            b+=int(math.log(b-a))
            break
        else:
            if i==int(math.log(b-a))-1:
                print("out of attempt")
                flag = False
                break
            else:
                print("wrong answer")
                if p<k:
                    if k-p>int(math.log(b-a)):
                        print("too small ")
                    else:
                        print("a little small ")
                else:
                    if p-k>int(math.log(b-a)):
                        print("too Large ")
                    else:
                        print("a little large")
                continue
    if a<0:
        a=0
    if flag!=False:
        c = input("do you want to play moer y or n ")
        if c.lower() == 'n':
            break