import write_number

def message_split(message, driver, By, time):
    """This function processes the message."""

    # List with subject and address.
    message_faces = [
        # Letter subject. 
        "//div[@class='Title_content_Q-Xik']/h1/span",
        # From whom.о 
        "//div[@class='Sender_wrapper_9wUBG']/span"
    ]
    # Empty list.
    result = {}
    # Filling the dictionary with the topic and the address..
    for m in message_faces:

        value = driver.find_element(By.XPATH, m).text
        if m == "//div[@class='Title_content_Q-Xik']/h1/span":
            result["Title"] = value
        elif m == "//div[@class='Sender_wrapper_9wUBG']/span":
            result["Email"] = value
    # Adding the body of the email..
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

    # Sending a phone number.
    write_number.write(send_message)
