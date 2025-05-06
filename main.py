import random
hewan = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password =""
for i in range(10):
    password +=random.choice ( hewan)
print(password)
