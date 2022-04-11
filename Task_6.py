from itertools import count

print("<<inturnal intagrator of numbers from your")
n = int(input("Your number:"))

for i in count(n):
    print(i, end=' ')

from itertools import cycle

list = [6, 4, 3, 1, 0, 9, 8, 2, 5]
for i in cycle(list):
    print(i, end=' ')