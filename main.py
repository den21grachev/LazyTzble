# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import gspread

import time
from datetime import date


import registration
import message_processing
import parser_sheat
import write_number


# Настройки для браузера. 
option = webdriver.FirefoxOptions()
# Selenium dedection bypass.
option.set_preference('dom.webdriver.enabled', False)
# Disable Notifications.
option.set_preference('dom.webnotifications.enabled', False)
# Agent.
user = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gec"\
                                            "ko) Chrome/104.0.0.0 Safari/537.36"
option.set_preference('general.useragent.override', user)

# Creates a new table.
parser_sheat.create(time, gspread, date)

# Passing settings to the driver.
driver = webdriver.Firefox(options=option)
# Standby function.
driver.implicitly_wait(90)

def mail_parser():

    driver.get("https://mail.yandex.ru")
    # Registration on the website.
    registration.run(driver, Keys, By, time)

    # Function launch.
    total = 1
    while True:

        data_list = read_mail()

        iteration_and_reading(data_list)

        time.sleep(8)
        print(float(total), "... цикл пройден.")
        total += 1


def read_mail():
    """Gets old and new messages"""

    # Xpath with messages.
    command_list = "//span[@class='Text Text_color_primary Text_typography_"\
        "body-short-m qa-LeftColumn-Counters FolderControls-m__count--1gpCR']"
    # Gets raw text.
    list_mail = driver.find_element(By.XPATH, command_list).\
                                                get_attribute("aria-label")
    # Creates an empty dictionary.
    list_mail = list_mail.split("/")

    data_list = {'new messages': list_mail[0],  'old messages': list_mail[1]}

    return data_list

# Reads the message and sends them to message_split.
def iteration_and_reading(data_list):

    number = int(data_list["new messages"])

    print("Количество новых сообщений: ", data_list["new messages"])
    print("Количество прочитанных сообщений: ", data_list["old messages"])

    # Empty list.
    list_message = []
    total = 1

    while len(list_message) != number:

        check = driver.find_element(By.XPATH, f"//div[{str(total)}]/div[@data"\
                "-key='box=messages-item-box']/div").get_attribute("aria-label")

        print(total, "Письмо проверено...")

        # Return true fi text starts with (unread).
        if check.startswith("не прочитано"):
            list_message.append(check)

            # Selects the next message.
            run = driver.find_element(By.XPATH, f"//div[{str(total)}]/div[@da"\
                                    "ta-key='box=messages-item-box']").click()
            # Passes a new message and objects.
            message_processing.message_split(check, driver, By, time)

        total += 1
        time.sleep(2)

mail_parser()
