# Список команд для регистрации.
list_xpath = {
    # Кнопка Войти
    "enter": "//button[@class='Button2 Button2_size_m Button2_view_acti"\
    "on Button2_weight_500 Button_Vd8eu21iIVyRdyjGPVfYF P"\
    "SHeader-NoLoginButton']",
    # Кнопка Майл
    "mail": "//button[@data-type='login']",
    # Поле логина
    "login": "//input[@class='Textinput-Control']",
    # Кнопка ввессти логин
    "enter_login": "//button[@class='Button2 Button2_size_l Button2_v"\
    "iew_action Button2_width_max Button2_type_submit']",
    # Поле пароля
    "password": "//input[@class='Textinput-Control']",
    # Кнопка ввести пароль
    "enter_password": "//button[@class='Button2 Button2_size_l Button2_vi"\
    "ew_action Button2_width_max Button2_type_submit']",
}

# ЭТА ФУНКЦИЯ АВТОРИЗУЕТСЯ НА САЙТЕ.
def run(driver, Keys, By, time):

    log = input("Введите свой логин: ")
    pas = input("Введите свой пароль: ")

    # Накопиель
    total = 0
    # Шаги
    step = 1

    lp = [log, pas]

    for key, value in list_xpath.items():

        if value != "//input[@class='Textinput-Control']":
            # Проверка на исключение
            try:

                key = driver.find_element(By.XPATH, value).click()

            except:
                print("Что-то пошло не так...")
                driver.quit()
        else:

            key = driver.find_element(By.XPATH, value)
            key.clear()

            key.send_keys(lp[total])
            total += 1
        time.sleep(2)

        url = driver.current_url
        print(url)
        print(step, '......Этап загрузки.....')
        step += 1
