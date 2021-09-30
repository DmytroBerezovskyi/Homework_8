def arithmetic(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b
    else:
        return '\nНеизвестная операция'
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = input('Введите операцию: ')
k = arithmetic(x, y, z)
print(k)
