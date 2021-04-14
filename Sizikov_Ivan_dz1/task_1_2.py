for i in range(1, 1000):
    cub = i ** 3
    chek_sum = 0
    ostatok = cub
    while ostatok != 0:
        chek_sum += ostatok % 10
        ostatok = ostatok // 10
    if chek_sum % 7 == 0:
        print('число =', cub, 'sum =', chek_sum)
