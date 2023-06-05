# отображение содержимого в справочнике
def show_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()
    return book

# добавление строки в справочник
def new_data():
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: '+ '\n') )

# поиск по справочнику
def find_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file_read().split('\n')
        temp = input('поиск контакта: ')
        for i in book:
            if temp in i:
                print(i)

# удаление данных в справочнике
def delete_person(name):
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person)

# изменение данных
def change_person(new_name, first_name):
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if  first_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")

while True:
    mode = input('Опции справочника' + '\n' + '0-поиск, 1-чтение файла, 2-добавление в файл, 3-удаление, 4-замена, 5-выход: ')
    if mode == '1':
        print(show_data())
    elif mode == '0':
        find_data()
    elif mode == '2':
        new_data()
    elif mode == '3':
        name = input('удаление контакта: ')
        delete_person(name)
    elif mode == '4':
        first_name = input('переименование контакта: ')
        new_name = input('ввод имени конткакта: ')
        change_person(new_name,first_name)
    elif mode == '5':
        break
    else:
        print('No mode')

