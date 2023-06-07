flag_exit = True

# Список контактів.
contacts = {"Name": "+380935555555", 'Bill': '+380931234567', 'Din': '+380931234588'}

# Обробка помилок.
def input_error(func):
    def inner(*argsi,**kwargs): 
        try:
            return func(*argsi,**kwargs)
        except TypeError:
            print("Wrong command")
            return main()
        except IndexError:
            print('Enter name and phone separated by a space!')
            return main()
        except ValueError:
            print("ValueError") # що повинно статися щоб побачити тебе?
            return main()
        except KeyError:
            print("Enter another name.")
            return main()
        except AttributeError:
            print('Enter command.')
            return main()
    return inner

# Асистент вітається у відповідь.
@input_error
def hello(_):
    return "How can I help you?"

# Асистент додає дані до книги контактів.
@input_error
def add(uzer_input):
    text = uzer_input.split()
    contacts[text[1].capitalize()] = text[2]
    return f"Контакт {text[1].capitalize()} з номером {text[2]} створений"

# Асистент змінює дані в книзі контактів.
@input_error
def change(uzer_input):
    text = uzer_input.split()
    contacts[text[1].capitalize()] = text[2]
    return f"Номер телефона {text[1].capitalize()} змінений на : {text[2]}"
    
# Ассистент за ім'ям знаходить в контактах номер.
@input_error
def phone(uzer_input):
    text = uzer_input.split()
    text = [i.capitalize() for i in text]
    contacts[text[1]]
    return f"Номер телефону {text[1]} це : {contacts[text[1]]}"

# Ассистент показує всі контактні дані.
@input_error
def show_all(_):
    result = ""
    for name, num  in contacts.items():
        result += f"{name}: {num} " + "\n"
    return result

# Зупиняє роботу асистента.
@input_error
def exit_uzer(_):
    global flag_exit
    flag_exit = False
    return "Good bye!"

# Список команд.
COMMANDS = {"hello": hello,
            "add" : add,
            "change": change,
            "phone" : phone,
            "show all" : show_all,
            "good bye" : exit_uzer,
            "close" : exit_uzer,
            "exit" : exit_uzer
            }

# Знаходить команду.
@input_error
def handler(uzer_input):
    text = uzer_input.lower()
    for keys in COMMANDS.keys():
        if keys in text:
            return COMMANDS[keys]

@input_error
def main():
    while flag_exit:
        uzer_input = input("-->")
        com = handler(uzer_input)
        print(com(uzer_input.lower()))

if __name__ == "__main__":
    main()