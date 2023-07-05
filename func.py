phone_book = {}

def input_error(func):                  # Декоратор ошибок
    def inner_func(text):
        try:
            return func(text)
        except IndexError:
            return "index"
        except KeyError:
            return "key"
        except ValueError:
            return "value"
    return inner_func


def normalize(text):
    text = text.lower()
    return text

@input_error
def parcer(text):                       # Парсер команд
    line = text.split(" ")
    command = normalize(line[0])
    if command == "hello":
        return "hello"
    if command in ["good bye", "close", "exit"]:
        return "bye"
    if command in ["add", "change"]:
        return f"{command} {line[1]} {line[2]}"
    if command == "phone":
        return f"phone {line[1]}"
    if command == "show" and normalize(line[1]) == "all":
        return "show_all"
    else:
        return "skip"
    
@input_error                
def add(text):                          # Добавление новых контактов
    text = text.split(" ")
    if text[1] not in phone_book:
        phone_book.update({text[1]: text[2]})
        return "done"
    else:
        return "existed"
    
@input_error
def change(text):                       # Изменение существующих контактов
    text = text.split(" ")
    phone_book.pop(text[1])
    phone_book.update({text[1]: text[2]})
    return "done"

@input_error
def phone(text):                        # Достаём контак по имени
    text = text.split(" ")
    return phone_book[text[1]]


def get_phone_book():                   # Вывод всей телефонной книги
    result = ""
    for name, phone in phone_book.items():
        result += "\n" + name + " " + phone
    return result
