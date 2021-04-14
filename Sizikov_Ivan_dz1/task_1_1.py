duration = int(input('введите число '))
if duration < 60:
    print(duration, 's')
elif 60 <= duration < 3600:
    print(duration // 60, 'm', duration % 60, 's')
elif 3600 <= duration < 86400:
    print((duration // 3600), 'h', (duration % 3600) // 60, 'm', (duration % 3600) % 60, 's')
else:
    print(duration // 86400, 'd', (duration % 86400) // 3600, 'h', ((duration % 86400) % 3600) // 60, 'm',
          ((duration % 86400) % 3600) % 60, 's')
