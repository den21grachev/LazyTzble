import gspread
import time
from datetime import date

# Указываем путь к JSON
gc = gspread.service_account(filename="rgir28febk.json")
# Создаем переменную времяни.
name_table = "Заявки от " + str(date.today())
sh = gc.open(name_table)
# Получаем список всех листов.
worksheet_list = sh.worksheets()


def write(phone_number):
    """Этот модуль записывает номера в таблицу"""

    # Получаем список всех значений нашей жертывы.
    value_string = worksheet_list[0].col_values(3)
    print(value_string)

    total = 0

    # Если в списке есть пустая строка то result присвоится истина.
    result = "" in value_string

    if result == True:

        for value in value_string:
            if value == "":
                worksheet_list[0].update(f'C{total + 1}', phone_number)
                print("Номер добавлен......")
                break
            total += 1
    else:
        result_tab = len(value_string) + 1
        worksheet_list[0].update(f'C{result_tab}', phone_number)
        print("Номер добавлен......")

