from func import parcer, add, change, phone, get_phone_book

def main():

    def errors(error_name):                                         # Дабы не копировать эти строки по 5 раз, закинул их во внутреннюю функцию. Формально, принт всё еще в main :)
        if error_name == "index":
            print("Please enter command, name and phone number")
        if error_name == "key":
            print("No such name in the phone book")
        if error_name == "value":
            print("Please enter correct number")
        if error_name == "done":
            print("Completed!")
        if error_name == "existed":
            print("Such name already exists")

    while True:                                                     # Основной блок

        user_input = input("Please enter your command: ")
        parced = parcer(user_input)
        errors(parced)
        ps = parced.split(" ")

        if ps[0] == "hello":
            print("Hi! How can I help you?")

        if ps[0] == "bye":
            print("Good bye!")
            break

        if ps[0] == "add":
            result = add(parced)
            errors(result)

        if ps[0] == "change":
            result = change(parced)
            errors(result)

        if ps[0] == "phone":
            result = phone(parced)
            if result in ["index", "key", "value", "done"]:
                errors(result)
            else:
                print(result)

        if ps[0] == "show_all":
            print(get_phone_book())

        if ps[0] == "skip":
            continue



if __name__ == "__main__":
    main()