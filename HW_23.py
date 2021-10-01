"""
Распределение високосных годов:
год, номер которого кратен 400, — високосный;
остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300);
остальные годы, номер которых кратен 4, — високосные[5].
Високосными годами в Риме были 45, 42, 39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9 годы до н. э
"""
def is_year_leap(year):
    leap_year_4 = year%4        #годы номер которых кратен 4, — високосные
    leap_year_100 = year%100    #год номер которых кратен 100, — невисокосные
    leap_year_400 = year%400    #год номер которого кратен 400, — високосный
    leap_year_BC = year%3       #Високосными годы в Риме до н. э
    if leap_year_BC == 0 and  -45 <= year <=9:
        return True
    elif leap_year_BC != 0 and  -45 <= year < 0:
        return False
    if leap_year_4 != 0 and 1<= year or 99 <= year and leap_year_400 != 0 and leap_year_100 == 0:
        return False
    elif leap_year_4 == 0 and year > 0:
        return True


year = input('Please enter the year : ')
year = int(year)
if year < -45:
    print('Please enter the correct year, where the minus sign is BC (Before Christ)')
    year = input('Please enter the year : ')
    year = int(year)
print(is_year_leap(year))
