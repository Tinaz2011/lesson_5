def simple_calc():
    x = float(input('Hours : '))
    y = float(input('Salary : '))
    c = float(input('Bous - '))
    pay = x * y
    return pay + c
print(f'Fee is: {simple_calc() }')
