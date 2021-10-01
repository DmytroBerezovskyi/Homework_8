def season(a):
    if 1 <= a <= 2 or a == 12:
        return '\n\tЗима'
    if 3 <= a <= 5:
        return '\n\tВесна'
    if 6 <= a <= 8:
        return '\n\tЛето'
    if 9 <= a <= 11:
        return '\n\tОсень'

month = int(input('Введите пожалуйста номер месяца: '))
print(season(month))