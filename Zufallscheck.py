import random

data = {}

for x in range(0, 100000000):
    y = random.randint(0, 100)
    if y in data:
        data[y] += 1
    else:
        data[y] = 1

f = open('data.txt', 'x')
f.write(str(data))
f.close()
