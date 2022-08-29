def create(time, gspread, date):
    """Создает новую таблицу в Google"""

    title_samara = {
            "A1": "ФИО",
            "B1": "Адрес",
            "C1": "Номер телефона",
            "D1": "Кол-во",
            "E1": "Дата",
            "F1": "Примечание"
            }
    title_tlt = {
            "A1": "ФИО",
            "B1": "Район",
            "C1": "Адрес",
            "D1": "Номер телефона",
            "E1": "Кол-во",
            "F1": "Дата",
            "G1": "Примечание"
            }

    # Помещаем словари в список.
    list_create = [title_samara, title_tlt]

    # Переменная времяни.
    name_table = "Заявки от " + str(date.today())
    # Путь до файла json.
    gc = gspread.service_account(filename="rgir28febk.json")

    # Проверяет есть ли такой файл в Googl.
    try:
        gc.open(name_table)

        print("Документ уже существует")
    except:
        print("Создание документа")
        # Запуск функций.
        create_sheat(gc, list_create, name_table, time)



def create_sheat(gc, list_create, name_table, time):
    """Эта функция создает новый документ"""

    # Создает новую таблицу.
    sh = gc.create(name_table)
    # Делает видимой для всех grachev613@gmail.com
    sh.share('grachev613@gmail.com', perm_type='user', role='writer')

    # Создает новые листы.
    SAMARA = sh.add_worksheet(title="Самара", rows="300", cols="50")
    TLT = sh.add_worksheet(title="ТЛТ", rows="300", cols="50")

    city = [SAMARA, TLT]

    index = 0
    for l in list_create:
        for key, value in l.items():
            city[index].update(key, value)
            print(key, value)
            # Задержка.
            time.sleep(2)
        city[index].format('A1:F1', {'textFormat': {'bold': True}})
        index += 1
    gc.list_spreadsheet_files()

    # Открываем таблицу.
    sh = gc.open(name_table)

    # Сохраняем в переменную список листов.
    worksheet_list = sh.worksheets()

    # Если листов 3 то первый удаляется.
    if len(worksheet_list) == 3:
        sh.del_worksheet(worksheet_list[0])


