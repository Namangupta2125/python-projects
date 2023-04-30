import string
import random
a = []
a.append(string.ascii_letters)
a.append(string.ascii_uppercase)
a.append(string.punctuation)
a.append(string.digits)
e = random.randint(8,12)
k =[]
for i in range(e):
    p = random.randint(0,3)
    k.append(random.choice(a[p]))

random.shuffle(k)
k = ''.join(k)
print(k)