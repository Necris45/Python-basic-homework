chek_number = int(input('Введите целое число от 1 до 20: '))
if chek_number == 1:
    print(chek_number, 'процент')
elif 2 <= chek_number <= 4:
    print(chek_number, 'процента')
elif 5 <= chek_number <= 20:
    print(chek_number, 'процентов')
else:
    print('введенное число не входит в требуемый диапазон')
