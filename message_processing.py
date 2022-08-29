import write_number

def message_split(message, driver, By, time):
    """Эта функция обрабатывает сообщения"""

    # Список с темой и адресатом.
    message_faces = [
        # Тема письма
        "//div[@class='Title_content_Q-Xik']/h1/span",
        # От кого
        "//div[@class='Sender_wrapper_9wUBG']/span"
    ]
    # Пустой список.
    result = {}
    # Заполняем словарь темой и адресом.
    for m in message_faces:

        value = driver.find_element(By.XPATH, m).text
        if m == "//div[@class='Title_content_Q-Xik']/h1/span":
            result["Title"] = value
        elif m == "//div[@class='Sender_wrapper_9wUBG']/span":
            result["Email"] = value
    # Добавляем тело письма.
    result["Body"] = message

    address = "Письмо пришло от: " + result["Email"]
    themes = "Тема письма: " + result["Title"]
    body = "Тело письма: " + result["Body"][14:]

    print(address)
    print()
    print(themes)
    print()
    print(body)

    value = body.split(" ")
    send_message = value[-1]
    print(send_message)

    # Посылаем номер телефона.
    write_number.write(send_message)
