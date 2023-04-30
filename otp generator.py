import string
import random
print("welcome to the otp generator")
a = string.digits
b = string.ascii_letters
a = a+b
a = list(a)
random.shuffle(a)
c = random.randint(6,8)
l = random.choices(a,k = c)
l = ''.join(l)
print(f"Your one time passowrd is {l}")
