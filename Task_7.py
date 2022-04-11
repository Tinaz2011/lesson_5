from math import factorial

def factorial_gen(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)

print("<<programm of faktorial>>")
for el in factorial_gen(15):
    print(el)