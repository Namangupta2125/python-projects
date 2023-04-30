import random
a = ''' -----
|     |
|  o  |
|     |
 -----  '''
b = ''' -----
|     |
| o o |
|     |
 -----  '''
c = ''' -----
|  o  |
| o o |
|     |
 -----  '''
d = ''' -----
| o o |
|     |
| o o |
 -----  '''
e = ''' -----
| o o |
|  o  |
| o o |
 -----  '''
f = ''' -----
| o o |
| o o |
| o o |
 -----  '''
l =[a,b,c,d,e,f]
print("Welcome to the dice ")
k = input("press y for rolling the dice")
if k.lower() =='y':
    flag = True
else:
    flag =False
while flag:
    print(random.choice(l))
    k = input("do you want to play more y or n")
    if k.lower() =='n':
        print("thankyou for visiting us")
        flag =False

