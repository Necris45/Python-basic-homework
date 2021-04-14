from requests import get, utils
from datetime import datetime
from decimal import Decimal


def currency_rates(valute_name):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    where_valute = content.find(valute_name.upper())
    if where_valute == -1:
        return None
    else:
        open_value_tag = '<Value>'
        close_value_tag = '</Value>'
        start_of_number = content.find(open_value_tag, where_valute) + len(open_value_tag)
        end_of_number = content.find(close_value_tag, where_valute)
        value = content[start_of_number:end_of_number]
        decimal_value = Decimal(value.replace(',', '.'))
        decimal_value = decimal_value.quantize(Decimal("1.00"))
        open_date_tag = '<ValCurs Date="'
        date_index = content.find(open_date_tag) + len(open_date_tag)
        close_date_tag = '"'
        end_date_index = content.find(close_date_tag, date_index)
        date_str = content[date_index:end_date_index]
        request_date = datetime.strptime(date_str, "%d.%m.%Y")
        request_date = datetime.strftime(request_date, "%Y-%m-%d")
        return f'{decimal_value}, {request_date}'


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('EUR'))
