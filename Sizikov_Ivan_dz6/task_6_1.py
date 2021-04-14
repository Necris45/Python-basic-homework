# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
# кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
# Примечание:
# - код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# - Вы не знате заранее насколько идентичен шаблон строк файла. Попробуйте оценить это.

with open('nginx_logs.txt', 'r', encoding='utf-8') as logs_file:
    log_list = []
    for line in logs_file:
        temp_list = line.split(" ")
        remote_adr = temp_list[0]
        request_type = temp_list[5][1:]
        requested_resource = temp_list[6]
        log = (remote_adr, request_type, requested_resource)
        log_list.append(log)
print(log_list[0:3])