import json
from random import choice


def write_json(person_dict, filename):
    try:
        data = json.load(open(filename))
    except:
        data = []
    data.append(person_dict)
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)


def create_contact():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    description = input('Введите описание контакта: ')

    person_contact = {
        'surname': surname,
        'name': name,
        'phone_number': phone_number,
        'description': description
    }

    return person_contact


def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def search_in_json(name_params, search_params, json_file):
    result_search = []
    for search in json_file:
        if search[name_params] == search_params:
            result_search.append(search)
    return result_search


def print_result_search(list_result):
    print(f'---------Результат поиска---------\n')
    for res in list_result:
        print(f'----------------------------------------\n')
        for key, value in res.items():
            print(f'{key}: {value}')
        print(f'----------------------------------------\n')


def choice_params_search(json_file):
    list_key = list(json_file[0].keys())
    for i, key in enumerate(list_key):
        print(f'{i + 1}) {key}')
    number_params = int(input('Введите номер параметра по которому искать: '))
    return list_key[number_params - 1]


menu = 'Что хотите сделать?(Введите номер пункта)\n 1) Создать котнакт\n 2) Найти контакт\n'
file = 'telephone.json'

if __name__ == "__main__":
    print(r'-----------telephone_directory-----------')
    print(menu)
    choice_menu = int(input('Введите номер пункта: '))
    if choice_menu == 1:
        person_contact = create_contact()
        write_json(person_contact, file)
        print('контакт добавлен')
    elif choice_menu == 2:
        telephone_directory = read_json(file)
        name_params = choice_params_search(telephone_directory)
        search_params = input(f'Введите {name_params}: ')
        search = search_in_json(name_params=name_params, search_params=search_params, json_file=telephone_directory)
        print_result_search(search)
